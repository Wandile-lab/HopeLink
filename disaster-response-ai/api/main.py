from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import emergency, prediction, routing, aid_optimizer, explainability

app = FastAPI(title="HopeLink Disaster Response AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

app.include_router(emergency.router, prefix="/emergency")
app.include_router(prediction.router, prefix="/prediction")
app.include_router(routing.router, prefix="/routing")
app.include_router(aid_optimizer.router, prefix="/aid")
app.include_router(explainability.router, prefix="/explain")
app.include_router(prediction.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "operational"}
