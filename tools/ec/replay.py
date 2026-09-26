"""Counterfactual credit by replay on a deterministic pipeline.

A pipeline is a list of steps; each step is a function state -> state. Human interventions are overrides
attached to step indices: at that step the human's function runs instead of the workflow's default.
Contribution = Shapley value of each contributor over subsets of contributors (exact for n <= 6, sampled beyond),
where the outcome measure is a function of the final state (binary or scalar).
"""
from __future__ import annotations
import itertools, math, random
from dataclasses import dataclass, field

@dataclass
class Intervention:
    contributor: str
    step: int
    fn: object          # state -> state
    description: str = ""
    mode: str = "edit"  # "edit": applied after the default step; "replace": runs instead of the default

@dataclass
class Pipeline:
    steps: list                          # default step functions
    interventions: list = field(default_factory=list)
    def run(self, active: set[str] | None = None, state=None):
        active = set(active) if active is not None else {i.contributor for i in self.interventions}
        state = dict(state or {})
        acts = [i for i in self.interventions if i.contributor in active]
        for k, fn in enumerate(self.steps):
            replaces = [i for i in acts if i.step == k and i.mode == "replace"]
            state = replaces[-1].fn(state) if replaces else fn(state)   # a later replace supersedes an earlier one
            for i in (i for i in acts if i.step == k and i.mode == "edit"):
                state = i.fn(state)
        return state

def shapley(pipeline: Pipeline, outcome, contributors: list[str], max_exact=6, samples=200, seed=0):
    n = len(contributors)
    if n <= max_exact:
        vals = {c: 0.0 for c in contributors}
        for c in contributors:
            others = [o for o in contributors if o != c]
            for k in range(len(others) + 1):
                for S in itertools.combinations(others, k):
                    w = math.factorial(k) * math.factorial(n - k - 1) / math.factorial(n)
                    vals[c] += w * (outcome(pipeline.run(set(S) | {c})) - outcome(pipeline.run(set(S))))
        return {c: (round(v, 4), 0.0) for c, v in vals.items()}
    rng = random.Random(seed); acc = {c: [] for c in contributors}
    for _ in range(samples):
        order = contributors[:]; rng.shuffle(order); S = set(); prev = outcome(pipeline.run(S))
        for c in order:
            S.add(c); cur = outcome(pipeline.run(S)); acc[c].append(cur - prev); prev = cur
    out = {}
    for c, xs in acc.items():
        m = sum(xs) / len(xs); se = (sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5 / len(xs) ** 0.5
        out[c] = (round(m, 4), round(se, 4))
    return out

def contribution_record(pipeline: Pipeline, outcome, log_id: str, workflow: dict, level=3, outcome_measure="result obtained"):
    contributors = sorted({i.contributor for i in pipeline.interventions})
    sh = shapley(pipeline, outcome, contributors)
    full = pipeline.run(); base = outcome(full)
    rec = {"log_id": log_id, "level": level, "replay_method": "deterministic", "outcome_measure": outcome_measure, "contributors": [], "workflow": workflow, "unlogged_segments": []}
    for c in contributors:
        ints = [i for i in pipeline.interventions if i.contributor == c]
        without = outcome(pipeline.run({x for x in contributors if x != c}))
        rec["contributors"].append({"id": c, "interventions": len(ints), "outcome_changing": int(without != base), "shapley": sh[c][0], "se": sh[c][1]})
    return rec

def demo(verbose=True):
    # Lena's pipeline: default screens family A (finds nothing); her override switches to phosphonates (finds Q)
    def propose(s): s["family"] = "A"; return s
    def screen(s): s["hit"] = "Q" if s["family"] == "phosphonates" else None; return s
    def analyse(s): s["result"] = s["hit"] is not None; return s
    def write(s): s["report"] = f"result={s['result']}"; return s
    p = Pipeline(steps=[propose, screen, analyse, write])
    p.interventions.append(Intervention("person:LN", 0, lambda s: {**s, "family": "phosphonates"}, "override family choice", mode="edit"))
    p.interventions.append(Intervention("person:JK", 3, lambda s: {**s, "report": s["report"] + " (formatted)"}, "formatting"))
    p.interventions.append(Intervention("person:MR", 3, lambda s: s, "budget approval (no-op in pipeline)"))
    rec = contribution_record(p, lambda s: 1.0 if s.get("result") else 0.0, "L-47", {"id": "W-3", "host": "org:H", "version": "2.4.1"})
    if verbose:
        print("contribution record:")
        for c in rec["contributors"]: print(f"  {c['id']:<10} interventions={c['interventions']} outcome_changing={c['outcome_changing']} shapley={c['shapley']}")
    return rec
