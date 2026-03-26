"""
Chapter 3: Control Flow — Conditions and Loops
"""
import math

# === if/elif/else ===
temperature = 25
if temperature < 0:
    print("Ice (solid)")
elif temperature < 100:
    print("Water (liquid)")
else:
    print("Steam (gas)")

# === for loop ===
print("\n--- Squares ---")
for n in range(1, 11):
    print(f"{n}² = {n**2}")

# === while loop: convergence ===
print("\n--- Square root by Newton's method ---")
S = 2.0
x = S
for i in range(10):
    x = 0.5 * (x + S / x)
    print(f"Iteration {i+1}: sqrt(2) ≈ {x:.10f}")
print(f"math.sqrt(2) = {math.sqrt(2):.10f}")

# === Nested loops: multiplication table ===
print("\n--- Multiplication Table ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# === Radioactive decay simulation ===
print("\n--- Radioactive Decay ---")
N0 = 1000
half_life = 5.0  # years
for t in range(0, 31, 5):
    N = N0 * (0.5 ** (t / half_life))
    print(f"t = {t:2d} years: N = {N:.0f}")
