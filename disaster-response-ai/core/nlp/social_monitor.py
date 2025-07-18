from transformers import pipeline

class SocialMonitor:
    def __init__(self):
        self.nlp = pipeline("text-classification", model="bert-base-uncased")

    def analyze_social_media(self, text: str):
        result = self.nlp(text)[0]  # pipeline returns a list of results
        return {
            "disaster": result["label"],
            "confidence": result["score"]
        }
