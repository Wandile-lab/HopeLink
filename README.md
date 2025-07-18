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

