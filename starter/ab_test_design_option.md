# Option A: A/B Test Design

Pick this option OR `causal_program_eval_option.md` (not both for MVP —
see `../ABOVE_AND_BEYOND.md` if you want to do both). Design a real A/B
test for a real business change relevant to your chosen domain
(`../SCENARIOS.md`) — this is a design document, not something you need
to actually run.

## 1. The business change being tested

TODO: name a specific, real change you'd want to test (e.g., a new
claims-processing workflow, a different appointment-reminder method, a
new permit-review process) — specific to your own domain, not generic.

## 2. Control and treatment

TODO: what exactly differs between the control group and the treatment
group? A real A/B test changes **one thing** — name it precisely.

## 3. Primary metric

TODO: what's the one real metric you'd measure to judge success? (Reuse
Module 11's own hypothesis-testing instincts here — this should be a
metric you could actually run a real test on.)

## 4. Minimum detectable effect and sample size

TODO: state the smallest real-world effect size that would actually be
worth acting on, then compute (don't just assert) a real required
sample size for that effect at a stated significance level and power —
reuse Module 11's own sample-size/power reasoning
(`sample_size_power_scenario.md` from that project, and
`predictive_pipeline.py`'s own real data, if it gives you a real
baseline rate/variance to plug in).

## 5. Threats to validity

TODO: name at least one real threat to this test's validity (e.g.,
seasonality, a confound between groups, contamination between control
and treatment) and how your design addresses or fails to address it.
