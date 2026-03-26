"""
Chapter 6: NumPy — Arrays and Numerical Computing
"""
import numpy as np
import time

# === Speed comparison ===
n = 1_000_000
python_list = list(range(n))
numpy_array = np.arange(n)

start = time.time()
result_py = [x**2 for x in python_list]
t_py = time.time() - start

start = time.time()
result_np = numpy_array ** 2
t_np = time.time() - start

print(f"Python list: {t_py:.4f} s")
print(f"NumPy array: {t_np:.4f} s")
print(f"Speedup: {t_py/t_np:.0f}x")

# === Array creation ===
a = np.array([1, 2, 3, 4, 5])
print(f"\nArray: {a}, dtype: {a.dtype}, shape: {a.shape}")

zeros = np.zeros(5)
ones = np.ones((2, 3))
linsp = np.linspace(0, 1, 5)
print(f"Zeros: {zeros}")
print(f"Ones:\n{ones}")
print(f"Linspace: {linsp}")

# === Operations ===
x = np.array([1.0, 2.0, 3.0, 4.0])
print(f"\nx = {x}")
print(f"x + 10 = {x + 10}")
print(f"x * 2 = {x * 2}")
print(f"x ** 2 = {x ** 2}")
print(f"sqrt(x) = {np.sqrt(x)}")

# === Math functions ===
t = np.linspace(0, 2*np.pi, 8)
print(f"\nsin(t) = {np.sin(t).round(3)}")
print(f"cos(t) = {np.cos(t).round(3)}")

# === Statistics ===
data = np.random.normal(170, 10, 1000)  # heights
print(f"\nMean: {np.mean(data):.1f}")
print(f"Std:  {np.std(data):.1f}")
print(f"Min:  {np.min(data):.1f}")
print(f"Max:  {np.max(data):.1f}")

# === Monte Carlo pi ===
np.random.seed(42)
N = 1_000_000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
inside = np.sum(x**2 + y**2 <= 1)
pi_est = 4 * inside / N
print(f"\nMonte Carlo pi ({N} points): {pi_est:.6f}")
print(f"True pi: {np.pi:.6f}")
print(f"Error: {abs(pi_est - np.pi):.6f}")
