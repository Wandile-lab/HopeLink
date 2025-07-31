from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
from pathlib import Path

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
CURRENT_DIR = Path(__file__).resolve().parent
MODEL_DIR = CURRENT_DIR.parent / "models"
clf_path = MODEL_DIR / "hope_classifier.pkl"
vec_path = MODEL_DIR / "hope_vectorizer.pkl"

# Load model and vectorizer once at startup
try:
    clf = joblib.load(clf_path)
    vectorizer = joblib.load(vec_path)
except Exception as e:
    print(f"❌ Error loading model or vectorizer: {e}")
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
    try:
        pred_label = clf.predict([text])[0]
        proba = clf.predict_proba([text]).max()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")

    print(f"Predicted: {pred_label}, Confidence: {proba:.2f}")

    if proba < 0.6 or pred_label == "unknown":
        response_message = (
            "Thank you for your report. Our system is currently analyzing the details. "
            "Although some specifics are still being confirmed, your alert has been prioritized. "
            "Please stay alert and follow any official guidance. If you're in danger, call emergency services immediately."
        )
        return PredictionResponse(
            disaster_type="unknown",
            urgency="none",
            confidence=proba,
            response_message=response_message
        )

    disaster_type, urgency = parse_label(pred_label)

    if urgency == "high":
        action = "🚨 Emergency responders have been alerted."
    elif urgency == "moderate":
        action = "⚠️ Situation is under observation by local authorities."
    else:
        action = "📁 Report archived for record-keeping and further analysis."

    response_message = (
        f"Detected disaster: **{disaster_type.capitalize()}** | Urgency: **{urgency.upper()}**. "
        f"{action} Stay safe."
    )

    return PredictionResponse(
        disaster_type=disaster_type,
        urgency=urgency,
        confidence=proba,
        response_message=response_message
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
