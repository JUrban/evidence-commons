# Pilot A — Truth market with resolution fund

*Pre-registration, from Section 42 of the master document (v3.4). Numbers marked as placeholders depend on the field chosen.*


**Title.** Do market prices on registered claims predict independent resolution better than existing signals, and does open-interest-triggered resolution allocate checking to claims that matter?

**Hypotheses.** H1: The Brier score of final market prices against resolution outcomes is lower than that of a pre-specified baseline model using citation count, venue tier and reviewer scores. H2: The set of claims selected for resolution by the open-interest trigger has higher confirmed reliance than an equal-sized random set. H3: Forecasters' ledger scores on the first half of resolved positions predict their scores on the second half (split-half reliability > 0.3 among forecasters with at least 100 resolved positions).

**Design.** ~500 claims from the field's last two conference cycles, registered with hosts' consent under template 1 or 2. Prize-form markets with allocated points; LMSR with *b* set so that worst-case loss equals the market's subsidy; per-principal position limit 0.5*b*; resolution fee 0.5%. Resolution triggered when the resolution fund reaches the protocol's cost estimate; resolution auction among ≥3 accredited services with protected evaluation sets; adjudication by the service named at registration.

**Sample.** Resolutions: target ≥60 in twelve months; the power calculation for H1 at the smallest Brier difference worth detecting (0.02) is run before launch and fixes the minimum; if the field's resolution costs make 60 unreachable within €100,000, the claim set is reduced before launch, not the target.

**Analysis.** H1: paired comparison of Brier scores on resolved claims, one-sided, α = 0.05; baseline model fitted on claims outside the resolved set to avoid in-sample flattery. H2: confirmed reliance (Section 19.3) of selected versus random sets, permutation test. H3: Spearman correlation of split-half ledger scores. All analyses by the oversight board's statistician; code and data published.

**Stop rule.** If after the first 40 resolutions the pre-registered H1 test shows no advantage over baseline, trading stops and the result is published.

**Secondary.** Participation; principals per market; challenge frequency and outcomes; adjudication times; cost per resolution versus the field's published replication cost; survey of attitudes.

**Conflicts and governance.** As Section 22.5. The pilot registers itself as a claim ("H1 will hold") and opens a market on it.
