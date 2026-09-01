# Causal / Program-Evaluation Analysis

**Required, alongside `ab_test_design_option.md`** — the team version
requires both, not either/or. Analyze a real causal question in your
team's chosen domain (`../SCENARIOS.md`) using data you already have —
no new experiment to run, just a disciplined causal analysis of what you
can already observe.

## 1. The policy/business question

TODO: state the real causal question you want to answer (e.g., "did
[some real change] actually cause [some real outcome] to improve?") —
specific to your own domain.

## 2. The causal claim vs. what your data can actually show

TODO: distinguish, explicitly, what a correlational finding in your
data would show from what an actual causal claim would require. Reuse
Module 5's own causal-reasoning discipline here.

## 3. A real, named confounder

TODO: name a specific, plausible confounder for your comparison (not a
generic "other factors could matter" — a real, specific alternative
explanation, grounded in your actual data, the way Module 5's own
solution grounded `community_number` in real, checked evidence).

## 4. What design addresses it

TODO: describe a real approach that would address (or at least reduce)
the confounder's threat — e.g., comparing only within the same
sub-group/location, a before/after comparison with a real comparison
group, or an honest acknowledgment that your available data can't fully
rule it out.

## 5. Threat to validity (program-evaluation framing)

TODO: name at least one real threat to validity beyond the confounder
above (e.g., regression to the mean, a selection effect in who
receives the "treatment," a trend that would have happened anyway) —
and explicitly distinguish your design from a naive pre/post comparison
that ignores it.
