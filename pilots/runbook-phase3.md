# Runbook: the first small test (Phase 3)

Pilot A at one-tenth scale, with a friendly community, using only what is in this repository plus a play-money market venue. Target: 50–100 registered claims, 10–20 resolutions, the first real ledger and coverage report, in about three months. Budget: a few thousand euros of prizes and resolution compute; no platform build.

## 0. Choose the community (week 0)

Pick a group that meets four criteria: claims that resolve in days (machine-learning benchmarks, formal proofs, computational reproductions); an existing habit of re-running each other's work; 30–150 people willing to forecast; one person willing to be coordinator. A reading group, a lab cluster, a workshop community, or a formal-mathematics library's contributors all qualify.

Name: a coordinator; two adjudicators who will not register claims of their own; a screening contact (for the rare hazardous request).

## 1. Register claims (weeks 1–3)

- Ask each participating lab or contributor for 3–10 claims from their last two years of work. Use the *Claim* issue template; the coordinator turns each into `records/claims/<id>.yaml` with a protocol from `templates/protocols/` (mostly 01, 02, 03 or 10).
- Time every registration (EC-007 predicts a median under fifteen minutes after the first).
- `ec validate records` in CI keeps the registry consistent.
- Bonds are optional and symbolic in this test (play money, e.g. 1,000 points per bonded claim), but record them: the bond-pool arithmetic is what the test exercises.

## 2. Open markets (week 3)

- One market per registered claim on the play-money venue (see `manifold-howto.md`), or via `ec market open` if you run the reference engine. Title = claim id + statement; description = the protocol; resolution date = protocol expiry.
- Every forecaster gets the same allocation of points. Prizes: announce a small pool (e.g. €2,000) distributed by ledger rank at the end, with the first fifty positions provisional.
- Ask forecasters to attach a one-line rationale to each trade; the venue's comment field is fine.
- Record trades weekly into `records/markets/<id>.yaml` (schema `market.schema.json`) — a script or a spreadsheet export is enough for a first test.

## 3. Resolve (weeks 4–12)

- Resolution fund: in this test the coordinator's budget is the fund. Priority rule as in the master: confirmed reliance × price uncertainty first; a claim other registered claims depend on and that trades near 50 cents goes first. Open interest is the tiebreak, not the ranking.
- Resolution auction: post the claim and protocol; accept bids from any member not on the claim; lowest credible bid wins; pay on delivery of the resolution record (`records/resolutions/<id>.yaml`).
- Adjudicator checks the validity checks in the protocol and signs the record. Settle the market. Bonds return or forfeit per the outcome map.
- Target 10–20 resolutions. If a resolution is challenged, use the *Challenge* template; record the outcome in `records/challenges/`.

## 4. Score and report (week 12)

- Export forecasts as `principal, claim, forecast, outcome` and run `ec ledger forecasts.csv`. Expect split-half reliability near zero at these position counts (EC-003); report it anyway.
- `ec reliance records` for load-bearing claims; `ec report records --md` for the coverage table; fill Appendix N's template with the real numbers.
- Test EC-001 at this scale: compare the Brier score of final prices with a baseline (citation count, or the group's prior vote) on the resolved claims. Report the result whatever it is.
- Run `contributions/make_contribution_record.py` for the quarter.
- Open a PR that replaces the "targets rendered as example" in Appendix N with what happened, and adds a revision-record line. If EC-001 or EC-007 fail, revise or withdraw them in the same PR.

## 5. Stop rules for this test

Stop and write up if: fewer than 30 forecasters trade in the first three weeks; fewer than 8 resolutions can be bought within budget; or the coordinator's time exceeds 5 hours a week for more than a month. A stopped test that reports why is a success for the repository.
