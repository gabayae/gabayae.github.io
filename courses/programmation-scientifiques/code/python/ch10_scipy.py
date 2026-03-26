"""
Chapter 10: Scientific Computing with SciPy
"""
import numpy as np
from scipy import optimize, integrate, linalg, stats, interpolate

# === Curve fitting ===
np.random.seed(42)
t_data = np.linspace(0, 5, 20)
y_data = 3.0 * np.exp(-0.5 * t_data) + np.random.normal(0, 0.1, 20)

def exp_decay(t, A, k):
    return A * np.exp(-k * t)

popt, pcov = optimize.curve_fit(exp_decay, t_data, y_data)
print(f"Curve fit: A = {popt[0]:.3f}, k = {popt[1]:.3f}")

# === Numerical integration ===
result, error = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(f"\n∫₀^π sin(x) dx = {result:.6f} (error: {error:.2e})")

result2, _ = integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(f"∫₋∞^∞ exp(-x²) dx = {result2:.6f} (√π = {np.sqrt(np.pi):.6f})")

# === Linear algebra ===
A = np.array([[2, 1], [5, 3]])
b = np.array([4, 7])
x = linalg.solve(A, b)
print(f"\nSolve Ax=b: x = {x}")

eigenvalues, eigenvectors = linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")

# === Statistics ===
data = np.random.normal(170, 10, 100)
stat, p_value = stats.shapiro(data)
print(f"\nShapiro-Wilk test: p = {p_value:.4f}")

t_stat, p_val = stats.ttest_1samp(data, 170)
print(f"t-test (μ=170): t = {t_stat:.3f}, p = {p_val:.4f}")

# === Interpolation ===
x_pts = np.array([0, 1, 2, 3, 4, 5])
y_pts = np.array([0, 0.8, 0.9, 0.1, -0.8, -1.0])
f_interp = interpolate.interp1d(x_pts, y_pts, kind='cubic')
x_fine = np.linspace(0, 5, 50)
y_fine = f_interp(x_fine)
print(f"\nInterpolated f(2.5) = {f_interp(2.5):.4f}")
