# Evidence Commons

**Price trust, record contribution, pay for value — organizing science when AI does most of the work.**

This repository holds a proposal for how science should decide what to trust, whom to fund and whom to credit once the research paper is cheap to produce, and the beginnings of the tools the proposal describes. It runs on its own rules: pull requests are change requests, issues are claims and challenges, CI is the resolution service for anything checkable, and git is the flight recorder.

## The argument in one paragraph

The paper let institutions *infer* three things at once — that a result was dependable, that its producers deserved more money, and that the named humans were capable. AI-produced research broke those inferences. Instead of repairing them, the proposal replaces inference with observation: **truth markets** price every registered claim and pay for the replication that settles it; **flight recorders** log human–AI work so a person's contribution can be measured by replaying the work without them; **value-based funding** pays for datasets, tools and results after their usefulness is visible. Around these sit rules on who owns research systems, how people are employed and trained, and how human inquiry is funded from AI-produced value.

## Read

| Length | File | For |
|---|---|---|
| 3 pages | [`docs/short/summary-3-page.md`](docs/short/summary-3-page.md) | Anyone |
| 9 pages | [`docs/short/explainer-9-page.md`](docs/short/explainer-9-page.md) | Readers new to prediction markets, provenance signing, retroactive funding |
| 85 pages | [`docs/master/price-trust-full-proposal.md`](docs/master/price-trust-full-proposal.md) | The master document: instruments, six fields, institutions, law, pilots with pre-registrations, simulation, budgets |

The master is the single source of truth. The short versions are derived from it. Earlier drafts are in `docs/archive/` for history only.

## Current state of the design (the maintained account)

*Release 3.4, 26 September 2026.*

**Established in the document:** three separate decisions (dependable? fundable? what did this person do?) each with an instrument that observes rather than infers; markets that commission their own resolution from a fund prioritized by confirmed reliance × price uncertainty; bonds posted by hosts with premiums from forfeited bonds weighted by contest; counterfactual credit by replay of logged work; retroactive, quadratic and assurance-contract funding; a counting ban as a funder condition.

**Established by simulation (toy model, `sim/`):** prices beat a citation baseline; reliance-guided resolution captures ~24× the reliance-weighted uncertainty of random selection; position limits cut a manipulator's effect by ~⅔; a ledger needs several hundred resolved positions to separate forecasters.

**Open:** whether real forecasters' attention tracks reliance; whether replay-based credit agrees with expert judgment; whether any institution will actually stop counting papers. These are the three pilots' hypotheses (`pilots/`).

**What would change this account:** Pilot A's pre-registered test failing on the first 40 resolutions; replay credit uncorrelated with blinded expert judgment; a sustained challenge to any claim in `records/claims/`.

## Use the tools

```bash
cd tools && pip install -e .
ec validate ../records                # validate every record against the schemas
ec market demo                        # run Claim 47 through a market with a resolution fund
ec ledger ../tools/tests/data/forecasts.csv   # Brier, reliability, provisional status
ec recorder demo                      # hash-chained, Merkle-checkpointed workflow log with selective disclosure
ec replay demo                        # counterfactual credit on a deterministic pipeline
ec reliance ../records                # load-bearing claims and cascade flags
ec report ../records                  # the state-of-the-field tables
```

## Contribute

- **Propose a design change:** open a PR against `docs/master/` using the template. Every design change adds a line to Appendix H (revision record). Short versions are regenerated, not edited.
- **Register a claim:** open an issue with the *Claim* template, or add a YAML file under `records/claims/` (CI validates it).
- **Challenge a claim:** open an issue with the *Challenge* template naming the claim, the alleged defect and a test.
- **Change the simulation:** PRs touching `sim/` get the simulation re-run by CI and the numbers posted as a comment.
- **AI-assisted contributions:** add a commit trailer `Assisted-by: <model>` and, where you have one, `Log: <link or hash>`.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md).

## Roadmap

- **Phase 0 (this repo):** documents, schemas, protocol templates, CI, seed records.
- **Phase 1:** run the process on the proposal's own claims; first challenges; quarterly contribution record.
- **Phase 2:** the tools in `tools/ec/` grow from reference implementations into services: market engine, ledger, recorder plugin, replay.
- **Phase 3:** a first small test with a friendly community (`pilots/runbook-phase3.md`): 50–100 registered claims, play-money markets, 10–20 resolutions, the first real coverage report.

## License

Text: CC BY 4.0 (`LICENSE-DOCS`). Code, schemas and templates: Apache-2.0 (`LICENSE-CODE`).
