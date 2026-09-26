# Price Trust, Record Contribution, Pay for Value

## Organizing science when AI does most of the work

*Version 1.2 — three-page summary, aligned with the full proposal v3.4 — 26 September 2026*

---

## Summary

The scientific paper let us infer three things at once: that a result was dependable, that its producers deserved further resources, and that the named humans had demonstrated ability. AI-produced research breaks the third inference completely and is eroding the first two. Every incremental reform — contribution statements, disclosure rules, submission caps, more reviewers — tries to restore inference from outputs.

This proposal stops inferring. It **prices** dependability with markets that buy their own resolution, **records** contribution at the moment of production instead of reconstructing it afterwards, and **pays for value** after it is demonstrated instead of buying promises. Three pilots, each under €600,000, can start within a year, and each is designed so that it can be stopped.

---

## 1. What actually broke

Not every function of publication failed. A cheap paper can still contain a correct result, explain it well, and name an accountable organization. What failed is inference. "This impressive document exists, so this named person has demonstrated ability" no longer holds, because the document, its contribution statement and its reviews can all be machine-written. "This document passed review, so it is dependable" is failing because review is drowning and reviewers use the same tools as authors.

Two corrections to earlier drafts follow from this. First, ration scarce services — expert attention, experiments, prominent placement — but never production itself; caps on human authors and submission deposits smuggle the human author back in as the bottleneck. Second, an audit of an organization's process does not certify the particular result someone wants to rely on; reliance needs focused assessment of that result, paid for by whoever relies on it or by a public resolution fund.

Three decisions must therefore be made separately, each with its own instrument.

| Decision | Old proxy | New instrument |
|---|---|---|
| Is this dependable? | Peer review, venue prestige | Truth markets with resolution funds; author bonds; calibration ledgers |
| Is further work worth funding? | Proposals, publication record | Retroactive and quadratic funding; impact certificates; capacity spot markets |
| What has this person demonstrated? | Authorship, counts, h-index | Flight recorders; counterfactual credit; logged examinations |

---

## 2. Truth markets: price dependability, then buy the answer

**Mechanism.** Every claim registered in the research record carries a subsidized prediction market on a specified resolution event: an independent replication, a preregistered prediction, a formal check, a blind comparison against fresh data. An automated market maker, funded from the assessment budget, pays whoever moves the price toward the eventual answer. Humans and AI agents may trade; an agent trades under an accountable principal's account with position limits and disclosed model dependencies.

**The price is the reliability estimate.** The spread measures disagreement; the volume measures reliance. A claim nobody prices remains visibly unassessed, which is its honest state.

**Markets buy their own resolution.** Each priced claim has a resolution fund, filled by a base allocation from the field's assessment fund, a small fee on every trade, and direct payments from parties that need the answer. When the fund reaches the cost stated in the resolution protocol, resolution is commissioned automatically — a resolution auction among accredited laboratories, adjudicated by the service named at registration. Base allocations follow confirmed reliance and price uncertainty; open interest is the measure of disagreement, not of importance. The claims that get checked are the ones people are uncertain about and rely upon; a claim nobody trades remains visibly unassessed, which is its honest state.

**To author is to underwrite.** The host organization — never an individual — posts a bond behind a claim, scaled to the strength claimed. A successful refutation pays the bond to the refuter, who posted a stake to challenge; a claim that survives returns the bond with a premium paid from the pool of forfeited bonds, weighted by how contested the claim was, so that bonding trivially true claims earns nothing. Credit is the bond that survived. Cheap AI criticism becomes valuable exactly when it is right and worthless when it is noise.

**The calibration ledger replaces the h-index.** Every person and every system accumulates a public record of realized performance and proper-scored forecasts on the claims it traded. Counts become irrelevant because every position costs something to hold. One caveat the simulation in the full proposal established: a ledger separates good forecasters from bad only after several hundred resolved positions, so the first fifty are provisional and the ledger is a multi-year credential, built fastest in fields where resolution is cheap.

**Precedents.** Markets predicted replication outcomes well in the Camerer et al. replication studies; DARPA's SCORE program ran replication markets over roughly three thousand social-science claims. Hanson's logarithmic market scoring rule gives a standard subsidized market maker. Knuth's reward cheques and Erdős prizes are bonds on claims at small scale.

**First build.** One field with fast, cheap resolution — empirical machine learning, where a claim re-runs on a held-out benchmark split for hundreds of euros. About five hundred registered claims, a €150,000 subsidy fund, a €100,000 resolution fund buying at least sixty resolutions, a platform adapted from open-source market software, twelve months. Experimental psychology follows in year two with a larger resolution fund. Success means resolution decisions track prices better than citation counts, the ledger begins to separate forecasters, and cost per resolved claim falls below a conventional replication study.

**Failure modes.** Thin markets; manipulation by deep pockets; resolution disputes that recreate the review queue; agent swarms dominating trading. Mitigations: subsidy weighted by reliance, position limits per principal, a pre-agreed resolution protocol with an independent adjudicator, and disclosure of shared models so agreement among related agents is not counted as independent evidence.

---

## 3. Flight recorders: record contribution instead of reconstructing it

**The problem, restated.** Contribution cannot be recovered from an output, because the AI may have written the contribution statement too. It can, however, be recorded while the work is being done.

**Attested workspaces.** Research environments log prompts, model outputs, human edits, decisions and data accesses into a signed provenance stream. The researcher controls what is logged and whether it is disclosed. Unlogged work receives organizational authorship by default; personal credit is available to those who opt into the recorder. Precedent: content credentials for media, and aviation flight recorders.

**Counterfactual credit.** For logged computational work, replay the workflow with one person's interventions removed or replaced by the system's own defaults. The difference in outcome is that person's measured marginal contribution. This is the direct answer to "did the person or the AI supply the idea": stop asking and run the experiment.

**Contribution records list what was measured.** Unknown shares remain unknown. No manufactured percentages, no inherited credit for supervisors or system owners.

**Examinations become logged sessions.** A doctoral defence or a hiring exercise runs in an attested workspace on unfamiliar material with tools allowed. The log shows what the candidate did with the tools, including what they did when the tools were wrong. Medicine certifies competence separately from output; this is the scientific equivalent.

**First build.** A plugin for common AI-assisted research environments — notebooks and agent frameworks — that produces signed logs and supports replay, piloted with volunteer groups. About €200,000.

**Failure modes.** Surveillance and chilling of exploration; staged interventions to game ablation; steps that cannot be replayed, such as laboratory work. Mitigations: researcher-controlled logs with selective disclosure, sampled audits of replays, and recorders confined to computational segments with organizational authorship elsewhere.

---

## 4. Funding without proposals

**Retroactive public-goods funding.** A fixed share of budgets — start at 10% — pays for contributions after they have demonstrably been useful: datasets, tools, methods, negative results, maintenance. Paid, rotating badgeholders decide with usage evidence in hand. It is far easier to judge what was useful than what will be. Precedent: the Optimism retroactive funding rounds.

**Impact certificates.** Tradeable claims on future retroactive awards. Investors fund early or long-horizon work and are paid when it proves out. This is the financing route that "small allocations earn larger ones" never provides for work whose value takes years to show.

**Quadratic funding for shared infrastructure.** Many small pledges from researchers steer a matching pool toward what many need. Precedent: Gitcoin's rounds for open-source software.

**Dominant assurance contracts for pooled experiments.** Groups pledge toward a shared measurement; if the target is not met, pledges are refunded with a bonus. This solves the free-rider problem that pooling schemes usually only name.

**Spot markets for capacity.** Instrument and compute time are auctioned like cloud spot instances. AI investigators buy directly within their budgets, and prices reveal scarcity publicly. Cloud laboratories already sell experiments this way.

**Futarchy on a slice.** Funders fix an outcome measure; conditional markets choose between candidate investigations for 5% of the budget. Metric gaming is the known risk, so the slice stays small and is watched.

**A human-judged share remains.** People-not-projects fellowships with partial lotteries, for questions that cannot yet be measured. Markets are for what can be scored; the fellowship is for what cannot.

**First build.** A retroactive round of €500,000 for datasets and tools in the same field as the truth market, with a small impact-certificate market attached and about €50,000 for operations.

**Failure modes.** Retroactive funding as a popularity contest; sybil attacks on quadratic funding; spot markets pricing out newcomers. Mitigations: usage evidence required, badgeholder rotation, identity through accountable principals, and reserved allocations for newcomers fixed before outcomes are known.

---

## 5. Structure: who owns the systems, and what people are for

**Essential-facility access.** Research systems above a capability threshold must license access to accredited researchers at regulated rates, as antitrust law treats bottleneck infrastructure. Consortium ownership is a complement; this is the legal defense against concentration.

**Research cooperatives.** Worker-owned laboratories that own their systems and share revenue from what those systems produce. The decentralized-science experiments show token governance is fragile; the cooperative form is old and sturdy.

**A science dividend.** Royalties from AI-produced intellectual property flow into a permanent fund that pays for human inquiry, training and fellowships, on the model of a sovereign wealth fund. Human science is funded because understanding, education and independent scrutiny are goods in themselves; the dividend is how, not why.

**Employment for stated roles.** Participating institutions remove publication counts and journal rank from hiring, promotion and doctoral decisions and are audited for it. Evidence comes from the calibration ledger, logged exercises, and what a person built or maintained. There is no promise that everyone moves into "judgment": that activity is inside the scenario too. Research employment may shrink or shift; the proposal funds training and preserves existing commitments rather than pretending otherwise.

---

## 6. What to build first

| Build | Setting | Indicative cost | Twelve-month test |
|---|---|---|---|
| Truth market with resolution fund and author bonds | One fast-replication field, ~500 claims | €300,000 | Resolution decisions track price; ledger separates forecasters; cost per resolved claim below a replication study |
| Flight recorder with counterfactual replay | Volunteer computational groups | €200,000 | Logs replay; ablation credit agrees with blinded expert judgment on a sample; friction no higher than today |
| Retroactive round with impact certificates | Same field as the market | €550,000 | Awarded items show measured use; certificate prices predict awards; awards reach groups outside the top funded |

Total about €1.05 million — roughly a quarter of a conventional two-year institutional trial, aimed at problems such a trial leaves untouched.

**Stop rules, fixed before launch.** If markets do not beat a simple baseline such as citation count at predicting resolution, stop. If replay-based credit does not correlate with blinded expert judgment, stop. If retroactive awards concentrate in already well-funded groups, redesign before a second round. Expansion is a new decision, not a reward for a persuasive final report.

---

## 7. What would make this wrong

Markets could stay thin, be manipulated, or turn resolution disputes into a new review queue. Recorders could chill exploration or become a management surveillance tool. Retroactive funding could reward the visible; futarchy metrics could be gamed. Essential-facility rules could be captured or freeze development. Employment effects remain uncertain, and nothing here guarantees jobs.

Each pilot is small, measured against a stated baseline, and stoppable. That is the point of running three instead of one.

**Parked, not abandoned.** Claims registered as executable tests that auto-score as data arrives. Structured debate between AI systems before a time-limited judge as the review artifact. Attention tokens that let researchers pledge review priority to claims they intend to rely on. Warranted results with underwriters whose premiums are the public reliability signal. Commit-reveal preregistration on a public timestamp chain.

---

## Precedents referred to

Camerer et al., replication prediction markets (2016, 2018) · DARPA SCORE / Replication Markets · Hanson, logarithmic market scoring rule and futarchy · Optimism RetroPGF · Gitcoin quadratic funding · Tabarrok, dominant assurance contracts · C2PA content credentials · cloud laboratories (e.g. Emerald Cloud Lab) · essential facilities doctrine in antitrust · Alaska Permanent Fund · Irving, Christiano and Amodei, AI safety via debate · Knuth reward cheques and Erdős prizes.

*Precedent citations are by name; link and verify each before wider circulation.*

---

*Change note, v1.1–1.2.* Aligned with the full proposal v3.3: resolution funds are now filled by base allocations, trade fees and direct payments and prioritized by confirmed reliance times uncertainty rather than open interest; the reliant party hedges and pays for resolution rather than buying contracts; bonds are posted by hosts with premiums from forfeited bonds weighted by contest and challengers post stakes; the calibration ledger carries the caveat that it needs several hundred resolved positions; the first build is machine learning, with psychology in year two.
