# app.py
from flask import Flask, request, jsonify
from predictor import classify_message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call API

@app.route("/")
def home():
    return "HopeLink AI Backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    prediction = classify_message(message)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
