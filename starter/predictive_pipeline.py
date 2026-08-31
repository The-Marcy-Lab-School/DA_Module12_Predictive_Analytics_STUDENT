# %% [markdown]
# # Predictive Analytics Pipeline (team project)
#
# Run this file cell-by-cell in VS Code's Jupyter extension. See
# `../required_components.md` for exactly what each section needs
# (sections 1-9 core, 10-12 also required for the team version), and
# `../SCENARIOS.md` to pick your team's one shared dataset/target. The
# written synthesis (business framing, **both** the A/B design and the
# causal component, final interpretation) lives in `../business_memo.md`
# — a separate deliverable, not this file. Real accountability for who
# owns which section lives in `team_charter.md`.

# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score, r2_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import mlflow

# %% [markdown]
# ## 1. Load your data
#
# Reuse your own established domain dataset — this repo's
# `../data/<domain>/` folder has the real CSVs. See `../SCENARIOS.md`
# for a real, verified classification/regression/clustering angle per
# domain.

# %%
# TODO: load the real CSV(s) you're using
df = None

# %% [markdown]
# ## 2. Frame the business question
#
# Before fitting anything: what are you predicting, and what real
# business or policy decision would this model actually inform?
#
# TODO (markdown, right here):
# - What am I predicting, and for whom?
# - What decision would this model's output actually change?

# %% [markdown]
# ## 3. Real train/test split (no leakage)
#
# Split BEFORE any fitting/scaling — fitting a scaler or imputer on the
# full dataset before splitting is a real, common leakage mistake
# (`common_project_mistakes` doesn't list this one by name, but it's the
# same family as "reporting accuracy with no train/test split at all").

# %%
# TODO: real train_test_split call

# %% [markdown]
# ## 4. Fit a model
#
# Pick a real scikit-learn model matching your target type
# (classification or regression).

# %%
# TODO: fit a real model on your training data

# %% [markdown]
# ## 5. Evaluate with a justified metric
#
# Not just "accuracy." Pick precision, recall, AUC, or R² based on the
# real business tradeoff you named in section 2 — and say why that
# metric, not another one, fits your specific decision.

# %%
# TODO: compute your chosen metric(s), print them
# TODO (markdown): why this metric, given your section 2 framing?

# %% [markdown]
# ## 6. Fairness/disparity check
#
# Pick a real segment variable in your data (not your target, not your
# main predictive feature) and check whether your classifier's
# false-negative rate (or another relevant error rate) differs
# meaningfully across segments. This must be an actual computed number,
# not a sentence asserting the model is "fair."

# %%
# TODO: compute a real per-segment error rate, print it
# TODO (markdown): is there a meaningful disparity? What would you do
# about it if there were?

# %% [markdown]
# ## 7. Log this run with MLflow
#
# See `../starter/mlflow_setup.md` for the real local-tracking setup
# (`sqlite:///mlflow.db`, not the older file-store default).

# %%
# TODO: mlflow.set_tracking_uri(...), mlflow.set_experiment(...)
# TODO: inside `with mlflow.start_run():`, log your model type, key
# hyperparameters, and your real metric(s) from section 5

# %% [markdown]
# ## 8. Clustering / segmentation
#
# Cluster a real, meaningful unit in your data (not individual rows of
# your prediction target — a real aggregate business unit: e.g.
# communities, facilities, agencies, or clients — see `../SCENARIOS.md`
# for your domain's suggestion) and evaluate the result against a real
# business use case, not just a silhouette score in isolation.

# %%
# TODO: build real aggregate features per unit, scale them, run KMeans
# TODO (markdown): what would each cluster mean to someone making a
# real business decision?

# %% [markdown]
# ## 9. Interpret in business terms
#
# Pull your model's coefficients (if a linear model) or feature
# importances (if tree-based) and explain what they mean in plain,
# business-framed language — not just "feature X has coefficient 0.4."

# %%
# TODO: print coefficients/importances
# TODO (markdown): what do they mean for the business question in
# section 2?

# %% [markdown]
# ## 10. A/B test design: a real, computed sample size
#
# `../starter/ab_test_design_option.md` is where the full design lives
# (business change, control/treatment, threat to validity) — this
# section is specifically the real, computed sample-size math, using a
# real baseline rate/variance from your own data, not an assumed one.
# `pip install statsmodels` if you haven't — `statsmodels.stats.power`
# has real, standard power-calculation tools; don't hand-derive the
# formula yourself.

# %%
# TODO: a real baseline rate (or mean/variance, if your metric is
# continuous) computed from your own data
# TODO: state a real minimum detectable effect
# TODO: a real power calculation (e.g. statsmodels.stats.power.NormalIndPower
# for a proportion, or the continuous-data equivalent) -- print the
# required sample size, don't just assert it's "big enough"

# %% [markdown]
# ## 11. Second model comparison
#
# A different real scikit-learn model against the same honest feature
# set from section 4. Report both metrics and discuss the real
# tradeoff — not just whichever number is highest.

# %%
# TODO: fit a second, genuinely different model
# TODO: compute the same metric as section 5, print both
# TODO (markdown): which would you actually recommend, and why?

# %% [markdown]
# ## 12. Second fairness segment
#
# Extend section 6's fairness check to a second real segment variable
# in your data.

# %%
# TODO: compute the same error-rate check as section 6, for a different
# real segment variable
# TODO (markdown): does this second check change your section 6
# conclusion at all?
