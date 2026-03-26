"""
Chapter 5: Polynomial Interpolation
"""
import numpy as np
from scipy.interpolate import lagrange, CubicSpline
import matplotlib.pyplot as plt

# Lagrange interpolation
x_nodes = np.array([-1, -0.5, 0, 0.5, 1])
f = lambda x: 1 / (1 + 25*x**2)
y_nodes = f(x_nodes)
p = lagrange(x_nodes, y_nodes)

x_fine = np.linspace(-1, 1, 300)
plt.figure(figsize=(10, 5))
plt.plot(x_fine, f(x_fine), 'b-', label='f(x)', lw=2)
plt.plot(x_fine, p(x_fine), 'r--', label=f'Lagrange deg {len(x_nodes)-1}')
plt.plot(x_nodes, y_nodes, 'ko', markersize=8)
plt.legend(); plt.title("Lagrange Interpolation")
plt.savefig("ch05_lagrange.pdf"); plt.show()

# Chebyshev nodes
n = 15
cheb = np.cos((2*np.arange(n+1)+1)/(2*(n+1))*np.pi)
y_cheb = f(cheb)
p_cheb = lagrange(cheb, y_cheb)

equi = np.linspace(-1, 1, n+1)
p_equi = lagrange(equi, f(equi))

err_equi = np.max(np.abs(f(x_fine) - p_equi(x_fine)))
err_cheb = np.max(np.abs(f(x_fine) - p_cheb(x_fine)))
print(f"Error equidistant (n={n}): {err_equi:.4f}")
print(f"Error Chebyshev   (n={n}): {err_cheb:.6f}")

# Cubic spline
cs = CubicSpline(x_nodes, y_nodes)
print(f"Spline at 0.25: {cs(0.25):.6f}, exact: {f(0.25):.6f}")

# Newton divided differences
def divided_diff(x, y):
    n = len(x)
    F = y.copy().astype(float)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            F[i] = (F[i] - F[i-1]) / (x[i] - x[i-j])
    return F

coeffs = divided_diff(x_nodes, y_nodes)
print(f"Newton coefficients: {coeffs}")
