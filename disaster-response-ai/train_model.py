import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
import pandas as pd
import random

# Your expanded training dataset (sampled & labeled)
training_data = (
    [("Fire in the forest, urgent help", "fire_high")] * 5 +
    [("Small fire, controlled", "fire_low")] * 5 +
    [("Smoke and flames near houses", "fire_moderate")] * 5 +
    [("Massive fire destroying buildings", "fire_high")] * 3 +
    [("Firefighters on site controlling blaze", "fire_moderate")] * 2 +

    [("Flooding in the streets", "flood_high")] * 5 +
    [("Minor flood after rain", "flood_low")] * 5 +
    [("River overflowing", "flood_moderate")] * 5 +
    [("Floodwaters rising rapidly", "flood_high")] * 3 +
    [("Flood barriers holding up", "flood_moderate")] * 2 +

    [("Tornado sighted near town", "tornado_high")] * 5 +
    [("Possible tornado forming", "tornado_moderate")] * 5 +
    [("Strong winds from tornado", "tornado_low")] * 5 +

    [("Hurricane approaching, evacuate!", "hurricane_high")] * 5 +
    [("Heavy winds from hurricane", "hurricane_moderate")] * 5 +
    [("Hurricane aftermath cleanup", "hurricane_low")] * 5 +

    [("Robbery in progress, police needed", "robbery_high")] * 5 +
    [("Someone broke into my house", "robbery_moderate")] * 5 +
    [("Suspicious activity reported", "robbery_low")] * 5 +

    [("Flu outbreak in the area", "disease_moderate")] * 4 +
    [("People showing symptoms of illness", "disease_low")] * 3 +
    [("Epidemic spreading fast", "disease_high")] * 3 +

    [("Hello, how are you?", "unknown")] * 2 +
    [("I love pizza and movies", "unknown")] * 2 +
    [("What's the weather like?", "unknown")] * 2 +
    [("Just chilling, nothing to report", "unknown")] * 2 +
    [("Random words not related to disasters", "unknown")] * 2
)

random.seed(42)
random.shuffle(training_data)

# Convert to DataFrame for easy handling
df = pd.DataFrame(training_data, columns=["message", "label"])

X = df["message"]
y = df["label"]

# Stratified train-test split (25% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Pipeline with TF-IDF vectorizer and logistic regression classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", lowercase=True, ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000)),
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

print(f"Accuracy: {acc:.2f}")
print(f"F1 Score: {f1:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Step 1: Make sure the directory exists — match this with where you're saving the file
os.makedirs("disaster-response-ai/api/models", exist_ok=True)

# Step 2: Save the pipeline to the same path
joblib.dump(pipeline, "disaster-response-ai/api/models/hope_classifier.pkl")
print("✅ Model pipeline saved successfully at 'disaster-response-ai/api/models/hope_classifier.pkl'")