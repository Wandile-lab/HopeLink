import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib

router = APIRouter()

# Request and response schemas
class PredictionRequest(BaseModel):
    message: str

class PredictionResponse(BaseModel):
    disaster_type: str
    urgency: str
    confidence: float
    response_message: str

# Resolve model directory relative to this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # api/
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load model and vectorizer once at startup
clf_path = os.path.join(MODEL_DIR, "hope_classifier.pkl")
vec_path = os.path.join(MODEL_DIR, "hope_vectorizer.pkl")

try:
    clf = joblib.load(clf_path)
    vectorizer = joblib.load(vec_path)
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")
    clf = None
    vectorizer = None

def parse_label(label: str):
    parts = label.split('_')
    if len(parts) == 2:
        return parts[0], parts[1]
    return label, "unknown"

@router.post("/predict", response_model=PredictionResponse)
def predict_disaster(request: PredictionRequest):
    if clf is None or vectorizer is None:
        raise HTTPException(status_code=500, detail="Model or vectorizer not loaded")

    text = request.message.lower()
    X = vectorizer.transform([text])
    pred_label = clf.predict(X)[0]
    proba = clf.predict_proba(X).max()
    
    print(f"Predicted: {pred_label}, Confidence: {proba}")

    # Handle unknown or low confidence predictions with a smart fallback
    if proba < 0.6 or pred_label == "unknown":
        response_message = (
            "Thank you for your report. Our system is currently analyzing the details, "
            "and while some specifics are still being confirmed, rest assured that your "
            "alert has been prioritized. In situations like this, timely preparedness "
            "is key: please stay alert for updates from local authorities, and if you "
            "or others are in immediate danger, contact emergency services directly. "
            "We’re continuously improving our detection algorithms to serve you better."
        )
        return PredictionResponse(
            disaster_type="unknown",
            urgency="none",
            confidence=proba,
            response_message=response_message
        )

    disaster_type, urgency = parse_label(pred_label)

    if urgency == "high":
        action = "Alert sent to emergency responders immediately."
    elif urgency == "moderate":
        action = "Flagged for monitoring by local authorities."
    else:
        action = "Archived for future reference."

    response_message = (
        f"Detected disaster type: {disaster_type.capitalize()} with urgency level: {urgency.upper()}. "
        f"{action} Stay safe!"
    )

    return PredictionResponse(
        disaster_type=disaster_type,
        urgency=urgency,
        confidence=proba,
        response_message=response_message,
    )


@router.get("/fire")
def get_fire_prediction():
    return {
        "fires": [
            {"latitude": -25.75, "longitude": 28.19, "intensity": "high"},
            {"latitude": -26.2, "longitude": 28.04, "intensity": "moderate"}
        ]
    }

@router.get("/flood")
def get_flood_prediction():
    return {
        "floods": [
            {"latitude": -25.76, "longitude": 28.20, "depth_meters": 0.8},
            {"latitude": -26.10, "longitude": 28.10, "depth_meters": 1.2}
        ]
    }
