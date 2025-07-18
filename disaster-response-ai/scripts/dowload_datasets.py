import requests
import os

NASA_FIRMS_URL = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_24h.csv"

def download_fire_data():
    os.makedirs("data/raw", exist_ok=True)
    response = requests.get(NASA_FIRMS_URL)
    with open("data/raw/fires_24h.csv", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    download_fire_data()