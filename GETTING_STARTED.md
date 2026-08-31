# Getting Started

## 1. Form your team, then use the template — not Fork

3-4 students, 4 roles (Project Manager, Technical Lead, Business
Analyst, Experimentation Lead — see `PROJECT_OVERVIEW.md`; at 3 people,
combine PM + Business Analyst). The **PM** clicks **"Use this
template"** on GitHub (not "Fork") for **one** clean copy for the whole
team, then adds the other 2-3 members as collaborators (repo
**Settings → Collaborators**) and turns on **branch protection** on
`main` (**Settings → Branches**, require ≥1 approving review). Everyone
clones that same repo.

## 2. Environment is already set up

`.gitignore` and `LICENSE` are already here — `git-version-control`
isn't a skill this project tests. Two real things to still do:

- **Open `LICENSE`** and list every team member's name on the copyright
  line (not just `[YOUR NAME]`), then commit.
- Confirm `.gitignore` covers `mlflow.db`/`mlruns/` (it already does —
  your local MLflow tracking database regenerates from your code, so it
  isn't part of your submission).

## 3. Install the libraries

```
pip install scikit-learn mlflow pandas statsmodels
```

`scikit-learn`, `mlflow`, and `statsmodels` are new this module —
`pandas` you've used since Module 4. `statsmodels` is for the A/B
test's real sample-size calculation (section 10) — both the A/B design
and the causal analysis are required this time, not either/or.

## 4. Set up local MLflow tracking

Read `starter/mlflow_setup.md` before you get to section 7 of the
pipeline — MLflow's classic local file-store tracking now errors by
default in recent versions; the given setup uses a local SQLite file
instead (`sqlite:///mlflow.db`), which is still fully local and free.

## 5. Pick your team's one dataset, target, and confirm your roles

Read `SCENARIOS.md` together — a real, verified classification/
regression/clustering angle per domain, not equally rich across all 4 —
and pick **one** as a team (you each have your own from earlier
modules; this project needs one shared choice, not four). Both
`starter/ab_test_design_option.md` and
`starter/causal_program_eval_option.md` are required — typically the
Experimentation Lead owns both, with the Technical Lead owning the
pipeline itself.

## 6. Open `starter/predictive_pipeline.py` in VS Code

Each `# %%` marks a separate cell — run cells one at a time so you can
see your own real output as you build. Sections 1-9 are the core
pipeline; sections 10-12 (A/B sample size, second model, second
fairness segment) are also required for the team version, not optional
stretch content.

⚠️ **Common mistake**: reporting "accuracy" with no real train/test
split at all. Split your data *first*, before fitting anything — this
is the single most common way this project goes wrong.

⚠️ **Common mistake**: writing up a correlational finding (your model's
predictions) as if it proves causation. Your model shows what's
*associated* with your outcome — your A/B test design or causal
write-up is the only place a causal claim actually belongs.

## 7. Commit incrementally, with real PR review

Commit as you finish each numbered section — a real commit history
(business framing → split → fit → evaluate → fairness check → MLflow →
clustering → interpretation) is worth more than one final dump. Work on
feature branches; every merge into `main` needs a real, substantive
review from a teammate (branch protection enforces this).

**Agree on a real review turnaround as a team** (e.g., "within 24
hours, or same-day if it's blocking someone") — if your PR sits
unreviewed past that, ping the team directly rather than silently
waiting, and any other teammate can review it if the original reviewer
is unavailable. Branch protection is meant to add safety, not become a
bottleneck — settle this norm before you need it.

Next: `team_charter.md` to assign real accountability, then
`CHECKLIST_TIMELINE.md` for pacing and the full submission checklist.
