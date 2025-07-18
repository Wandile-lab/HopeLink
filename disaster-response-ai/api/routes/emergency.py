from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmergencyForm(BaseModel):
    name: str
    location: str
    description: str

@router.post("/submit")
def submit_emergency(form: EmergencyForm):
    # Dummy response
    return {
        "message": "Emergency received",
        "data": form.dict()
    }
