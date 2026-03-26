"""
Chapter 10: Diffusion Models
Simple DDPM on MNIST
"""
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import math

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
BATCH_SIZE = 128
EPOCHS = 20
T = 1000  # Number of diffusion steps


def linear_beta_schedule(T, beta_start=1e-4, beta_end=0.02):
    return torch.linspace(beta_start, beta_end, T)


class SinusoidalPosEmb(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, t):
        half = self.dim // 2
        emb = math.log(10000) / (half - 1)
        emb = torch.exp(torch.arange(half, device=t.device) * -emb)
        emb = t[:, None].float() * emb[None, :]
        return torch.cat([emb.sin(), emb.cos()], dim=-1)


class SimpleDenoiser(nn.Module):
    """Simple MLP denoiser for flattened MNIST images."""
    def __init__(self, img_dim=784, time_dim=128, hidden=512):
        super().__init__()
        self.time_embed = nn.Sequential(
            SinusoidalPosEmb(time_dim),
            nn.Linear(time_dim, hidden), nn.GELU(),
        )
        self.net = nn.Sequential(
            nn.Linear(img_dim + hidden, hidden), nn.GELU(),
            nn.Linear(hidden, hidden), nn.GELU(),
            nn.Linear(hidden, hidden), nn.GELU(),
            nn.Linear(hidden, img_dim),
        )

    def forward(self, x, t):
        t_emb = self.time_embed(t)
        x_flat = x.view(x.size(0), -1)
        return self.net(torch.cat([x_flat, t_emb], dim=1)).view_as(x)


class DDPM:
    def __init__(self, model, T=1000, device='cpu'):
        self.model = model
        self.T = T
        self.device = device
        betas = linear_beta_schedule(T).to(device)
        self.betas = betas
        self.alphas = 1.0 - betas
        self.alpha_bar = torch.cumprod(self.alphas, dim=0)

    def q_sample(self, x0, t, noise=None):
        """Forward diffusion: sample x_t given x_0."""
        if noise is None:
            noise = torch.randn_like(x0)
        ab = self.alpha_bar[t]
        while ab.dim() < x0.dim():
            ab = ab.unsqueeze(-1)
        return ab.sqrt() * x0 + (1 - ab).sqrt() * noise

    def train_step(self, x0):
        t = torch.randint(0, self.T, (x0.size(0),), device=self.device)
        noise = torch.randn_like(x0)
        x_t = self.q_sample(x0, t, noise)
        pred_noise = self.model(x_t, t)
        return F.mse_loss(pred_noise, noise.view_as(pred_noise))

    @torch.no_grad()
    def sample(self, shape):
        x = torch.randn(shape, device=self.device)
        for t in reversed(range(self.T)):
            t_batch = torch.full((shape[0],), t,
                                 device=self.device, dtype=torch.long)
            pred = self.model(x, t_batch)
            alpha = self.alphas[t]
            alpha_bar = self.alpha_bar[t]
            x = (1 / alpha.sqrt()) * (
                x - (1 - alpha) / (1 - alpha_bar).sqrt() * pred)
            if t > 0:
                x += self.betas[t].sqrt() * torch.randn_like(x)
        return x


if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    train_data = datasets.MNIST('./data', train=True, download=True,
                                transform=transform)
    loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)

    model = SimpleDenoiser().to(DEVICE)
    ddpm = DDPM(model, T=T, device=DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    for epoch in range(1, EPOCHS + 1):
        total_loss = 0
        for x, _ in loader:
            x = x.to(DEVICE)
            loss = ddpm.train_step(x)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * x.size(0)
        print(f"Epoch {epoch:2d} | Loss: {total_loss/len(train_data):.6f}")

    # Generate samples
    samples = ddpm.sample((16, 1, 28, 28))
    print(f"Generated {samples.shape[0]} samples")
