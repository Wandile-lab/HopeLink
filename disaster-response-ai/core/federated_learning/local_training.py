import torch
from cryptography.hazmat.primitives.asymmetric import rsa

class FederatedTrainer:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    def train_local_model(self, local_data):
        model = load_global_model()  # From central server
        optimizer = torch.optim.Adam(model.parameters())
        
        for epoch in range(10):
            for x, y in local_data:
                loss = model.loss_fn(model(x), y)
                loss.backward()
                optimizer.step()
        
        encrypted_weights = self._encrypt_weights(model.state_dict())
        return encrypted_weights
    
    def _encrypt_weights(self, weights):
        # Homomorphic encryption for secure aggregation
        return self.private_key.encrypt(weights)