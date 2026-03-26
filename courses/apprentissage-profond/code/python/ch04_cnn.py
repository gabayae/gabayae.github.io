"""
Chapter 4: Convolutional Neural Networks
CNN + ResNet on CIFAR-10
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
BATCH_SIZE = 128
EPOCHS = 20


class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
        )
        self.classifier = nn.Linear(128, 10)

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x.view(x.size(0), -1))


class ResBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        return self.relu(out + x)  # Skip connection


class SimpleResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU()
        )
        self.layer1 = nn.Sequential(ResBlock(64), ResBlock(64))
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.layer1(x)
        x = self.pool(x)
        return self.fc(x.view(x.size(0), -1))


if __name__ == '__main__':
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2470, 0.2435, 0.2616)),
    ])
    transform_test = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465),
                             (0.2470, 0.2435, 0.2616)),
    ])
    train_data = datasets.CIFAR10('./data', train=True, download=True,
                                  transform=transform_train)
    test_data = datasets.CIFAR10('./data', train=False,
                                 transform=transform_test)
    train_loader = DataLoader(train_data, batch_size=BATCH_SIZE,
                              shuffle=True)
    test_loader = DataLoader(test_data, batch_size=BATCH_SIZE)

    for ModelClass in [SimpleCNN, SimpleResNet]:
        model = ModelClass().to(DEVICE)
        n_params = sum(p.numel() for p in model.parameters())
        print(f"\n{ModelClass.__name__} ({n_params:,} params)")
        print("-" * 40)

        optimizer = optim.Adam(model.parameters(), lr=1e-3)
        criterion = nn.CrossEntropyLoss()

        for epoch in range(1, EPOCHS + 1):
            model.train()
            for X, y in train_loader:
                X, y = X.to(DEVICE), y.to(DEVICE)
                optimizer.zero_grad()
                criterion(model(X), y).backward()
                optimizer.step()

            if epoch % 5 == 0:
                model.eval()
                correct = 0
                with torch.no_grad():
                    for X, y in test_loader:
                        X, y = X.to(DEVICE), y.to(DEVICE)
                        correct += (model(X).argmax(1) == y).sum().item()
                print(f"Epoch {epoch:2d} | Acc: {correct/len(test_data):.4f}")
