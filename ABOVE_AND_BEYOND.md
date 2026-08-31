# Above & Beyond: Stretch Scope (team project)

The team version's MVP already includes what used to be this project's
stretch goals (both experimental components, a second model, a second
fairness segment — see `MVP.md`). Each item below is optional, and each
one previews something Module 13 (Generative AI, Prompt Engineering &
Agentic AI Tooling) or Module 14 (Responsible AI, AI Governance &
Ethics) will assume you already have a real feel for.

## 1. A real regression-adjustment causal check

Your MVP causal analysis stratifies by one confounder. Go further: fit
a real regression model (e.g. logistic regression) predicting your
outcome from your treatment variable **plus** the confounder(s) as
covariates, and compare the treatment coefficient with and without the
adjustment. This is the real technique named as "beyond this project's
scope" in a well-built causal write-up — controlling for multiple
covariates at once, not just one stratification. **Why this matters
next**: Module 14's governance work assumes you can reason about
confounding at this level, not just a single stratified check.

## 2. A real MLflow Model Registry workflow

Register your section-4 model and your section-11 second model in
MLflow's Model Registry, tag one `staging` and one `production`, and
show a real query that retrieves "whichever model is currently in
production" without hardcoding a run ID. **Why this matters next**: real
MLOps work routinely needs to answer "which model is live right now"
programmatically, not by remembering a run ID.

## 3. Sample-size sensitivity for your A/B design

Recompute your section-10 sample size at 2-3 different minimum
detectable effects (e.g. 3pp, 5pp, 8pp) and show how required sample
size changes. Discuss the real tradeoff: a smaller MDE needs more
sample (and more calendar time) — what would your team actually
recommend to a stakeholder who wants results faster? **Why this matters
next**: real experiment design is rarely a single fixed number — it's a
negotiation between statistical rigor and business timeline.
