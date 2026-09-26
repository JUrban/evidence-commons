"""Logarithmic market scoring rule engine with resolution funds, fees, position limits and settlement.

A market prices a binary contract paying 1 if the claim's resolution protocol succeeds.
Scalar markets are ladders of these (see docs, Section 7.10); this reference engine implements the binary leg.
"""
from __future__ import annotations
import json, math, pathlib, datetime as dt
from dataclasses import dataclass, field, asdict

@dataclass
class Trade:
    principal: str
    side: str            # "buy" (long yes) or "sell" (short yes)
    size: float          # contracts
    price: float         # average price paid
    cost: float          # cash paid (negative = received)
    fee: float
    time: str
    forecast: float | None = None
    rationale: str = ""
    agent: str | None = None

@dataclass
class Market:
    id: str
    claim: str
    b: float = 300.0
    subsidy: float | None = None          # worst-case loss = b ln 2 unless overridden
    fee_rate: float = 0.005
    position_limit_frac: float = 0.5      # per principal, as multiple of b
    resolution_cost: float = 20000.0      # from the protocol
    q: float = 0.0                        # net yes-contracts sold by the maker
    positions: dict = field(default_factory=dict)
    trades: list = field(default_factory=list)
    fund_base: float = 0.0
    fund_fees: float = 0.0
    fund_direct: dict = field(default_factory=dict)
    settled: dict | None = None
    host: str | None = None               # host may buy but not sell (constitutional rule)

    # ---- pricing ----
    def price(self, q: float | None = None) -> float:
        q = self.q if q is None else q
        return 1.0 / (1.0 + math.exp(-q / self.b))
    def cost_fn(self, q: float) -> float:
        return self.b * math.log1p(math.exp(q / self.b)) if q / self.b < 500 else q
    def worst_case_loss(self) -> float:
        return self.subsidy if self.subsidy is not None else self.b * math.log(2)
    def open_interest(self) -> float:
        return sum(abs(v) for v in self.positions.values())
    def fund_balance(self) -> float:
        return self.fund_base + self.fund_fees + sum(self.fund_direct.values())
    def fund_ready(self) -> bool:
        return self.fund_balance() >= self.resolution_cost
    def principals(self) -> int:
        return sum(1 for v in self.positions.values() if v != 0)

    # ---- trading ----
    def trade(self, principal: str, side: str, size: float, forecast: float | None = None,
              rationale: str = "", agent: str | None = None, time: str | None = None) -> Trade:
        if self.settled: raise ValueError("market settled")
        if side not in ("buy", "sell"): raise ValueError("side must be buy or sell")
        if self.host and principal == self.host and side == "sell":
            raise ValueError("hosts cannot short their own claims")
        delta = size if side == "buy" else -size
        limit = self.position_limit_frac * self.b
        cur = self.positions.get(principal, 0.0)
        new = max(-limit, min(limit, cur + delta))
        delta = new - cur
        if abs(delta) < 1e-9: raise ValueError("position limit reached")
        q0, q1 = self.q, self.q + delta
        cost = self.cost_fn(q1) - self.cost_fn(q0)
        fee = abs(cost) * self.fee_rate
        self.q = q1
        self.positions[principal] = new
        self.fund_fees += fee
        t = Trade(principal, side, abs(delta), abs(cost) / abs(delta), cost, fee,
                  time or dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), forecast, rationale, agent)
        self.trades.append(asdict(t))
        return t

    def pay_resolution(self, principal: str, amount: float):
        self.fund_direct[principal] = self.fund_direct.get(principal, 0.0) + amount
    def allocate_base(self, amount: float):
        self.fund_base += amount

    # ---- settlement ----
    def settle(self, outcome: str, measured: float | None = None, adjudication: str = "") -> dict:
        """outcome: 'confirmed' -> yes pays 1; 'refuted' or 'qualified' -> yes pays 0 (binary leg on the stated claim)."""
        pay = 1.0 if outcome == "confirmed" else 0.0
        pnl = {}
        for p, pos in self.positions.items():
            paid = sum(t["cost"] for t in self.trades if t["principal"] == p)
            pnl[p] = round(pos * pay - paid, 2)
        maker_loss = round(sum(pnl.values()), 2)
        self.settled = {"outcome": outcome, "measured": measured, "pay": pay, "pnl": pnl,
                        "maker_loss": maker_loss, "worst_case": round(self.worst_case_loss(), 2),
                        "adjudication": adjudication, "time": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        return self.settled

    # ---- persistence and display ----
    def to_record(self) -> dict:
        return {"id": self.id, "claim": self.claim, "contract": {"kind": "binary"},
                "maker": {"rule": "LMSR", "b": self.b, "subsidy": round(self.worst_case_loss(), 2)},
                "fee_rate": self.fee_rate, "position_limit": self.position_limit_frac * self.b,
                "resolution_fund": {"balance": round(self.fund_balance(), 2), "base_allocation": self.fund_base,
                                     "fees": round(self.fund_fees, 2), "direct": self.fund_direct, "threshold": self.resolution_cost},
                "trades": [{k: v for k, v in t.items() if k in ("principal", "agent", "side", "size", "price", "forecast", "rationale", "time") and v is not None} for t in self.trades],
                **({"settlement": {"outcome": self.settled["outcome"], "time": self.settled["time"], "adjudication": self.settled["adjudication"]}} if self.settled else {})}
    def display(self) -> dict:
        liquid = self.open_interest() >= 50
        return {"claim": self.claim, "price": round(self.price(), 3) if liquid else None,
                "status": "priced" if liquid else "unassessed (below liquidity floor)",
                "open_interest": round(self.open_interest(), 1), "principals": self.principals(),
                "resolution_fund": round(self.fund_balance(), 2), "resolution_threshold": self.resolution_cost,
                "resolution_ready": self.fund_ready()}
    def save(self, path): pathlib.Path(path).write_text(json.dumps(asdict(self), indent=1))
    @classmethod
    def load(cls, path):
        d = json.loads(pathlib.Path(path).read_text()); return cls(**d)

def demo(verbose=True):
    """Claim 47 through the market, as in the master document Sections 7.2–7.3."""
    m = Market("m47", "c47", b=577, subsidy=400, resolution_cost=20000, host="org:H", position_limit_frac=0.8)
    log = []
    def say(s):
        log.append(s)
        if verbose: print(s)
    say(f"Monday: market opens at {m.price():.2f}")
    m.trade("org:GR", "sell", 435, forecast=0.25, rationale="Family-A analogue failed at anode interface in our runs", time="Tue")
    say(f"Tuesday: Grenoble sells -> price {m.price():.2f}")
    m.trade("org:H", "buy", 140, forecast=0.65, rationale="Own data; bonded", time="Wed")
    m.trade("lab:A", "buy", 50, forecast=0.55, time="Wed"); m.trade("lab:B", "buy", 35, forecast=0.5, time="Wed")
    say(f"Wednesday: host and two labs buy -> price {m.price():.2f}, open interest {m.open_interest():.0f}")
    try:
        m.trade("org:H", "sell", 50)
    except ValueError as e:
        say(f"  (host tries to sell: refused — {e})")
    m.trade("org:BM", "sell", 40, forecast=0.40, rationale="hedge against development cost", time="Thu")
    m.pay_resolution("org:BM", 8000)
    say(f"Thursday: manufacturer hedges and pays 8,000 into the fund -> fund {m.fund_balance():.0f} / {m.resolution_cost:.0f}")
    say("  priority rule: confirmed reliance x uncertainty puts c47 above the floor -> base allocation 6,000 + top-up")
    m.allocate_base(6000); m.allocate_base(max(0, m.resolution_cost - m.fund_balance()))
    say(f"Friday: fund {m.fund_balance():.0f} -> resolution commissioned: {m.fund_ready()}")
    s = m.settle("qualified", measured=22, adjudication="a47-r")
    say(f"June: measured 22% (<35%): binary leg settles at 0; P&L {s['pnl']}; maker loss {s['maker_loss']} (worst case {s['worst_case']})")
    say(f"Display: {json.dumps(m.display())}")
    return m, log
