"""
Chapter 10: Eigenvalues and Eigenvectors
"""
import numpy as np

def power_iteration(A, x0=None, tol=1e-10, maxiter=1000):
    n = A.shape[0]
    x = x0 if x0 is not None else np.random.randn(n)
    x = x / np.linalg.norm(x)
    lam_old = 0
    for k in range(maxiter):
        w = A @ x
        x = w / np.linalg.norm(w)
        lam = x @ A @ x  # Rayleigh quotient
        if abs(lam - lam_old) < tol:
            return lam, x, k+1
        lam_old = lam
    return lam, x, maxiter

def inverse_iteration(A, mu=0, x0=None, tol=1e-10, maxiter=1000):
    n = A.shape[0]
    x = x0 if x0 is not None else np.random.randn(n)
    x = x / np.linalg.norm(x)
    B = A - mu * np.eye(n)
    lam_old = 0
    for k in range(maxiter):
        w = np.linalg.solve(B, x)
        x = w / np.linalg.norm(w)
        lam = x @ A @ x
        if abs(lam - lam_old) < tol:
            return lam, x, k+1
        lam_old = lam
    return lam, x, maxiter

def qr_algorithm(A, maxiter=100):
    Ak = A.astype(float).copy()
    for k in range(maxiter):
        Q, R = np.linalg.qr(Ak)
        Ak = R @ Q
        off = np.sum(np.abs(np.tril(Ak, -1)))
        if off < 1e-12:
            break
    return np.diag(Ak)

# Test
A = np.array([[4, 1, 0],
              [1, 3, 1],
              [0, 1, 2]], dtype=float)

print("=== Power iteration ===")
lam1, v1, n_iter = power_iteration(A)
print(f"lambda_1 = {lam1:.6f} ({n_iter} iterations)")

print("\n=== Inverse iteration (shift mu=1.5) ===")
lam_inv, v_inv, n_iter = inverse_iteration(A, mu=1.5)
print(f"Closest eigenvalue to 1.5: {lam_inv:.6f} ({n_iter} iterations)")

print("\n=== QR algorithm ===")
eigenvalues_qr = sorted(qr_algorithm(A), reverse=True)
print(f"QR eigenvalues: {eigenvalues_qr}")

print("\n=== numpy.linalg.eig ===")
evals = sorted(np.linalg.eig(A)[0], reverse=True)
print(f"numpy eigenvalues: {evals}")

# SVD
print("\n=== SVD ===")
B = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)
U, s, Vt = np.linalg.svd(B)
print(f"Singular values: {s}")
print(f"cond(B) = {s[0]/s[-1]:.4f}")
print(f"rank(B) = {np.sum(s > 1e-10)}")

# Gerschgorin discs
print("\n=== Gerschgorin discs ===")
for i in range(A.shape[0]):
    center = A[i, i]
    radius = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
    print(f"D_{i+1}: center={center:.1f}, radius={radius:.1f}")
