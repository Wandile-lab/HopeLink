from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_emergency_detection():
    response = client.post(
        "/emergency/detect",
        json={"text": "Flood in Nairobi!", "location": [1.0, 2.0], "source": "twitter"}
    )
    assert response.status_code == 200
    assert "id" in response.json()