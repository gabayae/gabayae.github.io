"""
Chapter 11: Theoretical Aspects
Double descent demonstration
"""
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_data(n=100, d=20, noise=0.3):
    """Generate regression data."""
    np.random.seed(42)
    X = np.random.randn(n, d).astype(np.float32)
    w_true = np.random.randn(d).astype(np.float32)
    y = X @ w_true + noise * np.random.randn(n).astype(np.float32)
    return torch.tensor(X), torch.tensor(y)


class FlexibleMLP(nn.Module):
    def __init__(self, d_in, width):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_in, width), nn.ReLU(),
            nn.Linear(width, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


if __name__ == '__main__':
    X_train, y_train = generate_data(n=50, d=20)
    X_test, y_test = generate_data(n=200, d=20)

    widths = [2, 5, 10, 20, 30, 50, 80, 100, 150, 200, 300, 500]
    train_errors = []
    test_errors = []

    for w in widths:
        model = FlexibleMLP(20, w)
        optimizer = optim.Adam(model.parameters(), lr=1e-3)
        criterion = nn.MSELoss()

        # Train to convergence
        for _ in range(2000):
            optimizer.zero_grad()
            criterion(model(X_train), y_train).backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            train_err = criterion(model(X_train), y_train).item()
            test_err = criterion(model(X_test), y_test).item()

        n_params = sum(p.numel() for p in model.parameters())
        train_errors.append(train_err)
        test_errors.append(test_err)
        print(f"Width {w:4d} | Params: {n_params:6d} | "
              f"Train MSE: {train_err:.4f} | Test MSE: {test_err:.4f}")

    # Plot double descent
    plt.figure(figsize=(10, 5))
    plt.plot(widths, train_errors, 'b-o', label='Train MSE')
    plt.plot(widths, test_errors, 'r-o', label='Test MSE')
    plt.axvline(x=50, color='gray', linestyle='--', alpha=0.5,
                label='Interpolation threshold')
    plt.xlabel('Network Width')
    plt.ylabel('MSE')
    plt.title('Double Descent Phenomenon')
    plt.legend()
    plt.yscale('log')
    plt.savefig('double_descent.png', dpi=150, bbox_inches='tight')
    print("Plot saved to double_descent.png")
