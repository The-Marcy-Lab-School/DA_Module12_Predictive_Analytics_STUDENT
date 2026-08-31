# Recommended Timeline & Submission Checklist

A recommended schedule for this 14-day team project — the
richest-breadth project so far, now built by a 3-4 person team. That's
genuinely a lot of new mechanics at once (roles, a shared repo, branch
protection, a RACI) on top of real technical breadth — **real setup
cost on Day 1 is expected, not a sign you're behind.** Every team hits
a slower first day; the pace picks up once the mechanics are settled.

## Day 1 — Form the team, roles, repo setup

- [ ] Team formed (3-4), roles assigned — PM, Technical Lead, Business
  Analyst, Experimentation Lead (3-person teams: PM+BA combined).
- [ ] **One shared repo** created (PM), collaborators added, **branch
  protection on `main`** turned on (require 1 approving review).
- [ ] `pip install scikit-learn mlflow pandas statsmodels`; open
  `LICENSE`, list every team member's name, commit.
- [ ] Read `SCENARIOS.md` together, pick your team's **one** shared
  domain and target (not four separate ones).

**Exit criterion**: the team has one repo, one domain, and branch
protection confirmed on.

## Day 2 — Team charter + business framing + train/test split

- [ ] **`team_charter.md` written** — the real RACI, before any real
  modeling work.
- [ ] Load your team's real data (section 1).
- [ ] Write your business-question framing (section 2) — what you're
  predicting and what real decision it informs.
- [ ] Real `train_test_split`, done **before** any fitting (section 3).
  - ⚠️ Fitting anything (a scaler, an imputer) on the full dataset
    before splitting is a real leakage mistake — split first.

**Exit criterion**: a real, filled-in RACI, and your split happens
before any model touches the data.

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

## Days 10-11 — Both experimental/causal components, required

- [ ] Complete **both** `ab_test_design_option.md` **and**
  `causal_program_eval_option.md` in full — every TODO real and
  specific to your own comparison, not generic. The A/B design needs a
  **real, computed sample size** (section 10 — `statsmodels.stats.power`,
  a real baseline from your own data, not an assumed one).
  - ⚠️ Writing up a correlational finding as if it proves causation is
    the #2 mistake on record — this is exactly what this component
    exists to prevent.
  - ⚠️ Asserting a sample size is "big enough" without a real
    computation is the team-version equivalent of the same mistake.

**Exit criterion**: a named, specific confounder **and** a real,
computed sample size — neither is a placeholder.

## Day 12 — Second model + second fairness segment

- [ ] Second model comparison (section 11) — a different real
  scikit-learn model, same honest feature set, a real tradeoff
  discussion.
- [ ] Second fairness segment (section 12) — section 6's check extended
  to a different real segment variable.

**Exit criterion**: two real, comparable metric numbers, and a second
real per-segment disparity check.

## Day 13 — Final memo, real PR review

- [ ] Complete `business_memo.md` in full, synthesizing everything above
  — don't re-derive, reference your real numbers. All 6 sections
  required: (1) the business/policy question, (2) what the model shows,
  (3) what the model **can't** claim — correlation vs. causation,
  explicit, (4) **both** your A/B test design and causal analysis,
  integrated, (5) your real fairness-check finding and what it implies,
  (6) a specific, concrete recommendation. Doing the underlying analysis
  elsewhere doesn't satisfy this — each section must actually appear in
  the memo itself.
- [ ] Every feature branch merged only after a real, substantive review
  from a teammate — ≥2 real comments given, by ≥2 different team
  members, ≥2 received and incorporated.
- [ ] Each member's own `individual_reflection_<name>.md` filled in.

**Exit criterion**: every section in `required_components.md` has real
content, no placeholder `# TODO` text left.

## Day 14 — Group readout, submit

- [ ] **Group readout presentation**: PM opens with scope/timeline, Tech
  Lead covers the model/pipeline, Business Analyst covers findings and
  the recommendation, Experimentation Lead covers the A/B design and
  causal analysis. Each person fields Q&A on their own piece.
- [ ] **Delete `PROJECT_OVERVIEW.md` and `SCENARIOS.md`** — they explain
  the assignment, not your project; a real portfolio repo shouldn't have
  "here's what you were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment:
  - **Business Problem** — the real decision your model informs.
  - **Methodology** — your target, features, and train/test approach.
  - **Model Performance & Fairness** — your real metric and disparity
    check.
  - **Experimental/Causal Analysis** — your A/B design and causal
    findings.
  - **Recommendations** — `business_memo.md`'s real final call.
  - **Team & Roles** — who owned what, linking back to your real RACI.
- [ ] Final commit, repo check.
- [ ] **Non-PM members**: fork the finished repo to your own GitHub
  before the deadline, so it's part of your own portfolio too.

**Heads up**: after this project is due, there's a group readout session
on your actual model and findings — see above, not an informal peer
share-out this time.
