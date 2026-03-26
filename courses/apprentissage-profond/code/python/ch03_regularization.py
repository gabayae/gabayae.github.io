"""
Chapter 3: Regularization and Generalization
Dropout, weight decay, batch normalization experiments
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
BATCH_SIZE = 128
EPOCHS = 15


class RegularizedMLP(nn.Module):
    def __init__(self, dropout_rate=0.0, use_batchnorm=False):
        super().__init__()
        layers = []
        dims = [784, 512, 256, 128]
        for i in range(len(dims) - 1):
            layers.append(nn.Linear(dims[i], dims[i + 1]))
            if use_batchnorm:
                layers.append(nn.BatchNorm1d(dims[i + 1]))
            layers.append(nn.ReLU())
            if dropout_rate > 0:
                layers.append(nn.Dropout(dropout_rate))
        layers.append(nn.Linear(128, 10))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x.view(x.size(0), -1))


def train_eval(model, wd=0.0, epochs=EPOCHS):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_data = datasets.MNIST('./data', train=True, download=True,
                                transform=transform)
    test_data = datasets.MNIST('./data', train=False, transform=transform)
    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE,
                              shuffle=True)
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=wd)

    for epoch in range(1, epochs + 1):
        model.train()
        for X, y in train_loader:
            X, y = X.to(DEVICE), y.to(DEVICE)
            optimizer.zero_grad()
            criterion(model(X), y).backward()
            optimizer.step()

    model.eval()
    correct = 0
    with torch.no_grad():
        for X, y in test_loader:
            X, y = X.to(DEVICE), y.to(DEVICE)
            correct += (model(X).argmax(1) == y).sum().item()
    return correct / len(test_data)


if __name__ == '__main__':
    print("Regularization Ablation Study")
    print("=" * 60)

    configs = [
        ("No regularization", 0.0, False, 0.0),
        ("Dropout 0.2",       0.2, False, 0.0),
        ("Dropout 0.5",       0.5, False, 0.0),
        ("BatchNorm",         0.0, True,  0.0),
        ("Weight decay 1e-4", 0.0, False, 1e-4),
        ("All combined",      0.3, True,  1e-4),
    ]

    for name, drop, bn, wd in configs:
        model = RegularizedMLP(dropout_rate=drop,
                               use_batchnorm=bn).to(DEVICE)
        acc = train_eval(model, wd=wd)
        print(f"{name:25s} | Test Acc: {acc:.4f}")
