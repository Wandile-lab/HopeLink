from fastapi import APIRouter

router = APIRouter()

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
