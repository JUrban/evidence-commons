# Contributing

This repository runs on the rules the proposal describes. The short version:

## The master document

- `docs/master/price-trust-full-proposal.md` is the single source of truth. Edit it, not the short versions.
- Every change to the design adds one line to **Appendix H — Revision record** stating what changed and why. PRs without that line are not merged.
- `docs/short/` files are derived. If the design changes, regenerate them from the master (a PR that changes the master and leaves the short versions inconsistent should say so in the PR body; a follow-up PR regenerates them).
- Section numbers are stable. Do not renumber. New material goes into new subsections or new appendices.
- `docs/archive/` is history. Do not edit it.

## Pull requests are change requests

A PR is a proposed change to the current account of the question. The template asks for:

1. **What changes** — the design element, the section.
2. **Why** — the evidence, argument, or failure it responds to.
3. **What it supersedes** — which earlier statement is withdrawn, if any.
4. **Revision-record line** — the Appendix H entry.
5. **Consistency** — whether the short versions, schemas, templates, or simulation need to follow.

CI builds the PDFs, checks that every `Section N.M` reference resolves, scans for superseded phrasings (`build/check_consistency.py`), validates every record in `records/` against `schemas/`, runs the tests, and — for PRs touching `sim/` — re-runs the simulation and posts the numbers.

## Issues are claims and challenges

- **Claim:** a statement the proposal makes or a hypothesis a pilot tests, with a resolution protocol from `templates/protocols/`. Claims live as YAML in `records/claims/` and are validated by CI; the issue is the discussion.
- **Challenge:** names a claim, states the alleged defect, proposes a test. A maintainer records the outcome (sustained / not sustained / unresolved) on the issue and in `records/challenges/`.
- **Protocol:** proposes a new resolution-protocol template.

## AI-assisted work

Add a commit trailer:

```
Assisted-by: <model name and version>
Log: <hash or link to a workflow log, if one exists>
```

This is the flight recorder at zero cost. It carries no penalty; most contributions to a document like this will carry it.

## Code

- `tools/ec/` is a Python package. Run `pytest` in `tools/` before opening a PR.
- Schemas in `schemas/` are the contract; changing one is a design change and needs a revision-record line.
- Keep the simulation reproducible: fixed seeds, results written to `sim/results/`, figures to `sim/figures/`.

## Contribution record

Quarterly, `contributions/make_contribution_record.py` generates `contributions/RECORD.md` from git: merged change requests and sustained challenges per person, with `Assisted-by` trailers counted. That — not lines changed — is what the proposal says credit should follow.
