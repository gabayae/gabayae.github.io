"""
Chapter 4: Functions and Scope
"""
import math

# === Basic function ===
def kinetic_energy(mass, velocity):
    """Compute kinetic energy E = 0.5 * m * v²."""
    return 0.5 * mass * velocity ** 2

print(f"Ek = {kinetic_energy(75.0, 10.0)} J")

# === Gravitational force ===
def gravitational_force(m1, m2, r):
    """Compute gravitational force F = G * m1 * m2 / r²."""
    G = 6.674e-11
    return G * m1 * m2 / r ** 2

F = gravitational_force(5.972e24, 7.342e22, 3.844e8)
print(f"Earth-Moon force: {F:.3e} N")

# === Default arguments ===
def falling_distance(t, g=9.81):
    """Distance fallen in time t under gravity g."""
    return 0.5 * g * t ** 2

print(f"Earth: {falling_distance(3.0):.2f} m")
print(f"Moon:  {falling_distance(3.0, g=1.62):.2f} m")

# === Multiple returns ===
def quadratic(a, b, c):
    """Solve ax² + bx + c = 0."""
    delta = b**2 - 4*a*c
    if delta < 0:
        return None, None
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

x1, x2 = quadratic(1, -5, 6)
print(f"x² - 5x + 6 = 0: x1 = {x1}, x2 = {x2}")

# === Lambda ===
square = lambda x: x ** 2
print(f"square(7) = {square(7)}")
