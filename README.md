# Module 12: Predictive Analytics, Machine Learning & Experimentation

A real end-to-end scikit-learn predictive pipeline, a real fairness
check, real MLflow tracking, real clustering, and either a real A/B
test design or a real causal analysis — against your own already-
established domain dataset.

**Before you do anything else**: click **"Use this template"** on this
repo's GitHub page (not "Fork") to create your own copy — see
`GETTING_STARTED.md` step 1 for why this matters.

- **What/why**: see `PROJECT_OVERVIEW.md`.
- **Setup, step by step**: see `GETTING_STARTED.md`.
- **Pacing + full submission checklist**: see `CHECKLIST_TIMELINE.md`.
- **Exactly what to build**: see `required_components.md`, and
  `SCENARIOS.md` to pick your dataset/target.

## Dataset

Reuse your own established Module 3/7/8/9/10/11 domain dataset
(`finance_insurance`, `healthcare_operations`, `public_sector`, or
`professional_services`) — this repo's own `data/<domain>/` folder has
the same real CSVs, no need to go back to your Module 3 repo. See
`SCENARIOS.md` for a real, verified classification/regression/clustering
angle per domain.

## Setup

```
pip install scikit-learn mlflow pandas
```

No accounts, no cloud — MLflow tracking runs entirely locally (see
`starter/mlflow_setup.md` for the real, current setup — MLflow's older
file-store default is now deprecated in favor of a local SQLite file).
Open `starter/predictive_pipeline.py` in VS Code with the Jupyter
extension installed, and run it cell by cell.
