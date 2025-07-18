# HopeLink: AI-Powered Disaster Response Platform
HopeLink is a smart, AI-powered disaster response and coordination platform designed to assist civilians, aid workers, and emergency services during crises. It combines geospatial mapping, real-time emergency form submissions, shelter tracking, chatbot assistance, and AI-generated predictions to streamline humanitarian response in disaster-affected regions.

# What HopeLink Does
Emergency Form Submission
Users can report disasters and request aid in real-time via a dynamic form UI.

AI-Powered Predictions
Uses mock ML models (TensorFlow-based placeholder) to simulate predictions for floods, fires, and other emergencies.

Live Map & Routing Panel
Interactive Leaflet-powered map to visualize user reports and optimal emergency routes.

Shelter Status Monitoring
View nearby shelters with status indicators (open, full, unknown) and location details.

Aid Optimization Dashboard
Backend logic to simulate AI-based decision-making for allocating aid based on severity, urgency, and location.

# HopeLink Disaster Response Demo

## Backend Setup

1. Activate the virtual environment:
venv\Scripts\activate

2. Install dependencies:
pip install -r disaster-response-ai/requirements.txt


3. Run the FastAPI backend:
uvicorn api.main:app --reload


API will be available at http://127.0.0.1:8000

---

## Frontend Setup

1. Navigate to frontend folder:
cd frontend


2. Install dependencies:
npm install



3. Run the frontend:
npm run dev


Access frontend on http://localhost:3000

---

## Quick Start

Alternatively, just run the `start.bat` script from the HopeLink root folder — it activates the backend venv, launches backend and frontend servers automatically.

---

## Notes

- This is a demo with dummy data for development and testing.
- Extend backend API with real ML models or APIs as needed.
- Frontend can be extended with maps, charts, and chatbot components later.

