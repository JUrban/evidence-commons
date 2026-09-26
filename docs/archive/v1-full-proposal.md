# Price Trust, Record Contribution, Pay for Value

## A full proposal for organizing science when AI does most of the work

*Version 1.7 — circulation draft, 26 September 2026 (five review rounds plus alignment with v3; see Appendix E)*

---

### Abstract

The scientific paper has carried six jobs at once: reporting a finding, claiming a discovery, credentialing its authors, justifying the next grant, identifying who is responsible, and conferring distinction. Each job worked because a paper was expensive to produce and mostly human-made, so its existence let institutions *infer* things they could not observe directly — that the result was probably sound, that its producers deserved more money, that the named people were capable. AI-assisted and AI-produced research has made the paper cheap and has broken those inferences. Review is overwhelmed, authorship no longer evidences ability, and counting outputs measures access to compute.

This proposal does not try to restore inference. It replaces it with three instruments that observe directly what the paper only implied. **Truth markets** attach a subsidized prediction market to every registered claim; the price is the reliability estimate, authors post bonds behind their claims, and the money at stake pays for the replication or adjudication that settles the question. **Flight recorders** capture human–AI collaboration while it happens, so that a person's contribution can be measured by replaying the work without them rather than asserted in a contribution statement. **Value-based funding** pays for datasets, tools, methods and results after their usefulness is visible, lets many small pledges steer shared infrastructure, and lets scarce experimental capacity find its price. Around these sit four structural measures: essential-facility access rules for research systems, cooperative ownership, a science dividend that funds human inquiry from AI-produced value, and employment criteria that no longer count papers.

The proposal specifies three pilots totalling about €1.1 million, each with a baseline and a pre-registered stop rule, a five-year transition path, an illustrative reallocation of a funder's budget, a risk register, and replies to the objections we expect. It draws on precedents that already exist at scale — replication prediction markets, decision markets that chose which studies to replicate, retroactive and quadratic funding programs that have distributed tens of millions, content-provenance standards, funding lotteries, and antitrust doctrine — and is explicit about what each precedent does and does not show.

---

### How to read this document

Part I explains what broke and why incremental fixes fail. Part II specifies the three instruments in detail, each with a worked example, precedents, failure modes and a first build. Part III covers the institutions around them: ownership, employment, journals and the record. Part IV makes it operational: pilots, transition, economics, risks, objections. Appendices contain a glossary, record templates, worked numbers, annotated precedents and the revision history of this draft. Boxes marked **What is…** introduce concepts for readers new to them and can be skipped by readers who are not.

A reader with fifteen minutes should read the executive summary (Section 1), the running example (Section 4), and the pilots (Section 12). A funder should add Sections 7, 13 and 14. A skeptic should start at Section 16.

---

### Contents

**Part I — Why**
1. Executive summary
2. What broke, precisely
3. Design principles

**Part II — The instruments**
4. The running example: Claim 47
5. Truth markets
6. Flight recorders
7. Paying for value
8. Which instruments fit which science

**Part III — Institutions**
9. Who owns the machines
10. What people are employed for
11. Journals, societies and the record

**Part IV — Making it real**
12. Three pilots
13. Transition: the first five years
14. Economics
15. Risk register
16. Objections and replies
17. Further ideas
18. Conclusion

**Appendices**
A. Glossary · B. Record templates · C. Worked numbers for one field · D. Annotated precedents · E. Revision record

---

# Part I — Why

## 1. Executive summary

**The problem.** In 2025 the NeurIPS conference received 21,575 submissions, up from 9,467 five years earlier, and needed 20,518 reviewers to handle them. After review by three to five experts each, accepted papers were found to contain a hundred fabricated citations. Independent estimates put the share of machine-written reviews at leading venues in the double digits. This is not a machine-learning peculiarity; it is the leading edge of what happens to every field once the cost of producing a plausible paper falls toward zero. The institutions that decide what to trust, whom to fund and whom to hire were built on the assumption that a paper is costly evidence of human work. That assumption is gone.

**The diagnosis.** Not every function of the paper has failed. A cheap paper can still contain a correct result and name an accountable organization. What failed is *inference* — the step from "this document exists" to "this person is capable," and increasingly from "this passed review" to "this is dependable." Reforms that add disclosure rules, contribution statements, submission caps or more reviewers all try to repair inference from outputs. They cannot, because the outputs can be produced by the same tools they are trying to detect.

**The principle.** Three decisions must be made separately, each by an instrument that observes rather than infers:

| Decision | Old proxy | New instrument |
|---|---|---|
| Is this dependable? | Peer review; venue prestige | Truth markets: priced claims, author bonds, resolution bought by the money at stake, calibration ledgers |
| Is more work here worth funding? | Proposals; publication record | Retroactive and quadratic funding; impact certificates; capacity spot markets; a human-judged share with lotteries |
| What has this person demonstrated? | Authorship; counts; h-index | Flight recorders; counterfactual credit by replay; logged examinations |

**The instruments.**

*Truth markets.* Every registered claim carries a specified resolution protocol and a subsidized prediction market. The price is the reliability estimate; the volume measures reliance. When enough is at stake, the market's resolution fund commissions the replication or adjudication. Authors post bonds that refuters can win. Everyone who trades or endorses accumulates a public calibration record that volume cannot inflate. Decision markets have already chosen which studies to replicate, and the studies they priced highest replicated at 83% against 33% for the lowest.

*Flight recorders.* Contribution cannot be recovered from a jointly produced output, but it can be recorded while the work happens. Attested workspaces log prompts, outputs, edits and decisions under the researcher's control. A person's contribution to a logged result is measured by replaying the work without their interventions. Unlogged work gets organizational authorship by default. Examinations become logged sessions.

*Value-based funding.* A fixed share of budgets is paid retroactively for contributions that proved useful — datasets, tools, negative results, maintenance — by paid, rotating evaluators with usage evidence in hand. Impact certificates let early funders of long-horizon work be repaid when it proves out. Quadratic matching lets many small pledges steer shared infrastructure. Dominant assurance contracts make pooled experiments fund themselves. Spot markets price scarce instrument and compute time. A human-judged fellowship share with lotteries remains for what cannot be measured.

**The record.** Underneath the instruments sits a small shared record: claims with resolution protocols, markets and bonds, workflow logs and contribution records, assessment records, and a reliance graph that replaces the citation graph with the thing citations always approximated — what actually depended on what. When a load-bearing claim fails, everything that relied on it is flagged and re-priced.

**The structures.** Research systems above a capability threshold become essential facilities with regulated access. Laboratories may organize as cooperatives that own their systems. A science dividend, funded from AI-produced value, pays for human inquiry on its own terms. Institutions that receive public research money stop counting papers and are audited for it.

**The pilots.** Three, in one field with fast replication cycles, totalling about €1.1 million over twelve months: a truth market with a resolution fund, a flight-recorder plugin with replay, and a retroactive funding round with impact certificates. Each has a baseline and a stop rule fixed before launch.

**The ask.** One funder, one field, one year. Nothing here requires everyone to agree first.

---

## 2. What broke, precisely

### 2.1 Six jobs, one artifact

For roughly a century the research paper has performed six distinct institutional functions:

1. **Report** a finding so others can use it.
2. **Claim** priority for a discovery.
3. **Credential** the named authors as capable researchers.
4. **Justify** the next allocation of money to its producers.
5. **Identify** who is responsible if the finding is wrong.
6. **Confer** distinction — prizes, invitations, standing.

These functions were bundled because bundling was efficient. A paper was expensive to produce: it required months of a trained person's time, access to a laboratory, and the ability to survive expert scrutiny. Its existence was therefore *evidence* — not proof, but evidence — that a capable human had done real work that survived criticism. Hiring committees, funders and readers could infer from the artifact things they could not directly observe.

### 2.2 The inference broke, not the artifact

It is tempting to say that AI "broke the paper." That overstates it. A paper produced with heavy AI assistance can still contain a correct result, explain it clearly, and name an organization that will answer for it. Functions 1, 2 and 5 survive in weakened form.

What broke is the inferential step behind functions 3, 4 and 6, and increasingly behind readers' trust in function 1:

- "This person is listed as author of impressive papers, therefore this person is capable." — False when the paper, its contribution statement and its rebuttals can all be generated.
- "This group produced many results, therefore it deserves more resources." — Measures access to compute, not scientific judgment.
- "This paper passed peer review, therefore it is probably sound." — Fails when reviewers are overwhelmed and use the same tools as authors, and when a fabricated citation can pass three to five expert readers.

The evidence is already public. NeurIPS grew from 9,467 submissions in 2020 to 21,575 in 2025. Post-hoc scans found 100 fabricated citations in 53 accepted 2025 papers. One detector's estimate for ICLR reviews was that about a fifth were AI-generated, and a separate study found that AI-assisted reviews systematically raised paper scores and acceptance rates. None of this required malice. It is what happens when the cost of producing an artifact that *looks like* evidence falls faster than the cost of checking it.

### 2.3 Why the incremental fixes fail

Each proposed repair tries to restore inference from the output. Each fails for the same reason: the output can be manufactured by the thing being screened for.

| Proposed fix | Why it fails |
|---|---|
| Mandatory AI-use disclosure | Unverifiable; penalizes honesty; the disclosure can be generated too |
| Detailed contribution statements (CRediT etc.) | The statement is itself an output; the AI can write it; CRediT's own documentation says it does not determine authorship |
| Submission caps per author | Punishes production rather than rationing scarce services; re-imports the human author as the bottleneck; results in name-shuffling |
| More reviewers, reviewer credits, mandatory reviewing | Reviewers use the same tools; mandatory reviewing produces machine reviews of machine papers |
| AI reviewers | Correlated with the AI authors; agreement among copies of one model is one opinion |
| Better metrics (altmetrics, normalized citations) | Any metric computed from outputs is inflated by volume; volume is now free |
| Organizational audits of random output samples | Tells you a process is sound, not whether the specific result you rely on is correct |

Two of these — submission caps and organizational audits — appeared in earlier versions of this proposal. They are withdrawn here. The correct principle is stated in Section 3: ration scarce *services* (expert attention, experiments, prominence), never production; and assess the *specific result* when reliance matters, not the organization in general.

### 2.4 What we are not claiming

We are not claiming that AI has already produced reliable, autonomous science across fields. Bounded demonstrations exist; general autonomy does not. We are not claiming that peer review never worked, or that every paper is now suspect. We are claiming something narrower and harder to escape: institutions that decide trust, money and careers by inference from artifacts will be gamed at scale as soon as artifacts are cheap, and the design must stop depending on that inference before the gaming completes.

---

## 3. Design principles

Every mechanism in Parts II and III is derived from ten principles. They are stated here so that a reader can check the mechanisms against them and so that future revisions have something to be checked against.

1. **Observe, don't infer.** A decision about trust, money or capability should rest on something that was measured — a price backed by money, a replay of logged work, a record of demonstrated use — not on properties inferred from an artifact.

2. **Separate the three decisions.** Whether a result is dependable, whether more work deserves resources, and what a person has demonstrated are different questions with different evidence. A good result can justify the first two without settling the third.

3. **Ration services, not production.** Expert attention, experiments, prominent placement and money are scarce and must be allocated. Producing and registering a result must never be restricted; the world is better with ten thousand cheap true results than a hundred expensive ones.

4. **Volume-proof by construction.** Any mechanism that can be improved by producing more must be rejected. A bet costs something whether or not it pays; a replay measures what changed; a retroactive award follows use. An h-index rises with output; a calibration score only rises with being right.

5. **"Unassessed" is an honest state.** Most claims will never be priced, replicated or adjudicated. That is not failure; it is the truth about them. The record must display it rather than convert silence into either acceptance or rejection.

6. **Money attaches to information, never to verdicts.** Assessors are paid for doing agreed work, traders profit from being right, refuters win bonds for sustained refutations. No one is ever paid per favorable verdict, and no submitter ever pays their own assessor.

7. **Accountability attaches to organizations; credit attaches to measured contribution.** An accountable host answers for a result — preserves records, responds to challenges, funds corrections. Personal credit is separate and requires evidence.

8. **People control their own records.** A researcher owns their workflow log and decides what to disclose. Institutions get summaries and sampled audits, never the stream.

9. **Pluralism over canon.** Many maintained accounts of a question may coexist over one shared record. No single organization decides the canon; the record preserves disagreement.

10. **Everything stoppable.** Every pilot has a baseline, a pre-registered stop rule, and an owner who can end it. Expansion is a new decision, not a reward for a persuasive report.

# Part II — The instruments

## 4. The running example: Claim 47

Everything in Part II is illustrated with one claim, followed from registration to reliance. The example is invented but ordinary — a materials claim of the kind produced by the thousand every week.

A materials laboratory operates an AI research workflow under a revocable authorization from its host organization. The workflow reads the literature, proposes that a small amount of a phosphonate additive should slow the degradation of lithium-ion battery electrolytes, designs cycling experiments, runs them on a robotic bench, analyses the data and drafts a report. Halfway through, a battery chemist on the team — call her Lena — overrules the workflow's initial choice of additive family, based on bench experience the literature does not record. Two colleagues authorized the budget and maintained the equipment.

> **Claim 47.** Adding 2% of additive Q to a standard lithium-ion electrolyte halves capacity loss over 1,000 charge cycles.
>
> *Registered by:* Host organization H, on behalf of authorized workflow W-3.
> *Human contributions:* to be established from the workflow log.
> *Resolution protocol:* An independent laboratory runs the preregistered cycling test on three cells from a fresh batch of the specified formulation. "Replicates" means capacity loss reduced by at least 35% relative to control at 1,000 cycles. Adjudication of protocol validity by the assessment service designated at registration.
> *Bond:* €2,000, posted by H.
> *Market:* opened at registration with a €400 market-maker subsidy; resolution fund eligible for a base allocation once the claim crosses the field's priority floor on confirmed reliance times price uncertainty.

The life of a claim under this proposal, in one picture:

```
  REGISTER ──► PRICE ──► FUND RESOLUTION ──► RESOLVE ──► UPDATE
  claim +      market    base allocation +   auction +   ledger scores;
  protocol +   opens;    trade fees +        adjudicate  bond returns or
  bond by      traders   reliant parties                 forfeits; reliant
  host         reveal    pay in                          claims re-flagged;
               what                                      retro awards use
               they                                      usage records
               know
       │                                                      │
       └──────── workflow log runs throughout ────────────────┘
                 (contribution measured by replay at registration)
```

Three things are already different from a paper. The claim is registered by an organization, not by three people asserting they conceived it. Human contribution is a question to be answered from evidence, not a statement to be trusted. And the claim carries, from birth, a precise statement of what would settle it. Everything else builds on these three moves.

### 4.1 What a claim record contains

A registered claim is a small structured record with a human-readable report attached. The structured part is what the instruments act on:

| Field | Content | Why it matters |
|---|---|---|
| Statement | The claim, scoped: population, conditions, effect size, uncertainty | Markets and bonds need something precise to settle |
| Resolution protocol | What test settles it, who may run it, what counts as success, how disputes about the test itself are adjudicated | Fixed at registration so the fight about "was the replication valid" cannot start afterwards |
| Host | The accountable organization, its obligations (records, challenges, corrections) | Accountability attaches to organizations |
| Authorization | The workflow or person that produced it, and the scope of their authority | Agents act under revocable, scoped authorizations |
| Provenance | Data, code, instruments, dependencies, and the workflow log if disclosed | Reproduction, replay and audit |
| Bond | Amount, terms, expiry | Skin in the game; the refuter's prize |
| Market | Subsidy, resolution threshold, resolution fund | The price and the trigger |
| Contributions | Measured human contributions, or "not established" | Credit is measured, not asserted |
| Status | Registered / priced / resolution commissioned / resolved / challenged / superseded — several may hold at once | "Unassessed" is displayed, not hidden |

The report attached to the record can be as long and discursive as any paper. What changes is that the report is no longer the unit that institutions act on.

---

## 5. Truth markets

### 5.1 The idea

Instead of asking two or three anonymous reviewers whether Claim 47 is sound, let anyone who thinks they know something put money on it; read the price; and use the money at stake to pay for the experiment that settles the question.

> **What is a prediction market?**
>
> A prediction market trades contracts that pay out depending on a future event. A contract on "Claim 47 replicates" pays €1 if the replication succeeds and nothing if it fails. If that contract trades at 60 cents, the market is collectively estimating a 60% chance of success.
>
> Why should a price beat a vote? In a vote everyone counts equally. In a market, people who know something profit and people who guess lose. A laboratory that has privately tried and failed to reproduce an effect can sell contracts and collect when the price falls. Their knowledge moves the price; their profit is the payment for revealing it. The University of Iowa has run election markets since 1988. In two large studies led by Colin Camerer and Anna Dreber, markets among scientists predicted which published findings would replicate; the studies with the highest and lowest prices were then replicated and the market was right far more often than not.

> **What is an automated market maker?**
>
> A market needs someone willing to trade at every moment. A bookmaker does this by quoting odds and adjusting them as bets arrive. An automated market maker is a program that does the same by formula: it always quotes a price, raising it when people buy and lowering it when they sell. On average it loses a bounded amount to well-informed traders. That bounded loss is the *subsidy*, and it is the elegant part: the subsidy is exactly the price paid for the information the market extracts. Whoever funds the market maker is buying knowledge at a known maximum cost. The standard design is Robin Hanson's logarithmic market scoring rule.

### 5.2 Claim 47 in the market

*Monday.* The claim is registered. The assessment fund seeds a market maker with €400. The opening price is 50 cents.

*Tuesday.* A group in Grenoble that spent the spring trying to reproduce a related effect, and failing, sells contracts. The price falls to 32 cents. Nobody wrote a letter to the editor; nobody had to publish a negative-result paper that no journal wanted. The information is in the price, and Grenoble will be paid for it if they are right.

*Wednesday.* Host H, which posted the bond and believes the claim, buys. Two other laboratories that have seen encouraging pilot data buy too. The price recovers to 41 cents. Open interest reaches €18,000 — a sign that people with money at risk disagree, which is the market's definition of a claim worth settling.

*Thursday.* A battery manufacturer would like to build on additive Q, but only if the effect is real. It has two moves available and makes both. It buys "no" contracts as a hedge — if the claim fails, the payout offsets the development work it is about to waste — and it pays €8,000 directly into the claim's resolution fund, because what it actually wants is an answer, not a position. Reliance is expressed by paying for resolution.

### 5.3 Markets buy their own resolution

Ordinary prediction markets wait for the world to settle the question. Scientific markets can *commission* the settlement.

Each priced claim has a **resolution fund**. Money enters it from three sources: a base allocation from the field's assessment fund, granted only once the claim crosses the field's published priority floor on confirmed reliance times price uncertainty — so that the fund's money follows what depends on the claim rather than being spread thinly over every market; a small resolution fee — a fraction of a percent — on every trade, so that trading volume itself accumulates the means of settlement; and direct payments from reliant parties who want the question answered. The **trigger** is mechanical: when the resolution fund reaches the cost stated in the resolution protocol, resolution is commissioned. Open interest is not spent — it is traders' money and settles the contracts — but it is one of the signals that determine how the assessment fund prioritizes its base allocations among thousands of markets. The priority rule ranks claims by confirmed reliance (other registered claims or paying parties that depend on them) times price uncertainty, adds direct payments by reliant parties as revealed reliance, and uses open interest as the measure of disagreement; a simulation in the full proposal (v3, Section 33.6) shows that open interest alone tracks what forecasters look at, which need not be what matters.

For Claim 47, the base allocation of €6,000 was granted on Wednesday, when two registered claims declaring reliance on it and a price near 40 cents put it above the field's priority floor; the resolution fee had accumulated €400 by Thursday; and the manufacturer's €8,000 brings the fund to €14,400. The assessment fund, applying its published rule that markets in the top decile of confirmed reliance times price uncertainty are topped up to threshold — Claim 47 is relied on by two registered claims and a manufacturer has paid in — adds the remaining €5,600. Resolution is commissioned on Friday.

The consequence is that the claims which get checked are the ones people are both uncertain about and rely upon. No committee decides which of ten thousand claims deserve replication; the money already said so. A claim nobody trades remains visibly unassessed — not rejected, not accepted, priced at nothing because nobody has needed it yet.

This is not hypothetical. In a study published in 2025, 162 social scientists traded on 41 published experiments knowing that the twelve highest-priced and twelve lowest-priced would be replicated. The high group replicated at 83%; the low group at 33%. The market chose what to test and chose well.

*June.* The replication finds capacity loss reduced by 22% — real, but below the 35% threshold. The contract settles at zero. Grenoble profits from being right; host H and the two optimistic laboratories lose their positions. The manufacturer's hedge pays out, offsetting the development it had started, and it has an independent answer for €8,000 instead of a €20,000 study it would have had to organize itself. Lena's laboratory learns the effect is smaller than claimed and registers a revised claim — "reduces capacity loss by at least 15%" — which supersedes Claim 47; the bond rolls over to it, and a new market opens at 70 cents.

### 5.4 To author is to underwrite

> **What is a bond?**
>
> A builder who wins a public contract posts a performance bond: money held by a third party, forfeited if the work is not delivered. It aligns incentives without anyone having to trust anyone's word.

The host that registers a claim posts a bond behind it, scaled to how strongly the claim is stated. "Halves capacity loss" is strong; €2,000 is posted. Bonds are posted by hosts — organizations — never by individual researchers; a doctoral student never needs capital to make a claim, and a host's decision about which of its claims to bond is a signal in itself. A successful refutation — a failed preregistered replication, a reproducible counterexample, a demonstrated analytical flaw — pays the bond to the refuter. A claim that survives its term returns the bond with a premium.

The premium comes from a **bond pool** funded by forfeited bonds, not from the assessment fund, and each surviving claim's share of the pool is weighted by the open interest its market attracted. This closes an obvious exploit: a host cannot farm premiums by bonding thousands of trivially true claims, because trivial claims attract no trading and therefore earn nothing. Bonds on claims that people actually contested, and that survived, earn the most. Premiums are paid by the losers to the winners of the contest over what is true.

A challenger who lodges a refutation posts a **challenger stake** — 10% of the bond — forfeited to the host if the challenge fails adjudication. This makes noise expensive and sustained challenges profitable.

Bonds do two things the current system cannot.

First, they make cheap criticism valuable exactly when it is right and worthless when it is noise. AI systems can generate a thousand objections to any paper overnight. Under a bond regime, lodging a challenge costs something and winning one pays. The flood of automated criticism turns into a bounty hunt, and the bounties are only collected by challenges that survive adjudication.

Second, they price overstatement. The bolder the wording, the more must be put behind it. A laboratory that wants to claim "halves" rather than "reduces by 15–30%" can do so, at a price. Effect-size inflation — one of the most persistent pathologies of the current literature — acquires a cost.

For Claim 47, the June replication does not forfeit the bond: a smaller real effect is a qualification, not a refutation. The protocol registered at birth said what counted, and the adjudicator applies it.

Credit, in this system, is the bond that survived. Donald Knuth has paid reward cheques for decades to anyone who finds an error in his books; Paul Erdős offered cash for solutions to his problems. Both are bonds on claims at small scale. This proposal makes them the default.

### 5.5 The calibration ledger

> **What is calibration?**
>
> A forecaster who says "70% chance of rain" is calibrated if, on the days she says so, it rains about 70% of the time. Calibration is not boldness or caution; it is stated confidence matching reality. The Brier score, from 1950, measures it: it rewards confidence when right and punishes confidence when wrong, and a hedged forecast that says 50% to everything scores poorly against a forecaster who actually knows.

Every person and every AI system that trades on or endorses claims accumulates a public record. It has two parts. **Realized performance**: profit and loss across resolved positions, which measures skill the way a fund manager's record does. **Calibration**: each trade or endorsement is accompanied by an explicit probability, scored with a proper scoring rule when the claim resolves. Proper scoring rules reward both calibration and sharpness, so a hedged forecaster who says 50% to everything scores worse than one who actually knows. The ledger also displays the number of positions and the average difficulty of the claims taken — measured by how contested their markets were — so that a record built on easy claims is visibly a record built on easy claims.

This record has the property the h-index lacks: **it cannot be inflated by volume.** More papers raise an h-index; more positions only improve a ledger if the positions are good. A scientist who endorses ten claims at 90% and sees five replicate has a worse record than one who endorses them at 60% and sees six replicate — and everyone can see it. One caveat, established by simulation in the full proposal (v3, Section 33): a ledger separates good forecasters from bad only after several hundred resolved positions, so it is a multi-year credential, earned fastest where resolution is cheap and frequent.

The ledger also solves a problem specific to AI agents. An agent's track record on the ledger is the only evidence of its reliability that cannot be produced by the agent itself. A critic model with a good record on sustained challenges is worth listening to; one with a record of noise is not, however fluent its objections.

This makes a **critic league** possible. Critic agents — and human critics — compete on sustained challenges, ranked on a public leaderboard like a forecasting tournament, with prizes from the bond pool and from challenger stakes forfeited by losing rivals. The flood of automated criticism that threatens to drown every venue becomes a sport with a scoreboard, in which only challenges that survive adjudication score. A laboratory choosing which objections to take seriously reads the league table.

**Provisional ledgers for newcomers.** A researcher's first fifty positions are scored privately and displayed publicly only as "provisional." Nobody's early learning bets follow them for a career, and the ledger starts at zero for everyone on the day the system starts — a senior researcher has no accumulated advantage.

### 5.6 Design details that matter

**Resolution protocols are fixed at registration.** The fight "the replication was done wrong" is the new "the reviewer didn't understand my paper." It is pre-empted by fixing, at registration, what test settles the claim, who may run it, what counts as success, and who adjudicates disputes about validity. Templates for common claim types (Appendix B) make this a five-minute step, not a legal negotiation.

**Protocols can be amended until a market opens, and can be ruled inadequate.** For novel claims the right test is not always obvious at registration. A host may amend the protocol, with the amendment logged, at any time before the first trade. After that, only the named adjudicator may rule that a protocol is inadequate — for example, that its success criterion is unfalsifiable — in which case the market is suspended, the claim is displayed as "unpriceable pending protocol," and the host may re-register with a better one.

**Hosts cannot short their own claims.** A host's bond is its long position. Allowing a host to also sell contracts on its own claim would let it profit from private knowledge that the claim is weak — registering claims in order to bet against them. Hosts, their authorized workflows and their principals may buy but not sell contracts on claims they registered.

**The assessment fund operates under published rules.** How base allocations are sized, how markets are prioritized for top-up, and how subsidies are set are published rules administered by the field's assessment fund under the oversight board (Section 12.5). No individual decides which claim gets resolved.

**Prices need reasons.** A number is not a review, and a scientist who wants to know *why* a claim trades at 32 cents is entitled to an answer. Two records supply it. Every trade may carry a short **rationale**, attached to the position and revealed on resolution, so that the ledger scores not only who was right but whose reasons held up. And every **challenge record** states an alleged defect and a test for it. Together, the market gives the price and the challenge records give the reasons; the critic league ranks the reasons by whether they survived. This is more than peer review supplies today, where the reasons are two paragraphs read once and discarded.

**Resolutions are not final.** A replication can itself be wrong. A resolved claim can be re-opened by a new challenge with a new stake and a new protocol; the original resolution is itself a claim on the record with its own provenance, and the laboratory that performed it has its own ledger. Ledger scores are marked against the resolution at the time and re-marked if it is overturned. "Resolved" means "settled on the evidence then available under the protocol agreed," which is what science has always meant by established.

**Resolution is commissioned by threshold, not by vote.** The trigger is the resolution fund reaching the protocol's cost estimate; the base allocations that fill it are granted by the published priority rule. Both are mechanical and cannot be lobbied.

**Resolution auctions.** When resolution is triggered, accredited laboratories bid to perform it. The lowest credible bid wins, where "credible" is a function of the bidder's own ledger and past resolutions. Bidders post a small performance bond. This creates a market for replication labor, which does not exist today, and gives replication a price.

**Agents trade under principals.** An AI agent trades through the account of an accountable organization, with position limits per principal and disclosure of the models it depends on. Agreement among copies of one model counts as one opinion.

**No-loss markets where real-money markets are illegal.** In many jurisdictions a real-money market on scientific claims is gambling. The Replication Markets project ran on allocated play-money with $142,000 in cash prizes paid to the best forecasters, which is a prize competition, not a bet. Institutional markets, where only accredited organizations trade, are another lawful design. The pilot uses the prize design; the proposal is indifferent between the two as long as trading has a cost and being right pays.

**Not every claim gets a market.** Registration is free. A market is opened when the host asks for one, when a reliant party asks for one, or when the assessment fund's rules select it. Most claims will never be priced. That is correct.

**Structured elicitation feeds the price.** In the DARPA SCORE program, a structured deliberation protocol (repliCATS) matched or exceeded market forecasts on some measures. The market should be able to ingest panel forecasts as trades by an institutional participant. Markets are the aggregation layer, not the only source of judgment.

### 5.7 Precedents and what they show

- *Dreber et al. (2015), Camerer et al. (2016, 2018).* Prediction markets among researchers predicted replication outcomes across three large replication projects. They show that scientists collectively know which findings are fragile, and that markets extract that knowledge.
- *Holzmeister et al. (2025).* A decision market chose which of 41 studies to replicate; the top twelve replicated at 83%, the bottom twelve at 33%. It shows that markets can *allocate* replication, not just predict it.
- *DARPA SCORE (2019–2022).* Forecasts on more than 3,000 claims across eight disciplines, by markets and by structured panels; a subset replicated to ground-truth the forecasts. It shows the approach scales to thousands of claims, and that structured elicitation is a competitive alternative to trading.
- *Replication Markets prize payouts.* $142,000 in cash prizes over 121 resolved questions shows the no-loss legal design works and attracts serious forecasters, including at least one who built a quantitative model and dominated early rounds — a warning about liquidity and a demonstration that skill is rewarded.
- *Hanson's LMSR (2003).* The subsidized market maker with bounded loss is standard and implemented in open-source software.

What these precedents do not show: that markets work for claims whose resolution takes decades (Section 8), that they resist manipulation by parties with large commercial stakes at scale, or that the calibration ledger changes hiring behavior. The pilot is designed around those gaps.

### 5.8 Failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Thin markets: two traders, one moves the price | Low-volume prices are displayed as "unassessed," not as estimates; subsidy weighted toward claims with demonstrated reliance |
| Deep pockets prop up a claim | Position limits per principal; a manipulated price is a subsidy to anyone with real information, who will take the other side; bond forfeiture on refutation |
| Resolution disputes become the new review queue | Protocol fixed at registration; independent adjudicator named at registration; adjudicators have their own ledger |
| Agent swarms trade in concert | Agents trade under principals; shared-model disclosure; correlated positions collapsed to one |
| Claims registered to be unresolvable | Registration requires a resolution protocol; claims without one are "unpriceable" and get no market, no bond, and no credit |
| Gambling law | No-loss prize design or institutional-only markets |
| Markets reward the well-connected forecaster, not the field | The ledger is public; a good forecaster who is not a domain expert is still useful; expertise shows up as profit |

### 5.9 First build

One field with fast, cheap resolution: empirical machine learning, where a claim can be re-run on a held-out benchmark split in days for hundreds of euros. About five hundred registered claims, drawn from the past two years of the field's output with the hosts' consent. A subsidy fund of €150,000, a resolution fund of €100,000 buying at least sixty resolutions, a platform adapted from open-source market software, twelve months. Experimental psychology, with its existing replication culture but €10,000-plus replications, follows in year two.

The test: resolution decisions track prices better than a simple baseline (citation count, venue); the ledger separates good forecasters from bad ones out of sample; cost per resolved claim comes in below a conventional replication study.

---

## 6. Flight recorders

### 6.1 The idea

You cannot work out afterwards who contributed what to a piece of work done jointly by people and machines. You can record it while it happens, and then measure each person's contribution by replaying the work without them.

### 6.2 Why reconstruction is hopeless

Return to Lena's paper. Its contribution statement reads: "L.N. conceived the additive selection; M.R. and J.K. supervised." Did she? The workflow wrote the statement. Perhaps accurately; perhaps flattering the humans who authorized its budget. Nothing in the document can tell you, and asking the humans is asking the people with the strongest incentive to say yes.

This is where most reform proposals give up and demand more detailed contribution statements. That is asking a student, after the group project is handed in, who did what. Everyone who has taught knows how that goes. The alternative is to watch the project being done.

The patent system reached the same wall from the other side. In November 2025 the United States Patent and Trademark Office reaffirmed that only a natural person who *conceived* an invention may be named inventor, and that AI tools are to be treated like laboratory equipment. That answers the legal question and leaves the evidential one untouched: how does anyone establish, after the fact, that the human rather than the tool did the conceiving? The Office's own practical advice is to *document* human contribution during the work. That is the flight recorder.

> **What is a flight recorder?**
>
> Every airliner carries a recorder that logs the pilots' inputs and the aircraft's state, continuously, into a protected store. Nobody reads it on a normal flight. When something goes wrong it answers "what actually happened?" without relying on anyone's memory or interest.
>
> The same idea now exists for photographs. Under the C2PA standard, a camera can cryptographically sign each image, and each editing step adds a signed record, so anyone can later tell an original from a manipulation. The signature does not say the photo is *good*; it says what was done to it and by what.

### 6.3 Attested research workspaces

A research flight recorder is a workspace — a computational notebook, an agent framework, a laboratory information system — that writes a signed, tamper-evident stream of:

- every prompt or instruction a human gives an AI system;
- every output the system returns;
- every edit, acceptance, rejection or override by a human;
- every decision point where a branch was chosen;
- every data access and every tool invocation, with versions.

Each entry is hashed into a chain and signed by the workspace; the researcher holds the key. Optionally the workspace runs in a trusted execution environment so that the log's integrity does not depend on the researcher's own machine.

**The log is not a surveillance feed.** The researcher owns it, decides whether and to whom to disclose it, and can keep it sealed forever. But only logged work can support a personal credit claim. Unlogged work is published under the host's name with human contribution marked "not established." That is not a punishment; it is the honest default, and it is what most AI-produced work should say.

For Lena's project the log shows the following. The workflow proposed screening additives from family A, citing the literature. Lena wrote: "Family A always looks good in simulation and always fails at the anode interface — we saw this in 2023. Try the phosphonates." The workflow switched, and additive Q, a phosphonate, emerged from the screen. Her colleagues' logged interventions were two budget approvals and one formatting change.

### 6.4 Counterfactual credit

> **What is counterfactual credit?**
>
> In baseball, a player's value is measured as "wins above replacement": how many more games did the team win with this player than it would have with an ordinary substitute? It is computed by statistically replaying the season without the player. It does not ask the player how important they were.

With a logged workflow the replay can be literal. Remove Lena's intervention from the log and re-run the workflow from that point with the system left to its defaults. In the replay, the workflow screens family A, finds nothing at the anode, and reports a null result. Her marginal contribution to Claim 47 is, measurably, the claim's existence. Remove the formatting change and the replay is identical; that colleague's contribution to *this result* is zero — which says nothing about the value of their role, only that discovery credit for this claim does not belong to them.

For several contributors, the standard tool is the Shapley value: average each person's marginal contribution over all subsets of the other contributors. For three people this is eight replays; for ten it is a thousand, so beyond small teams the standard sampling approximations are used and the record states the sampling error. For stochastic workflows, replay with fixed random seeds and report a distribution rather than a point. Replay also requires the same model versions the original run used; the log pins them, and because commercial models are deprecated, contribution records should be generated promptly or against archived weights — a practical reason to compute credit at the time of registration rather than years later.

This is the direct answer to the objection that "naming the required contribution doesn't establish it." Stop asking. Run the experiment.

### 6.5 Contribution records

A contribution record lists what was measured:

> *Claim 47 — contributions.* L.N.: intervention at step 14 changed outcome from null to positive (replay, 5 seeds, 5/5). M.R., J.K.: budget authorization; no outcome-changing intervention measured. Workflow W-3 (host H): all other steps. Unlogged segments: none.

Unknown shares remain unknown. Nobody inherits credit for owning the software or approving the budget; nobody manufactures percentages; and the record is dull, which is what an honest record looks like.

### 6.6 Examinations become logged sessions

> A driving examiner does not inspect your car and infer your competence. She sits beside you while you drive.

A doctoral defence or a hiring exercise becomes a session in an attested workspace on unfamiliar material, with AI tools permitted and logged. The log shows what the candidate did with the tools — including what they did when the tools were wrong, which is where competence actually shows. This establishes what the person can do *with* the tools, which is what an employer needs to know. It deliberately does not claim to establish unaided genius, which nobody needs to know and nothing can establish.

### 6.7 Design details that matter

**What gets logged is configurable and declared.** A workspace declares its logging level (interactions only; interactions plus data access; full environment), and the contribution record states the level. Credit claims are only as strong as the log that supports them.

**Replay requires reproducibility.** Workflows that cannot be replayed cannot support counterfactual credit; they can still support a descriptive record ("L.N. made 14 interventions; 3 at branch points"). This is an incentive toward reproducible workflows that does not need a mandate.

**Laboratory steps are recorded as roles, not replayed.** Bench work cannot be re-run without you. It is logged as who did what, with instrument records, and credited by role. Counterfactual credit applies to the computational and decision segments.

**Sealed by default; disclosed by choice.** A researcher can disclose the log to a hiring committee and to no one else. Institutions may audit sampled replays with consent; they never get the stream.

**Agents have logs too.** An AI workflow's log is what allows its outputs to be audited and its own reliability to be tracked. The same infrastructure that protects human credit disciplines machine production.

**Logs are personal data.** A workflow log records a person's working behavior and falls under data-protection law in most jurisdictions. Researcher ownership of the key, sealing by default and disclosure by consent are not only design choices; they are what makes the recorder lawful. Employers who want access get summaries under a lawful basis, never the stream.

### 6.8 Precedents and what they show

- *C2PA content credentials.* Cameras from several manufacturers already sign images at capture, and major editing tools add signed provenance. It shows that signed, chained provenance is deployable in consumer hardware and software, and that the standard can be adopted without a mandate.
- *Aviation and rail recorders.* Continuous, protected logging that is read only on demand is a mature safety practice with well-understood privacy arrangements (pilots' unions negotiated them).
- *Reproducible-research tooling.* Containerized pipelines, notebooks with execution records, and workflow managers already make replay feasible for a large share of computational science.
- *"Wins above replacement."* Counterfactual attribution by replay is standard in sports analytics and accepted by the people being measured.

What they do not show: that researchers will accept logging (adoption is the pilot's main question), that replay-based credit agrees with expert judgment (the pilot's main metric), or that the approach extends to conceptual work that happens away from a keyboard (it does not, and the record says so).

### 6.9 Failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Surveillance chills exploration | Researcher owns the key; sealed by default; institutions receive summaries and consented sampled audits only |
| Staged interventions inflate measured credit | A staged intervention that does not change the outcome measures zero; sampled independent replays |
| Non-replayable work | Descriptive records; role credit; incentive toward reproducibility |
| Log tampering | Hash chain plus signatures; optional trusted execution; independent timestamping |
| Credit inequality between logged and unlogged researchers | Organizational authorship is the default and carries no stigma; the recorder is an option for those who want personal credit |
| Vendor lock-in of workspace software | Open log format specified in Appendix B; any workspace can implement it |

### 6.10 First build

A plugin for the environments where AI-assisted research already happens — computational notebooks and agent frameworks — that produces signed logs and supports replay with fixed seeds. Piloted with volunteer groups who want their contributions attributable. About €200,000.

The test: logs replay reliably; replay-based credit agrees with blinded expert judgment on a sample of cases; friction is no higher than working without the recorder; and at least one hiring or doctoral decision uses a logged session.

---

## 7. Paying for value

### 7.1 The idea

Stop buying promises through proposals. Pay for inputs and outputs after their value is visible; let many small pledges steer shared infrastructure; let scarce capacity find its price; keep a human-judged share for what cannot be measured.

### 7.2 Retroactive funding

> **What is retroactive public-goods funding?**
>
> A Nobel Prize is retroactive: it pays for work whose value has become obvious. The general form was articulated by Vitalik Buterin in 2021 and has been run at scale by the Optimism collective, which has distributed over sixty million OP tokens — its third round alone allocated tokens then worth roughly $90 million to 501 projects, judged by 146 "badgeholders" on demonstrated impact. The principle: **it is far easier to judge what was useful than what will be.**

Research is full of contributions no proposal system funds well: datasets, software, negative results, methods, replications, and the maintenance that keeps them alive. A fixed share of research budgets — 10% to start — is paid retroactively for such contributions, by paid, rotating evaluators with usage evidence in hand.

For Claim 47: the June replication used a calibration dataset for cycling tests that a small group in Uppsala has maintained for eight years without a grant. The dataset appears in the usage records of forty resolved claims that year. It receives a retroactive award. Nobody wrote a proposal.

**What the precedent teaches.** Optimism's rounds were gamed: in the third round more than a thousand of nearly 1,600 applications were reported for rule violations, badgeholders were overwhelmed by 644 eligible projects, and cross-category comparison proved hard. The design here responds directly: awards require usage evidence from the truth-market and provenance records rather than self-description; evaluator pools are paid and rotated; and rounds are scoped to one field at a time so comparison is like with like.

### 7.3 Impact certificates

> **What is an impact certificate?**
>
> A ticket that says "I funded this work early; if it later receives a retroactive award, I get a share." It is an early investor's stake, except that the payoff comes from a public prize rather than profit. Small funders have run impact-certificate markets since 2023.

The sensible-sounding rule "small allocations earn larger ones on evidence" quietly starves work whose value takes years to show. Impact certificates give long-horizon work a financing route: someone who believes in the Uppsala dataset in year one can fund it and be repaid in year eight. They also create a second price signal — the certificate's trading price is a forecast of future usefulness, and certificate holders have every reason to help the work get used.

### 7.4 Quadratic funding

> **What is quadratic funding?**
>
> Suppose a funder has a €10,000 matching pool for shared tools. Project A is supported by 100 researchers pledging €10 each. Project B is supported by one wealthy laboratory pledging €1,000. Both raised €1,000. Under ordinary matching they get the same. Under quadratic funding the match depends on the *number* of supporters as well as the amount — technically, on the square of the sum of the square roots of the pledges — so A receives nearly the whole pool and B almost none.
>
> The formula was published by Buterin, Hitzig and Weyl in 2018; Gitcoin has used it since 2019 to distribute more than $60 million to open-source projects through several million individual donations.

For shared scientific infrastructure — the tool, the database, the instrument everyone in a field needs but nobody's grant covers — this is the right allocation rule. The community pledges small sums; the pool follows the pledges. Sybil resistance (one person pretending to be a hundred) comes from pledging through accountable principals, the same identities the rest of the system uses; Gitcoin built a dedicated identity layer for exactly this reason.

### 7.5 Dominant assurance contracts

> **What is a dominant assurance contract?**
>
> Kickstarter runs all-or-nothing campaigns: if the target is missed, everyone is refunded. Alex Tabarrok's 1998 refinement: if the target is missed, contributors are refunded **plus a bonus.** Now there is no reason to wait for others to pay first. Pledging is the best move whether or not the project happens.

Three laboratories each need the same €20,000 low-temperature measurement of additive Q. Each would rather someone else paid. A dominant assurance contract solves this in an afternoon: each pledges €7,000; if all three pledge, the measurement runs; if fewer do, pledgers are refunded plus €500 from the fund. Pooled demand for experiments — which earlier versions of this proposal could only describe — now has a mechanism.

### 7.6 Spot markets for capacity

> **What is a spot market?**
>
> Cloud providers sell spare capacity at a fluctuating, visible price. When demand is low an hour of computation costs pennies; when it spikes the price rises and the least urgent jobs wait. Nobody applies for compute; they buy it.

Instrument time, robotic laboratory runs and compute can be sold the same way. Cloud laboratories already sell experiments by the run. An AI-driven investigation with a budget buys capacity directly; so does a human researcher. The price of an hour on a given instrument becomes public information, which tells funders exactly where the bottlenecks are and where to invest in more capacity. Reserved allocations for newcomers, fixed in advance, prevent the market from pricing out those without budgets.

### 7.7 Futarchy, on a slice

> **What is futarchy?**
>
> "Vote on values, bet on beliefs." Robin Hanson's proposal: a community decides what outcome it wants — say, the number of independently confirmed useful results in a field after three years — then runs *conditional* markets on which of several candidate investigations would best produce it. Prices, not a committee, choose.

This is the most radical mechanism here and the most exposed to gaming of the outcome measure. It is included for 5% of a budget, as an experiment, with the measure chosen by the funder and watched.

### 7.8 What remains human-judged

Not everything can be scored. Questions nobody has asked, conceptual work, and research whose value cannot be measured within any reasonable horizon still need people to back people. Fellowships on the "people, not projects" model remain, with one modification: when a panel cannot distinguish between qualified applicants, the decision is made by lottery. The Swiss National Science Foundation already does this at its funding boundary. A coin flip is fairer than a tie-break on prose style and cheaper than pretending the panel sees differences it cannot.

Below the fellowship sits something simpler: a **research voucher**. Every accredited researcher receives a small annual allocation of compute, data access and experiment capacity with no application at all — spendable on the spot market, in pooled experiments, or on resolution funds. It is universal, it is small, and it is the cheapest possible protection for newcomers and unfashionable questions, because it requires no one's approval. It is the research equivalent of a library card.

### 7.9 How the funding pieces interlock

| Need | Instrument | Signal it uses |
|---|---|---|
| Reward what proved useful | Retroactive funding | Usage evidence from provenance and resolved markets |
| Finance long-horizon work | Impact certificates | Expected future retro awards |
| Fund shared infrastructure | Quadratic funding | Number of pledgers |
| Fund pooled experiments | Dominant assurance contracts | Pledges with refund-plus-bonus |
| Allocate scarce capacity | Spot markets | Visible price |
| Choose between investigations | Futarchy slice | Conditional market prices |
| Back people and unformed questions | Fellowships with lotteries | Panel judgment, then chance |

### 7.10 Failure modes and mitigations

| Failure | Mitigation |
|---|---|
| Retroactive funding rewards the visible | Usage evidence required; evaluators paid and rotated; one field per round |
| Sybil attacks on quadratic matching | Pledges through accountable principals; identity layer |
| Spot markets price out newcomers | Reserved allocations fixed before outcomes |
| Futarchy measure gamed | Small slice; measure chosen by funder; audited |
| Impact certificates become speculation detached from science | Certificates pay only from retro awards, which require usage evidence |
| Retro rounds swamped by applications | Nomination via usage records, not self-application |

### 7.11 First build

A retroactive round of €500,000 for datasets and tools in the same field as the truth-market pilot, with a small impact-certificate market attached and about €50,000 for operations. The test: awarded items show measured use; certificate prices predict awards; awards reach groups outside the already well-funded.

---

## 8. Which instruments fit which science

Not every instrument fits every field, and a proposal that pretends otherwise will be dismissed by the fields it fits worst. The table is candid.

| Kind of science | Resolution available? | Truth markets | Bonds | Recorders / replay | Retro funding |
|---|---|---|---|---|---|
| Formal mathematics and verified software | Yes: proof checking, counterexample | Markets on "proved or refuted by date X"; resolution by formal check | Strong fit | Strong fit: proof assistants already log everything | Libraries, tactics, formalized datasets |
| Computational science, ML | Yes: reproduction, held-out benchmarks | Strong fit; fast cycles | Strong fit | Strong fit | Datasets, tools, benchmarks |
| Fast experimental science (materials, chemistry, psychology) | Yes: replication in weeks | Strong fit | Fit | Computational segments; roles for bench work | Datasets, protocols, instruments |
| Slow experimental science (clinical, ecological) | Years | Long-dated contracts; intermediate observables | Long terms | Partial | Cohorts, registries, maintenance |
| Observational science (cosmology, climate, epidemiology) | Decades or never directly | Markets on next survey / next data release; consensus marks | Weak | Partial | Data pipelines, models |
| Theory and conceptual work | Rarely direct | Markets on adoption by maintained accounts; on derived predictions | Weak | Weak (much work is off-keyboard) | Retro awards for adopted frameworks |
| Humanities and interpretive scholarship | Mostly no | Not applicable | Not applicable | Weak | Editions, archives, tools |

### 8.1 Long-horizon fields

Fields whose claims resolve over decades — cosmology, climate, evolutionary biology, much of medicine — cannot be priced on the same terms as a materials claim. Four adaptations keep them inside the system without pretending:

1. **Intermediate observables.** A claim about the universe's expansion history implies predictions for the next survey's data release. Markets trade on those, which resolve in years, not centuries.
2. **Consensus marks.** A long-dated contract is periodically "marked" by an expert panel whose own calibration is tracked on the ledger. The panel does not settle the claim; it provides an interim price against which trading and bonds can be measured.
3. **Knowledge bonds.** For claims that will not resolve within a career, bonds can be structured as long-dated instruments whose value depends on survival, transferable and tradeable, so that a researcher can be paid for a surviving claim without waiting forty years.
4. **Honest non-pricing.** Where none of the above applies, the claim is registered, its provenance recorded, and its status displayed as "unpriceable." Retroactive funding and recorders still apply. Nothing is forced.

### 8.2 Formal mathematics

Formal mathematics is the one domain where resolution is exact and cheap: a proof assistant checks a proof. This makes markets and bonds unusually clean — a market on "Conjecture C will be formally proved or refuted by 2028" resolves mechanically — and it makes recorders nearly free, since proof assistants already log every step. Different assistants and foundations (higher-order logic, set theory, dependent type theory) impose different notions of what "checked" means, and the resolution protocol must name the checker and its trust base; a claim checked in one system is not automatically established for a user of another. The proposal treats proof assistants as a family of resolution services, not as a single template.

# Part III — Institutions

## 9. Who owns the machines

The three instruments answer what is dependable, what deserves money, and what a person contributed. They do not answer who controls the research systems that produce most of the output, and no mechanism design does. If a handful of organizations own those systems, provenance will document the concentration beautifully and do nothing about it.

### 9.1 Essential-facility access

> **What is the essential facilities doctrine?**
>
> In 1912 the United States Supreme Court ruled that the railroads which jointly owned the only bridges and terminals into St Louis could not exclude competitors from them. If you own the only bridge, you must let others cross at a fair toll. The principle has since been applied to power grids, telephone networks and ports, and has counterparts in European competition law.

Research systems above a capability threshold — defined by what they can do, not by who owns them — are treated as essential facilities: their operators must license access to accredited researchers at regulated rates, with the accreditation and the rates set by a public body, and with the same safety screening the operator applies to itself. This is the legal defense against concentration. Consortium ownership of open systems is a complement, not a substitute, because a consortium can exclude outsiders too.

### 9.2 Research cooperatives

> Credit unions, agricultural cooperatives and the Mondragon industrial group are businesses owned by the people who work in or use them. They have competed successfully for a century.

Laboratories organized as cooperatives own their research systems and share revenue from what those systems produce. The "decentralized science" experiments of the early 2020s tried token-based governance with mixed results; the cooperative form is older, legally mature in every jurisdiction, and answers "who benefits when the machine discovers something" without a lawsuit.

### 9.3 A science dividend

> Alaska pays every resident an annual dividend from a fund built on oil royalties; Norway's sovereign wealth fund does the same at national scale.

Value produced by AI research systems flows in part into a permanent fund that pays for human inquiry, training and fellowships. This is the financial answer to "what are humans for," and it is deliberately separate from any claim that humans out-produce machines. Human science is funded because understanding, education and independent scrutiny are goods in themselves. The dividend is how, not why.

**A wrinkle the patent office created.** Because inventorship requires a natural person who conceived the invention, an invention that was in fact conceived by an AI system has, under current United States guidance, no valid inventor and therefore no patent. Two consequences follow. First, organizations have a strong incentive to name a human inventor whether or not one exists — which is exactly the misattribution this proposal is trying to end, and which flight recorders would expose. Second, a science dividend cannot rely on patent royalties from AI-conceived inventions, because there may be none. It must be funded instead by a levy on commercial use of research systems above the essential-facility threshold, or by licensing revenue from the systems themselves. Either way, the fund's source is the machine's productivity, which is the point.

### 9.4 Data and evidence trusts

Evidence that many programs need — reference datasets, calibration materials, cohort data — is held in trusts with fiduciary duties to the research community rather than to any producer. Trustees are appointed under published charters with fixed terms. This is the institutional form for the Uppsala dataset once it is recognized as infrastructure rather than one group's side project.

### 9.5 Safety, ethics and screening

Markets, resolution auctions and capacity spot markets route work to laboratories automatically. That is the point, and it is also a hazard: an automated route from "someone wants this answered" to "a robot runs it" is exactly where dual-use and human-subjects risks concentrate.

Three rules apply everywhere in the design. **Screening precedes routing.** Every resolution protocol and every capacity purchase passes a screening step — automated for the routine, expert for the flagged — before it is offered to any laboratory, and again at the laboratory before execution. **Ethics approval is part of the protocol.** A resolution protocol that involves human participants, animals or hazardous materials names the approval it requires; without it the claim is unpriceable. **Payment never overrides screening.** A reliant party's money in a resolution fund buys priority, not exemption. Laboratories retain the right to decline.

Screening is itself a service with disclosed operators, an appeal route, and its own ledger, because a screening service that quietly blocks unwelcome science is a censorship mechanism with a safety label.

---

## 10. What people are employed for

### 10.1 The counting ban

Participating institutions remove publication counts, journal rank and citation indices from hiring, promotion and doctoral decisions, and are audited for compliance. The San Francisco Declaration on Research Assessment has urged this since 2012 and has thousands of signatories and little effect; China's 2020 rules restricting evaluation by paper counts show that enforcement is possible when someone decides to enforce. The lever is money: funders make the ban a condition of institutional eligibility.

### 10.2 The hiring file

Without paper counts, a hiring file contains:

- the candidate's **calibration ledger** — how their stated confidence in claims matched outcomes;
- one or two **logged exercises** on unfamiliar problems, with tools allowed;
- the things they **built or maintained**, and the retroactive awards those attracted;
- **contribution records** from logged work, showing measured marginal contributions;
- **references** from people who worked alongside them.

Every item is measured or observed. None can be inflated by running a model overnight. The file is also shorter than a current one, because it contains no list of two hundred papers nobody on the committee will read.

### 10.3 The doctorate as residency

The current doctorate is a stapled thesis of papers; its examination is a discussion of a document. Under this proposal it becomes a **residency**: a period of supervised participation in real research programs, with logged contributions, followed by a **logged examination** on unfamiliar material with tools permitted. Medicine certifies competence separately from research output; so can science. The residency also answers the training question: if entry-level checking is automated, where do future experts come from? From doing the work under supervision, as they always have, with the log as evidence.

### 10.4 The apprenticeship share

A defined share of the assessment budget — adjudications, replays, retroactive evaluations — is reserved for supervised trainees, with mentor review and attributable records. Supervision time is counted as real cost. This is not charity; it is how the system produces the adjudicators and evaluators it needs in ten years.

### 10.5 A week in 2031

*Monday.* A researcher opens her attested workspace and continues an investigation with her workflow. The log runs; she does not think about it.

*Tuesday.* She notices a claim in an adjacent field that her group relies on is trading at 38 cents. She reads the provenance, sees a plausible confounder nobody has raised, and lodges a challenge with a small stake and a specified test. The host's bond is €3,000; if her challenge is sustained she collects.

*Wednesday.* Her group's calibration dataset is nominated for a retroactive award because eleven resolutions this quarter used it. She spends an hour making the usage evidence legible.

*Thursday.* A pooled measurement she pledged toward via a dominant assurance contract clears its target. Three groups will get the result for a third of the price each.

*Friday.* She reviews a trainee's replay of a contested contribution record, signs off with a note, and logs the hour as apprenticeship supervision. Her own ledger shows 214 positions, Brier score 0.19, improving.

At no point does she count her papers. She has written two this year, both syntheses, both useful.

### 10.6 Human tracks

Chess did not die when engines surpassed players. It split: human competition continued under anti-cheating rules and became more popular, while engines became the analysis tools everyone trains with. Science will split the same way, and the design should say so rather than let it happen by accident. **Open tracks** admit any mixture of human and machine work, under organizational authorship and measured contribution. **Human tracks** — for training, for examination, and for the intrinsic value of a person working a problem through — run with disclosure rules and logged sessions, the way a chess tournament runs with anti-cheating measures. Neither track is superior; they answer different questions. What the design refuses is the pretense that open-track work was human-track work, which is the pretense the current system rewards.

### 10.7 Protections for early-career researchers

Three features of the design exist specifically for people at the start of a career. Bonds are posted by hosts, so a student never needs capital to make a claim. Ledgers are provisional for the first fifty positions and start at zero for everyone on the same day. And a logged contribution record is the first instrument in the history of science that lets a junior researcher prove what they did on a project in a way a senior co-author cannot absorb.

### 10.8 The honest paragraph

Nothing in this proposal guarantees that everyone finds a new role in "judgment," "curation" or "asking the right questions." Those activities are inside the automation scenario too. Research employment may shrink or shift. The honest response is to preserve existing commitments, fund training and the apprenticeship share, pay for human inquiry from the science dividend on its own terms, and measure what happens — not to pretend that a reorganized labor market is guaranteed. A proposal that promised otherwise would not deserve to be believed.

---

## 11. Journals, societies and the record

### 11.1 What journals become

Journals stop being the gate through which a result enters existence. They become three things they are better at:

- **Maintained accounts.** A journal or society takes responsibility for the current account of a question: what is established, what is disputed, what the markets say, what would change the account. Releases are versioned and citable; the live version updates as claims resolve.
- **Syntheses and explanation.** Long-form writing that makes a field intelligible. In an abundant system this becomes more valuable, not less.
- **Adjudication.** A journal can operate as the independent adjudicator named in resolution protocols, paid by the assessment fund, never by the submitter. Its reputation then rests on the quality of its adjudications, which are themselves on the ledger. One rule of separation: a journal may not adjudicate claims that fall within an account it maintains, because a maintainer has a stake in how its own account's claims resolve. Adjudication and maintenance of any given question are held by different organizations.

Different journals maintain different accounts of the same question over one shared record. Pluralism is a feature.

### 11.2 The minimal shared record

The common infrastructure is deliberately small. It specifies how records travel, not how science is done:

| Record type | Purpose | Existing basis |
|---|---|---|
| Identifiers, versions, provenance | Addressable, immutable, linked research objects | DOIs, RO-Crate, content hashes |
| Accountable authorizations | Who may register and spend, under whose responsibility | ORCID plus organizational identity |
| Claim records with resolution protocols | What is claimed and what would settle it | New; template in Appendix B |
| Market and bond records | Prices, positions, bonds, resolutions | New; open-source market software |
| Workflow logs and contribution records | Provenance of human–AI work; measured credit | C2PA-style chained signatures; new schema |
| Assessment records | What was checked, by whom, with what result and limits | Signed, versioned; COAR Notify for transport |
| Usage records | What was relied on by what | Derived from provenance and resolutions |
| Maintained-account releases | Versioned syntheses with revision conditions | New; journals as maintainers |

Everything else — disciplinary methods, formats, ontologies — stays local.

### 11.3 The reliance graph replaces the citation graph

Citations were always a proxy for reliance: a paper cited what it built on, mixed with what it wished to acknowledge, what it argued against, and what its reviewers asked for. The usage record is the thing itself. Claim R **relies on** claim C when R's provenance or resolution protocol depends on C — its data, its method, its result. Reliance is recorded when R is registered, and it is confirmed when R resolves, because a resolution that depended on C is a use of C that mattered.

The reliance graph does three jobs the citation graph could not. It identifies **load-bearing claims** — those with many dependants — and the assessment fund prioritizes their resolution, because a wrong load-bearing claim is expensive. It drives **revalidation cascades**: when a load-bearing claim fails resolution, every claim that relied on it is flagged "support withdrawn," its market reopens, and its host is notified; nothing is silently declared false, but nothing silently keeps standing on a foundation that has gone. And it supplies the **usage evidence** for retroactive funding, so that awards follow what was relied upon rather than what was cited for politeness.

### 11.4 Relation to existing infrastructure

The proposal extends rather than replaces: preprint servers and repositories keep hosting reports; OpenAlex and Crossref keep resolving identifiers; ORCID keeps identifying people; the Open Science Framework keeps hosting preregistrations, which are the ancestors of resolution protocols; COAR Notify already carries assessment records between repositories and services. What is new is the claim record with its resolution protocol, the market layer, the workflow log, and the usage record. Each can be added to existing infrastructure without a new platform. Where a platform is needed — the market and the ledger — it is open-source, operated by a non-profit under published rules, and federated: several operators can run instances that exchange records, so that no single operator becomes the new gatekeeper.

# Part IV — Making it real

## 12. Three pilots

The pilots are designed to be small, measured against a stated baseline, and stoppable. They run in the same field so that their records interlock: the truth market produces resolution and usage data; the retroactive round consumes it; the flight recorder produces contribution records that the field's hiring committees can use.

### 12.1 Choosing the field

Criteria: claims resolvable in weeks; an existing replication or benchmark culture; a community with some appetite for experiment; and, decisively for the first year, low cost per resolution. Empirical machine learning satisfies all four and is the first-year choice: a claim can be re-run on a held-out benchmark split for hundreds of euros, so the resolution fund buys enough resolutions to test the instrument. Experimental psychology satisfies the first three and is the natural second-year field with a larger resolution fund. A materials subfield with robotic synthesis is a third candidate if a cloud laboratory partner is available. Within the chosen field, the pilot goes to whichever community volunteers a host organization and five hundred claims.

### 12.2 Pilot A — Truth market with resolution fund

**Scope.** ~500 claims registered from the field's last two years with hosts' consent; each with a resolution protocol from a template; bonds optional in the pilot (hosts who post them are tracked separately). The field must be one where resolution is cheap — in computational science and machine learning, re-running a claim on a held-out benchmark split costs hundreds to a few thousand euros — so that the resolution fund buys at least sixty resolutions. In an experimental field, where a replication costs €10,000–€30,000, the same fund would buy five to ten, too few to test the instrument; such a field is a second-year pilot with a larger fund or a smaller claim set.

**Budget.** Subsidy fund €150,000; resolution fund €100,000 (target: ≥60 resolutions at ≤€1,700 average); platform and operations €50,000. Total €300,000.

**Participants.** Any accredited researcher; institutional traders (structured panels) allowed; AI agents under principals with position limits.

**Legal design.** Play-money allocation with cash prizes for forecasting performance; no real-money wagers.

**Resolution.** Triggered when the resolution fund reaches the protocol's stated cost, with base allocations granted by confirmed reliance and price uncertainty; resolution auction among pre-accredited laboratories; independent adjudicator per protocol.

**Timeline.** Months 1–2 registration and protocol templating; months 3–10 trading and resolutions; months 11–12 analysis.

**Primary outcomes.** (i) Predictive accuracy of final prices against resolution, versus citation-count and venue baselines. (ii) Number and cost of resolutions triggered. (iii) Out-of-sample separation of forecasters by ledger score.

**Stop rule.** If, under the pre-registered analysis, prices do not beat the citation baseline at predicting resolution on the first 40 resolutions, stop and publish.

### 12.3 Pilot B — Flight recorder with counterfactual replay

**Scope.** A plugin for two common environments (a notebook system and an agent framework) producing signed, chained logs; a replay engine with fixed seeds; a contribution-record generator.

**Budget.** Engineering €120,000; pilot support and independent replays €60,000; operations €20,000. Total €200,000.

**Participants.** Ten to twenty volunteer groups in the same field; at least two hiring or doctoral committees willing to use a logged session.

**Timeline.** Months 1–4 build; months 5–10 use; months 11–12 replays and analysis.

**Primary outcomes.** (i) Replay success rate. (ii) Agreement between replay-based contribution records and blinded expert judgment on 30 sampled cases. (iii) Measured friction versus unlogged work. (iv) At least one real decision using a logged session.

**Stop rule.** If replay-based credit does not correlate with blinded expert judgment above chance on the sample, stop and publish.

### 12.4 Pilot C — Retroactive round with impact certificates

**Scope.** A €500,000 round for datasets, tools, methods and negative results in the field; nominations generated from usage records of Pilot A's resolutions and the field's provenance graph; twelve paid, rotating evaluators; a small impact-certificate market where early supporters of nominated items can hold certificates paying from awards.

**Budget.** Awards €500,000; evaluator pay and operations €50,000. Total €550,000.

**Timeline.** Months 1–8 usage-record accumulation; months 9–11 evaluation; month 12 awards and analysis.

**Primary outcomes.** (i) Awarded items show measured use. (ii) Certificate prices predict awards. (iii) Distribution of awards across groups by prior funding level.

**Stop rule.** If awards concentrate in the top-funded quartile beyond their share of measured use, redesign before a second round.

### 12.5 Governance common to all three

An oversight board of five: the funder, the host community, an independent assessment organization, a researcher-rights representative, and a methods statistician. Conflict disclosures published. Every resolution protocol in Pilot A passes the screening step in Section 9.5 before it is offered to a laboratory; protocols involving human participants name their ethics approval or are unpriceable. All protocols, code and data open. A pre-registered analysis plan for each pilot. Results published regardless of outcome — the pilots are themselves claims with resolution protocols.

### 12.6 Combined budget

| Pilot | Cost |
|---|---|
| A — Truth market | €300,000 |
| B — Flight recorder | €200,000 |
| C — Retroactive round | €550,000 |
| Oversight, evaluation, publication | €50,000 |
| **Total** | **€1,100,000** |

For comparison, the field's conventional review effort for one large conference — twenty thousand reviewers at a conservative four hours each — is roughly eighty thousand hours of donated expert time per year, worth several million euros at any reasonable rate, producing no reusable record.

---

## 13. Transition: the first five years

Nothing here requires everyone to agree first. The sequence is designed so that each step is useful on its own and makes the next cheaper.

**Year 1 — Prove the instruments.** Run the three pilots in one field. Publish everything. Begin the counting-ban conversation with two or three willing institutions.

**Year 2 — Second field, first institutions.** Repeat in a contrasting field (experimental if the first was computational). Two institutions adopt logged examinations for doctoral defences and remove counts from one department's promotion criteria. One funder adds a 5% retroactive slice to one program. One journal begins maintaining an account of one question and acts as adjudicator for the pilot's protocols.

**Year 3 — Funder conditions.** One national or foundation funder makes the counting ban a condition of institutional eligibility and adds resolution protocols as a condition for claims it funds. Markets extend to claims funded that year. Impact certificates trade on a public venue. A capacity spot market opens at one shared facility.

**Year 4 — Structure.** Essential-facility rules drafted for research systems above a capability threshold; consultation on accreditation and rates. First research cooperative chartered. Science dividend fund established with a levy on commercial use of covered systems.

**Year 5 — Consolidation.** Several fields, several funders, several journals. Maintained accounts become the default citation target for policy and industry. Hiring files in participating institutions contain ledgers and logs, not counts. The pilots' stop rules, all still in force, have either been passed or have ended something.

> **What a conference could do next year.**
>
> A machine-learning conference accepts five thousand papers. For each, the authors register one claim with a resolution protocol drawn from a template — for most ML claims, "reproduces on the stated benchmark within stated tolerance, on a held-out split the authors have not seen." A market opens on each; the twenty thousand reviewers, who already spent four hours per paper, are invited to trade with allocated points and compete for prizes. By the end of the conference the field has five thousand prices instead of fifteen thousand reviews nobody will read again; the two hundred claims with the most money at risk are resolved on held-out data within a month by resolution auction; the ledger begins. Bonds are optional in year one. Nothing about submission changes. The cost is a platform integration and a prize pool smaller than the catering budget.

### 13.1 What each actor does first

| Actor | First move | Cost |
|---|---|---|
| A funder | Fund the three pilots; add a retroactive slice to one program | €1.1M plus 5–10% of one program |
| A university | Adopt logged doctoral examinations in one department; remove counts from its promotion criteria | Policy change; training |
| A journal or society | Maintain one account; act as adjudicator for one set of protocols | Editorial time, paid by the assessment fund |
| A conference | Register accepted claims with resolution protocols; open markets on them | Platform integration |
| A laboratory | Post bonds on its strongest claims; adopt a recorder for one project | Bond capital; plugin install |
| A researcher | Trade on ten claims in her field; keep a log on one project | Hours |
| A regulator | Begin consultation on essential-facility rules for research systems | Staff time |

### 13.2 Why each party would participate before anyone requires it

A design that only works under mandate will never get its mandate. Each party has a reason to join while the system is still voluntary.

| Party | What they get from joining early |
|---|---|
| A laboratory with strong results | A bond that survives is a credential no paper count can match; a priced claim attracts reliant parties and pooled experiments; a logged workflow makes its people's contributions attributable before a senior co-author can absorb them |
| A laboratory with private doubts about a published claim | Payment for being right, without having to publish a negative-result paper nobody wants |
| A company that needs to rely on a result | Independent resolution for a fraction of the cost of its own study; a hedge; a place to express reliance without publishing |
| A journal or society | A paid role — adjudication and maintained accounts — that replaces an unpaid, collapsing one |
| A funder | Its money produces prices, resolutions and usage records instead of unread reports; its portfolio's reliability becomes measurable |
| A junior researcher | Contributions measured and attributable; a ledger that starts at zero for everyone; newcomer reserves in every allocation |
| A replication laboratory or contract research organization | A market for replication labor that does not exist today |
| A forecaster with no laboratory | Payment and a credential for knowing which claims are fragile |
| A university | A hiring file that can be read in an afternoon and cannot be gamed by volume |

The party with the least to gain is a laboratory whose standing rests on volume. That is the party the current system over-rewards, and the design is not neutral about it.

### 13.3 What disappears in return

Adoption fails if the new obligations are added on top of the old. Institutions that adopt the counting ban stop requesting publication lists. Funders that accept resolution protocols stop requesting narrative progress reports for the same work; the maintained account is the report. Journals that adjudicate stop pre-publication review for claims with protocols. Double reporting proves nothing and kills adoption.

---

## 14. Economics

### 14.1 An illustrative reallocation

Consider a funder disbursing €100 million a year through investigator grants. Under this proposal, after transition:

| Line | Share | Amount | Notes |
|---|---|---|---|
| Investigator and program grants (conventional and autonomous) | 45% | €45M | Reduced from ~90%; still the largest line |
| Shared facilities and capacity (including spot-market subsidy and newcomer reserves) | 15% | €15M | Telescope-time model |
| Retroactive awards | 10% | €10M | Datasets, tools, negative results, maintenance |
| Assessment: market subsidies, resolution funds, adjudication, replays | 10% | €10M | Replaces unpaid peer review |
| Fellowships (people, not projects; lotteries at the boundary) | 10% | €10M | Human-judged share |
| Quadratic matching pool for infrastructure | 5% | €5M | Community-steered |
| Futarchy experiment | 2% | €2M | Small, watched |
| Apprenticeship, training, oversight, publication | 3% | €3M | Real cost, counted |

The shares are opening bids. The point is that assessment, retroactive reward and shared capacity — currently funded from volunteers' evenings and grant overheads — become explicit lines.

### 14.2 What assessment costs today

Peer review is not free; it is unpriced. A 2021 estimate put the global time spent on journal peer review in 2020 above 100 million hours, with the salary-based value of United States reviewers' time alone above $1.5 billion — and the authors note the figure is an underestimate because it covers only a portion of journals. That expert time is spent on a process that produces no reusable record and, at the leading venues, cannot catch a fabricated citation. A 10% assessment line that produces prices, resolutions, ledgers and usage records is not an additional cost; it is the first time the cost has been written down.

### 14.3 Cost per resolved claim

A conventional replication study in psychology or materials costs €20,000–€80,000 and takes a year to organize. Under Pilot A, the marginal cost of resolution is the auction price plus adjudication, and the decision to resolve is made in days. The pilot's target — cost per resolved claim below a conventional replication — is conservative; the larger saving is in the claims that are never resolved because nobody relied on them.

### 14.4 Who pays for the science dividend

A levy of a small percentage on commercial use of research systems above the essential-facility threshold, or licensing revenue from publicly owned systems, capitalizes the fund. At the scale of the current AI research infrastructure market, a 1% levy would capitalize a fund of hundreds of millions within a few years. The number is illustrative; the mechanism is not.

---

## 15. Risk register

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| 1 | Markets too thin to price most claims | High | Medium | Display low-volume prices as unassessed; subsidy weighted by reliance; structured panels as institutional traders | Pilot A lead |
| 2 | Commercial manipulation of prices | Medium | High | Position limits; bond forfeiture; manipulation is a subsidy to informed traders | Market operator |
| 3 | Resolution disputes recreate the review queue | Medium | Medium | Protocols fixed at registration; named adjudicator; adjudicator ledger | Adjudication service |
| 4 | Gambling law blocks real-money markets | High in some jurisdictions | Low | Prize design; institutional-only markets | Legal counsel |
| 5 | Researchers refuse logging | Medium | High for Pilot B | Researcher-owned keys; sealed by default; organizational authorship without stigma | Pilot B lead |
| 6 | Replay-based credit disagrees with expert judgment | Medium | High for Pilot B | Stop rule; descriptive records as fallback | Pilot B lead |
| 7 | Retroactive rounds gamed by self-promotion | High (precedent) | Medium | Nomination from usage records; paid rotating evaluators; one field per round | Pilot C lead |
| 8 | Impact certificates become detached speculation | Low–Medium | Medium | Certificates pay only from awards requiring usage evidence | Pilot C lead |
| 9 | Counting ban ignored in practice | High | High | Funder conditions; audits; "what disappears in return" | Funders |
| 10 | Essential-facility rules captured by incumbents | Medium | High | Public accreditation body; published rates; sunset and review clauses | Regulator |
| 11 | Concentration persists despite rules | Medium | High | Cooperatives; consortium systems; the dividend funds alternatives | Coalition |
| 12 | Long-horizon fields excluded | High if ignored | Medium | Intermediate observables; consensus marks; honest non-pricing | Field maintainers |
| 13 | Junior researchers bear transition costs | Medium | High | Existing commitments honored; apprenticeship share; training funded | Institutions |
| 14 | Double reporting kills adoption | High if ignored | High | Explicit list of what disappears | Funders, institutions |
| 15 | AI agents game every mechanism at once | Medium | High | Volume-proof design; principals; ledgers for agents; sampled audits | Oversight board |
| 16 | The proposal becomes a platform monopoly | Low–Medium | High | Open record formats; federation; no single operator | Oversight board |
| 17 | Political outcry over "betting on science" | Medium | High | Prize design, not wagering; start in fields where no life is the contract; exclude markets that create incentives to harm | Communications; screening service |
| 18 | Securities or gambling regulators block certificates or markets | Medium | Medium | Conservative legal forms; sandbox; institutional-only variants | Counsel |
| 19 | A wrong resolution stands | Medium | Medium | Resolutions are re-openable claims; performing laboratories have ledgers | Adjudication service |

---

## 16. Objections and replies

**"This turns science into gambling."** Real-money markets on claims are gambling in some jurisdictions and are not required. The pilot uses allocated play-money with prizes; institutional-only markets are another lawful form. What matters is that trading has a cost and being right pays. Peer review already asks scientists to bet their time and reputation on judgments; this makes the bet visible and scores it.

**"This turns science into finance."** It attaches money to information, which science has always done through grants, prizes and salaries. The difference is that here the money follows demonstrated reliability and use rather than a proposal's prose. Every mechanism is chosen to be volume-proof; the one thing the current system rewards — producing more — is the one thing none of these reward.

**"Markets will be wrong."** Sometimes. The evidence is that they are wrong less often than reviewers, and, unlike reviewers, they say how confident they are and get scored. A wrong price is corrected by whoever knows better and is paid for it. A wrong review is corrected by nobody.

**"This is surveillance."** The log is owned by the researcher, sealed by default, disclosed by choice. Institutions never see the stream. The alternative — inferring capability from outputs the researcher may not have produced — is worse for the researcher, not better.

**"What about theory, mathematics, the humanities?"** Section 8 is candid: markets and bonds fit fields with resolution and fit others weakly or not at all. For formal mathematics, resolution is a proof check and the fit is excellent. For conceptual work, markets on adoption by maintained accounts and retroactive awards apply; recorders mostly do not. For interpretive scholarship, only the record and retroactive funding apply. The proposal does not pretend otherwise.

**"Won't AI agents just game everything?"** They will try. That is why every mechanism is volume-proof, why agents act under accountable principals with position limits, why agreement among copies of one model counts once, and why agents have their own ledgers. A mechanism that can be gamed by producing more is excluded by design principle 4. Gaming by being *right* is not gaming.

**"Junior researchers will be exploited."** The transition risk is real and is in the register. Existing commitments are honored; the apprenticeship share is funded; and a junior researcher's logged contributions are, for the first time, attributable in a way a senior co-author cannot appropriate.

**"What about the Global South and under-resourced institutions?"** Newcomer reserves are fixed before outcomes in every allocation mechanism; quadratic funding favors breadth of need over depth of one pocket; essential-facility access is by accreditation, not by wealth; and the counting ban removes an advantage that currently accrues to those who can afford volume. The proposal is not neutral on this; it is designed to reduce the advantage of resources.

**"Companies won't participate."** They will if the bargain is real: independent characterization they can use with customers, pooled experiments at a third of the price, access to shared capacity, and a place to express reliance (buying contracts) without publishing. Confidentiality windows can be honored with time-locked disclosure. What they cannot have is a veto on unfavorable results after paying.

**"Why would anyone trade?"** Because being right pays, in prizes or money; because reliant parties need to know; because the ledger is a credential; and because structured panels trade as institutions. The Replication Markets project attracted serious forecasters with modest prizes.

**"This has been tried — DeSci, tokens, blockchains."** Some pieces have; the proposal cites what worked (retroactive and quadratic funding at scale) and what did not (token governance). Nothing here requires a blockchain. It requires signed records, a market maker, and a replay engine.

**"Isn't this just a more sophisticated metric?"** A metric is computed from outputs and can be inflated by producing more. A price backed by money, a replay of logged work and a usage record cannot. The distinction is principle 4 and it is the whole design.

**"Betting on whether a cancer treatment works is ghoulish."** This objection killed a market before: in 2003 a DARPA program proposing markets on geopolitical events was cancelled within days of public outcry over "terrorism futures," whatever its analytical merits. Three answers. First, the pilot design is a forecasting competition with prizes, not wagering, and forecasting tournaments on clinical and public-health questions already run without outrage. Second, the alternative to a market on whether a treatment works is not dignified silence; it is a patient population relying on a claim nobody has priced or checked. Third, the design explicitly excludes markets whose resolution would create an incentive to harm — a market on an individual's outcome, for example — and the screening service in Section 9.5 exists to draw that line. Political acceptability is a real risk and is in the register; it is managed by framing, by design, and by starting in fields where nobody's life is the contract.

**"You are atomizing knowledge into betting slips."** A claim record is scoped and can be as coarse as a theory's central prediction; the report attached to it is as discursive as any paper; and not everything must be a claim — exploratory findings, methods and syntheses are registered without one. Markets need a resolvable statement; they do not need science to be made of nothing else. The reliance graph (Section 11.3) is precisely a representation of how claims depend on each other, which is the holism the objection is worried about, made inspectable.

**"Impact certificates are securities; markets are regulated; you will be shut down."** Possibly, in some jurisdictions, in some forms. Impact certificates can be structured as non-transferable claims on prizes, or traded only among accredited institutions, or run in a regulatory sandbox; the pilot uses the most conservative form. Markets use the prize design. The proposal is indifferent to the legal wrapper as long as trading has a cost and being right pays; the risk register assigns this to counsel and it is not a reason to do nothing.

**"Commercial research can't register claims — the data are secret."** Markets trade on outcomes, not on data; a claim can be priced while its provenance is sealed, and resolved by an independent laboratory under a confidentiality agreement with time-locked disclosure. What the company gives up is only the ability to keep an unfavorable resolution off the record after it has paid for one.

**"What if the pilots fail?"** Then they stop, and the field has learned something at a cost lower than one year of one conference's review effort. The stop rules are in Section 12 and they are real.

---

## 17. Further ideas

These are not in the pilots. Some are half-built; some are provocations. They are here because the problem is large and the design space is not exhausted.

**Executable claims.** Register each claim with a machine-checkable prediction and a data schema; as data arrives, the record scores the claim automatically and the market trades on the score. Unit tests for science, with money attached.

**Resolution auctions as a labor market.** Section 5 introduces them; the full version is a standing exchange where accredited laboratories list capacity and price for replication classes, and where a laboratory's ledger is its credit rating.

**Adversarial collaboration exchanges.** Disputes are listed with pooled bounties; opposing parties register what would change their minds; independent laboratories bid to run the discriminating test. Precedent: the registered adversarial collaboration on theories of consciousness, which showed the organizational pattern works even when minds do not change.

**Debate as review.** Two AI systems argue for and against a claim before a time-limited judge; the transcript is the review artifact and the judge's decision is on the ledger. Proposed in AI-safety research in 2018; never tried at scale on scientific claims.

**Attention tokens.** Each researcher receives a fixed annual budget of review-priority credits and pledges them to claims they intend to rely on; a claim's place in the human-review queue is the sum of pledges. This replaces "important" with "needed."

**Warranted results.** Producers sell results with a warranty; underwriters price the risk of retraction; the premium is the public reliability signal and pays for the audits. Product safety certification has worked this way for over a century.

**Replication insurance for funders.** Funders buy insurance against the failure of findings they funded; premiums are priced off the markets. A funder whose portfolio replicates badly pays more, which aligns funders with reliability rather than volume.

**Commit-reveal preregistration.** Publish a cryptographic hash of a prediction to a public timestamp chain; reveal later. Preregistration becomes free, universal and impossible to backdate. Priority disputes are settled by the chain.

**Time-capsule predictions.** Scientists register ten-year predictions about their fields; the ledger scores them at maturity. A prediction record becomes a career document.

**Fork markets.** When two maintained accounts of a question diverge, a market on which will be adopted by the field's major accounts by a given date gives the disagreement a price and a resolution.

**Knowledge bonds, fully specified.** Section 8.1 introduces them; the full version is a standard instrument with a coupon that steps down on each sustained challenge and a face value paid at term to whoever holds it, so that a long-horizon claim's survival is priced continuously and a researcher can sell a stake in a claim that will outlive her career.

**Scientific escrow.** Commercial data deposited under time-lock and released automatically after an agreed period, so that confidentiality windows cannot become permanent vetoes.

**Verifiable computation badges.** Results whose computation is attested by a trusted execution environment or a succinct proof carry a badge that means "this ran as described." For computational science this can replace reproduction for a class of claims.

---

## 18. Conclusion

The paper was a remarkable compression: one artifact that told institutions what to trust, whom to fund, whom to hire and whom to honor. It worked because producing one was expensive and human. That condition has ended, and the institutions built on it are failing in public.

This proposal does not try to make the paper expensive again. It replaces inference with observation. A claim's dependability is priced by people who pay to be wrong and are paid to be right, and the money at stake buys the experiment that settles it. A person's contribution is recorded while it happens and measured by replaying the work without them. Value is paid for after it is visible, by evaluators with usage evidence in hand, and shared infrastructure is steered by the many who need it rather than the few who can pay. Around these sit rules about who may own the machines, how people are employed and trained, and how human inquiry is funded when machines produce most of the results.

None of it requires everyone to agree first. It requires one funder, one field and one year, three pilots with stop rules, and the willingness to let the results end something. The precedents exist. The instruments exist. What has been missing is the decision to stop patching inference and start observing.

---

# Appendices

## Appendix A — Glossary

**Accountable principal.** The organization or person under whose authorization a workflow acts and who answers for its outputs.

**Adjudicator.** The independent service named in a resolution protocol that rules on whether a resolution was validly performed.

**Automated market maker.** A program that always quotes a price for a contract, adjusting as people trade, and loses at most a fixed subsidy to informed traders.

**Bond.** Money posted behind a claim, forfeited to whoever successfully refutes it, returned with a premium if the claim survives its term.

**Calibration ledger.** A public record of how well a person's or system's stated confidence in claims matched outcomes; scored with a proper scoring rule such as the Brier score.

**Consensus mark.** An interim price assigned to a long-dated contract by an expert panel whose own calibration is tracked.

**Contribution record.** The measured marginal contributions of people to a logged piece of work, obtained by replay.

**Counterfactual credit.** A person's measured contribution to logged work, found by replaying the work without their interventions.

**Dominant assurance contract.** A crowdfunding arrangement in which pledgers are refunded with a bonus if the target is missed, so that pledging is always the best move.

**Essential facility.** Infrastructure whose owner must, by law, grant access to competitors on fair terms because it cannot practically be duplicated.

**Flight recorder.** A signed, tamper-evident log of human–AI interactions during research, controlled by the researcher.

**Futarchy.** A decision procedure in which people vote on the outcome they want and markets choose the action most likely to produce it.

**Impact certificate.** A tradeable claim on a share of any future retroactive award for a piece of work, held by whoever funded it early.

**Maintained account.** A versioned, citable synthesis of the current state of a question, with stated revision conditions, maintained by a journal or society.

**Prediction market.** A market in contracts that pay out depending on a future event; the price is the crowd's probability estimate.

**Quadratic funding.** A matching rule that favors projects supported by many small contributors over projects supported by one large one.

**Resolution auction.** A procurement in which accredited laboratories bid to perform a triggered resolution.

**Resolution fund.** Money attached to a market that pays for the experiment or adjudication that settles the claim once enough is at stake.

**Resolution protocol.** The statement, fixed at registration, of what test settles a claim, who may run it, what counts as success, and who adjudicates disputes.

**Retroactive funding.** Money paid for work after its usefulness has been demonstrated, rather than in advance on a proposal.

**Science dividend.** A permanent fund, capitalized from the productivity of AI research systems, that pays for human inquiry, training and fellowships.

**Spot market.** A market in which capacity is sold immediately at a price that rises and falls with demand.

**Usage record.** A derived record of which research objects were relied on by which resolutions, claims and programs.

## Appendix B — Record templates

### B.1 Claim record

```
claim_id:            <content hash>
statement:           <scoped claim: population, conditions, effect, uncertainty>
claim_type:          <replication | prediction | formal | computational | ...>
host:                <organization id>; obligations: records, challenges, corrections
authorization:       <workflow or person id>; scope; expiry
provenance:          <data, code, instruments, dependencies; log id if disclosed>
resolution_protocol: <see B.2>
bond:                <amount; term; forfeiture conditions>
market:              <subsidy; resolution threshold; resolution fund id> | none
contributions:       <see B.3> | "not established"
status:              [registered | priced | resolution commissioned | resolved:<outcome>
                      | challenged | superseded_by:<id>]
```

### B.2 Resolution protocol

```
test:                <what is done: replication design, prediction target, formal check>
performer:           <who may perform: accredited class | named lab | any with ledger ≥ x>
success_criterion:   <quantitative threshold or checkable predicate>
partial_outcomes:    <qualification vs refutation; bond consequences for each>
validity_checks:     <pre-specified; who adjudicates disputes>
cost_estimate:       <sets the resolution threshold>
expiry:              <after which the claim is "unresolved, expired">
```

### B.3 Contribution record

```
log_id:              <hash of the workflow log>
logging_level:       <interactions | interactions+data | full environment>
replay_method:       <deterministic | seeded (n seeds) | not replayable>
contributors:
  - id: <person>; interventions: <n>; outcome_changing: <k>; shapley: <value ± sd>
  - ...
workflow:            <id; host; version>
unlogged_segments:   <list, or none>
```

### B.4 Retroactive award criteria

Eligibility: appears in the usage records of at least *n* resolved claims or maintained accounts in the round's field. Evidence: the usage records themselves; no self-description required. Evaluators: paid, rotating, conflict-screened, scored on their own consistency. Distribution: by evaluator allocation, published with reasons.

### B.5 Market terms

Contract: pays 1 if resolution succeeds, 0 otherwise; qualification outcomes settle per protocol. Market maker: logarithmic scoring rule with subsidy *b*. Position limits: per principal, published. Resolution trigger: resolution fund ≥ protocol cost estimate; base allocations by the published priority rule. Settlement: on adjudicated resolution or expiry.

## Appendix C — Worked numbers for one field

Take a field producing 5,000 registered claims a year.

- Markets opened: 1,500 (30%), those with a host or reliant party requesting one. Market-maker subsidy €300 each: €450,000.
- Resolution-fund base allocations: granted only to markets crossing the open-interest floor — about 200 — so the assessment fund's exposure is bounded by its priority rule, not by the number of markets.
- Resolutions triggered: 150 (10% of markets). Average auction price €15,000: €2.25M, of which roughly a third comes from reliant parties' direct payments and resolution fees, the rest from base allocations.
- Bonds posted: 800 claims, average €1,500: €1.2M at risk, returned with premium on survival; forfeited on roughly 10%: €120,000 to refuters.
- Retroactive round: 10% of the field's funding, say €5M, to ~200 items nominated from usage records.
- Assessment total ≈ €3M against a field budget of €50M: 6%.

Compare: the same field's conventional review, at 5,000 papers × 3 reviews × 4 hours × €60, is €3.6M of unpriced expert time producing no record. The instruments cost about the same and produce prices, resolutions, ledgers and usage records.

## Appendix D — Annotated precedents

| Precedent | What it shows | What it does not show |
|---|---|---|
| Dreber et al. 2015; Camerer et al. 2016, 2018 | Markets among scientists predict replication | Scaling beyond hundreds of claims; long-horizon claims |
| Holzmeister et al. 2025 (decision market) | Markets can choose what to replicate; 83% vs 33% | Commercial manipulation at scale |
| DARPA SCORE 2019–22 | Forecasting 3,000+ claims is feasible; structured panels competitive with markets | That the forecasts changed any institution's behavior |
| Replication Markets prizes ($142k) | No-loss prize design attracts serious forecasters | That it works without a sponsor |
| Hanson LMSR 2003 | Subsidized market makers with bounded loss | — |
| Iowa Electronic Markets | Decades of accurate small markets | Applicability to technical claims |
| USPTO guidance, Nov 2025 | Law requires documented human conception; AI treated as a tool | How to document it — which is the recorder |
| C2PA | Signed provenance is deployable in consumer devices | Adoption without vendor support |
| Optimism RetroPGF (60M+ OP; round 3 ≈ $90M) | Retroactive funding works at scale | That it resists gaming without usage evidence — it did not |
| Gitcoin ($60M+, millions of donations) | Quadratic funding works at scale; Sybil defense needed | Applicability to scientific infrastructure |
| Tabarrok 1998 | Dominant assurance contracts solve free-riding in theory | Large-scale scientific use |
| Cloud laboratories | Experiments can be bought by the run | Price transparency across providers |
| SNSF lotteries | Funders can randomize at the boundary | Randomizing more than the boundary |
| DORA; China 2020 | Declarations do little; enforcement does something | That enforcement survives without funder conditions |
| Terminal Railroad 1912 | Essential-facility doctrine exists | Application to AI systems — untested |
| Alaska, Norway funds | Permanent dividend funds are stable | Funding from a levy rather than resources |
| Registered adversarial collaboration on consciousness | The organizational pattern works | That minds change |
| NeurIPS 2025 (21,575 submissions; 100 fabricated citations) | The current system has scaled past its verification capacity | — |
| DARPA policy analysis market, 2003 (cancelled) | Markets on sensitive outcomes can be killed by public reaction regardless of merit | That the reaction is unavoidable with a prize design and careful scope |
| Aczel, Szaszi & Holcombe 2021 | Peer review consumed >100M hours in 2020, >$1.5B of US reviewers' time | That paying for assessment produces better assessment — the pilots test that |

## Appendix E — Revision record

*Version 1.0 (initial full draft).* Consolidated from a nine-page explainer and a three-page summary. Added: full pilot protocols with stop rules; transition path; economics; risk register; objections; record templates; annotated precedents; Section 8 on fit by field, including long-horizon adaptations; resolution auctions; the USPTO wrinkle for the science dividend; structured elicitation feeding markets. Withdrawn from earlier drafts: submission caps, forfeitable deposits, compulsory review-for-submission, organizational audits as certification, and the claim that "every function of the paper failed."

Subsequent review rounds and their changes are recorded below.

*Consistency sweep (26 September 2026).* A systematic scan for phrasings superseded by the priority-rule change found five residual "open interest crosses the cost" statements — in the claim record, the base-allocation sentence, the Wednesday example, the design-details bullet and the Pilot A resolution line — and corrected them to the resolution-fund trigger with allocations by confirmed reliance times uncertainty.

*Alignment with v3 (26 September 2026).* Two changes back-ported from the full proposal: the resolution-fund priority rule now ranks by confirmed reliance times price uncertainty, with open interest as a disagreement signal, after a sensitivity analysis showed open interest alone fails when attention is uncorrelated with reliance; and the calibration ledger carries the caveat that it needs several hundred resolved positions to separate forecasters.

*Review round 5 — final proof.* Removed duplicates between Section 17 and the main text after promotions; corrected page layout (forced page breaks before Parts produced near-empty pages); verified heading numbering and cross-references; final read for prose.

*Review round 4 — numbers and consistency.* Found and fixed: resolution-fund base allocations "at market opening" would have cost €9 million across the 1,500 markets in Appendix C against a €3 million assessment total — allocations are now granted only when open interest crosses a published floor, and the appendix reflects it; Pilot A's €100,000 resolution fund would buy five to seven replications at experimental-field prices while its stop rule requires forty — the first-year field is now fixed as computational, where resolution costs hundreds of euros, with experimental psychology as the second-year field; the Claim 47 record, the first-build paragraph and the pilot description were aligned; cross-references checked after renumbering.

*Review round 3 — adversarial domain reviews (science studies, working scientist, counsel, historian).* Added: "prices need reasons" — trade rationales and challenge records as the reasons behind a price; "resolutions are not final" — resolutions as re-openable claims with their own provenance; objections and replies on ghoulishness (with the 2003 DARPA policy-market cancellation as the cautionary precedent), atomization, securities and gambling regulation, and commercial secrecy; three new risks; a record paragraph in the executive summary.

*Review round 2 — funder, junior researcher and structure.* Added: a lifecycle diagram (Section 4); bonds posted by hosts, never individuals; provisional ledgers for the first fifty positions; critic leagues promoted from "further ideas" into Section 5; research vouchers promoted into Section 7; human tracks and early-career protections (Sections 10.6–10.7); the reliance graph and revalidation cascades (Section 11.3), which make explicit the replacement for the citation graph; a federated, non-profit platform rule; and a concrete "what a conference could do next year" scenario.

*Review round 1 — logic and incentives (skeptical economist; red team).* Found and fixed: (1) the resolution-fund money flow was incoherent — open interest is traders' money and cannot pay a laboratory; replaced with a fund built from base allocations, a resolution fee on trades, and direct payments by reliant parties, with a mechanical trigger and a published priority rule; (2) the manufacturer "buying to express reliance" was economically wrong — replaced with a hedge plus a direct payment for resolution; (3) the bond "premium" was undefined and could be farmed by bonding trivially true claims — now paid from a pool of forfeited bonds, weighted by open interest; (4) no challenger stake — added at 10% of bond; (5) hosts could short their own claims — prohibited; (6) Shapley "a handful of replays" was wrong — corrected to 2^n with sampling beyond small teams, plus model-version pinning; (7) no rule for inadequate or amended protocols — added; (8) journals adjudicating claims in their own accounts — separation rule added; (9) no adoption incentive — Section 13.2 added; (10) no safety screening — Section 9.5 added; (11) reviewer-cost estimate replaced with the published figure; (12) ledger scoring clarified into realized performance and proper-scored explicit forecasts, with difficulty displayed.

