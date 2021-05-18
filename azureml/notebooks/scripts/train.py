from azureml.core import Workspace, Dataset, Run, Model

import joblib
import pandas as pd

import sklearn.metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit


# Cross validation settings
cv_splits = 5
test_prop = .3

# Training metrics to log in AzureML
log_metrics = "mean_absolute_percentage_error", "mean_absolute_error", "median_absolute_error", "r2_score"

# Model ID and file settings
model_id = "house_prices_linear_model"
model_file = f"{model_id}.joblib"

# Percentage error threshold for registering the model
performance_threshold = 5


def main():
    """Model training routine."""
    
    ws = Workspace.from_config()

    # Get the dataset from the workspace
    data = Dataset.get_by_name(ws, "house_prices")
    data = data.to_pandas_dataframe()

    # Split features and labels
    X = data.drop(columns="price")
    y = data["price"]

    # Get the run to start logging
    run = Run.get_context()

    # Log training data and CV params
    run.log("Training size", X.shape[0])
    run.log("CV splits", cv_splits)
    run.log("CV test proportion", test_prop)
    
    # Run cross-validation
    metrics = []
    results = []
    model = LinearRegression()
    cv = ShuffleSplit(n_splits=cv_splits, test_size=test_prop)
    
    for train, test in cv.split(X):
        model.fit(X.loc[train, :], y[train])

        y_true = y[test]
        y_pred = model.predict(X.loc[test, :])

        results.append(
            pd.DataFrame({
                "actual": y_true,
                "predicted": y_pred,
                "residual": y_pred - y_true,
            })
        )

        metrics.append(compute_metrics(y_true, y_pred, log_metrics))
    
    results = pd.concat(results)
    metrics = pd.DataFrame(metrics)
    
    # Log accuracy metrics in AzureML (mean from splits)
    for metric in metrics.columns:
        run.log(metric.replace("_", " ").title(), metrics[metric].mean())

    # Log predictions and residuals histograms
    run.log_predictions("Predictions", histogram_predictions(results["predicted"]))
    run.log_residuals("Residuals", histogram_residuals(results["residual"]))

    # Register if percentage error below threshold
    performance = sklearn.metrics.mean_absolute_percentage_error(
        results["actual"], results["predicted"]
    )
    if performance <= performance_threshold:
        
        # Retrain on all data
        model = model.fit(X, y)
        
        # Complete the run so files get uploaded
        joblib.dump(model, model_file)
        run.upload_file(model_file, model_file)

        # Register the model
        run.register_model(
            model_name=model_id,
            model_path=model_file,
            model_framework=Model.Framework.SCIKITLEARN,
            model_framework_version=sklearn.__version__,
            description=f"Mean Absolute Percentage Error: {performance}",
        )        


def compute_metrics(y_true, y_pred, metrics=None):
    """Computes requested scikit-learn performance metrics """
    
    results = {}
    for metric in metrics:
        if not hasattr(sklearn.metrics, metric):
            raise ValueError(f"Unknown metric: {metric}")
        
        metric_func = getattr(sklearn.metrics, metric)
        results[metric] = metric_func(y_true, y_pred)
    
    return results


def histogram_predictions(predictions, bins=20):
    """Returns histogram for the predictions as dict."""

    # Compute bin statistics as JSON
    labels, edges = pd.cut(predictions, bins=bins, retbins=True)
    bins = predictions.groupby(labels)
    
    return {
        "schema_type": "predictions",
        "schema_version": "v1",
        "data": {
            "bin_averages": list(bins.mean()),
            "bin_errors": list(bins.std()),
            "bin_counts": list(bins.count()),
            "bin_edges": list(edges),
        },
    }


def histogram_residuals(residuals, bins=20):
    """Returns histogram for the residuals as dict."""
    
    # Construct histogram data as JSON
    labels, edges = pd.cut(residuals, bins=bins, retbins=True)
    bins = residuals.groupby(labels)
    
    return {
        "schema_type": "residuals",
        "schema_version": "v1",
        "data": {"bin_counts": list(bins.count()), "bin_edges": list(edges)},
    }


if __name__ == "__main__":
    main()