# Using an existing play-money market venue

Before building a market engine, use one that exists. Manifold Markets runs on play money ("mana"), lets anyone create binary and multiple-choice markets with a stated resolution rule and date, records trades and comments, and is open source, so the record can be exported. Other forecasting platforms (Metaculus, INFER-style tournaments) work for forecasts without trading.

## Mapping the design onto the venue

| Design element | On the venue |
|---|---|
| Claim + resolution protocol | Market title = claim id and statement; description = the protocol verbatim; close date = protocol expiry |
| Binary contract on "resolution succeeds" | A yes/no market |
| Scalar claim | A multiple-choice market with interval buckets (the ladder in Section 7.10) |
| Market-maker subsidy | The venue's own liquidity provision; add subsidy from the coordinator's points where the venue allows |
| Position limits | Not enforced by the venue: publish a limit and apply it by rule at scoring time |
| Host cannot short own claim | By rule: hosts declare their accounts; short positions on own claims are voided at scoring |
| Trade rationales | Comments on the market |
| Settlement | The adjudicator resolves the market after signing the resolution record |
| Ledger | Export trades; run `ec ledger` on forecasts derived from trades (the price after each trade is the trader's implied forecast; better, ask forecasters to state a probability in the comment) |
| Resolution fund | Off-venue: the coordinator's budget, allocated by the priority rule |

## What the venue does not give you

Resolution funds, fees, bonds, reliance-weighted priority, and the record formats. Keep those in this repository's `records/` and tools, and treat the venue as the trading layer only. When the venue's limits bind — position limits, institutional accounts, scalar ladders — that is the signal to run the reference engine (`ec market`) or a hosted instance of an open-source market.

## Legal form

Play money with prizes for forecasting performance is a prize competition, not wagering (Section 21.1). Keep it that way: no cash trades, prizes by ledger rank, terms published before the first market opens.
