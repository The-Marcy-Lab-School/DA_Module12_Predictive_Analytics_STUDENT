# Required Components

**Team project** — see `team_charter.md` for roles/RACI. Files:
`starter/predictive_pipeline.py` (the code artifact, 12 numbered
sections), `business_memo.md` (the written synthesis, 6 sections),
`team_charter.md`, and each member's own
`individual_reflection_<name>.md`. See `SCENARIOS.md` first — as a team
— to pick your one shared dataset/target.

## Code artifact (`starter/predictive_pipeline.py`)

1. **Load data** — your team's one real domain dataset.
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
10. **A/B test design with a real, computed sample size** —
    `starter/ab_test_design_option.md`, a real baseline rate/variance
    from your own data plugged into a real power calculation (not just
    asserted "big enough").
11. **Second model comparison** — a different real scikit-learn model
    against the same honest feature set, with a real tradeoff
    discussion (not just whichever number is highest).
12. **Second fairness segment** — the section-6 check extended to a
    second real segment variable.

## Written synthesis (`business_memo.md`)

1. The business/policy question.
2. What the model shows (real performance, real strengths/limits).
3. What the model can't claim (correlation vs. causation, explicit).
4. **Both** your A/B test design **and** your causal/program-evaluation
   analysis (`starter/ab_test_design_option.md` **and**
   `starter/causal_program_eval_option.md`), integrated into one
   coherent read — not two disconnected sections.
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
- Only one of A/B design or causal analysis genuinely built out.
- A RACI where every role is marked the same on every row.
