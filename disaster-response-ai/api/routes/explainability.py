from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy")
def get_explanation():
    return {
        "explanation": "This prediction was made using historical data and satellite imagery analysis.",
        "confidence": 0.85
    }
