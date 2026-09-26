# Pilot B — Flight recorder with counterfactual replay

*Pre-registration, from Section 42 of the master document (v3.4). Numbers marked as placeholders depend on the field chosen.*


**Title.** Can logged human–AI research workflows be replayed, and does replay-based contribution agree with expert judgment at acceptable friction?

**Hypotheses.** H1: Level 3 logs from the plugin replay to the original outcome in ≥90% of cases with fixed seeds and pinned models. H2: Replay-based contribution ranks agree with blinded expert ranks on a sample of 30 cases (Spearman ρ > 0.5). H3: Instrumented time per task with the recorder is not more than 10% greater than without (non-inferiority).

**Design.** Plugin for one notebook environment and one agent framework; 10–20 volunteer groups in the pilot field; each group runs matched tasks with and without the recorder in counterbalanced order; independent replays by the oversight board's engineer; blinded experts rank contributions from the disclosed log without seeing replay results.

**Sample.** 30 sampled cases for H2, chosen by lot from logged projects with ≥2 human contributors; task-time measurements on all groups.

**Analysis.** H1: proportion with exact confidence interval. H2: Spearman correlation. H3: non-inferiority test on log time ratio. Descriptive: logging-level choices, disclosure choices, friction by environment.

**Stop rule.** If H2's correlation is not above zero at α = 0.05 on the 30 cases, the counterfactual-credit feature is withdrawn and the plugin continues as a descriptive recorder only.

**Ethics.** Data-protection impact assessment completed (Appendix E); researcher-held keys; consent for each disclosure; no institutional access to streams.
