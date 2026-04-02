"""
Chapter 1: Getting Started with Julia
======================================
All code examples from Chapter 1 of the Julia programming course.
Covers: REPL usage, package management, first programs, Pluto notebooks,
IJulia, and Unicode support.
"""

# ============================================================
# Section: Package management with Pkg
# ============================================================

using Pkg

# Install a package
# Pkg.add("DataFrames")

# Install multiple packages at once
# Pkg.add(["CSV", "Plots", "BenchmarkTools"])

# Update all packages
# Pkg.update()

# Check installed packages
Pkg.status()

# Create a project environment (recommended for reproducibility)
# Pkg.activate("MyProject")
# Pkg.add("DataFrames")
# This creates Project.toml and Manifest.toml

# ============================================================
# Section: Your first Julia program
# ============================================================

# Variables
name = "Julia"
year = 2012
age = 2026 - year

println("Hello from $name!")
println("Julia is $age years old and faster than ever.")

# A simple computation
function fibonacci(n)
    n <= 1 && return n
    a, b = 0, 1
    for _ in 2:n
        a, b = b, a + b
    end
    return b
end

# Print the first 15 Fibonacci numbers
for i in 0:14
    println("F($i) = $(fibonacci(i))")
end

# ============================================================
# Section: Pluto notebooks
# ============================================================

# Install and launch Pluto (uncomment to run)
# using Pkg
# Pkg.add("Pluto")
# using Pluto
# Pluto.run()   # opens a browser tab at localhost:1234

# Inside a Pluto notebook, each cell contains one expression:
x = 42
y = x^2 + 1
println("The value of y is $(y)")

# ============================================================
# Section: IJulia and Jupyter
# ============================================================

# using Pkg
# Pkg.add("IJulia")
# using IJulia
# notebook()   # opens Jupyter in the browser with Julia kernel

# ============================================================
# Section: Unicode in Julia
# ============================================================

# Type \alpha then press Tab to get α
α = 0.05
β = 1 - α
println("α = $α, β = $β")

# Type \sqrt then Tab to get √
√2 = √(2)    # equivalent to sqrt(2)
println("√2 = $√2")

# Greek letters in functions
function Δ(a, b, c)
    return b^2 - 4a*c
end
println("Discriminant of x² + 5x + 6: $(Δ(1, 5, 6))")

# Matrix operations with Unicode
A = [1 2; 3 4]
x⃗ = [5, 6]
result = A * x⃗
println("A * x⃗ = $result")

# ============================================================
# Section: REPL computations (exercises)
# ============================================================

println("\n--- Exercise computations ---")
println("√(2^10 + 3^10) = $(sqrt(2^10 + 3^10))")
println("∑(1/k² for k=1:100) = $(sum(1/k^2 for k in 1:100))")
println("π²/6 ≈ $(π^2/6)")

# Collatz sequence exercise
function collatz(n)
    steps = 0
    while n != 1
        n = iseven(n) ? n ÷ 2 : 3n + 1
        steps += 1
    end
    return steps
end
println("Collatz steps for n=27: $(collatz(27))")
