"""
Chapter 7: Performance and Optimization
=========================================
Comprehensive examples of Julia performance analysis and optimization.
Covers: BenchmarkTools, type stability, memory allocation, profiling,
SIMD, multithreading, and performance tips.
"""

using BenchmarkTools

# ============================================================
# Section: Benchmarking with BenchmarkTools.jl
# ============================================================

println("=== BenchmarkTools ===")

# Basic benchmarking
println("--- @btime (simple operations) ---")
@btime sum($(rand(1000)))
@btime sort($(rand(1000)))

# Compare implementations
function sum_loop(v)
    s = zero(eltype(v))
    for x in v
        s += x
    end
    return s
end

function sum_simd(v)
    s = zero(eltype(v))
    @simd for i in eachindex(v)
        @inbounds s += v[i]
    end
    return s
end

v = rand(10_000)
println("\n--- Comparing sum implementations ---")
println("Built-in sum:")
@btime sum($v)
println("Manual loop:")
@btime sum_loop($v)
println("SIMD loop:")
@btime sum_simd($v)

# @benchmark for detailed statistics
println("\n--- @benchmark (detailed stats) ---")
result = @benchmark sum($v)
println("Minimum time: $(minimum(result.times)) ns")
println("Median time:  $(median(result.times)) ns")
println("Memory:       $(result.memory) bytes")
println("Allocations:  $(result.allocs)")

# ============================================================
# Section: Type stability
# ============================================================

println("\n=== Type Stability ===")

# BAD: Type-unstable function
function unstable_sum(n)
    s = 0  # Int64
    for i in 1:n
        s += i / 2  # becomes Float64 -- type changes!
    end
    return s
end

# GOOD: Type-stable function
function stable_sum(n)
    s = 0.0  # Float64 from the start
    for i in 1:n
        s += i / 2
    end
    return s
end

println("--- Type stability comparison ---")
println("Unstable:")
@btime unstable_sum(10_000)
println("Stable:")
@btime stable_sum(10_000)

# Check type stability with @code_warntype
println("\n--- @code_warntype unstable_sum ---")
@code_warntype unstable_sum(100)
println("\n--- @code_warntype stable_sum ---")
@code_warntype stable_sum(100)

# BAD: Abstract field types in structs
struct ParticleBad
    x      # Any type -- BAD
    y      # Any type -- BAD
    mass   # Any type -- BAD
end

# GOOD: Concrete field types
struct ParticleGood
    x::Float64
    y::Float64
    mass::Float64
end

# BEST: Parametric types (flexible AND fast)
struct ParticleBest{T<:Real}
    x::T
    y::T
    mass::T
end

function total_mass_bad(particles::Vector{ParticleBad})
    s = 0.0
    for p in particles
        s += p.mass
    end
    return s
end

function total_mass_good(particles::Vector{ParticleGood})
    s = 0.0
    for p in particles
        s += p.mass
    end
    return s
end

function total_mass_best(particles::Vector{ParticleBest{Float64}})
    s = 0.0
    for p in particles
        s += p.mass
    end
    return s
end

n = 10_000
bad_particles = [ParticleBad(rand(), rand(), rand()) for _ in 1:n]
good_particles = [ParticleGood(rand(), rand(), rand()) for _ in 1:n]
best_particles = [ParticleBest(rand(), rand(), rand()) for _ in 1:n]

println("\n--- Struct field type comparison ---")
println("Any fields (BAD):")
@btime total_mass_bad($bad_particles)
println("Concrete fields (GOOD):")
@btime total_mass_good($good_particles)
println("Parametric fields (BEST):")
@btime total_mass_best($best_particles)

# ============================================================
# Section: Memory allocation and views
# ============================================================

println("\n=== Memory Allocation ===")

A = rand(1000, 1000)

# BAD: Allocating slices
function col_sums_alloc(A)
    s = zeros(size(A, 2))
    for j in 1:size(A, 2)
        s[j] = sum(A[:, j])  # allocates a new vector each time
    end
    return s
end

# GOOD: Using views
function col_sums_view(A)
    s = zeros(size(A, 2))
    for j in 1:size(A, 2)
        s[j] = sum(@view A[:, j])  # no allocation
    end
    return s
end

# BEST: Using eachcol
function col_sums_each(A)
    return [sum(col) for col in eachcol(A)]
end

println("--- Column sums comparison ---")
println("Allocating slices:")
@btime col_sums_alloc($A)
println("Using @view:")
@btime col_sums_view($A)
println("Using eachcol:")
@btime col_sums_each($A)

# Pre-allocation
println("\n--- Pre-allocation ---")

# BAD: Growing array
function grow_array(n)
    result = Float64[]
    for i in 1:n
        push!(result, sin(i * 0.01))
    end
    return result
end

# GOOD: Pre-allocated
function preallocated(n)
    result = Vector{Float64}(undef, n)
    for i in 1:n
        result[i] = sin(i * 0.01)
    end
    return result
end

# BEST: Broadcasting
prealloc_broadcast(n) = sin.(collect(1:n) .* 0.01)

println("Growing array:")
@btime grow_array(10_000)
println("Pre-allocated:")
@btime preallocated(10_000)
println("Broadcasting:")
@btime prealloc_broadcast(10_000)

# ============================================================
# Section: In-place operations
# ============================================================

println("\n=== In-place Operations ===")

x = rand(10_000)
y = rand(10_000)
out = similar(x)

# BAD: allocating
f_alloc(x, y) = sin.(x) .+ cos.(y)

# GOOD: in-place with @.
function f_inplace!(out, x, y)
    @. out = sin(x) + cos(y)
    return out
end

println("Allocating:")
@btime f_alloc($x, $y)
println("In-place:")
@btime f_inplace!($out, $x, $y)

# ============================================================
# Section: Loop optimization tips
# ============================================================

println("\n=== Loop Optimization ===")

# @inbounds removes bounds checking
function dot_product_safe(a, b)
    s = 0.0
    for i in eachindex(a, b)
        s += a[i] * b[i]
    end
    return s
end

function dot_product_fast(a, b)
    s = 0.0
    @inbounds @simd for i in eachindex(a, b)
        s += a[i] * b[i]
    end
    return s
end

a = rand(100_000)
b = rand(100_000)

println("Safe dot product:")
@btime dot_product_safe($a, $b)
println("@inbounds @simd dot product:")
@btime dot_product_fast($a, $b)

# ============================================================
# Section: Global variable pitfalls
# ============================================================

println("\n=== Global Variable Pitfalls ===")

# BAD: Using global variables in hot loops
global_data = rand(10_000)

function sum_global_bad()
    s = 0.0
    for x in global_data  # type cannot be inferred at compile time
        s += x
    end
    return s
end

# GOOD: Pass as argument
function sum_arg(data)
    s = 0.0
    for x in data
        s += x
    end
    return s
end

# GOOD: Use const for globals
const CONST_DATA = rand(10_000)

function sum_const()
    s = 0.0
    for x in CONST_DATA
        s += x
    end
    return s
end

println("Global (non-const):")
@btime sum_global_bad()
println("Passed as argument:")
@btime sum_arg($global_data)
println("Const global:")
@btime sum_const()

# ============================================================
# Section: Profiling summary
# ============================================================

println("\n=== Profiling ===")

# Using @time for quick profiling
println("@time for matrix multiply:")
A = rand(500, 500)
@time B = A * A'

# @elapsed returns time as a value
t = @elapsed begin
    C = rand(1000, 1000)
    D = C * C'
end
println("Matrix 1000x1000 multiply: $(round(t, digits=4))s")

# @allocated returns bytes allocated
bytes = @allocated rand(1000, 1000) * rand(1000, 1000)
println("Bytes allocated for 1000x1000 multiply: $bytes")

# For deeper profiling, use Profile.jl (interactive, not shown here)
# using Profile
# @profile my_heavy_function()
# Profile.print()

println("\n=== Performance Tips Summary ===")
println("1. Write type-stable functions (avoid changing types)")
println("2. Use concrete types in struct fields")
println("3. Avoid global variables (use const or pass as args)")
println("4. Pre-allocate outputs, use in-place operations (!)")
println("5. Use @view instead of array slices in loops")
println("6. Use @inbounds and @simd for tight numeric loops")
println("7. Profile before optimizing (@btime, @benchmark)")
println("8. Broadcasting (@.) fuses operations, reducing allocations")
