import googlemaps
from datetime import datetime
from typing import Dict, List, Optional
import os
from geopy.distance import great_circle

class GoogleMapsClient:
    def __init__(self):
        self.client = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))
        self.MODE = "driving"
        self.AVOID = ["tolls", "ferries"]

    def get_route(
        self,
        origin: str,
        destination: str,
        waypoints: Optional[List[str]] = None
    ) -> Dict:
        """Returns route with distance (meters) and duration (seconds)"""
        now = datetime.now()
        result = self.client.directions(
            origin,
            destination,
            mode=self.MODE,
            avoid=self.AVOID,
            waypoints=waypoints,
            departure_time=now
        )
        
        if not result:
            raise ValueError("No route found")

        route = result[0]["legs"][0]
        return {
            "distance": route["distance"]["value"],
            "duration": route["duration"]["value"],
            "steps": [
                {
                    "start": step["start_location"],
                    "end": step["end_location"],
                    "polyline": step["polyline"]["points"]
                } for step in route["steps"]
            ],
            "waypoint_order": result[0].get("waypoint_order", [])
        }

    def get_distance_matrix(self, origins: List[str], destinations: List[str]) -> List[List[float]]:
        """Returns distance matrix in meters"""
        matrix = self.client.distance_matrix(
            origins,
            destinations,
            mode=self.MODE
        )
        return [
            [row["elements"][j]["distance"]["value"] for j in range(len(destinations))]
            for i, row in enumerate(matrix["rows"])
        ]