"""Module containing AzureML utility functions."""

import pandas as pd
import sklearn.metrics


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
    """Logs histogram for the predictions."""

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
    """Logs histogram for the residuals of a regresion model."""
    
    # Construct histogram data as JSON
    labels, edges = pd.cut(residuals, bins=bins, retbins=True)
    bins = residuals.groupby(labels)
    
    return {
        "schema_type": "residuals",
        "schema_version": "v1",
        "data": {"bin_counts": list(bins.count()), "bin_edges": list(edges)},
    }
