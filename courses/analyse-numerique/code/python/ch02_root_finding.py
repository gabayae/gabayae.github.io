"""
Chapter 2: Root Finding Methods
"""
import numpy as np

def bisection(f, a, b, tol=1e-12):
    while b - a > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def newton(f, df, x0, tol=1e-12, maxiter=100):
    x = x0
    for i in range(maxiter):
        dx = f(x) / df(x)
        x -= dx
        if abs(dx) < tol:
            return x, i+1
    return x, maxiter

def secant(f, x0, x1, tol=1e-12, maxiter=100):
    for i in range(maxiter):
        fx0, fx1 = f(x0), f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2, i+1
        x0, x1 = x1, x2
    return x1, maxiter

# Test: f(x) = e^x - 3x
f = lambda x: np.exp(x) - 3*x
df = lambda x: np.exp(x) - 3

print("=== Root of e^x - 3x ===")
print(f"Bisection : {bisection(f, 0, 1):.12f}")
x_newton, n = newton(f, df, 2.0)
print(f"Newton    : {x_newton:.12f} ({n} iterations)")
x_sec, n = secant(f, 0.0, 1.0)
print(f"Secant    : {x_sec:.12f} ({n} iterations)")

# Newton convergence table
print("\n=== Newton convergence ===")
x = 2.0
print(f"{'n':>3} {'x_n':>14} {'f(x_n)':>14} {'|x_n - x_{n-1}|':>16}")
print(f"{0:3d} {x:14.6f} {f(x):14.6f} {'---':>16}")
for n in range(1, 10):
    x_old = x
    x = x - f(x) / df(x)
    print(f"{n:3d} {x:14.6f} {f(x):14.6e} {abs(x-x_old):16.6e}")
    if abs(x - x_old) < 1e-14:
        break

# sqrt(2) by Newton
print("\n=== sqrt(2) by Newton ===")
g = lambda x: x**2 - 2
dg = lambda x: 2*x
x_sqrt2, n = newton(g, dg, 1.0)
print(f"sqrt(2) = {x_sqrt2:.15f} ({n} iterations)")
print(f"exact   = {np.sqrt(2):.15f}")
