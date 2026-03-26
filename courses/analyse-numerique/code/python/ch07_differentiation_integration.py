"""
Chapter 7: Numerical Differentiation and Integration
"""
import numpy as np

def trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b - a) / n
    return h * (f(a)/2 + np.sum(f(x[1:-1])) + f(b)/2)

def simpson(f, a, b, n):
    assert n % 2 == 0
    x = np.linspace(a, b, n+1)
    h = (b - a) / n
    return h/3 * (f(a) + 4*np.sum(f(x[1::2])) + 2*np.sum(f(x[2:-1:2])) + f(b))

f = lambda x: np.exp(-x**2)
exact = 0.7468241328124271  # scipy.integrate.quad

print("=== Convergence table ===")
print(f"{'n':>5} {'Trapezoidal':>15} {'Simpson':>15} {'Err_T':>12} {'Err_S':>12}")
for n in [2, 4, 8, 16, 32]:
    T = trapezoidal(f, 0, 1, n)
    S = simpson(f, 0, 1, n)
    print(f"{n:5d} {T:15.10f} {S:15.10f} {abs(T-exact):12.2e} {abs(S-exact):12.2e}")

# Finite differences
print("\n=== Finite differences ===")
g = lambda x: np.sin(x)
x0 = 1.0
exact_deriv = np.cos(x0)
for h in [1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]:
    forward = (g(x0+h) - g(x0)) / h
    centered = (g(x0+h) - g(x0-h)) / (2*h)
    print(f"h={h:.0e}: forward err={abs(forward-exact_deriv):.2e}, "
          f"centered err={abs(centered-exact_deriv):.2e}")
