# Business Memo

Write this as a memo to a real stakeholder, not a lab report. Reuse the
real numbers from `starter/predictive_pipeline.py` and your chosen
option (`starter/ab_test_design_option.md` or
`starter/causal_program_eval_option.md`) — don't re-derive anything
here, synthesize what you already found.

## 1. The business/policy question

TODO: what real decision does this project inform?

## 2. What the model shows

TODO: your model's real performance (the metric you justified in
`predictive_pipeline.py` section 5), what it's actually good at
predicting, and what it isn't.

## 3. What the model can't claim

TODO: explicitly state what your model does **not** prove — a
predictive model answers "what's associated with what," not "what
causes what." This is the single most common mistake on this project
(`required_components.md`) — don't let a correlational finding read
like a causal one.

## 4. Your A/B test design or causal analysis

TODO: summarize your chosen option's real findings — the confounder (or
the sample-size justification), the threat to validity, and what it
means for whether this finding is trustworthy.

## 5. Fairness note

TODO: your real fairness/disparity check result from
`predictive_pipeline.py` section 6 — was there a meaningful disparity?
What would you recommend before this model is used to inform a real
decision affecting people?

## 6. Recommendation

TODO: given everything above, what should the stakeholder actually do?
Be specific — not "more research is needed," but a real, concrete next
step your findings actually support.
