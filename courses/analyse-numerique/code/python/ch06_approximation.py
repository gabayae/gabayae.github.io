"""
Chapter 6: Approximation — Least Squares and Chebyshev
"""
import numpy as np
import matplotlib.pyplot as plt

# Polynomial least squares
np.random.seed(42)
x = np.linspace(0, 5, 50)
y = 2 + 0.5*x + 0.3*x**2 + np.random.normal(0, 1, 50)

for deg in [1, 2, 5]:
    c = np.polyfit(x, y, deg)
    p = np.poly1d(c)
    residual = np.sqrt(np.mean((y - p(x))**2))
    print(f"Degree {deg}: RMSE = {residual:.4f}")

# Normal equations
A = np.column_stack([np.ones_like(x), x, x**2])
c_normal = np.linalg.solve(A.T @ A, A.T @ y)
print(f"Coefficients (normal eq.): {c_normal}")

# Condition number comparison
print(f"cond(A) = {np.linalg.cond(A):.1f}")
print(f"cond(A^T A) = {np.linalg.cond(A.T @ A):.1f}")
print(f"Ratio: {np.linalg.cond(A.T @ A) / np.linalg.cond(A)**2:.4f}")

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, s=10, label='Data')
x_fine = np.linspace(0, 5, 200)
plt.plot(x_fine, np.polyval(np.polyfit(x, y, 2), x_fine), 'r-', label='LS deg 2')
plt.legend(); plt.title("Least Squares Fit")
plt.savefig("ch06_least_squares.pdf"); plt.show()
