# Simulation of the market layer

Two scripts, both deterministic (fixed seeds), reported in Section 33 and Appendix I of the master document.

- `sim_market.py` — 5,000 claims, 200 forecasters, LMSR maker (b = 300), position limits, fees; measures pricing accuracy vs a citation baseline, allocation of 150 resolutions by four rules, ledger split-half reliability vs positions, bond-pool premiums for contested vs trivial claims, and manipulation with and without limits. Writes `figures/sim_results.json` and four PNGs.
- `sim_cascade.py` — a preferential-attachment reliance graph; measures dependents of false claims flagged under three selection rules; then a seven-way sensitivity sweep of `sim_market.py`. Writes `figures/sim_cascade.json`, `figures/sim_sensitivity.json` and a PNG.

Run: `python sim_market.py && python sim_cascade.py` (needs numpy, scipy, matplotlib). CI re-runs both on any PR touching this directory and posts the numbers.

The model is a toy. Its omissions are listed in Section 33.3 of the master document; each is a question for the pilots.
