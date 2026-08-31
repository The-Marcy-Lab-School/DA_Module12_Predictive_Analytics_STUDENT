# Module 12: Predictive Analytics, Machine Learning & Experimentation

**This is a team project — 3-4 students, one shared repo.** A real
end-to-end scikit-learn predictive pipeline, a real fairness check, real
MLflow tracking, real clustering, and **both** a real A/B test design
**and** a real causal analysis — against your team's one chosen domain
dataset.

**Before you do anything else**: form your team and assign roles (see
`PROJECT_OVERVIEW.md`), then the **Project Manager** clicks **"Use this
template"** on this repo's GitHub page (not "Fork") to create **one**
copy for the whole team — see `GETTING_STARTED.md` step 1 for the full
setup, including adding the rest of the team as collaborators.

- **What/why + roles**: see `PROJECT_OVERVIEW.md`.
- **Setup, step by step**: see `GETTING_STARTED.md`.
- **Pacing + full submission checklist**: see `CHECKLIST_TIMELINE.md`.
- **Exactly what to build**: see `required_components.md`, and
  `SCENARIOS.md` to pick your team's one shared dataset/target.

## Dataset — your team picks one

Each of you has your own established Module 3/7/8/9/10/11 domain from
earlier in the program — likely **different** domains across the team.
This project needs **one shared dataset**, not four. Pick one member's
domain (`finance_insurance`, `healthcare_operations`, `public_sector`,
or `professional_services`) as a team — this repo's own `data/<domain>/`
folder has the same real CSVs for all 4, no need to go back to anyone's
Module 3 repo. See `SCENARIOS.md` for a real, verified
classification/regression/clustering angle per domain — worth reading
all 4 before the team picks, since they aren't equally rich.

## Setup

```
pip install scikit-learn mlflow pandas statsmodels
```

No accounts, no cloud — MLflow tracking runs entirely locally (see
`starter/mlflow_setup.md` for the real, current setup — MLflow's older
file-store default is now deprecated in favor of a local SQLite file).
Open `starter/predictive_pipeline.py` in VS Code with the Jupyter
extension installed, and run it cell by cell. `statsmodels` is new —
needed for the A/B test design's real sample-size calculation
(section 10).
