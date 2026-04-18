"""
Iris Prediction API
===================
A FastAPI application that serves a scikit-learn model for iris species classification.

Run with:
    uvicorn app:app --reload --port 8000

API docs available at:
    http://localhost:8000/docs
"""

import joblib
import json
import numpy as np
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


# --------------- Pydantic Models ---------------


class PredictionRequest(BaseModel):
    """Input schema for a single prediction."""

    sepal_length: float = Field(..., ge=0, le=10, description="Sepal length in cm")
    sepal_width: float = Field(..., ge=0, le=10, description="Sepal width in cm")
    petal_length: float = Field(..., ge=0, le=10, description="Petal length in cm")
    petal_width: float = Field(..., ge=0, le=10, description="Petal width in cm")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2,
                }
            ]
        }
    }


class PredictionResponse(BaseModel):
    """Output schema for predictions."""

    prediction: str
    prediction_id: int
    probabilities: dict


class BatchRequest(BaseModel):
    """Input schema for batch predictions."""

    instances: List[PredictionRequest]


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    model_loaded: bool
    model_type: Optional[str] = None


# --------------- App Setup ---------------

app = FastAPI(
    title="Iris Prediction API",
    description="Predict iris species from flower measurements. "
    "Part of the MLOps in Practice workshop.",
    version="1.0.0",
)

# Model and metadata paths
MODEL_PATH = Path("models/iris_pipeline.joblib")
METADATA_PATH = Path("models/metadata.json")

model = None
metadata = None


@app.on_event("startup")
def load_model():
    """Load the trained model and metadata at startup."""
    global model, metadata
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
    else:
        print(f"WARNING: Model not found at {MODEL_PATH}")

    if METADATA_PATH.exists():
        with open(METADATA_PATH) as f:
            metadata = json.load(f)
        print(f"Metadata loaded from {METADATA_PATH}")


# --------------- Endpoints ---------------


@app.get("/health", response_model=HealthResponse)
def health_check():
    """Check if the service is healthy and the model is loaded."""
    return HealthResponse(
        status="healthy" if model is not None else "unhealthy",
        model_loaded=model is not None,
        model_type=metadata.get("model_type") if metadata else None,
    )


@app.get("/model/info")
def model_info():
    """Return model metadata (type, accuracy, features)."""
    if metadata is None:
        raise HTTPException(status_code=503, detail="Metadata not loaded")
    return metadata


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """Make a single prediction for iris species."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    features = np.array(
        [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )

    prediction_id = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]

    target_names = metadata.get("target_names", ["0", "1", "2"]) if metadata else ["0", "1", "2"]

    return PredictionResponse(
        prediction=target_names[prediction_id],
        prediction_id=prediction_id,
        probabilities={
            name: round(float(prob), 4) for name, prob in zip(target_names, probabilities)
        },
    )


@app.post("/predict/batch", response_model=List[PredictionResponse])
def predict_batch(request: BatchRequest):
    """Make batch predictions for multiple instances."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    features = np.array(
        [
            [inst.sepal_length, inst.sepal_width, inst.petal_length, inst.petal_width]
            for inst in request.instances
        ]
    )

    predictions = model.predict(features)
    probabilities = model.predict_proba(features)
    target_names = metadata.get("target_names", ["0", "1", "2"]) if metadata else ["0", "1", "2"]

    return [
        PredictionResponse(
            prediction=target_names[int(pred)],
            prediction_id=int(pred),
            probabilities={
                name: round(float(prob), 4) for name, prob in zip(target_names, probs)
            },
        )
        for pred, probs in zip(predictions, probabilities)
    ]
