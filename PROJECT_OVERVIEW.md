# Project Overview: Predictive Analytics, Machine Learning & Experimentation

## The objective

Build a real, end-to-end predictive model with scikit-learn that
answers a real business question, track it properly (not just print
results and lose them), check whether it treats different groups
fairly, segment your data in a way that's actually useful to a
business, and pair all of it with either a real A/B test design or a
real causal analysis — then write a memo that's honest about what your
model actually proves versus what it doesn't.

## Why this matters

Module 11 taught you to run a real hypothesis test and separate
statistical significance from practical significance. This project asks
the natural next question: once you can *predict* something, does that
mean you understand *why* it happens — and is your model actually fair
to the people it affects? A model that predicts well but can't
distinguish correlation from causation, or one that's never checked for
disparate impact, is a real, common way predictive analytics goes wrong
in practice.

## What you'll build on

- Module 11's hypothesis-testing, effect-size, and causal-reasoning
  instincts — directly reused in your A/B test design or causal
  write-up.
- Module 2's descriptive-statistics habits — justifying a modeling
  choice (e.g. "this outcome is skewed, so I'm evaluating with median
  error, not just mean").
- Your own domain data, from every project since Module 3.

## What this unlocks

`machine-learning` and `scikit-learn` are explicit prerequisites for
Module 14 (Responsible AI, AI Governance & Ethics) — this project's own
fairness-check requirement is a direct, hands-on preview of that
module's formal bias/fairness content.

## Skills you'll practice

- **Regression & Classification** — diagnosing a fitted model's
  assumptions and interpreting its coefficients in business terms.
- **Predictive Modeling** — building a real end-to-end pipeline.
- **A/B Testing** — designing a real test with a defensible sample size.
- **Causal Inference** — distinguishing a correlational finding from an
  actual causal claim.
- **Unsupervised Learning** — clustering/segmentation evaluated against
  a real business use case.
- **Machine Learning** — selecting and justifying a performance metric
  for a real business tradeoff.
- **scikit-learn** — the real, current standard classical-ML library.
- **MLOps** — logging a model version and its metrics so they're
  actually retrievable, not lost.
- **Data Science** — combining modeling and causal/experimental work
  into one coherent, business-framed narrative.
- **Program Evaluation Methodology** — naming real threats to validity
  in a causal design.
- **Business Acumen** — tying a model/experiment result to a specific
  real decision.
- **Statistical Analysis** — reusing descriptive-statistics reasoning to
  justify a modeling choice.

## Deliverables at a glance

Two files: `starter/predictive_pipeline.py` (the code — train/test
split, model, evaluation, fairness check, MLflow tracking, clustering,
interpretation) and `business_memo.md` (the written synthesis). See
`required_components.md` for the full breakdown and
`CHECKLIST_TIMELINE.md` for pacing.
