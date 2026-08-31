# MVP: Minimum Bar (team project)

See `instructor` materials distributed separately for full grading
detail. This is a short, scannable bar — one line per requirement.

## The pipeline

- [ ] A real, justified train/test split, done before any fitting — no
  leakage.
- [ ] A real scikit-learn model fit, with a justified evaluation metric
  (not just "accuracy") matching the stated business tradeoff.
- [ ] A real, computed fairness/disparity check across a real segment
  variable — not an asserted claim of fairness — **extended to a real
  second segment variable** (section 12).
- [ ] Real MLflow tracking: model type, hyperparameters, and metrics
  logged and proven retrievable.
- [ ] A real clustering/segmentation result, evaluated against an
  actual business use case.
- [ ] Coefficients/feature importances interpreted in real business
  language.
- [ ] **A real second model** (section 11), fit on the same honest
  feature set, with a genuine tradeoff discussion — not just whichever
  metric is highest.

## Both experimental components — required, not either/or

- [ ] A real A/B test design (section 10): real control/treatment spec,
  and a **real, computed sample size** (`statsmodels.stats.power` or
  equivalent, grounded in a real baseline from your own data — not
  asserted "big enough").
- [ ] A real causal/program-evaluation write-up: named confounder, a
  stated threat to validity.

## Team accountability

- [ ] `team_charter.md` written **before** any real modeling work — a
  real RACI naming one clear accountable owner per real task.
- [ ] Shared `.gitignore`/`LICENSE` (every member's name on it), real
  branch protection on `main`, ≥2 real substantive review comments given
  by ≥2 different members, ≥2 received and incorporated.
- [ ] Each member's own `individual_reflection_<name>.md`, with real,
  checkable evidence (commit/PR links) for their own RACI row.

## The group readout

- [ ] Each role presents their own piece (PM: scope/timeline, Tech Lead:
  model/pipeline, Business Analyst: findings/recommendation,
  Experimentation Lead: A/B + causal) and fields real Q&A on it.

## Written work

- [ ] A final memo that explicitly separates what the model shows from
  what it can causally claim, integrates **both** experimental
  components, and ends in a specific, concrete recommendation.
