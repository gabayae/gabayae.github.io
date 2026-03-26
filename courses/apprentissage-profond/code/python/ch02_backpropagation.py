"""
Chapter 2: Backpropagation and Optimization
Manual backprop + optimizer comparison
"""
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# --- Manual Backpropagation ---
class ManualMLP:
    """2-layer MLP with manual backprop (NumPy)."""
    def __init__(self, d_in, d_hid, d_out):
        self.W1 = np.random.randn(d_hid, d_in) * np.sqrt(2 / d_in)
        self.b1 = np.zeros(d_hid)
        self.W2 = np.random.randn(d_out, d_hid) * np.sqrt(2 / d_hid)
        self.b2 = np.zeros(d_out)

    def relu(self, z):
        return np.maximum(0, z)

    def softmax(self, z):
        e = np.exp(z - z.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)

    def forward(self, X):
        self.z1 = X @ self.W1.T + self.b1
        self.h1 = self.relu(self.z1)
        self.z2 = self.h1 @ self.W2.T + self.b2
        self.probs = self.softmax(self.z2)
        return self.probs

    def backward(self, X, y_onehot, lr=0.01):
        N = X.shape[0]
        delta2 = (self.probs - y_onehot) / N
        dW2 = delta2.T @ self.h1
        db2 = delta2.sum(axis=0)
        delta1 = (delta2 @ self.W2) * (self.z1 > 0)
        dW1 = delta1.T @ X
        db1 = delta1.sum(axis=0)
        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1

    def loss(self, y_onehot):
        return -np.mean(np.sum(
            y_onehot * np.log(self.probs + 1e-8), axis=1))


# --- PyTorch MLP for optimizer comparison ---
class MLP(nn.Module):
    def __init__(self, input_dim=784, hidden_dims=[256, 128],
                 num_classes=10):
        super().__init__()
        layers = []
        prev = input_dim
        for h in hidden_dims:
            layers += [nn.Linear(prev, h), nn.ReLU()]
            prev = h
        layers.append(nn.Linear(prev, num_classes))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x.view(x.size(0), -1))


if __name__ == '__main__':
    # --- Manual backprop demo ---
    print("=" * 50)
    print("Manual Backpropagation (NumPy)")
    print("=" * 50)
    np.random.seed(42)
    X = np.random.randn(1000, 20)
    y_true = (X[:, 0] + X[:, 1] > 0).astype(int)
    y_oh = np.eye(2)[y_true]

    mlp = ManualMLP(20, 64, 2)
    for epoch in range(100):
        mlp.forward(X)
        if epoch % 20 == 0:
            acc = (mlp.probs.argmax(1) == y_true).mean()
            print(f"Epoch {epoch:3d} | Loss: {mlp.loss(y_oh):.4f} "
                  f"| Acc: {acc:.4f}")
        mlp.backward(X, y_oh, lr=0.1)

    # --- Optimizer comparison ---
    print("\n" + "=" * 50)
    print("Optimizer Comparison on MNIST")
    print("=" * 50)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_data = datasets.MNIST('./data', train=True, download=True,
                                transform=transform)
    test_data = datasets.MNIST('./data', train=False, transform=transform)
    train_loader = DataLoader(train_data, batch_size=128, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=128)

    configs = {
        "SGD":          lambda p: optim.SGD(p, lr=0.01),
        "SGD+Momentum": lambda p: optim.SGD(p, lr=0.01, momentum=0.9),
        "Adam":         lambda p: optim.Adam(p, lr=1e-3),
        "AdamW":        lambda p: optim.AdamW(p, lr=1e-3,
                                              weight_decay=0.01),
    }
    criterion = nn.CrossEntropyLoss()

    for name, opt_fn in configs.items():
        model = MLP().to(DEVICE)
        opt = opt_fn(model.parameters())

        model.train()
        for epoch in range(5):
            for X, y in train_loader:
                X, y = X.to(DEVICE), y.to(DEVICE)
                opt.zero_grad()
                loss = criterion(model(X), y)
                loss.backward()
                opt.step()

        model.eval()
        correct = 0
        with torch.no_grad():
            for X, y in test_loader:
                X, y = X.to(DEVICE), y.to(DEVICE)
                correct += (model(X).argmax(1) == y).sum().item()
        acc = correct / len(test_data)
        print(f"{name:15s} | Test Acc: {acc:.4f}")
