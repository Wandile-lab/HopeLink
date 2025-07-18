# schemas/emergency.py
from pydantic import BaseModel
from typing import Optional

class EmergencyReport(BaseModel):
    id: str
    text: str
    location: tuple[float, float]  # (lat, lon)
    source: str  # "twitter", "sensor", etc.
    confidence: Optional[float] = None

# schemas/prediction.py
class SatellitePrediction(BaseModel):
    type: str  # "flood", "fire", "earthquake"
    risk: str  # "low", "medium", "high"
    confidence: float
    geometry: dict  # GeoJSON