# Deploy checklist

Everything below is what a maintainer does once; the repository does the rest.

## 1. Create the repository (10 minutes)

1. Create an empty GitHub repository (suggested name `evidence-commons`). Do not initialize it with a README.
2. In this folder: `git remote add origin git@github.com:<org>/evidence-commons.git && git push -u origin main --tags`.
3. Replace `<org>` in `CITATION.cff` and `.github/ISSUE_TEMPLATE/config.yml`; commit.
4. Settings → Actions → allow GitHub Actions; allow workflows to create pull requests (needed by `contribution-record.yml`).
5. Settings → Branches → protect `main`: require the `validate` check to pass; require one review for PRs touching `docs/master/` (add a `CODEOWNERS` line: `docs/master/ @<your-handle>`).
6. Create labels: `claim`, `challenge`, `protocol`, `appeal`, `sustained`, `not-sustained`, `design-change`.
7. Optionally enable Discussions for conversation that is not a claim or a challenge.

## 2. First actions on the repository (an hour)

- Open one issue per seed claim (EC-001 … EC-007) with the *Claim* template, pasting from `records/claims/`. These are the proposal's own claims; their issues are where challenges arrive.
- Open the sample challenge CH-001 as an issue, mark it sustained, close it. It shows the pattern.
- Trigger `contribution-record.yml` manually once (Actions → run workflow) to produce the first `contributions/RECORD.md` PR.
- Check that `validate`, `build-docs` and `simulation` workflows ran green on the initial push.
- The `v3.4` tag you pushed triggers `build-docs` to create a GitHub Release with the three PDFs attached. Future versions: bump the version line in the master, add the revision-record entry, `git tag vX.Y && git push --tags`.

## 3. Phase 1 (weeks)

- Announce the repository to the people you want as forecasters and challengers; point them at the 3-page summary and CONTRIBUTING.
- Every design suggestion that arrives becomes a PR against the master with a revision-record line, or an issue. Do not edit the short versions.
- Record challenge outcomes in `records/challenges/` as they are decided.

## 4. Phase 2 (as effort allows)

The tools are reference implementations that work today from the command line. To grow them:

- **Ledger:** already usable on any CSV of forecasts and outcomes; the first real ledger comes from Phase 3.
- **Market engine:** `ec market` runs one market per JSON file. A hosted instance means wrapping `ec/market.py` in a small web service with per-principal accounts; or use an existing play-money venue first (`pilots/manifold-howto.md`).
- **Recorder:** `ec/recorder.py` is the log format and verification; a notebook plugin wraps `WorkflowLog.append` around cell execution and model calls. The schema is the contract; any workspace can implement it.
- **Replay:** `ec/replay.py` handles deterministic pipelines; real workflows need pinned models and seeds, which is why the recorder logs the environment.

## 5. Phase 3 (three months)

Follow `pilots/runbook-phase3.md`. Its stop rules are real; a stopped test that reports why is a success.

## Placeholders to replace

`<org>` (two files), `<your-handle>` in CODEOWNERS, prize amounts and dates in `pilots/`.
