"""Scoring script for a scikit-learn model."""

import os
import json
import joblib


def init():
    """Load the model from file."""
    
    # Ugly, but needs global variables...
    global model

    # Load the model from disk, use environmental variable to get the path.
    # Note: Replace the filename if needed.
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "house_prices_linear_model.joblib")
    model = joblib.load(model_path)
  

def run(request):
    """Generate scores for the provided dataset."""

    request = json.loads(request)
    if "data" not in request:
        return "Error: No data in request!"
    
    return model.predict(request["data"]).tolist()
