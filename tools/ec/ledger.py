"""Forecaster ledgers: proper scores, realized performance, provisional status, split-half reliability.

Input CSV columns: principal, claim, forecast (0-1), outcome (0/1), [pnl], [difficulty]
"""
from __future__ import annotations
import csv, math, pathlib
from collections import defaultdict
import numpy as np
from scipy.stats import spearmanr

PROVISIONAL = 50

def read_csv(path):
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append({"principal": r["principal"], "claim": r["claim"], "forecast": float(r["forecast"]),
                         "outcome": int(float(r["outcome"])), "pnl": float(r.get("pnl") or 0), "difficulty": float(r.get("difficulty") or 0)})
    return rows

def brier(rows):
    return float(np.mean([(r["forecast"] - r["outcome"]) ** 2 for r in rows])) if rows else float("nan")

def log_score(rows):
    return float(np.mean([math.log(max(1e-6, r["forecast"] if r["outcome"] else 1 - r["forecast"])) for r in rows])) if rows else float("nan")

def per_principal(rows):
    by = defaultdict(list)
    for r in rows: by[r["principal"]].append(r)
    out = {}
    base = float(np.mean([r["outcome"] for r in rows])) if rows else 0.5
    for p, rs in by.items():
        n = len(rs)
        out[p] = {"positions": n, "brier": round(brier(rs), 4), "log_score": round(log_score(rs), 4),
                  "base_rate_brier": round(float(np.mean([(base - r["outcome"]) ** 2 for r in rs])), 4),
                  "realized_pnl": round(sum(r["pnl"] for r in rs), 2),
                  "mean_difficulty": round(float(np.mean([r["difficulty"] for r in rs])), 3),
                  "provisional": n < PROVISIONAL}
    return out

def split_half(rows, min_positions=8, seed=0):
    """Split claims at random into halves; correlate each principal's Brier across halves."""
    rng = np.random.default_rng(seed)
    claims = sorted({r["claim"] for r in rows})
    half = {c: rng.random() < 0.5 for c in claims}
    a = per_principal([r for r in rows if half[r["claim"]]]); b = per_principal([r for r in rows if not half[r["claim"]]])
    common = [p for p in a if p in b and a[p]["positions"] >= min_positions and b[p]["positions"] >= min_positions]
    if len(common) < 5: return {"rho": None, "n_principals": len(common)}
    rho = spearmanr([a[p]["brier"] for p in common], [b[p]["brier"] for p in common]).correlation
    return {"rho": round(float(rho), 3), "n_principals": len(common)}

def report(path):
    rows = read_csv(path)
    pp = per_principal(rows)
    thresholds = {t: sum(1 for v in pp.values() if v["positions"] >= t) for t in (100, 300, 1000)}
    return {"rows": len(rows), "principals": len(pp), "overall_brier": round(brier(rows), 4),
            "split_half": split_half(rows), "forecasters_at_or_above": thresholds,
            "ledger": dict(sorted(pp.items(), key=lambda kv: kv[1]["brier"]))}
