"""
Chapter 1: Floating-Point Arithmetic, Errors, and Stability
"""
import numpy as np

# Machine epsilon
eps = np.finfo(float).eps
print(f"eps_mach = {eps}")  # 2.220446049250313e-16

# Catastrophic cancellation
x = 1e-8
f_bad = (1 - np.cos(x)) / x**2
f_good = 2 * np.sin(x/2)**2 / x**2
print(f"Bad formula : {f_bad}")   # 0.0
print(f"Good formula: {f_good}")  # 0.49999999...

# Condition number of a matrix
A = np.array([[1, 1], [1, 1.0001]])
print(f"cond(A) = {np.linalg.cond(A):.1f}")  # ~40000

# Hilbert matrix conditioning
print("\nHilbert matrix conditioning:")
for n in range(2, 16):
    H = np.array([[1.0/(i+j+1) for j in range(n)] for i in range(n)])
    print(f"  n={n:2d}: cond(H) = {np.linalg.cond(H):.2e}")

# Computing eps_mach by bisection
e = 1.0
while 1.0 + e > 1.0:
    e /= 2
e *= 2
print(f"\neps_mach (computed) = {e}")
print(f"eps_mach (numpy)    = {eps}")
