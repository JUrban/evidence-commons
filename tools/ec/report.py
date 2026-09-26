"""State-of-the-field coverage tables from a records directory (docs, Section 34)."""
from __future__ import annotations
import pathlib, yaml
from collections import Counter

def load(root, kind):
    out = []
    for f in pathlib.Path(root).rglob("*.y*ml"):
        if kind in f.parts: out.append(yaml.safe_load(f.read_text()))
    return out

def coverage(root):
    claims = load(root, "claims"); ch = load(root, "challenges"); res = load(root, "resolutions")
    st = Counter()
    for c in claims:
        for s in c.get("status", []): st[s.split(":")[0]] += 1
    with_protocol = sum(1 for c in claims if c.get("protocol"))
    with_bond = sum(1 for c in claims if c.get("bond"))
    with_log = sum(1 for c in claims if c.get("log"))
    outcomes = Counter(r["outcome"] for r in res)
    chall = Counter(x["outcome"] for x in ch)
    return {"registered": len(claims), "with_protocol": with_protocol, "bonded": with_bond, "logged": with_log,
            "status_counts": dict(st), "resolutions": len(res), "resolution_outcomes": dict(outcomes),
            "challenges": len(ch), "challenge_outcomes": dict(chall),
            "unpriced_share": round(1 - st.get("priced", 0) / len(claims), 3) if claims else None}

def as_markdown(cov):
    lines = ["| measure | value |", "|---|---|"]
    for k, v in cov.items(): lines.append(f"| {k} | {v} |")
    return "\n".join(lines)
