# Price Trust, Record Contribution, Pay for Value

## How to organize science when AI does most of the work — the long version, for readers who are new to the ideas

*Version 1.2 — explainer edition, aligned with the full proposal v3.4 — 26 September 2026*

---

## Why this document exists

The short version of this proposal fits on three pages, and several readers said it reads like a telegram: prediction markets, automated market makers, flight recorders, retroactive funding, quadratic matching, essential facilities. Each of those is an existing idea with a track record somewhere outside science, but none of them is common knowledge inside it.

This version slows down. Every mechanism is introduced with a plain-language explanation, an everyday analogy, and a worked example using one running case — a single scientific claim we follow from the moment it is made to the moment someone relies on it. Boxes marked **"What is…"** can be read on their own. The final sections contain a glossary and a list of the precedents referred to.

The argument itself has not changed. The paper used to let us *infer* three different things — that a result was dependable, that its producers deserved more money, and that the named people were capable. AI-produced research breaks that inference. Instead of trying to repair it, this proposal replaces it with three things that do not depend on inference: **markets that price trust and buy their own answers, recorders that capture contribution while it happens, and funding that pays for value after it is demonstrated.**

---

## 1. The problem, told through one paper

Picture a materials laboratory in 2026. An AI system reads the literature, proposes that a small amount of a particular additive should slow the degradation of lithium-ion battery electrolytes, designs the experiments, runs them on a robotic bench, analyses the data, writes the paper, drafts the contribution statement, and — because the journal also uses AI — receives reviews that were largely machine-written too. Three humans are listed as authors. One of them, a battery chemist we will call Lena, made a decisive intervention halfway through: she overruled the system's choice of additive family based on years of bench experience. The other two authorized the budget and maintained the equipment.

The paper looks exactly like any other paper. That is the problem.

For a century, one artifact carried six jobs. A paper **reported** a finding, **claimed** a discovery, **credentialed** its authors, **justified** the next grant, **identified** who was responsible, and **conferred** distinction. A hiring committee could look at a list of papers and reasonably infer that the person had the ability to produce them. A funder could infer that a productive group deserved more money. A reader could infer that peer review had filtered out the weak work.

Not all of those jobs have failed. The paper about Lena's additive may well contain a correct result, explain it clearly, and name an accountable organization. What has failed is **inference**: the step from "this document exists" to "this named person demonstrated ability," and increasingly the step from "this passed review" to "this is dependable." Both inferences depended on production being expensive and human. Neither holds when production is cheap and mostly automated.

The symptoms are visible everywhere. Conferences receive tens of thousands of submissions. Reviewers, overwhelmed, use the same tools as authors. Publication counts, once a rough proxy for capability, now measure access to compute. And the honest lab that says "the AI did most of it" is penalized relative to the lab that quietly puts human names on machine output.

Two mistaken responses should be named and set aside. **Restricting production** — caps on submissions, deposits, mandatory reviewing — punishes the honest and re-imports the human author as the bottleneck; the world is better off with ten thousand true, cheap results than with a hundred expensive ones. **Auditing organizations** — checking a random sample of a lab's output each year — tells you whether the lab's process is sound, not whether the particular result you want to rely on is correct. Both were in earlier drafts; both are withdrawn here.

What remains is to make three decisions separately, each with an instrument that does not require inferring anything from a paper.

| The decision | What we used to look at | What this proposal uses instead |
|---|---|---|
| Is this result dependable? | Whether it passed peer review; where it was published | A market price, backed by bonds, that pays for its own resolution |
| Is more work here worth funding? | The applicants' proposal and publication record | Money paid after value is shown; markets for capacity; matched small pledges |
| What has this person demonstrated? | Their authorship and citation counts | A recording of what they actually did, and a replay of the work without them |

---

## 2. Meet Claim 47

To keep everything concrete, follow one claim through the whole system.

> **Claim 47.** Adding 2% of additive Q to a standard lithium-ion electrolyte halves capacity loss over 1,000 charge cycles.
>
> *Registered by:* the laboratory's host organization, on behalf of an authorized AI workflow. *Human contributions:* to be established from the workflow log. *Resolution protocol:* an independent laboratory runs the preregistered cycling test on three cells from a fresh batch; "replicates" means capacity loss reduced by at least 35% relative to control.

Notice three things already. The claim is registered by an organization, not by three people pretending to have conceived it. Human contribution is a question to be answered from evidence, not a statement to be trusted. And the claim carries, from birth, a precise description of what would settle it. Everything else in this document builds on those three moves.

---

## 3. Instrument one: truth markets

### The idea in one sentence

Instead of asking two anonymous reviewers whether Claim 47 is true, let anyone who thinks they know something put money on it, read the price, and use the money at stake to pay for the experiment that settles the question.

> **What is a prediction market?**
>
> A prediction market is a place where people trade contracts that pay out depending on a future event. A contract on "Claim 47 replicates" pays €1 if the replication succeeds and nothing if it fails. If that contract trades at 60 cents, the crowd is collectively saying there is roughly a 60% chance of success.
>
> Why should a price be more reliable than a vote? Because in a vote everyone counts equally, while in a market people who know something profit and people who guess lose money. A lab that has privately tried and failed to reproduce the effect can sell contracts at 60 cents and collect when the price falls. Their knowledge moves the price; their profit is the payment for revealing it. Prediction markets have forecast elections since the University of Iowa opened one in 1988, and in two large studies led by Colin Camerer, markets among scientists predicted which published psychology and economics findings would replicate with an accuracy that peer review has never demonstrated.

> **What is an automated market maker?**
>
> A market needs someone willing to trade with you at every moment. A human bookmaker does this by quoting odds and adjusting them as bets come in. An automated market maker is a small program that does the same thing according to a fixed formula: it always quotes a price, raises the price when people buy and lowers it when they sell. It will, on average, lose a bounded amount of money to well-informed traders. That bounded loss is the **subsidy**, and it is the cleverest part of the design: the subsidy is precisely the payment for the information the market extracts. Whoever funds the market maker is buying knowledge at a known maximum price. The standard formula was published by the economist Robin Hanson.

### Claim 47 in the market

The claim is registered on a Monday. The assessment fund seeds a market maker with €400, which caps how much the market can lose to informed traders. The opening price is 50 cents.

On Tuesday, a group in Grenoble that spent the spring trying to reproduce a similar effect and failing sells contracts. The price drops to 32 cents. Nobody had to write a letter to the editor; nobody had to publish a negative-result paper that no journal wanted. The information is in the price.

On Wednesday, host H — which posted the bond and believes the claim — buys, and two laboratories with encouraging pilot data buy too. The price recovers to 41 cents, and open interest reaches €18,000: people with money at risk disagree, which is the market's definition of a claim worth settling. On Thursday a battery manufacturer that would like to build on additive Q makes two moves. It buys "no" contracts as a hedge — if the claim fails, the payout offsets the development work it is about to start — and it pays €8,000 directly into the claim's resolution fund, because what it actually wants is an answer, not a position. Reliance is expressed by paying for resolution.

### Markets buy their own resolution

Here the design departs from ordinary prediction markets. Most markets wait for the world to settle the question. Scientific markets can **commission** the settlement.

Each priced claim has a **resolution fund**. Money enters it from three sources: a base allocation from the field's assessment fund, granted once the claim shows confirmed reliance — other registered claims or a paying party depend on it — and price uncertainty; a small fee on every trade, so that trading volume accumulates the means of settlement; and direct payments from reliant parties who want the question answered. When the fund reaches the cost stated in the resolution protocol — for Claim 47, the €20,000 replication — resolution is commissioned automatically from an independent laboratory, and the market settles on the outcome. Open interest is not spent; it is traders' money and settles the contracts. It measures disagreement, and the full proposal's simulation shows why it must not be the priority signal on its own: forecasters look at what interests them, which need not be what matters.

The consequence is that the claims which get checked are the ones people are both uncertain about and rely upon. Nobody has to decide which of ten thousand claims deserve replication; the money already said so. A claim that nobody trades remains visibly unassessed, which is its honest state. It is not "rejected," and it is not "accepted." It is priced at nothing because nobody needed it yet.

For Claim 47, the replication runs in June. Capacity loss is reduced by 22%, below the 35% threshold. The contract settles at zero. Grenoble profits from being right; host H and the optimistic laboratories lose their positions. The manufacturer's hedge pays out, offsetting the development it had started, and it has an independent answer for €8,000 instead of a €20,000 study it would have had to organize itself. Lena's laboratory learns the effect is real but smaller than claimed, registers a revised claim — "reduces capacity loss by at least 15%" — which supersedes Claim 47, and the bond rolls over to it.

### To author is to underwrite

> **What is a bond?**
>
> When a builder takes on a public contract, they often post a performance bond: money held by a third party that is forfeited if the work is not delivered. It aligns incentives without anyone having to trust anyone's word.

In this system, the organization that registers a claim — never an individual researcher — posts a bond behind it, scaled to how strongly the claim is stated. "Halves capacity loss" is a strong claim; a bond of €2,000 is posted. If someone produces a successful refutation — a failed preregistered replication, a reproducible counterexample, a demonstrated flaw in the analysis — the bond goes to the refuter, who posted a stake of 10% of the bond to lodge the challenge and forfeits it if the challenge fails. If the claim survives three years, the bond comes back with a premium paid from the pool of forfeited bonds, weighted by how much trading the claim attracted — so a host cannot farm premiums by bonding thousands of trivially true claims that nobody contests.

This does something the current system cannot. It makes cheap AI criticism valuable exactly when it is right and worthless when it is noise. A thousand automated objections cost the objector something to lodge and pay nothing unless one is sustained. Meanwhile, the incentive to overstate a claim is priced: the bolder the wording, the more you have to put behind it.

**Credit, in this system, is the bond that survived.** Donald Knuth has paid small reward cheques for decades to anyone who finds an error in his books; Paul Erdős offered cash prizes for solving his problems. Both are bonds on claims at small scale. This proposal makes them the default.

### The calibration ledger replaces the h-index

> **What is calibration?**
>
> A weather forecaster who says "70% chance of rain" is well calibrated if, on the days she says that, it rains about 70% of the time. Calibration is not about being bold or cautious; it is about your stated confidence matching reality. It can be scored with a simple formula — the Brier score, from 1950 — that rewards being confident when right and punishes being confident when wrong.

Every person and every AI system that trades or endorses claims accumulates a public record: realized performance across resolved positions, and the calibration of the explicit forecasts attached to each trade, scored with a proper scoring rule. This record has a property the h-index lacks: **it cannot be inflated by volume.** Publishing more papers raises an h-index; making more bets only improves a ledger if the bets are good. One caveat, established by the simulation in the full proposal: a ledger separates good forecasters from bad only after several hundred resolved positions. The first fifty are therefore provisional, and the ledger is a credential that takes years to earn — fastest in fields where resolution is cheap and frequent.

Hiring committees, instead of counting papers, can look at two things: the calibration ledger, and what the person built or maintained. The first is honest by construction. The second is covered by the next instrument.

### What could go wrong, and what to do about it

*Thin markets.* Many claims will attract no trades. That is fine — they stay unassessed — but a market with two traders can be moved by one. Mitigation: weight the subsidy toward claims with demonstrated reliance, and treat low-volume prices as unassessed rather than as estimates.

*Deep pockets.* A company could try to prop up a claim it profits from. Mitigation: position limits per accountable principal, and the fact that a manipulated price is a subsidy to anyone with real information, who will happily take the other side.

*Resolution disputes.* "The replication was done wrong" is the new "the reviewer didn't understand my paper." Mitigation: the protocol, including what counts as a valid replication, is fixed at registration and adjudicated by an independent service, not by the parties.

*Agent swarms.* A thousand AI agents trading in concert could move prices while pretending to be independent. Mitigation: agents trade under their principal's account, with disclosure of shared models; agreement among copies of the same model counts as one opinion.

### First build

One field with fast, cheap resolution — empirical machine learning, where a claim can be re-run on a held-out benchmark split in days for hundreds of euros, so that the resolution fund buys at least sixty resolutions. About five hundred registered claims. A subsidy fund of €150,000, a resolution fund of €100,000, and a platform adapted from existing open-source market software. Twelve months. Experimental psychology, with its replication culture but €10,000-plus replications, follows in year two.

---

## 4. Instrument two: flight recorders

### The idea in one sentence

You cannot work out afterwards who contributed what to a piece of work done jointly by people and machines — but you can record it while it happens, and then measure each person's contribution by replaying the work without them.

### Why reconstruction is hopeless

Return to Lena's paper. The contribution statement says: "L.N. conceived the additive selection; M.R. and J.K. supervised." Did she? The AI wrote the statement. Perhaps it wrote it accurately. Perhaps it flattered the humans who authorized its budget. There is no way to tell from the document, and asking the humans is asking the people with the strongest incentive to say yes.

This is the point at which most proposals give up and say "require more detailed contribution statements." That is asking a student, after the group project is handed in, to describe who did what. Everyone who has taught knows how that goes. The alternative is to watch the project being done.

> **What is a flight recorder?**
>
> Every commercial aircraft carries a recorder that logs the pilots' inputs and the aircraft's state, continuously, into a protected store. Nobody reads it during a normal flight. When something goes wrong, it answers the question "what actually happened?" without relying on anyone's memory or interest.
>
> A closely related idea now exists for photographs. Under the C2PA standard, a camera can cryptographically sign each image it takes, and each editing step adds a signed record, so that anyone can later tell an original from a manipulation. The signature does not say the photo is *good*; it says what was done to it and by what.

### Attested research workspaces

A research flight recorder is a workspace — a notebook, an agent framework, a lab information system — that logs, in a signed and tamper-evident stream: every prompt a human gives an AI system, every output the system returns, every edit a human makes, every decision point, and every data access. The log is not a surveillance feed. The researcher controls it, decides what to disclose, and can keep it sealed. But only logged work can support a personal credit claim. Unlogged work is published under the organization's name, with human contribution marked "not established." That is not a punishment; it is the honest default.

For Lena's project, the log shows the following. The AI proposed screening additives from family A, citing the literature. Lena wrote, in the workspace, "Family A always looks good in simulation and always fails at the anode interface — we saw this in 2023. Try the phosphonates." The system switched, and additive Q, a phosphonate, emerged from the screen. The other two authors' logged interventions were budget approvals and one formatting change.

### Counterfactual credit

> **What is counterfactual credit?**
>
> In baseball, a player's value is often measured as "wins above replacement": how many more games did the team win with this player than it would have with an ordinary substitute? The measure comes from replaying the season, statistically, without the player. It does not ask the player how important they were.

With a logged workflow, the same replay can be done literally. Remove Lena's intervention from the log and re-run the workflow from that point with the system left to its own defaults. In the replay, the system screens family A, finds nothing at the anode, reports a null result. Her marginal contribution to Claim 47 is, measurably, the claim's existence. Remove the formatting change and the replay is identical; that colleague's contribution to *this result* is zero — which says nothing about the value of their role, only that discovery credit for this claim does not belong to them.

This is the direct answer to the objection that "naming the required contribution doesn't establish it." Stop asking. Run the experiment.

Contribution records then list what was measured. Unknown shares remain unknown. Nobody inherits credit for owning the software or approving the budget, and nobody has to manufacture percentages.

### Examinations become logged sessions

> A driving examiner does not inspect your car and infer your competence. She sits beside you while you drive.

A doctoral defence or a hiring exercise, in this system, is a session in an attested workspace on unfamiliar material, with AI tools permitted and logged. The log shows what the candidate did with the tools — including what they did when the tools were wrong, which is where competence actually shows. This establishes what the person can do *with* the tools, which is exactly what an employer needs to know. It deliberately does not claim to establish unaided genius, which nobody needs to know.

### What could go wrong

*Surveillance.* A log that management can read chills exploration and turns every wrong turn into a performance-review item. Mitigation: the researcher owns the log and discloses selectively; institutions may see summaries and sampled audits, not the stream.

*Gaming the replay.* A researcher could stage dramatic interventions to inflate their measured contribution. Mitigation: sampled audits of replays by independent assessors, and the fact that a staged intervention that does not change the outcome measures zero.

*Unreplayable steps.* Bench work cannot be replayed. Mitigation: recorders are confined to computational segments; laboratory contributions are recorded as roles and covered by organizational authorship.

### First build

A plugin for the common environments where AI-assisted research already happens — computational notebooks and agent frameworks — that produces signed logs and supports replay. Piloted with volunteer groups who want their contributions to be attributable. About €200,000. The test: do logs replay reliably, does replay-based credit agree with blinded expert judgment on a sample of cases, and is the friction no higher than working without the recorder?

---

## 5. Instrument three: paying for value

### The idea in one sentence

Stop buying promises through proposals; pay for research inputs and outputs after their value is visible, let small pledges from many researchers steer shared infrastructure, and let scarce capacity find its price.

### Retroactive funding

> **What is retroactive public-goods funding?**
>
> A Nobel Prize is retroactive: it pays for work whose value has become obvious, often decades after the fact. The insight, articulated by Vitalik Buterin in 2021 and put into practice by the Optimism blockchain community in several funding rounds since, is that **it is far easier to judge what was useful than what will be.** In those rounds, a group of "badgeholders" distributes a pool to projects on the basis of demonstrated use, not pitch decks.
>
> Research is full of contributions that no proposal system funds well: datasets, software tools, negative results, methods, and the unglamorous maintenance that keeps all of them alive.

In this proposal, a fixed share of research budgets — 10% to start — is set aside for retroactive awards, decided by paid, rotating badgeholders with usage evidence in hand. When Claim 47 is replicated in June, the replicating laboratory uses a calibration dataset for cycling tests that a small group in Uppsala has maintained for eight years without ever getting a grant for it. The dataset appears in the usage records of forty resolved claims that year. It receives a retroactive award. Nobody wrote a proposal.

### Impact certificates

> **What is an impact certificate?**
>
> It is a ticket that says "I funded this work early; if it later receives a retroactive award, I get a share." It is the research equivalent of an early investor's stake, except that the payoff comes from a public prize rather than from profit. Small funders have experimented with them since 2023.

Why does this matter? Because "small allocations earn larger ones on evidence" — the sensible-sounding rule in most reform proposals — quietly starves work whose value takes years to show. Impact certificates give long-horizon work a financing route: someone who believes in the Uppsala dataset in year one can fund it and be repaid in year eight.

### Quadratic funding

> **What is quadratic funding?**
>
> Suppose a funder has a €10,000 matching pool for shared research tools. Project A is supported by 100 researchers who each pledge €10. Project B is supported by one wealthy lab that pledges €1,000. Both have raised €1,000. Under ordinary matching, they would get the same. Under quadratic funding, the match is based on the *number* of supporters as well as the amount — technically, on the square of the sum of the square roots of the pledges — so Project A receives nearly the entire pool and Project B almost none.
>
> The formula rewards breadth of need over depth of one pocket. Gitcoin has used it since 2019 to distribute tens of millions of dollars to open-source software, chosen by the developers who actually use it.

For shared scientific infrastructure — the tool, the database, the instrument everyone in a field needs but nobody's grant covers — this is the right allocation rule. The community pledges small sums; the pool follows the pledges.

### Dominant assurance contracts

> **What is a dominant assurance contract?**
>
> Kickstarter runs "all or nothing" campaigns: if the target is not reached, everyone gets their money back. The economist Alex Tabarrok proposed a refinement in 1998: if the target is *not* reached, contributors get their money back **plus a bonus.** Now there is no reason to wait and see whether others will pay. Pledging is the best move whether or not the project happens.

Three laboratories each need the same €20,000 measurement to settle a shared question about additive Q's behavior at low temperature. Each would rather someone else paid. A dominant assurance contract solves this in an afternoon: each pledges €7,000; if all three pledge, the measurement runs; if fewer do, the pledgers get their money back plus €500 from the fund. Pooled demand for experiments — which earlier versions of this proposal could only describe — now has a mechanism.

### Spot markets for capacity

> **What is a spot market?**
>
> Cloud computing companies sell spare capacity at a fluctuating price that anyone can see. When demand is low, an hour of computation costs pennies; when it spikes, the price rises and the least urgent jobs wait. Nobody applies for compute; they buy it.

Instrument time, robotic laboratory runs and compute can be sold the same way. Cloud laboratories already sell experiments by the run. An AI-driven investigation with a budget buys capacity directly; a human researcher does the same. The price of an hour on a particular instrument becomes public information, which tells funders exactly where the bottlenecks are.

### Futarchy, on a small slice

> **What is futarchy?**
>
> "Vote on values, bet on beliefs." Robin Hanson's proposal: a community decides what outcome it wants — say, the number of independently confirmed useful results in a field after three years — and then runs *conditional* prediction markets on which of several candidate investigations would best produce it. The market prices, not a committee, choose the investigation.

This is the most radical mechanism here and the one most exposed to gaming of the outcome measure. It is included for 5% of a budget, as an experiment, with the measure watched closely.

### What remains human-judged

Not everything can be scored. Questions nobody has asked yet, conceptual work, and research whose value cannot be measured within any reasonable horizon still need people to back people. Fellowships on the "people, not projects" model remain — with one modification. When a panel cannot distinguish between qualified applicants, the decision is made by lottery. The Swiss National Science Foundation already does this at its funding boundary. A coin flip is fairer than a tie-break based on prose style, and cheaper than pretending the panel can see differences it cannot.

### What could go wrong

*Popularity contests.* Retroactive funding could reward the visible rather than the useful. Mitigation: usage evidence is required, badgeholders rotate, and the truth-market records show which contributions supported resolved claims.

*Sybil attacks.* Quadratic funding can be gamed by one person pretending to be a hundred. Mitigation: pledges come from accountable principals, the same identities the rest of the system runs on.

*Pricing out newcomers.* Spot markets favor those with budgets. Mitigation: reserved allocations for newcomers, fixed before outcomes are known — the same rule that protects unfamiliar questions in every other part of this proposal.

### First build

A retroactive round of €500,000 for datasets and tools in the same field as the truth-market pilot, with a small impact-certificate market attached, and about €50,000 for operations. The test: do awarded items show measured use, do certificate prices predict awards, and do awards reach groups outside the already well-funded?

---

## 6. Who owns the machines, and what people are for

The three instruments answer *what is dependable*, *what deserves money*, and *what a person contributed*. Two questions remain that no mechanism design settles: who controls the research systems, and what human scientists are employed to do.

### Essential-facility access

> **What is the essential facilities doctrine?**
>
> In 1912, the United States Supreme Court ruled that the group of railroads which owned the only bridges and terminals into St Louis could not exclude competitors from them. If you own the only bridge, you must let others cross at a fair toll. The principle has since been applied to power grids, telephone networks and ports.

If a handful of organizations own the research systems that produce most of science, provenance records will document that concentration beautifully and do nothing about it. The legal answer is to treat research systems above a capability threshold as essential facilities: their owners must license access to accredited researchers at regulated rates. Consortium ownership of open systems is a good complement; it is not a substitute, because a consortium can exclude outsiders too.

### Research cooperatives

> Credit unions, agricultural cooperatives and the Mondragon industrial group in Spain are all businesses owned by the people who work in or use them. They have survived for a century in competitive markets.

Laboratories organized as cooperatives own their systems and share the revenue from what those systems produce. The recent "decentralized science" experiments with token-based governance have had mixed results; the cooperative form is older and sturdier, and it answers the question "who benefits when the machine discovers something?" without a lawsuit.

### A science dividend

> Alaska pays every resident an annual dividend from a fund built on oil royalties. Norway's sovereign wealth fund does something similar at national scale.

Royalties from AI-produced intellectual property flow into a permanent fund that pays for human inquiry, training and fellowships. This is the financial answer to the question "what are humans for," and it is deliberately separate from any claim that humans out-produce machines. Human science is funded because understanding, education and independent scrutiny are goods in themselves. The dividend is how, not why.

### Employment for stated reasons

Participating institutions remove publication counts and journal rank from hiring, promotion and doctoral decisions, and are audited for it. The San Francisco Declaration on Research Assessment has urged this since 2012 and has thousands of signatories and little effect; China's 2020 rules restricting evaluation by paper counts show that enforcement is possible when someone decides to enforce.

What does a hiring file look like without paper counts? It contains the candidate's calibration ledger, one or two logged exercises on unfamiliar problems, the things they built or maintained and the retroactive awards those attracted, and references from people who worked alongside them. Every item in that file is either measured or observed. None of it can be inflated by running a model overnight.

One thing this proposal does not promise: that everyone will find a new role in "judgment," "curation" or "asking the right questions." Those activities are inside the automation scenario too. Research employment may shrink or shift. The honest response is to preserve existing commitments, fund training, and pay for human inquiry on its own terms — not to pretend that a reorganized labor market is guaranteed.

---

## 7. Claim 47, start to finish

Here is the whole life of the claim, with all three instruments working together.

**January.** Lena's laboratory, through its host organization, registers Claim 47 with a preregistered resolution protocol and posts a €2,000 bond. Human contributions are marked "to be established from log." A market opens at 50 cents with a €400 subsidy.

**February.** Grenoble sells; the price falls to 32 cents. Host H and two optimistic laboratories buy; the price recovers to 41 cents and open interest reaches €18,000. A manufacturer that needs to know hedges with "no" contracts and pays €8,000 into the claim's resolution fund. Nobody has written a review.

**March.** Claim 47 is relied on by two registered claims and a manufacturer has paid into its fund; the assessment fund's priority rule grants the base allocation, the fund reaches the €20,000 cost, and the preregistered replication is commissioned from an independent laboratory, which buys three days of cycling capacity on a spot market at a visible price.

**June.** The replication finds a 22% reduction, below the 35% threshold. The market settles at zero. Grenoble profits from being right; the manufacturer loses a small stake and avoids a large mistake. The bond is not forfeited — a smaller effect is not a refutation — but the maintained account of the question is revised to "real, smaller than claimed," and the market on the revised claim opens at 70 cents.

**July.** The replicating laboratory's usage records show it relied on the Uppsala calibration dataset. So did thirty-nine other resolutions that year. The dataset receives a retroactive award; the early funder who bought its impact certificate in year one is repaid.

**September.** Lena applies for a position. Her file contains her calibration ledger — provisional still, since she has fewer than the several hundred resolved positions a ledger needs to mean much on its own — and the workflow log of Claim 47, in which the counterfactual replay shows that her intervention is the reason the additive was found. The committee never asks how many papers she has.

**Three years later.** The revised claim has survived. The bond returns with a premium. The laboratory's record shows one claim overstated and corrected, one claim established. That is what a good scientific record looks like.

---

## 8. What to build first

Three pilots, each small, each measured against a stated baseline, each stoppable.

| Build | Setting | Indicative cost | Twelve-month test |
|---|---|---|---|
| Truth market with resolution fund and author bonds | One fast-replication field, about 500 claims | €300,000 | Resolution decisions track price better than citation counts; the ledger separates good forecasters from bad; cost per resolved claim below a replication study |
| Flight recorder with counterfactual replay | Volunteer computational research groups | €200,000 | Logs replay reliably; replay-based credit agrees with blinded expert judgment on a sample; friction no higher than today |
| Retroactive round with impact certificates | Same field as the market | €550,000 | Awarded items show measured use; certificate prices predict awards; awards reach groups outside the top funded |

Total: about €1.05 million, roughly a quarter of a conventional two-year institutional trial, aimed at problems that such a trial leaves untouched.

> **What is a stop rule?**
>
> A stop rule is a condition, written down before the pilot starts, under which the pilot ends. It exists because the people running a pilot always find reasons to continue it. Here: if markets do not beat citation counts at predicting resolution, stop. If replay-based credit does not correlate with blinded expert judgment, stop. If retroactive awards concentrate in already well-funded groups, redesign before a second round. Expansion is a new decision, not a reward for a persuasive final report.

---

## 9. What would make this wrong

Markets could stay thin, be manipulated, or turn resolution disputes into a new review queue. Recorders could chill exploration or become a management surveillance tool. Retroactive funding could reward the visible; futarchy measures could be gamed. Essential-facility rules could be captured by incumbents or freeze development. Employment effects remain uncertain, and nothing here guarantees jobs.

There is also a deeper objection worth stating plainly. Every mechanism here attaches money to truth, contribution or value. Money attracts gaming; science already suffers from metrics that were gamed. The reply is that the mechanisms here are chosen because they are **hard to game by volume** — a bet costs something whether or not it pays, a replay measures what changed rather than what was claimed, and a retroactive award follows use rather than promise. That is a design argument, not a guarantee. The pilots exist to find out.

---

## 10. Ideas parked, not abandoned

**Executable claims.** Register each claim with a machine-checkable prediction and a data schema; as data arrives, the record scores the claim automatically, and the market trades on the score. Unit tests for science, with money attached.

**Debate as review.** Two AI systems argue for and against a claim before a judge with limited time; the transcript, not a reviewer's paragraph, is the review artifact. This protocol was proposed in AI safety research in 2018 and has never been tried at scale on scientific claims.

**Attention tokens.** Each researcher receives a fixed annual budget of review-priority credits and pledges them to claims they intend to rely on. A claim's place in the human-review queue is the sum of pledges. This replaces "important" with "needed."

**Warranted results.** Producers sell results with a warranty; underwriters price the risk of retraction; the premium is the public reliability signal and pays for the audits. This is how product safety certification has worked for over a century.

**Commit-reveal preregistration.** Publish a cryptographic hash of your prediction to a public timestamp chain; reveal the prediction later. Preregistration becomes free, universal and impossible to backdate.

---

## Glossary

**Automated market maker.** A program that always quotes a price for a contract, adjusting it as people buy and sell, and loses at most a fixed subsidy to informed traders.

**Bond.** Money posted behind a claim, forfeited to whoever successfully refutes it, returned with a premium if the claim survives.

**Calibration ledger.** A public record of how well a person's or system's stated confidence in claims matched what actually happened.

**Counterfactual credit.** A person's measured contribution to a logged piece of work, found by replaying the work without their interventions.

**Dominant assurance contract.** A crowdfunding arrangement in which pledgers get their money back plus a bonus if the target is not reached, so that pledging is always the best move.

**Essential facility.** Infrastructure whose owner must, by law, grant access to competitors on fair terms because it cannot practically be duplicated.

**Flight recorder.** A signed, tamper-evident log of the interactions between humans and AI systems during research, controlled by the researcher.

**Futarchy.** A decision procedure in which people vote on the outcome they want and markets choose the action most likely to produce it.

**Impact certificate.** A tradeable claim on a share of any future retroactive award for a piece of work, held by whoever funded it early.

**Prediction market.** A market in contracts that pay out depending on a future event; the price is the crowd's probability estimate.

**Quadratic funding.** A matching rule that favors projects supported by many small contributors over projects supported by one large one.

**Resolution fund.** Money attached to a market that pays for the experiment or adjudication that settles the claim once enough is at stake.

**Retroactive funding.** Money paid for work after its usefulness has been demonstrated, rather than in advance on the basis of a proposal.

**Spot market.** A market in which capacity is sold immediately at a price that rises and falls with demand.

---

## Precedents referred to

Camerer et al., replication prediction markets in economics (2016) and social science (2018) · DARPA SCORE program and Replication Markets · Iowa Electronic Markets · Hanson, logarithmic market scoring rule and futarchy · Brier, verification of forecasts (1950) · Knuth's reward cheques; Erdős problem prizes · C2PA content credentials · "wins above replacement" in baseball analytics · Buterin, retroactive public goods funding (2021); Optimism RetroPGF rounds · impact certificate experiments (e.g. Manifund) · Gitcoin quadratic funding · Tabarrok, dominant assurance contracts (1998) · cloud laboratories (e.g. Emerald Cloud Lab) · Swiss National Science Foundation funding lotteries · United States v. Terminal Railroad Association (1912) and the essential facilities doctrine · Mondragon Corporation; credit unions · Alaska Permanent Fund; Norway's Government Pension Fund Global · San Francisco Declaration on Research Assessment (2012) · China's 2020 research evaluation reforms · Irving, Christiano and Amodei, AI safety via debate (2018).

*Precedents are cited by name; link and verify each before wider circulation.*

---

*Change note, v1.1–1.2.* Aligned with the full proposal v3.3: resolution funds are now filled by base allocations, trade fees and direct payments and prioritized by confirmed reliance times uncertainty rather than open interest; the reliant party hedges and pays for resolution rather than buying contracts; bonds are posted by hosts with premiums from forfeited bonds weighted by contest and challengers post stakes; the calibration ledger carries the caveat that it needs several hundred resolved positions; the first build is machine learning, with psychology in year two.
