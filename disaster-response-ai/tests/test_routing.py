import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from api.main import app

client = TestClient(app)

# Mock responses
MOCK_GOOGLE_ROUTE = {
    "routes": [{"legs": [{"distance": {"value": 5000}}]}]
}
MOCK_DANGER_ZONES = {
    "type": "FeatureCollection",
    "features": [{
        "geometry": {"type": "Polygon", "coordinates": [[[1.0, 2.0], [1.1, 2.1]]}
    }]
}

def test_safe_route_without_dangers():
    """Test route planning when no danger zones exist."""
    with patch("core.routing.maps_integration.GoogleMapsClient.get_route") as mock_gmaps:
        mock_gmaps.return_value = MOCK_GOOGLE_ROUTE
        
        response = client.get("/routing/safe_route?start=Nairobi&end=Mombasa")
        
        assert response.status_code == 200
        assert response.json()["original"] == MOCK_GOOGLE_ROUTE
        assert response.json()["optimized"] == MOCK_GOOGLE_ROUTE  # No changes

def test_safe_route_with_danger_avoidance():
    """Test rerouting around a danger zone."""
    with (
        patch("core.routing.maps_integration.GoogleMapsClient.get_route") as mock_gmaps,
        patch("core.routing.danger_zones.DangerZoneManager._fetch_danger_zones") as mock_zones,
        patch("core.routing.danger_zones.DangerZoneManager._reroute") as mock_reroute
    ):
        mock_gmaps.return_value = MOCK_GOOGLE_ROUTE
        mock_zones.return_value = MOCK_DANGER_ZONES
        mock_reroute.return_value = {"routes": [{"legs": [{"distance": {"value": 5500}}]}]}  # Longer but safer
        
        response = client.get("/routing/safe_route?start=Nairobi&end=Mombasa")
        
        assert response.status_code == 200
        assert response.json()["optimized"]["routes"][0]["legs"][0]["distance"]["value"] == 5500

def test_invalid_location_handling():
    """Test invalid start/end locations (e.g., non-existent city)."""
    with patch("core.routing.maps_integration.GoogleMapsClient.get_route") as mock_gmaps:
        mock_gmaps.side_effect = ValueError("Invalid address")
        
        response = client.get("/routing/safe_route?start=Nowhere&end=Narnia")
        
        assert response.status_code == 400
        assert "Invalid address" in response.json()["detail"]