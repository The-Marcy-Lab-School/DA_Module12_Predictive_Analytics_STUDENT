# Recommended Timeline & Submission Checklist

A recommended schedule for this 13-day project — the richest-breadth
project so far, so pacing matters more than usual here.

## Day 1 — Setup + pick your target

- [ ] `pip install scikit-learn mlflow pandas`; open `LICENSE`, replace
  `[YOUR NAME]`, commit.
- [ ] Read `SCENARIOS.md`, pick your domain, target, and either/or
  component (`ab_test_design_option.md` or `causal_program_eval_option.md`).
- [ ] Load your real data (section 1).

**Exit criterion**: your real data loads, and you've picked a specific
classification or regression target.

## Day 2 — Business framing + train/test split

- [ ] Write your business-question framing (section 2) — what you're
  predicting and what real decision it informs.
- [ ] Real `train_test_split`, done **before** any fitting (section 3).
  - ⚠️ Fitting anything (a scaler, an imputer) on the full dataset
    before splitting is a real leakage mistake — split first.

**Exit criterion**: your split is real and happens before any model
touches the data.

## Days 3-4 — Fit + evaluate

- [ ] Fit a real scikit-learn model (section 4).
- [ ] Compute and justify a real evaluation metric matching your
  section 2 framing — not just "accuracy" (section 5).
  - ⚠️ Reporting accuracy with no train/test split at all is the #1
    mistake on record for this project.

**Exit criterion**: a real metric, computed on your held-out test set,
with a written justification for why that metric fits your decision.

## Days 5-6 — Fairness check + MLflow tracking

- [ ] Real, computed per-segment error-rate check (section 6) — not an
  asserted "the model is fair."
  - ⚠️ Skipping the fairness/disparity check and just asserting
    fairness is the #3 mistake on record.
- [ ] Read `starter/mlflow_setup.md`; log your model + metrics; confirm
  you can retrieve them back via `MlflowClient` (section 7).
  - ⚠️ Not logging the model version or metrics anywhere retrievable is
    the #4 mistake on record.

**Exit criterion**: a real per-segment disparity number, and a real
MLflow run you can query back.

## Days 7-8 — Clustering / segmentation

- [ ] Real aggregate features on a real business unit; run `KMeans`
  (section 8).
- [ ] Evaluate the clusters against a real business use case, not just
  a silhouette score.

**Exit criterion**: clusters that mean something you could explain to a
stakeholder in one sentence each.

## Day 9 — Business-framed interpretation

- [ ] Pull coefficients/feature importances; explain them in plain
  business language (section 9).

**Exit criterion**: your explanation would make sense to someone who's
never seen a coefficient before.

## Days 10-12 — A/B test design or causal/program-evaluation analysis

- [ ] Complete your chosen option file in full — every TODO real and
  specific to your own comparison, not generic.
  - ⚠️ Writing up a correlational finding as if it proves causation is
    the #2 mistake on record — this is exactly what this component
    exists to prevent.

**Exit criterion**: a named, specific confounder or a justified,
computed sample size — not a placeholder.

## Day 13 — Final memo + submit

- [ ] Complete `business_memo.md` in full, synthesizing everything above
  — don't re-derive, reference your real numbers.
- [ ] Final commit, repo check.

**Exit criterion**: every section in `required_components.md` has real
content, no placeholder `# TODO` text left.

**Heads up**: after this project is due, there's a peer share-out
session on your actual model and findings — details in class.

---

## Above & Beyond (delta only — see `ABOVE_AND_BEYOND.md` for full detail)

- [ ] Complete **both** the A/B test design and the causal/program-
  evaluation analysis, not just one.
- [ ] Fit a second model (different algorithm or feature set) and
  discuss the real tradeoff against your first.
- [ ] Extend the fairness check to a second segment variable.
