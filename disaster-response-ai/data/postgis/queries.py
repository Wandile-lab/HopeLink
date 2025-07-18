from sqlalchemy import create_engine, text

class PostGISManager:
    def __init__(self):
        self.engine = create_engine("postgresql://user:pass@postgis:5432/disaster_db")
    
    def get_nearby_shelters(self, lat: float, lon: float, radius_km: int):
        query = text("""
            SELECT name, ST_Distance(
                location,
                ST_SetSRID(ST_MakePoint(:lon, :lat), 4326
            ) / 1000 AS distance_km
            FROM shelters
            WHERE ST_DWithin(
                location,
                ST_SetSRID(ST_MakePoint(:lon, :lat), 4326),
                :radius * 1000
            )
            ORDER BY distance_km
        """)
        with self.engine.connect() as conn:
            return conn.execute(query, {"lat": lat, "lon": lon, "radius": radius_km}).fetchall()