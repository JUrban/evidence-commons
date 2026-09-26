import math, pytest
from ec.market import Market, demo

def test_price_and_worst_case():
    m = Market("m", "c", b=300)
    assert abs(m.price() - 0.5) < 1e-9
    assert abs(m.worst_case_loss() - 300 * math.log(2)) < 1e-9

def test_trade_moves_price_and_accrues_fee():
    m = Market("m", "c", b=300)
    t = m.trade("p1", "buy", 100)
    assert m.price() > 0.5 and t.fee > 0 and m.fund_fees == pytest.approx(t.fee)

def test_position_limit_binds():
    m = Market("m", "c", b=300, position_limit_frac=0.5)
    m.trade("p1", "buy", 1000)
    assert m.positions["p1"] == pytest.approx(150)
    with pytest.raises(ValueError): m.trade("p1", "buy", 10)

def test_host_cannot_short():
    m = Market("m", "c", host="org:H")
    m.trade("org:H", "buy", 10)
    with pytest.raises(ValueError): m.trade("org:H", "sell", 5)

def test_resolution_fund_trigger_and_settlement():
    m = Market("m", "c", b=300, resolution_cost=1000)
    m.trade("a", "buy", 50); m.trade("b", "sell", 50)
    assert not m.fund_ready()
    m.pay_resolution("reliant", 600); m.allocate_base(400)
    assert m.fund_ready()
    s = m.settle("confirmed")
    assert s["pay"] == 1.0 and abs(s["maker_loss"]) <= s["worst_case"] + 1e-6

def test_maker_loss_bounded_by_subsidy():
    m = Market("m", "c", b=100, position_limit_frac=10)
    m.trade("a", "buy", 5000)
    s = m.settle("confirmed")
    assert s["maker_loss"] <= m.worst_case_loss() + 1e-6

def test_demo_runs():
    m, log = demo(verbose=False)
    assert m.settled["outcome"] == "qualified" and m.fund_ready()
