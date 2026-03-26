"""
Chapter 5: Recurrent Networks and LSTMs
Sequence classification with LSTM
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes,
                 bidirectional=False):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True, bidirectional=bidirectional)
        mult = 2 if bidirectional else 1
        self.fc = nn.Linear(hidden_size * mult, num_classes)

    def forward(self, x):
        out, (h_n, _) = self.lstm(x)
        return self.fc(out[:, -1, :])  # Last time step


class GRUClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers,
                          batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out, _ = self.gru(x)
        return self.fc(out[:, -1, :])


def generate_synthetic_sequences(n_samples=2000, seq_len=50, n_features=5):
    """Generate synthetic time series classification data."""
    np.random.seed(42)
    X = np.random.randn(n_samples, seq_len, n_features).astype(np.float32)
    # Class depends on cumulative sum pattern
    cum_sum = X[:, :, 0].cumsum(axis=1)[:, -1]
    y = (cum_sum > 0).astype(np.int64)
    return torch.tensor(X), torch.tensor(y)


if __name__ == '__main__':
    X, y = generate_synthetic_sequences()
    n_train = 1500
    train_ds = TensorDataset(X[:n_train], y[:n_train])
    test_ds = TensorDataset(X[n_train:], y[n_train:])
    train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=64)

    models = {
        "LSTM":       LSTMClassifier(5, 64, 2, 2),
        "BiLSTM":     LSTMClassifier(5, 64, 2, 2, bidirectional=True),
        "GRU":        GRUClassifier(5, 64, 2, 2),
    }

    for name, model in models.items():
        model = model.to(DEVICE)
        optimizer = optim.Adam(model.parameters(), lr=1e-3)
        criterion = nn.CrossEntropyLoss()

        for epoch in range(20):
            model.train()
            for Xb, yb in train_loader:
                Xb, yb = Xb.to(DEVICE), yb.to(DEVICE)
                optimizer.zero_grad()
                criterion(model(Xb), yb).backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()

        model.eval()
        correct = 0
        with torch.no_grad():
            for Xb, yb in test_loader:
                Xb, yb = Xb.to(DEVICE), yb.to(DEVICE)
                correct += (model(Xb).argmax(1) == yb).sum().item()

        n_params = sum(p.numel() for p in model.parameters())
        print(f"{name:10s} | {n_params:>7,} params | "
              f"Acc: {correct/len(test_ds):.4f}")
