from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy")
def get_aid_distribution():
    return {
        "aid_centers": [
            {"name": "Center 1", "available_supplies": 150, "location": "Township X"},
            {"name": "Center 2", "available_supplies": 200, "location": "Township Y"}
        ]
    }
