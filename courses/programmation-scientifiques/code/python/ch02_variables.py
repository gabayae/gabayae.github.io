"""
Chapter 2: Variables, Types, and Basic Operations
"""

# Variables
mass = 75.0
age = 20
name = "Alice"
is_student = True
print(f"Name: {name}, Age: {age}, Mass: {mass} kg, Student: {is_student}")

# Types
print(type(42), type(3.14), type("hello"), type(True))

# Scientific notation
c = 2.998e8
h = 6.626e-34
Na = 6.022e23
G = 6.674e-11
print(f"c = {c}, h = {h}, Na = {Na}, G = {G}")

# Type conversion
print(float(42), int(3.99), int("25"), float("3.14"))

# Strings
first, last = "Marie", "Curie"
full = first + " " + last
print(full, len(full), full[0], full[-1])
print(full.upper(), full.lower())

# f-strings
pi = 3.141592653589793
print(f"pi = {pi:.2f}, {pi:.6f}, {pi:.2e}")

# Comparisons
x = 10
print(x > 5, x == 10, x != 7, x >= 15)

# Atom identity card
element, symbol, Z = "Carbon", "C", 6
mass_a, eneg = 12.011, 2.55
print("=" * 35)
print(f"  IDENTITY CARD: {element}")
print("=" * 35)
print(f"  Symbol: {symbol}, Z: {Z}, Mass: {mass_a} u, EN: {eneg}")
print("=" * 35)
