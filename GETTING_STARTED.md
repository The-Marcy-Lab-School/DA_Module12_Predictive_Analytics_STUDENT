# Getting Started

## 1. Use this template — not Fork

Click **"Use this template"** on GitHub (not "Fork") for a clean,
independent copy for your own portfolio.

## 2. Environment is already set up

`.gitignore` and `LICENSE` are already here — `git-version-control`
isn't a skill this project tests. Two real things to still do:

- **Open `LICENSE`** and replace `[YOUR NAME]` with your own name, then
  commit.
- Confirm `.gitignore` covers `mlflow.db`/`mlruns/` (it already does —
  your local MLflow tracking database regenerates from your code, so it
  isn't part of your submission).

## 3. Install the two new libraries

```
pip install scikit-learn mlflow pandas
```

`scikit-learn` and `mlflow` are new this module — `pandas` you've used
since Module 4.

## 4. Set up local MLflow tracking

Read `starter/mlflow_setup.md` before you get to section 7 of the
pipeline — MLflow's classic local file-store tracking now errors by
default in recent versions; the given setup uses a local SQLite file
instead (`sqlite:///mlflow.db`), which is still fully local and free.

## 5. Pick your dataset, target, and either/or component

Read `SCENARIOS.md` for a real, verified classification/regression/
clustering angle per domain, and pick either `starter/ab_test_design_option.md`
or `starter/causal_program_eval_option.md` for the experimental/causal
component.

## 6. Open `starter/predictive_pipeline.py` in VS Code

Each `# %%` marks a separate cell — run cells one at a time so you can
see your own real output as you build.

⚠️ **Common mistake**: reporting "accuracy" with no real train/test
split at all. Split your data *first*, before fitting anything — this
is the single most common way this project goes wrong.

⚠️ **Common mistake**: writing up a correlational finding (your model's
predictions) as if it proves causation. Your model shows what's
*associated* with your outcome — your A/B test design or causal
write-up is the only place a causal claim actually belongs.

## 7. Commit incrementally

Commit as you finish each numbered section — a real commit history
(business framing → split → fit → evaluate → fairness check → MLflow →
clustering → interpretation) is worth more than one final dump.

Next: `CHECKLIST_TIMELINE.md` for pacing and the full submission
checklist.
