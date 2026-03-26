"""
Chapter 8: Generative Adversarial Networks
DCGAN on MNIST
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
LATENT_DIM = 64
BATCH_SIZE = 128
EPOCHS = 20


class Generator(nn.Module):
    def __init__(self, latent_dim=LATENT_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.BatchNorm1d(256), nn.ReLU(),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512), nn.ReLU(),
            nn.Linear(512, 1024),
            nn.BatchNorm1d(1024), nn.ReLU(),
            nn.Linear(1024, 784),
            nn.Tanh(),
        )

    def forward(self, z):
        return self.net(z).view(-1, 1, 28, 28)


class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 512), nn.LeakyReLU(0.2),
            nn.Linear(512, 256), nn.LeakyReLU(0.2),
            nn.Linear(256, 1), nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x.view(x.size(0), -1))


if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    train_data = datasets.MNIST('./data', train=True, download=True,
                                transform=transform)
    loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)

    G = Generator().to(DEVICE)
    D = Discriminator().to(DEVICE)
    opt_G = optim.Adam(G.parameters(), lr=2e-4, betas=(0.5, 0.999))
    opt_D = optim.Adam(D.parameters(), lr=2e-4, betas=(0.5, 0.999))
    criterion = nn.BCELoss()

    for epoch in range(1, EPOCHS + 1):
        d_loss_total, g_loss_total = 0, 0
        for real, _ in loader:
            B = real.size(0)
            real = real.to(DEVICE)

            # Train Discriminator
            z = torch.randn(B, LATENT_DIM, device=DEVICE)
            fake = G(z).detach()
            d_real = D(real)
            d_fake = D(fake)
            d_loss = (criterion(d_real, torch.ones_like(d_real))
                      + criterion(d_fake, torch.zeros_like(d_fake))) / 2
            opt_D.zero_grad()
            d_loss.backward()
            opt_D.step()

            # Train Generator
            z = torch.randn(B, LATENT_DIM, device=DEVICE)
            fake = G(z)
            g_loss = criterion(D(fake), torch.ones(B, 1, device=DEVICE))
            opt_G.zero_grad()
            g_loss.backward()
            opt_G.step()

            d_loss_total += d_loss.item()
            g_loss_total += g_loss.item()

        n_batches = len(loader)
        print(f"Epoch {epoch:2d} | D_loss: {d_loss_total/n_batches:.4f} "
              f"| G_loss: {g_loss_total/n_batches:.4f}")
