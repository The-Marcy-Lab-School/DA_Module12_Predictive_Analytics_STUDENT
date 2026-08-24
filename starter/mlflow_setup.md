# MLflow Local Tracking Setup

MLflow's classic `./mlruns` file-store tracking is now in maintenance
mode — recent versions raise an error if you use it directly. Use a
local SQLite file instead: still zero infrastructure, still fully
local, no server, no account.

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("your-project-name")

with mlflow.start_run():
    mlflow.log_param("model_type", "logistic_regression")
    mlflow.log_metric("auc", 0.81)
    # ... log your real params/metrics here
```

This creates a single `mlflow.db` file in your project folder (already
covered by `.gitignore` — don't commit it, it's a local artifact, not
part of your submission).

## Retrieving what you logged

The whole point of MLOps tracking is that a run's results are
*retrievable*, not just printed to console and lost. Confirm you can
pull your own logged run back:

```python
run = mlflow.last_active_run()
client = mlflow.tracking.MlflowClient()
data = client.get_run(run.info.run_id).data
print(data.params)
print(data.metrics)
```

If this prints your real logged values back, your tracking setup is
working. `required_components.md` asks you to show this retrieval step
as evidence your MLOps tracking is real, not just attempted.
