import geopandas as gpd
from shapely.geometry import Point

class DangerZoneManager:
    def __init__(self):
        self.zones = gpd.read_file("data/processed/danger_zones.db")

    def avoid_danger(self, route):
        for _, zone in self.zones.iterrows():
            if zone.geometry.intersects(Point(route["lon"], route["lat"])):
                return self._reroute(route, zone)
        return route