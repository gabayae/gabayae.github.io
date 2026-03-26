"""
Chapter 8: Gaussian Quadrature
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def gauss_legendre(f, a, b, n):
    """Gauss-Legendre quadrature with n points on [a,b]."""
    nodes, weights = leggauss(n)
    x = 0.5*(b-a)*nodes + 0.5*(a+b)
    w = 0.5*(b-a)*weights
    return np.sum(w * f(x))

f = lambda x: np.exp(-x**2)
exact = 0.7468241328124271

print("=== Gauss-Legendre convergence ===")
for n in [2, 3, 5, 10, 15, 20]:
    approx = gauss_legendre(f, 0, 1, n)
    print(f"n={n:2d}: I={approx:.15f}, error={abs(approx-exact):.2e}")

# Verify exactness for polynomials
print("\n=== Exactness test (x^3 on [0,1]) ===")
g = lambda x: x**3
exact_cubic = 0.25
for n in [2, 3, 5]:
    approx = gauss_legendre(g, 0, 1, n)
    print(f"n={n}: I={approx:.15f}, error={abs(approx-exact_cubic):.2e}")

# Nodes and weights
print("\n=== Nodes and weights ===")
for n in [1, 2, 3]:
    nodes, weights = leggauss(n)
    print(f"n={n}: nodes={nodes}, weights={weights}")
