# Scenarios: Real, Verified Modeling Angles Per Domain

Use your own already-established Module 3/5/7/8/9/10 domain — this
repo's own `data/<domain>/` folder has the same real CSVs from Module
3, so there's no need to go back to that repo. Every angle below was
independently run against the real data before being written here, not
guessed.

## `finance_insurance`

**Classification target**: `net_building_payment > 0` (does a claim get
a nonzero payment). **Regression target**: `net_building_payment` among
claims that did get paid. Real features: `occupancy_type`,
`cause_of_damage` (a real, honest note: this column is a messy
mixed-type field — string values `'0'`–`'9'` plus a real `'D'`
category, with 36 real nulls — clean it with
`.fillna('missing').astype(str)` before `pd.get_dummies`, or you'll hit
a duplicate-column error).

**A real, honest finding worth knowing before you pick your features**:
including `building_damage_amount` produces suspiciously strong
performance (real AUC ≈0.98, R² ≈0.94) — this isn't leakage in the
train/test sense, but a near-definitional relationship (assessed damage
almost directly determines payout), so it's real but not a useful
predictive insight for a decision made *before* damage is assessed.
Dropping it for `occupancy_type`/`cause_of_damage` alone gives more
modest, more honest, more decision-useful signal (real AUC ≈0.68, R²
≈0.055). Decide — and say explicitly in your memo — which framing your
project is actually doing.

**Clustering**: communities, by claim volume/mean payment/nonzero rate
— real, distinct segments confirmed (a low-volume/low-payment group, a
low-volume/high-payment group, a high-volume/mid-payment group).

## `healthcare_operations`

**Classification target**: `total_claim_cost` above the median
("high-cost encounter"), from `encounter_class`/`gender`. Real,
verified: AUC ≈0.66. **Regression target**: `total_claim_cost` directly
— real but weak signal (R² ≈0.09) from these same features; a good,
honest example of a model that's real but not strongly predictive.

**Clustering**: facilities, by encounter volume and mean cost — 3 real,
distinct groups (a small/cheap group, a medium-volume/moderate-cost
group, a small/expensive group).

## `public_sector`

**Classification target**: `status == "Closed"`, from
`agency_code`/`complaint_type`/`borough`. Real, verified: AUC ≈0.80 —
the strongest classification signal of any domain.

**Clustering**: agencies, by request volume and close rate — real,
distinct groups confirmed, though only ~12 agencies total (a real,
honest small-N caveat — say so if you pick this domain for clustering,
don't overstate how stable a 3-cluster split is on 12 points).

## `professional_services`

**Classification target**: `billable` (True/False). **Regression
target**: `hours`. **Real, honest note**: both come back genuinely
**weak** from `hourly_rate`/`service_type` (AUC ≈0.53, barely above
chance; R² ≈-0.085, worse than predicting the mean) — a real, valid
finding, not a failure to hide. If you pick this domain, your memo
should say plainly that these features don't predict billing outcomes
well, rather than searching for a "better" result. A real 160-row null
gap in `hours` also needs handling (`dropna` or documented imputation).

**Clustering**: clients, by total hours/average rate/engagement count —
3 real, distinct segments confirmed.

## Either/or component (`starter/ab_test_design_option.md` or `starter/causal_program_eval_option.md`)

Both options work with any of the 4 domains above — pick whichever real
business/policy question from your domain is more naturally a
"would-run-an-experiment" question (A/B) vs. a "can-I-explain-what-I-
already-observed" question (causal/program-eval).

## Lecture/lab-only resources — not your project's data source

`fema.gov/about/openfema/data-sets` and
`consumerfinance.gov/data-research/consumer-complaints/` are real
government data portals worth exploring in class, but they are not this
project's data source. Stick to your own domain data above.
