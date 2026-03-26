"""
Chapter 4: Iterative Methods for Linear Systems
"""
import numpy as np

def jacobi(A, b, x0, tol=1e-10, maxiter=1000):
    D = np.diag(np.diag(A))
    R = A - D
    x = x0.copy()
    for k in range(maxiter):
        x_new = np.linalg.solve(D, b - R @ x)
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k+1
        x = x_new
    return x, maxiter

def gauss_seidel(A, b, x0, tol=1e-10, maxiter=1000):
    n = len(b)
    x = x0.copy()
    for k in range(maxiter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - A[i,:i] @ x[:i] - A[i,i+1:] @ x_old[i+1:]) / A[i,i]
        if np.linalg.norm(x - x_old) < tol:
            return x, k+1
    return x, maxiter

def sor(A, b, x0, omega=1.5, tol=1e-10, maxiter=1000):
    n = len(b)
    x = x0.copy()
    for k in range(maxiter):
        x_old = x.copy()
        for i in range(n):
            gs = (b[i] - A[i,:i] @ x[:i] - A[i,i+1:] @ x_old[i+1:]) / A[i,i]
            x[i] = (1 - omega) * x_old[i] + omega * gs
        if np.linalg.norm(x - x_old) < tol:
            return x, k+1
    return x, maxiter

def conjugate_gradient(A, b, x0, tol=1e-10, maxiter=1000):
    x = x0.copy()
    r = b - A @ x
    p = r.copy()
    rs_old = r @ r
    for k in range(maxiter):
        Ap = A @ p
        alpha = rs_old / (p @ Ap)
        x += alpha * p
        r -= alpha * Ap
        rs_new = r @ r
        if np.sqrt(rs_new) < tol:
            return x, k+1
        p = r + (rs_new / rs_old) * p
        rs_old = rs_new
    return x, maxiter

# Test: tridiagonal matrix
n = 100
A = np.diag(2*np.ones(n)) - np.diag(np.ones(n-1), 1) - np.diag(np.ones(n-1), -1)
b = np.ones(n)
x0 = np.zeros(n)

x_j, nj = jacobi(A, b, x0)
x_gs, ngs = gauss_seidel(A, b, x0)
x_sor, nsor = sor(A, b, x0, omega=1.5)
x_cg, ncg = conjugate_gradient(A, b, x0)

print(f"Jacobi:       {nj:4d} iterations")
print(f"Gauss-Seidel: {ngs:4d} iterations")
print(f"SOR (w=1.5):  {nsor:4d} iterations")
print(f"CG:           {ncg:4d} iterations")

# Verify
x_exact = np.linalg.solve(A, b)
print(f"\nMax error Jacobi: {np.max(np.abs(x_j - x_exact)):.2e}")
print(f"Max error CG:     {np.max(np.abs(x_cg - x_exact)):.2e}")
