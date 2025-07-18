@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Starting FastAPI backend...
start cmd /k "uvicorn api.main:app --reload"

timeout /t 5

echo Starting React frontend...
cd frontend
npm install
npm run dev
