"""
Chapter 7: Transformers
Small Transformer for sequence classification
"""
import torch
import torch.nn as nn
import torch.optim as optim
import math
from torch.utils.data import DataLoader, TensorDataset
import numpy as np


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float()
            * (-math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]


class TransformerClassifier(nn.Module):
    def __init__(self, input_dim, d_model, n_heads, n_layers,
                 num_classes, max_len=512):
        super().__init__()
        self.embedding = nn.Linear(input_dim, d_model)
        self.pos_enc = PositionalEncoding(d_model, max_len)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=4*d_model,
            batch_first=True, norm_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, n_layers)
        self.classifier = nn.Linear(d_model, num_classes)

    def forward(self, x):
        x = self.pos_enc(self.embedding(x))
        x = self.encoder(x)
        x = x.mean(dim=1)  # Global average pooling
        return self.classifier(x)


if __name__ == '__main__':
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Synthetic sequence data
    np.random.seed(42)
    N, L, D = 2000, 30, 8
    X = np.random.randn(N, L, D).astype(np.float32)
    y = (X[:, :, 0].mean(axis=1) > 0).astype(np.int64)
    X, y = torch.tensor(X), torch.tensor(y)

    train_loader = DataLoader(TensorDataset(X[:1500], y[:1500]),
                              batch_size=64, shuffle=True)
    test_loader = DataLoader(TensorDataset(X[1500:], y[1500:]),
                             batch_size=64)

    model = TransformerClassifier(
        input_dim=D, d_model=64, n_heads=4, n_layers=3, num_classes=2
    ).to(DEVICE)

    n_params = sum(p.numel() for p in model.parameters())
    print(f"Transformer Classifier ({n_params:,} params)")

    optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(30):
        model.train()
        for Xb, yb in train_loader:
            Xb, yb = Xb.to(DEVICE), yb.to(DEVICE)
            optimizer.zero_grad()
            criterion(model(Xb), yb).backward()
            optimizer.step()

        if (epoch + 1) % 10 == 0:
            model.eval()
            correct = 0
            with torch.no_grad():
                for Xb, yb in test_loader:
                    Xb, yb = Xb.to(DEVICE), yb.to(DEVICE)
                    correct += (model(Xb).argmax(1) == yb).sum().item()
            print(f"Epoch {epoch+1:2d} | Acc: {correct/500:.4f}")
