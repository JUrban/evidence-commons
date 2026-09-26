import pathlib, json
from ec.replay import demo as replay_demo, Pipeline, Intervention, shapley
from ec.ledger import report
from ec.reliance import load_claims, load_bearing, cascade
from ec.report import coverage
from ec.validate import validate_paths

ROOT = pathlib.Path(__file__).resolve().parents[2]

def test_replay_credits_outcome_changing_intervention_only():
    rec = replay_demo(verbose=False)
    byid = {c["id"]: c for c in rec["contributors"]}
    assert byid["person:LN"]["outcome_changing"] == 1 and byid["person:LN"]["shapley"] == 1.0
    assert byid["person:JK"]["outcome_changing"] == 0 and byid["person:JK"]["shapley"] == 0.0

def test_shapley_sampling_path():
    p = Pipeline(steps=[lambda s: {**s, "x": s.get("x", 0)}])
    for k in range(8): p.interventions.append(Intervention(f"c{k}", 0, (lambda k: (lambda s: {**s, "x": s.get("x", 0) + k}))(k)))
    # only one override runs at step 0 (last wins in dict); outcome depends on which — just check it runs and returns n entries
    out = shapley(p, lambda s: float(s.get("x", 0)), [f"c{k}" for k in range(8)], samples=20)
    assert len(out) == 8

def test_ledger_report():
    r = report(ROOT / "tools/tests/data/forecasts.csv")
    assert r["principals"] == 40 and 0 < r["overall_brier"] < 0.4 and r["split_half"]["n_principals"] >= 5

def test_reliance_and_cascade_on_seed_records():
    claims = load_claims(ROOT / "records")
    lb = load_bearing(claims, top=3)
    assert lb and lb[0]["claim"] in ("EC-004", "c47", "c31", "c12")
    c = cascade(claims, "EC-004")
    assert {"EC-002", "EC-003", "EC-005"} <= set(c["flag_support_withdrawn"])

def test_seed_records_validate():
    n, errors = validate_paths([str(ROOT / "records"), str(ROOT / "templates/protocols")])
    assert n >= 20 and errors == []

def test_coverage():
    c = coverage(ROOT / "records")
    assert c["registered"] >= 9 and c["resolutions"] == 1 and c["challenges"] == 1
