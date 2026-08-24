# Required Components

Two files: `starter/predictive_pipeline.py` (the code artifact, 9
numbered sections) and `business_memo.md` (the written synthesis, 6
sections). See `SCENARIOS.md` first to pick your dataset/target.

## Code artifact (`starter/predictive_pipeline.py`)

1. **Load data** — your own real domain dataset.
2. **Frame the business question** — what you're predicting, and what
   real decision it informs.
3. **Real train/test split** — before any fitting, no leakage.
4. **Fit a model** — a real scikit-learn model matching your target
   type.
5. **Justified evaluation metric** — precision, recall, AUC, or R²,
   chosen and explained against your section 2 framing — not just
   "accuracy."
6. **Fairness/disparity check** — a real, computed per-segment error
   rate (e.g. false-negative rate across a real segment variable), not
   an asserted claim of fairness.
7. **MLflow logging** — your model type, hyperparameters, and metrics
   logged via `mlflow.log_param`/`log_metric`, then retrieved back via
   `MlflowClient` to prove it's actually retrievable (see
   `starter/mlflow_setup.md`).
8. **Clustering/segmentation** — a real aggregate business unit in your
   data (not individual prediction-target rows), evaluated against a
   real business use case.
9. **Business-framed interpretation** — your model's coefficients or
   feature importances, explained in plain business language.

## Written synthesis (`business_memo.md`)

1. The business/policy question.
2. What the model shows (real performance, real strengths/limits).
3. What the model can't claim (correlation vs. causation, explicit).
4. Your A/B test design **or** causal/program-evaluation analysis
   (pick one — `starter/ab_test_design_option.md` or
   `starter/causal_program_eval_option.md`).
5. Fairness note (your real section-6 finding, and what it implies).
6. Recommendation — a specific, concrete next step.

---

**Common mistakes this project watches for** (see `instructor/rubric.md`
for the full grading detail):

- Reporting accuracy with no train/test split at all.
- Writing up a correlational finding as if it proves causation.
- Skipping the fairness/disparity check and just asserting the model is
  "fair."
- Not logging the model version or metrics anywhere retrievable.
