# predictor.py
from transformers import pipeline

# Load zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

# Define candidate labels
DISASTER_TYPES = ["flood", "fire", "earthquake", "storm"]
URGENCY_LEVELS = ["low", "medium", "high"]

def classify_message(message):
    disaster_result = classifier(message, candidate_labels=DISASTER_TYPES)
    urgency_result = classifier(message, candidate_labels=URGENCY_LEVELS)

    return {
        "disaster_type": disaster_result["labels"][0],
        "disaster_confidence": round(disaster_result["scores"][0], 2),
        "urgency": urgency_result["labels"][0],
        "urgency_confidence": round(urgency_result["scores"][0], 2)
    }
