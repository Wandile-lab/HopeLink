import numpy as np
from sklearn.ensemble import IsolationForest
from typing import Dict, List
import redis

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.4,  # Increased sensitivity
            random_state=42,
            max_samples='auto'  # Let sklearn determine optimal sample size
        )
        self.redis = redis.Redis(host='redis', port=6379, db=1)
        self.SENSOR_FEATURES = ["water_level", "vibration", "temperature"]
        self.threshold = None  # Will be set during training

    def train(self, historical_data: List[Dict]):
        """Train on historical sensor data"""
        X = np.array([[d[f] for f in self.SENSOR_FEATURES] for d in historical_data])
        self.model.fit(X)
        
        # Get anomaly scores for training data
        scores = self.model.score_samples(X)
        # Set threshold to flag bottom 20% as anomalies
        self.threshold = np.percentile(scores, 30)

    def check_anomalies(self, realtime_data: Dict) -> Dict:
        """
        Returns: {"is_anomalous": bool, "confidence": float, "anomaly_score": float}
        """
        x = np.array([[realtime_data[f] for f in self.SENSOR_FEATURES]])
        score = self.model.score_samples(x)[0]
        is_anomaly = score < self.threshold
        
        # Cache anomalous readings
        if is_anomaly and 'sensor_id' in realtime_data:
            self.redis.set(
                f"anomaly:{realtime_data['sensor_id']}",
                str(realtime_data),
                ex=3600
            )
            
        return {
            "is_anomalous": bool(is_anomaly),
            "confidence": min(1.0, max(0.0, 1 - (score - self.threshold))),
            "anomaly_score": float(score)
        }