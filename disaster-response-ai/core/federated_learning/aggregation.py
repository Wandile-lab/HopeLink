import numpy as np
from cryptography.hazmat.primitives import serialization

class FederatedAggregator:
    def __init__(self):
        self.client_weights = []
    
    def add_client_update(self, encrypted_weights):
        decrypted = self._decrypt(encrypted_weights)  # Uses RSA private key
        self.client_weights.append(decrypted)
    
    def aggregate(self):
        avg_weights = {
            k: np.mean([w[k] for w in self.client_weights], axis=0)
            for k in self.client_weights[0].keys()
        }
        return avg_weights