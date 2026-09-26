# 0001 — Single master document; short versions derived

**Date:** 2026-09-26. **Status:** accepted.

**Decision.** `docs/master/price-trust-full-proposal.md` is the only edited design document. Short versions in `docs/short/` are regenerated from it after design changes. Earlier versions are archived and not edited.

**Why.** Five documents that must agree is a maintenance burden; a consistency sweep on 26 September 2026 found the same superseded phrasing in three versions, including the master. One source, derived outputs.

**Consequences.** PRs edit the master; a follow-up PR regenerates the short versions; CI's consistency scan runs on all of them.
