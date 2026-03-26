"""
Chapter 5: Data Structures — Lists, Tuples, Dictionaries
"""

# === Lists ===
temperatures = [20.1, 21.3, 19.8, 22.5, 20.9]
print(f"Temperatures: {temperatures}")
print(f"First: {temperatures[0]}, Last: {temperatures[-1]}")
print(f"Length: {len(temperatures)}")
print(f"Mean: {sum(temperatures)/len(temperatures):.1f}")

temperatures.append(23.1)
print(f"After append: {temperatures}")

# Slicing
print(f"First 3: {temperatures[:3]}")
print(f"Last 2:  {temperatures[-2:]}")

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

even = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers: {even}")

# === Tuples ===
point = (3.0, 4.0)
print(f"Point: {point}, x={point[0]}, y={point[1]}")

# === Dictionaries ===
hydrogen = {
    "symbol": "H",
    "atomic_number": 1,
    "atomic_mass": 1.008,
    "electronegativity": 2.20
}
print(f"Hydrogen: {hydrogen}")
print(f"Mass: {hydrogen['atomic_mass']} u")

# Periodic table
periodic = {
    "H":  {"Z": 1,  "mass": 1.008},
    "He": {"Z": 2,  "mass": 4.003},
    "C":  {"Z": 6,  "mass": 12.011},
    "O":  {"Z": 8,  "mass": 15.999},
}
for sym, info in periodic.items():
    print(f"{sym}: Z={info['Z']}, mass={info['mass']} u")

# === Sets ===
primes = {2, 3, 5, 7, 11, 13}
evens = {2, 4, 6, 8, 10, 12}
print(f"Primes ∩ Evens: {primes & evens}")
print(f"Primes ∪ Evens: {primes | evens}")
