"""
Chapter 3: Direct Methods for Linear Systems
"""
import numpy as np
from scipy.linalg import lu, cholesky, solve_triangular
import time

# LU factorization
A = np.array([[2., 1, 1], [4, 3, 3], [8, 7, 9]])
b = np.array([4., 10, 24])
P, L, U = lu(A)
y = solve_triangular(L, P @ b, lower=True)
x = solve_triangular(U, y)
print(f"LU: x = {x}")

# Cholesky
A_spd = np.array([[4., 2], [2, 5]])
b_spd = np.array([8., 9])
L_chol = cholesky(A_spd, lower=True)
y = solve_triangular(L_chol, b_spd, lower=True)
x = solve_triangular(L_chol.T, y)
print(f"Cholesky: x = {x}")
print(f"L = \n{L_chol}")

# Cost comparison
print("\n=== LU vs Cholesky timing ===")
for n in [100, 500, 1000]:
    M = np.random.randn(n, n)
    A_sym = M @ M.T + n * np.eye(n)
    b_test = np.random.randn(n)

    t0 = time.time()
    for _ in range(5):
        np.linalg.solve(A_sym, b_test)
    t_lu = (time.time() - t0) / 5

    t0 = time.time()
    for _ in range(5):
        L_test = cholesky(A_sym, lower=True)
        y_test = solve_triangular(L_test, b_test, lower=True)
        solve_triangular(L_test.T, y_test)
    t_chol = (time.time() - t0) / 5

    print(f"  n={n:4d}: LU={t_lu:.4f}s, Cholesky={t_chol:.4f}s, ratio={t_lu/t_chol:.2f}")
