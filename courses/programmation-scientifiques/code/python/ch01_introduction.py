"""
Chapter 1: Introduction to Programming
"""

# First program
print("Hello, future scientist!")

# Python as a calculator
print(3 + 5)
print(10 - 4)
print(6 * 7)
print(15 / 4)
print(15 // 4)
print(15 % 4)
print(2 ** 10)

# Speed of light
c = 299792458
print(f"Speed of light: {c} m/s")

# Kinetic energy
mass = 75.0
velocity = 10.0
Ek = 0.5 * mass * velocity ** 2
print(f"Mass: {mass} kg, Velocity: {velocity} m/s, Energy: {Ek} J")

# Temperature conversion
celsius = 100
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C = {fahrenheit}°F")

fahrenheit = 72
celsius = (5/9) * (fahrenheit - 32)
print(f"{fahrenheit}°F = {celsius:.1f}°C")

print("\n--- Conversion Table ---")
print(f"{'°C':>6}  {'°F':>6}")
for c in range(0, 101, 10):
    f = (9/5) * c + 32
    print(f"{c:>6}  {f:>6.1f}")
