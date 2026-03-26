"""
Chapter 9: Variational Autoencoders
VAE on MNIST
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
LATENT_DIM = 16
BATCH_SIZE = 128
EPOCHS = 20


class VAE(nn.Module):
    def __init__(self, latent_dim=LATENT_DIM):
        super().__init__()
        self.latent_dim = latent_dim
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(784, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256), nn.ReLU(),
            nn.Linear(256, 512), nn.ReLU(),
            nn.Linear(512, 784), nn.Sigmoid(),
        )

    def encode(self, x):
        h = self.encoder(x.view(-1, 784))
        return self.fc_mu(h), self.fc_logvar(h)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z):
        return self.decoder(z).view(-1, 1, 28, 28)

    def forward(self, x):
        mu, logvar = self.encode(x)
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar


def vae_loss(recon_x, x, mu, logvar, beta=1.0):
    recon = F.binary_cross_entropy(
        recon_x.view(-1, 784), x.view(-1, 784), reduction='sum')
    kl = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon + beta * kl


if __name__ == '__main__':
    transform = transforms.Compose([transforms.ToTensor()])
    train_data = datasets.MNIST('./data', train=True, download=True,
                                transform=transform)
    loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)

    model = VAE().to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0
        for x, _ in loader:
            x = x.to(DEVICE)
            recon, mu, logvar = model(x)
            loss = vae_loss(recon, x, mu, logvar)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_data)
        print(f"Epoch {epoch:2d} | Loss: {avg_loss:.2f}")

    # Generate samples
    model.eval()
    with torch.no_grad():
        z = torch.randn(16, LATENT_DIM, device=DEVICE)
        samples = model.decode(z)
        print(f"Generated {samples.shape[0]} samples of shape "
              f"{samples.shape[1:]}")
