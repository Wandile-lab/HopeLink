import sys
from pathlib import Path

# Add the correct path (only need this once at the top)
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "disaster-response-ai"))

# Now imports will work
from core.nlp.anomaly_detector import AnomalyDetector
import pytest

@pytest.fixture
def detector():
    detector = AnomalyDetector()
    detector.train([
            {"water_level": 1.0, "vibration": 0.1, "temperature": 25.0},
            {"water_level": 1.2, "vibration": 0.2, "temperature": 26.0}, 
            {"water_level": 1.3, "vibration": 0.3, "temperature": 27.0},  
            {"water_level": 1.1, "vibration": 0.25, "temperature": 25.0}
        ])
    return detector

def test_anomalous_reading(detector):
    result = detector.check_anomalies({
        "water_level": 10.0,
        "vibration": 3.0,
        "temperature": 85.0
    })
    assert result["is_anomalous"], f"Expected anomaly, got {result}"

def test_anomalous_reading(detector):
    result = detector.check_anomalies({
        "water_level": 5.0,
        "vibration": 1.0,
        "temperature": 40.0
    })
    assert result["is_anomalous"]
