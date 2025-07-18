import geopandas as gpd

danger_zones = gpd.read_file("data/raw/danger_zones.geojson")
danger_zones.to_file("data/processed/danger_zones.db", driver="GeoJSON")  # For PostGIS