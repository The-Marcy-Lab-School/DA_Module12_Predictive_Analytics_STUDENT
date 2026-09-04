# Project Overview: Predictive Analytics, Machine Learning & Experimentation

**This is a team project.** 3-4 students, one shared repo, 4 named roles
with real, individually graded accountability.

## The objective

Build a real, end-to-end predictive model with scikit-learn that
answers a real business question, track it properly (not just print
results and lose them), check whether it treats different groups
fairly, segment your data in a way that's actually useful to a
business, and pair all of it with **both** a real A/B test design
**and** a real causal analysis — then write a memo that's honest about
what your model actually proves versus what it doesn't.

## Roles

- **Project Manager** — owns timeline, scope, `business_memo.md`'s final
  assembly, shareout logistics.
- **Technical Lead** — owns the pipeline (`predictive_pipeline.py`
  sections 1-9): the model, the fairness check, MLflow tracking,
  clustering; final technical sign-off.
- **Business Analyst** — owns the business framing, the model's
  plain-language interpretation, the memo's narrative.
- **Experimentation Lead** — owns both experimental/causal components:
  the A/B test design (with a real, computed sample size) and the
  causal/program-evaluation analysis.

**At 3 people**: combine Project Manager and Business Analyst — the
lightest individual technical load of the four.

**If it's not obvious who takes which role**, don't just default to
whoever's loudest or most experienced — go around and have each person
name one role they'd genuinely like to grow in and one they'd rather
not take on this time, then fill gaps together. No role is "the easy
one": PM's real work is keeping 3 other people unblocked and on
schedule, which is its own skill. If two people want the same role,
it's fine to split *sub*-tasks within it (e.g., co-Experimentation-
Leads splitting the A/B design and the causal analysis) — say so in
`team_charter.md` rather than forcing an arbitrary pick.

## Why this matters

Module 5 taught you to run a real hypothesis test and separate
statistical significance from practical significance. This project asks
the natural next question: once you can *predict* something, does that
mean you understand *why* it happens — and is your model actually fair
to the people it affects? A model that predicts well but can't
distinguish correlation from causation, or one that's never checked for
disparate impact, is a real, common way predictive analytics goes wrong
in practice. It's also this program's second team project — the same
named-role, real-accountability shape as Module 8, applied to an
analytics team instead of an engineering one.

## What you'll build on

- Module 5's hypothesis-testing, effect-size, and causal-reasoning
  instincts — directly reused in both your A/B test design and your
  causal write-up.
- Module 2's descriptive-statistics habits — justifying a modeling
  choice (e.g. "this outcome is skewed, so I'm evaluating with median
  error, not just mean").
- Module 8's team-project mechanics — branch protection, real PR review
  across the whole team, individual accountability via a real RACI.
- Your team's one chosen domain dataset, from every project since
  Module 3.

## What this unlocks

`machine-learning` and `scikit-learn` are explicit prerequisites for
Module 12 (Generative & Responsible AI) — this project's own
fairness-check requirement is a direct, hands-on preview of that
module's formal bias/fairness content.

## Skills you'll practice

- **Regression & Classification** — diagnosing a fitted model's
  assumptions and interpreting its coefficients in business terms.
- **Predictive Modeling** — building a real end-to-end pipeline, plus a
  real second-model comparison.
- **A/B Testing** — designing a real test with a real, computed sample
  size (required this time, not either/or).
- **Causal Inference** — distinguishing a correlational finding from an
  actual causal claim (required this time, not either/or).
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
  justify a modeling choice, extended to a second fairness segment.
- **Project Management & Team Collaboration** — a real RACI, real
  branch-protected PR review across the whole team.
- **Ownership & Accountability** — real, individually checkable
  evidence tied to your own RACI row.

## Deliverables at a glance

`starter/predictive_pipeline.py` (the code — train/test split, model,
evaluation, fairness check, MLflow tracking, clustering, interpretation,
**both** a second-model comparison and a second fairness segment),
`business_memo.md` (the written synthesis integrating **both** the A/B
design and the causal analysis), a real, filled-in `team_charter.md`
(RACI), each member's own `individual_reflection_<name>.md`, and a
group readout presentation. See `required_components.md` for the full
breakdown and `CHECKLIST_TIMELINE.md` for pacing.

## Timeline

14 days (13 → 14, a team-coordination-overhead adjustment — see
`instructor/overview.md`). See `CHECKLIST_TIMELINE.md` for the
day-by-day pace and the full submission checklist.
