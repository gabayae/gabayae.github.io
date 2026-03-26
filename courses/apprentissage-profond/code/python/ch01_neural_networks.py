"""
Chapter 1: Artificial Neural Networks — Foundations
MLP implementation and ablation study on MNIST
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# --- Hyperparameters ---
BATCH_SIZE = 128
LR = 1e-3
EPOCHS = 10
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# --- Data ---
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
train_data = datasets.MNIST('./data', train=True, download=True,
                            transform=transform)
test_data = datasets.MNIST('./data', train=False, transform=transform)
train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_data, batch_size=BATCH_SIZE)


# --- MLP Model ---
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


def train_and_eval(model, optimizer, train_loader, test_loader, epochs=10):
    criterion = nn.CrossEntropyLoss()
    history = {'train_loss': [], 'test_acc': []}

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0
        for X, y in train_loader:
            X, y = X.to(DEVICE), y.to(DEVICE)
            optimizer.zero_grad()
            loss = criterion(model(X), y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * X.size(0)

        model.eval()
        correct = 0
        with torch.no_grad():
            for X, y in test_loader:
                X, y = X.to(DEVICE), y.to(DEVICE)
                correct += (model(X).argmax(1) == y).sum().item()

        train_loss = total_loss / len(train_data)
        test_acc = correct / len(test_data)
        history['train_loss'].append(train_loss)
        history['test_acc'].append(test_acc)
        print(f"Epoch {epoch:2d} | Loss: {train_loss:.4f} | "
              f"Test Acc: {test_acc:.4f}")

    return history


if __name__ == '__main__':
    # --- Train default MLP ---
    print("=" * 50)
    print("Training MLP (784, 256, 128, 10) on MNIST")
    print("=" * 50)
    model = MLP().to(DEVICE)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Parameters: {n_params:,}")
    optimizer = optim.Adam(model.parameters(), lr=LR)
    train_and_eval(model, optimizer, train_loader, test_loader, EPOCHS)

    # --- Ablation: architecture comparison ---
    print("\n" + "=" * 50)
    print("Ablation Study: Architecture Comparison")
    print("=" * 50)
    configs = {
        "Shallow-wide":  [1024],
        "2-layers":      [256, 128],
        "3-layers":      [256, 128, 64],
        "Deep-narrow":   [64, 64, 64, 64],
    }
    for name, hidden in configs.items():
        model = MLP(hidden_dims=hidden).to(DEVICE)
        n_params = sum(p.numel() for p in model.parameters())
        opt = optim.Adam(model.parameters(), lr=LR)
        history = train_and_eval(model, opt, train_loader, test_loader, 5)
        print(f"{name:20s} | {n_params:>8,} params | "
              f"Acc: {history['test_acc'][-1]:.4f}\n")
