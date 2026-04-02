"""
Chapter 2: Types, Variables, and Control Flow
==============================================
All code examples from Chapter 2 of the Julia programming course.
Covers: primitive types, variables, type hierarchy, strings,
conditionals, loops, comprehensions, tuples, Nothing/Missing.
"""

# ============================================================
# Section: Primitive types
# ============================================================

println("=== Primitive Types ===")

# Integers
x = 42              # Int64 (on 64-bit systems)
y = Int32(42)       # explicitly 32-bit
big_int = Int128(10)^30 # 128-bit integer
huge = big"999999999999999999999999999999999"  # BigInt (arbitrary precision)

println("typeof(42) = $(typeof(x))")
println("sizeof(42) = $(sizeof(x)) bytes")

# Floating-point
a = 3.14            # Float64 (double precision)
b = Float32(3.14)   # single precision
c = BigFloat(π)     # arbitrary precision

println("typeof(3.14) = $(typeof(a))")
println("BigFloat(π) = $c")

# Boolean
flag = true         # Bool (subtype of Integer)
println("true + 1 = $(flag + 1)")

# Characters and strings
ch = 'α'            # Char (Unicode character, 4 bytes)
s = "Hello, Julia"  # String (UTF-8 encoded)
println("typeof('α') = $(typeof(ch))")
println("typeof(\"Hello\") = $(typeof(s))")

# ============================================================
# Section: Variables and assignment
# ============================================================

println("\n=== Variables and Assignment ===")

x = 10        # x refers to an Int64
x = "hello"   # now x refers to a String -- no error
println("x is now: $x ($(typeof(x)))")

# Multiple assignment
a, b, c = 1, 2.0, "three"
println("a=$a, b=$b, c=$c")

# Swap without a temporary variable
a, b = b, a
println("After swap: a=$a, b=$b")

# Constants
const SPEED_OF_LIGHT = 299_792_458  # underscores for readability
const π_approx = 355 // 113        # Rational{Int64}
println("Speed of light: $SPEED_OF_LIGHT")
println("π ≈ $π_approx = $(Float64(π_approx))")

# ============================================================
# Section: The type hierarchy
# ============================================================

println("\n=== Type Hierarchy ===")

# Abstract types
abstract type Shape end

# Concrete types
struct Circle <: Shape
    radius::Float64
end

struct Rectangle <: Shape
    width::Float64
    height::Float64
end

# Check type relationships
println("Circle <: Shape = $(Circle <: Shape)")
println("Circle <: Any = $(Circle <: Any)")
println("Int64 <: Number = $(Int64 <: Number)")
println("String <: Number = $(String <: Number)")

# Useful introspection
println("subtypes(Integer) = $(subtypes(Integer))")
println("supertype(Float64) = $(supertype(Float64))")

# ============================================================
# Section: Strings
# ============================================================

println("\n=== Strings ===")

s = "Julia is fast"
println("length(\"$s\") = $(length(s))")
println("sizeof(\"$s\") = $(sizeof(s))")
println("s[1] = '$(s[1])'")
println("s[end] = '$(s[end])'")
println("s[1:5] = \"$(s[1:5])\"")

# String interpolation
name = "World"
greeting = "Hello, $name!"
computation = "2 + 3 = $(2 + 3)"
println(greeting)
println(computation)

# Multi-line strings
poem = """
    Roses are red,
    Julia is fast,
    Python is nice,
    but C won't last.
    """
println(poem)

# Common operations
println("uppercase(\"julia\") = $(uppercase("julia"))")
println("replace(\"Hello\", 'l'=>'r') = $(replace("Hello", "l" => "r"))")
println("split(\"a,b,c,d\", ',') = $(split("a,b,c,d", ","))")
println("join([\"one\",\"two\",\"three\"], \" + \") = $(join(["one", "two", "three"], " + "))")
println("occursin(\"fast\", \"Julia is fast\") = $(occursin("fast", "Julia is fast"))")

# Regular expressions
m = match(r"(\d+)\s*kg", "Weight: 82 kg")
println("Regex capture: $(m.captures[1])")

# ============================================================
# Section: Control flow -- conditionals
# ============================================================

println("\n=== Conditionals ===")

temperature = 38.5

if temperature >= 39.0
    status = "high fever"
elseif temperature >= 37.5
    status = "low-grade fever"
else
    status = "normal"
end
println("Temperature $temperature°C → Status: $status")

# Ternary operator
status = temperature >= 37.5 ? "fever" : "normal"
println("Ternary: $status")

# Short-circuit evaluation
x = 5
x > 0 && println("x is positive (short-circuit &&)")

# ============================================================
# Section: Control flow -- loops
# ============================================================

println("\n=== Loops ===")

# for loops with ranges
for i in 1:5
    println("Iteration $i")
end

# Iterating over collections
fruits = ["apple", "banana", "cherry"]
for fruit in fruits
    println(fruit)
end

# Enumerate (index + value)
for (i, fruit) in enumerate(fruits)
    println("$i: $fruit")
end

# Nested loops with a single for
for i in 1:3, j in 1:3
    i == j && println("($i, $j) is on the diagonal")
end

# while loop
n = 1
while n <= 1000
    n *= 2
end
println("First power of 2 above 1000: $n")

# break and continue
println("Multiples of 7 up to 50:")
for i in 1:100
    i % 7 != 0 && continue
    i > 50 && break
    println(i)
end

# ============================================================
# Section: Comprehensions
# ============================================================

println("\n=== Comprehensions ===")

# Array comprehension
squares = [x^2 for x in 1:10]
println("Squares: $squares")

# With a filter
even_squares = [x^2 for x in 1:10 if iseven(x)]
println("Even squares: $even_squares")

# 2D comprehension -> Matrix
multiplication_table = [i * j for i in 1:5, j in 1:5]
println("Multiplication table (5x5):")
display(multiplication_table)
println()

# Generator expression (lazy)
total = sum(1/k^2 for k in 1:1_000_000)
println("∑(1/k²) for k=1:10⁶ = $total (≈ π²/6 = $(π^2/6))")

# Dictionary comprehension
word_lengths = Dict(w => length(w) for w in ["Julia", "Python", "R"])
println("Word lengths: $word_lengths")

# Set comprehension
unique_remainders = Set(x % 7 for x in 1:100)
println("Unique remainders mod 7: $unique_remainders")

# ============================================================
# Section: Tuples and named tuples
# ============================================================

println("\n=== Tuples and Named Tuples ===")

# Tuples
point = (3.0, 4.0)
println("point[1] = $(point[1])")
x, y = point
println("Destructured: x=$x, y=$y")

# Named tuples
patient = (name="Alice", age=34, bp=120)
println("Patient: $(patient.name), age $(patient.age)")

# Returning multiple values
function divrem_custom(a, b)
    return (quotient=a ÷ b, remainder=a % b)
end
result = divrem_custom(17, 5)
println("17 ÷ 5: quotient=$(result.quotient), remainder=$(result.remainder)")

# ============================================================
# Section: Nothing, Missing, and error handling
# ============================================================

println("\n=== Nothing, Missing, and Error Handling ===")

# Nothing
function maybe_find(collection, target)
    for item in collection
        item == target && return item
    end
    return nothing
end

result = maybe_find([1, 2, 3], 5)
println("maybe_find([1,2,3], 5) → isnothing = $(isnothing(result))")

# Missing
data = [1.0, 2.0, missing, 4.0]
println("sum with missing: $(sum(data))")
println("sum(skipmissing): $(sum(skipmissing(data)))")

# Exception handling
try
    x = parse(Int, "not_a_number")
catch e
    println("Error: $(typeof(e))")
finally
    println("This always runs")
end

# ============================================================
# Exercises
# ============================================================

println("\n=== Exercises ===")

# Exercise 1: Type hierarchy climbing
println("Type hierarchy from Float64:")
t = Float64
while t != Any
    println("  $t")
    t = supertype(t)
end
println("  Any")

# Exercise 3: Pythagorean triples
triples = [(a, b, c) for a in 1:50 for b in a+1:50 for c in b+1:50 if a^2 + b^2 == c^2]
println("\nPythagorean triples (a < b < c ≤ 50):")
for t in triples
    println("  $t")
end

# Exercise 4: Missing values
v = [10, missing, 30, missing, 50]
using Statistics
println("\nMean of non-missing values: $(mean(skipmissing(v)))")

# Exercise 5: DNA nucleotide counter
function count_nucleotides(dna::String)
    counts = Dict{Char, Int}()
    for ch in dna
        counts[ch] = get(counts, ch, 0) + 1
    end
    return counts
end
println("Nucleotides in ATCGGATCCA: $(count_nucleotides("ATCGGATCCA"))")
