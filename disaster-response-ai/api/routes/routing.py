from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy")
def get_routing_info():
    return {
        "routes": [
            {"start": "Point A", "end": "Point B", "distance_km": 5.2, "duration_min": 12},
            {"start": "Point C", "end": "Point D", "distance_km": 8.5, "duration_min": 18}
        ]
    }
