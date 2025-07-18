import redis

r = redis.Redis(host="redis", port=6379, db=0)

def cache_emergency(emergency_id, lat, lon):
    r.geoadd("active_emergencies", lon, lat, emergency_id)

def get_nearby_emergencies(lat, lon, radius_km):
    return r.georadius("active_emergencies", lon, lat, radius_km, unit="km")