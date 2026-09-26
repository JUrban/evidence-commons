"""Reliance graph over claim records: load-bearing claims and revalidation cascades."""
from __future__ import annotations
import pathlib, yaml
from collections import defaultdict

def load_claims(root):
    claims = {}
    for f in pathlib.Path(root).rglob("*.y*ml"):
        if "claims" in f.parts:
            d = yaml.safe_load(f.read_text()); claims[d["id"]] = d
    return claims

def graph(claims):
    children = defaultdict(list); confirmed = defaultdict(list)
    for cid, c in claims.items():
        for r in c.get("relies_on", []) or []:
            children[r["id"]].append(cid)
            if r.get("confirmed"): confirmed[r["id"]].append(cid)
    return children, confirmed

def descendants(children, root):
    seen, stack = set(), [root]
    while stack:
        u = stack.pop()
        for c in children.get(u, []):
            if c not in seen: seen.add(c); stack.append(c)
    return seen

def load_bearing(claims, top=10):
    children, confirmed = graph(claims)
    rows = [(cid, len(descendants(children, cid)), len(confirmed.get(cid, []))) for cid in set(claims) | set(children)]
    rows.sort(key=lambda r: (-r[2], -r[1], r[0]))
    return [{"claim": c, "dependents": d, "confirmed_direct": k} for c, d, k in rows[:top]]

def cascade(claims, failed: str):
    children, _ = graph(claims)
    flagged = descendants(children, failed)
    return {"failed": failed, "flag_support_withdrawn": sorted(flagged)}

def report(root):
    claims = load_claims(root)
    resolved_failed = [c for c, d in claims.items() if any(s.startswith("resolved:refuted") for s in d.get("status", []))]
    return {"claims": len(claims), "load_bearing": load_bearing(claims), "cascades": [cascade(claims, f) for f in resolved_failed]}
