"""
Chapter 3: Functions and Multiple Dispatch
==========================================
All code examples from Chapter 3 of the Julia programming course.
Covers: function definitions, arguments, type annotations, multiple dispatch,
closures, composition/piping, metaprogramming, scope rules.
"""

# ============================================================
# Section: Defining functions
# ============================================================

println("=== Defining Functions ===")

# Standard form
function greet(name)
    return "Hello, $name!"
end

# Short form (for one-liners)
square(x) = x^2

# Anonymous (lambda) function
double = x -> 2x

println(greet("Julia"))
println("square(7) = $(square(7))")
println("double(21) = $(double(21))")

# Functions are first-class objects
println("map(square, [1,2,3,4]) = $(map(square, [1, 2, 3, 4]))")
println("filter(isodd, 1:10) = $(filter(isodd, 1:10))")

# Apply with do-block syntax
result = map(1:5) do x
    x^2 + 1
end
println("do-block map: $result")

# ============================================================
# Section: Arguments and return values
# ============================================================

println("\n=== Arguments and Return Values ===")

# Positional arguments
function power(base, exponent)
    return base^exponent
end
println("power(2, 10) = $(power(2, 10))")

# Default values
function power_default(base, exponent=2)
    return base^exponent
end
println("power_default(5) = $(power_default(5))")
println("power_default(5, 3) = $(power_default(5, 3))")

# Keyword arguments (after semicolon)
function create_grid(; rows=10, cols=10, fill_value=0.0)
    return fill(fill_value, rows, cols)
end
grid = create_grid(rows=3, cols=4, fill_value=1.0)
println("Grid size: $(size(grid))")

# Varargs (variable number of arguments)
function mysum(args...)
    total = 0
    for a in args
        total += a
    end
    return total
end
println("mysum(1,2,3,4,5) = $(mysum(1, 2, 3, 4, 5))")

# Multiple return values (as tuple)
function minmax_custom(v)
    return minimum(v), maximum(v)
end
lo, hi = minmax_custom([3, 1, 4, 1, 5, 9])
println("min=$lo, max=$hi")

# ============================================================
# Section: Type annotations
# ============================================================

println("\n=== Type Annotations ===")

# Annotate argument types
function add(x::Number, y::Number)
    return x + y
end
println("add(3, 4.5) = $(add(3, 4.5))")

try
    add("a", "b")
catch e
    println("add(\"a\",\"b\") → MethodError (String is not a Number)")
end

# Annotate return type
function safe_sqrt(x::Real)::Float64
    x < 0 && error("Cannot take sqrt of negative number")
    return sqrt(x)
end
println("safe_sqrt(16) = $(safe_sqrt(16))")

# Parametric type annotations
function first_element(v::Vector{T}) where T
    return v[1]::T
end
println("first_element([10,20,30]) = $(first_element([10, 20, 30]))")

# ============================================================
# Section: Multiple dispatch
# ============================================================

println("\n=== Multiple Dispatch ===")

# Define an abstract type and concrete subtypes
abstract type Shape end

struct Circle <: Shape
    radius::Float64
end

struct Rectangle <: Shape
    width::Float64
    height::Float64
end

struct Triangle <: Shape
    base::Float64
    height::Float64
end

# Define area() with multiple methods
area(c::Circle) = π * c.radius^2
area(r::Rectangle) = r.width * r.height
area(t::Triangle) = 0.5 * t.base * t.height

# Julia dispatches based on the argument type
println("area(Circle(5.0)) = $(area(Circle(5.0)))")
println("area(Rectangle(3.0, 4.0)) = $(area(Rectangle(3.0, 4.0)))")
println("area(Triangle(6.0, 3.0)) = $(area(Triangle(6.0, 3.0)))")

# Check all methods of a function
println("Number of area methods: $(length(methods(area)))")

# ============================================================
# Section: Closures
# ============================================================

println("\n=== Closures ===")

function make_counter(start=0)
    count = start
    increment() = (count += 1; count)
    reset() = (count = start; count)
    return (increment=increment, reset=reset)
end

c = make_counter(10)
println("increment: $(c.increment())")
println("increment: $(c.increment())")
println("increment: $(c.increment())")
println("reset: $(c.reset())")

# Closures with map/filter
threshold = 0.5
data = [0.1, 0.6, 0.3, 0.8, 0.4, 0.9, 0.2, 0.7]
filtered = filter(x -> x > threshold, data)
println("Filtered (>$threshold): $filtered")

# Adder factory
make_adder(n) = x -> x + n
add5 = make_adder(5)
println("add5(10) = $(add5(10))")

# ============================================================
# Section: Function composition and piping
# ============================================================

println("\n=== Composition and Piping ===")

# Composition operator
f = sqrt ∘ abs
println("(sqrt ∘ abs)(-16) = $(f(-16))")

# Pipe operator |>
result = -16 |> abs |> sqrt
println("-16 |> abs |> sqrt = $result")

# Chain operations on data
result = [3, 1, 4, 1, 5, 9, 2, 6] |>
    sort |>
    unique |>
    reverse
println("Chained ops: $result")

# With anonymous functions in the pipe
result = [1, 2, 3, 4, 5] |>
    xs -> filter(isodd, xs) |>
    xs -> map(x -> x^2, xs) |>
    sum
println("Pipe with lambdas: $result (= 1 + 9 + 25)")

# ============================================================
# Section: Metaprogramming basics
# ============================================================

println("\n=== Metaprogramming ===")

# An expression is a Julia data structure
ex = :(2 + 3 * x)
println("typeof(:(2+3*x)) = $(typeof(ex))")

# Evaluate an expression
x = 10
println("eval(:(2 + 3*x)) with x=10: $(eval(ex))")

# Macros transform code at parse time
macro sayhello(name)
    return :(println("Hello, ", $name, "!"))
end
@sayhello "Julia"

# Useful built-in macros
@show 2 + 3
@assert 1 + 1 == 2 "Math is broken!"

# @elapsed for timing
t = @elapsed begin
    A = rand(1000, 1000)
    B = A * A'
end
println("Matrix multiply took $t seconds")

# ============================================================
# Section: Scope rules
# ============================================================

println("\n=== Scope Rules ===")

# Global scope
x = 10

# Local scope (functions)
function demo()
    y = 20        # local to demo
    println("Inside demo: x=$x (global), y=$y (local)")
    return y
end
demo()

# let blocks create a fresh scope
let
    temp = 42
    println("Inside let: temp=$temp")
end
# temp is not defined here

# for loops have local scope
for i in 1:3
    local_var = i^2
end
# local_var is not defined here

println("\n=== Exercises ===")

# Exercise: Point2D with multi-dispatch distance
struct Point2D
    x::Float64
    y::Float64
end

distance(p::Point2D) = sqrt(p.x^2 + p.y^2)
distance(p::Point2D, q::Point2D) = sqrt((p.x - q.x)^2 + (p.y - q.y)^2)

p1 = Point2D(3.0, 4.0)
p2 = Point2D(6.0, 8.0)
println("Distance from origin: $(distance(p1))")
println("Distance between points: $(distance(p1, p2))")

# Exercise: Polynomial closure
function make_polynomial(coeffs)
    return x -> sum(c * x^(i-1) for (i, c) in enumerate(coeffs))
end
f = make_polynomial([1, 2, 3])  # 1 + 2x + 3x²
println("f(2) = 1 + 2*2 + 3*4 = $(f(2))")

# Exercise: Pipe operator
result = 1:100 |>
    x -> filter(n -> n % 3 == 0, collect(x)) |>
    x -> map(n -> n^2, x) |>
    sum
println("Sum of squares of multiples of 3 in 1:100 = $result")

# Exercise: Animal dispatch
abstract type Animal end
struct Dog <: Animal; name::String; end
struct Cat <: Animal; name::String; end

interact(a::Dog, b::Dog) = "$(a.name) and $(b.name) play fetch together!"
interact(a::Dog, b::Cat) = "$(a.name) chases $(b.name)!"
interact(a::Cat, b::Dog) = "$(a.name) hisses at $(b.name)!"
interact(a::Cat, b::Cat) = "$(a.name) and $(b.name) nap together."

println(interact(Dog("Rex"), Dog("Buddy")))
println(interact(Dog("Rex"), Cat("Whiskers")))
println(interact(Cat("Luna"), Dog("Rex")))
println(interact(Cat("Luna"), Cat("Mittens")))
