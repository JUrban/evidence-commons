"""ec — Evidence Commons command line."""
from __future__ import annotations
import argparse, json, sys, pathlib

def main(argv=None):
    ap = argparse.ArgumentParser(prog="ec", description="Evidence Commons reference tools")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("validate", help="validate records/templates against schemas"); p.add_argument("paths", nargs="*")
    p = sub.add_parser("market", help="LMSR market engine"); p.add_argument("action", choices=["demo", "open", "trade", "fund", "status", "settle"])
    p.add_argument("--file", default="market.json"); p.add_argument("--claim"); p.add_argument("--b", type=float, default=300); p.add_argument("--cost", type=float, default=20000)
    p.add_argument("--host"); p.add_argument("--principal"); p.add_argument("--side"); p.add_argument("--size", type=float); p.add_argument("--forecast", type=float)
    p.add_argument("--rationale", default=""); p.add_argument("--amount", type=float); p.add_argument("--base", type=float); p.add_argument("--outcome"); p.add_argument("--measured", type=float)
    p = sub.add_parser("ledger", help="score a forecasts CSV"); p.add_argument("csv")
    p = sub.add_parser("recorder", help="flight recorder"); p.add_argument("action", choices=["demo"])
    p = sub.add_parser("replay", help="counterfactual credit"); p.add_argument("action", choices=["demo"])
    p = sub.add_parser("reliance", help="reliance graph over records"); p.add_argument("root")
    p = sub.add_parser("report", help="state-of-the-field coverage"); p.add_argument("root"); p.add_argument("--md", action="store_true")
    a = ap.parse_args(argv)

    if a.cmd == "validate":
        from .validate import main as vmain; return vmain(a.paths)
    if a.cmd == "market":
        from .market import Market, demo
        if a.action == "demo": demo(); return 0
        f = pathlib.Path(a.file)
        if a.action == "open":
            m = Market(id=f"m-{a.claim}", claim=a.claim, b=a.b, resolution_cost=a.cost, host=a.host); m.save(f); print(m.display()); return 0
        m = Market.load(f)
        if a.action == "trade": t = m.trade(a.principal, a.side, a.size, forecast=a.forecast, rationale=a.rationale); print(f"filled {t.size:.1f} @ {t.price:.3f}, fee {t.fee:.2f}")
        elif a.action == "fund":
            if a.amount: m.pay_resolution(a.principal or "direct", a.amount)
            if a.base: m.allocate_base(a.base)
        elif a.action == "settle": print(json.dumps(m.settle(a.outcome, a.measured), indent=1))
        m.save(f); print(json.dumps(m.display(), indent=1)); return 0
    if a.cmd == "ledger":
        from .ledger import report; print(json.dumps(report(a.csv), indent=1)); return 0
    if a.cmd == "recorder":
        from .recorder import demo; demo(); return 0
    if a.cmd == "replay":
        from .replay import demo; demo(); return 0
    if a.cmd == "reliance":
        from .reliance import report; print(json.dumps(report(a.root), indent=1)); return 0
    if a.cmd == "report":
        from .report import coverage, as_markdown
        c = coverage(a.root); print(as_markdown(c) if a.md else json.dumps(c, indent=1)); return 0
    return 0

if __name__ == "__main__":
    sys.exit(main())
