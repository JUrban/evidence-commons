"""Flight recorder: hash-chained workflow log with Merkle-checkpointed selective disclosure and signatures.

Design (docs, Section 8.11):
- each entry: type, time, actor, content; content is stored separately (here: encrypted-at-rest is the
  deployment's job; the reference keeps content in a side store) and only its hash enters the chain;
- entry_hash = sha256(canonical(seq, type, time, actor, content_hash, prev_hash));
- a checkpoint commits to a Merkle root over the entry hashes in its range and is signed (Ed25519 via
  `cryptography` if available, else HMAC with the researcher's secret);
- selective disclosure: a subset of entries plus Merkle inclusion proofs; a verifier checks proofs against
  the signed root without seeing anything else.
"""
from __future__ import annotations
import hashlib, json, datetime as dt, os, base64
from dataclasses import dataclass, field, asdict

ENTRY_TYPES = ("prompt", "model_output", "human_edit", "decision", "data_access", "tool_call", "environment")

def sha(b: bytes | str) -> str:
    return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()
def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

# ---- signing ----
class Signer:
    def __init__(self, secret: bytes | None = None):
        self.kind = "hmac"; self.secret = secret or os.urandom(32); self.pub = None
        try:
            from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
            self._sk = Ed25519PrivateKey.generate(); self.kind = "ed25519"
            from cryptography.hazmat.primitives import serialization
            self.pub = base64.b64encode(self._sk.public_key().public_bytes(
                serialization.Encoding.Raw, serialization.PublicFormat.Raw)).decode()
        except Exception:
            self._sk = None
    def sign(self, msg: str) -> str:
        if self.kind == "ed25519":
            return "ed25519:" + base64.b64encode(self._sk.sign(msg.encode())).decode()
        import hmac
        return "hmac:" + hmac.new(self.secret, msg.encode(), hashlib.sha256).hexdigest()
    def verify(self, msg: str, sig: str) -> bool:
        if sig.startswith("ed25519:") and self.kind == "ed25519":
            try:
                self._sk.public_key().verify(base64.b64decode(sig[8:]), msg.encode()); return True
            except Exception:
                return False
        import hmac
        return hmac.compare_digest(sig, self.sign(msg))

# ---- Merkle ----
def merkle_root(leaves: list[str]) -> str:
    if not leaves: return sha("")
    level = [sha(bytes.fromhex(x)) for x in leaves]
    while len(level) > 1:
        if len(level) % 2: level.append(level[-1])
        level = [sha(bytes.fromhex(level[i]) + bytes.fromhex(level[i + 1])) for i in range(0, len(level), 2)]
    return level[0]

def merkle_proof(leaves: list[str], index: int) -> list[tuple[str, str]]:
    """Returns [(sibling_hash, 'L'|'R'), ...] from leaf to root."""
    level = [sha(bytes.fromhex(x)) for x in leaves]; proof = []; i = index
    while len(level) > 1:
        if len(level) % 2: level.append(level[-1])
        sib = i ^ 1
        proof.append((level[sib], "L" if sib < i else "R"))
        level = [sha(bytes.fromhex(level[j]) + bytes.fromhex(level[j + 1])) for j in range(0, len(level), 2)]
        i //= 2
    return proof

def verify_proof(leaf: str, proof: list, root: str) -> bool:
    h = sha(bytes.fromhex(leaf))
    for sib, side in proof:
        h = sha(bytes.fromhex(sib) + bytes.fromhex(h)) if side == "L" else sha(bytes.fromhex(h) + bytes.fromhex(sib))
    return h == root

# ---- log ----
@dataclass
class Entry:
    seq: int; type: str; time: str; actor: str; content_hash: str; prev_hash: str; entry_hash: str = ""

@dataclass
class WorkflowLog:
    id: str
    level: int = 3
    entries: list = field(default_factory=list)
    checkpoints: list = field(default_factory=list)
    environment: dict = field(default_factory=dict)
    contents: dict = field(default_factory=dict)   # content_hash -> content (side store; encrypt in deployment)
    signer: Signer = field(default_factory=Signer, repr=False, compare=False)

    def append(self, type: str, actor: str, content, time: str | None = None) -> Entry:
        if type not in ENTRY_TYPES: raise ValueError(f"unknown entry type {type}")
        seq = len(self.entries)
        prev = self.entries[-1].entry_hash if self.entries else sha("genesis:" + self.id)
        c = canon(content); ch = sha(c); self.contents[ch] = content
        e = Entry(seq, type, time or dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), actor, ch, prev)
        e.entry_hash = sha(canon(asdict(e) | {"entry_hash": ""}))
        self.entries.append(e); return e

    def checkpoint(self, anchor: str | None = None) -> dict:
        start = self.checkpoints[-1]["range"][1] + 1 if self.checkpoints else 0
        end = len(self.entries) - 1
        if end < start: raise ValueError("nothing to checkpoint")
        leaves = [e.entry_hash for e in self.entries[start:end + 1]]
        root = merkle_root(leaves)
        msg = canon({"log": self.id, "range": [start, end], "root": root})
        cp = {"range": [start, end], "merkle_root": root, "signature": self.signer.sign(msg), "signer": self.signer.kind,
              "public_key": self.signer.pub, "anchor": anchor}
        self.checkpoints.append(cp); return cp

    def verify_chain(self) -> bool:
        prev = sha("genesis:" + self.id)
        for e in self.entries:
            if e.prev_hash != prev: return False
            if e.entry_hash != sha(canon(asdict(e) | {"entry_hash": ""})): return False
            prev = e.entry_hash
        for cp in self.checkpoints:
            s, t = cp["range"]
            if merkle_root([e.entry_hash for e in self.entries[s:t + 1]]) != cp["merkle_root"]: return False
            msg = canon({"log": self.id, "range": [s, t], "root": cp["merkle_root"]})
            if not self.signer.verify(msg, cp["signature"]): return False
        return True

    def disclose(self, seqs: list[int]) -> dict:
        """Selective disclosure: chosen entries with content, each with a Merkle proof against its checkpoint."""
        out = {"log": self.id, "level": self.level, "checkpoints": [], "entries": []}
        for seq in seqs:
            cp = next((c for c in self.checkpoints if c["range"][0] <= seq <= c["range"][1]), None)
            if cp is None: raise ValueError(f"entry {seq} not yet checkpointed")
            s, t = cp["range"]; leaves = [e.entry_hash for e in self.entries[s:t + 1]]
            e = self.entries[seq]
            out["entries"].append({"entry": asdict(e), "content": self.contents[e.content_hash],
                                   "proof": merkle_proof(leaves, seq - s), "checkpoint_range": cp["range"]})
            if cp not in out["checkpoints"]: out["checkpoints"].append(cp)
        return out

    def to_record(self) -> dict:
        return {"id": self.id, "level": self.level, "entries": [asdict(e) for e in self.entries],
                "checkpoints": [{k: v for k, v in c.items() if k in ("range", "merkle_root", "signature", "anchor")} for c in self.checkpoints],
                "environment": self.environment}

def verify_disclosure(d: dict, signer_pub_or_signer=None) -> bool:
    """A verifier checks each disclosed entry against its checkpoint root and the entry's own hash."""
    for item in d["entries"]:
        e = item["entry"]
        if e["entry_hash"] != sha(canon(e | {"entry_hash": ""})): return False
        if sha(canon(item["content"])) != e["content_hash"]: return False
        cp = next(c for c in d["checkpoints"] if c["range"] == item["checkpoint_range"])
        if not verify_proof(e["entry_hash"], [tuple(p) for p in item["proof"]], cp["merkle_root"]): return False
    return True

def demo(verbose=True):
    log = WorkflowLog("L-47", level=3, environment={"model": "assistant-x@2031-01", "seed": 7, "container": "sha256:..."})
    t = "2031-01-04T10:00:00"
    log.append("prompt", "workflow:W-3", {"text": "Screen additive families for anode stability"}, t)
    log.append("model_output", "workflow:W-3", {"text": "Proposing family A (literature support)"}, t)
    log.append("human_edit", "person:LN", {"text": "Family A always looks good in simulation and fails at the anode interface — we saw this in 2023. Try the phosphonates."}, t)
    log.append("decision", "workflow:W-3", {"branch": "family: phosphonates"}, t)
    log.append("data_access", "workflow:W-3", {"dataset": "d47-cycles"}, t)
    log.append("human_edit", "person:JK", {"text": "fixed table formatting"}, t)
    cp = log.checkpoint(anchor="ots:example")
    ok = log.verify_chain()
    d = log.disclose([2])
    vd = verify_disclosure(d)
    if verbose:
        print(f"log {log.id}: {len(log.entries)} entries, checkpoint range {cp['range']}, root {cp['merkle_root'][:16]}…, signer {cp['signer']}")
        print(f"chain verifies: {ok}")
        print(f"selective disclosure of entry 2 (Lena's override) with Merkle proof: verifies = {vd}; other entries not revealed")
    return log, d, ok, vd
