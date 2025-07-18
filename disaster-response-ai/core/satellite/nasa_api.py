import tensorflow as tf
from core.satellite.utils import preprocess, mask_to_geojson  # if used

def predict_flood(image_path):  
    model = tf.keras.models.load_model("models/flood_prediction.h5")  
    img = preprocess(image_path)  
    mask = model.predict(img)  # Binary flood mask  
    return mask_to_geojson(mask)  # For GIS integration  

def get_fire_data():
    # Dummy fire data for demo/testing
    return {
        "fires": [
            {"latitude": -25.75, "longitude": 28.19, "intensity": "high"},
            {"latitude": -26.2, "longitude": 28.04, "intensity": "moderate"}
        ]
    }
