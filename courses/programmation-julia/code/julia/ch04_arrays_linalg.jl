"""
Chapter 4: Arrays and Linear Algebra
=====================================
All code examples from Chapter 4 of the Julia programming course.
Covers: creating arrays, matrices, indexing/slicing, broadcasting,
common operations, linear algebra, matrix factorizations, sparse arrays.
"""

using LinearAlgebra
using SparseArrays
using Statistics

# ============================================================
# Section: Creating arrays
# ============================================================

println("=== Creating Arrays ===")

# 1D arrays (vectors)
v = [1, 2, 3, 4, 5]          # Vector{Int64}
w = [1.0, 2.0, 3.0]          # Vector{Float64}
mixed = Any[1, "two", 3.0]   # Vector{Any}

println("v = $v, typeof = $(typeof(v))")
println("w = $w, typeof = $(typeof(w))")

# Ranges (lazy, no memory allocation)
r = 1:10
r2 = 0.0:0.1:1.0
println("collect(1:5) = $(collect(1:5))")

# Constructor functions
println("zeros(5) = $(zeros(5))")
println("ones(3) = $(ones(3))")
println("fill(42, 5) = $(fill(42, 5))")
println("rand(5) = $(rand(5))")
println("randn(5) = $(randn(5))")
println("range(0,1,length=11) = $(collect(range(0, 1, length=11)))")

# ============================================================
# Section: 2D arrays (matrices)
# ============================================================

println("\n=== 2D Arrays (Matrices) ===")

A = [1 2 3; 4 5 6; 7 8 9]    # 3x3 Matrix{Int64}
println("A = ")
display(A)
println()

B = [1.0 2.0
     3.0 4.0]
println("B = ")
display(B)
println()

# Constructor functions
println("zeros(3,4) size = $(size(zeros(3, 4)))")
println("ones(2,3) size = $(size(ones(2, 3)))")

I3 = Matrix{Float64}(I, 3, 3)
println("Identity 3x3:")
display(I3)
println()

# Useful constructors
println("diagm([1,2,3]):")
display(diagm([1, 2, 3]))
println()

println("reshape(1:12, 3, 4):")
display(reshape(1:12, 3, 4))
println()

# Properties
println("size(A) = $(size(A))")
println("size(A,1) = $(size(A, 1))")
println("ndims(A) = $(ndims(A))")
println("length(A) = $(length(A))")
println("eltype(A) = $(eltype(A))")

# ============================================================
# Section: Indexing and slicing
# ============================================================

println("\n=== Indexing and Slicing ===")

A = [10 20 30; 40 50 60; 70 80 90]

println("A[2,3] = $(A[2, 3])")
println("A[1] = $(A[1]) (linear index, column-major)")
println("A[1,:] = $(A[1, :])")
println("A[:,2] = $(A[:, 2])")
println("A[1:2, 2:3] = ")
display(A[1:2, 2:3])
println()

# Logical indexing
v = [3, 1, 4, 1, 5, 9, 2, 6]
println("v[v .> 3] = $(v[v .> 3])")

# Views (no copy)
v_sub = @view A[1:2, :]
println("View of A[1:2,:]: ")
display(v_sub)
println()

# findall, findfirst
println("findall(x -> x > 50, A) = $(findall(x -> x > 50, A))")
println("findfirst(x -> x > 50, A) = $(findfirst(x -> x > 50, A))")

# ============================================================
# Section: Broadcasting -- the dot syntax
# ============================================================

println("\n=== Broadcasting ===")

a = [1, 2, 3]
b = [10, 20, 30]

println("a .+ b = $(a .+ b)")
println("a .* b = $(a .* b)")
println("a .^ 2 = $(a .^ 2)")
println("sin.(a) = $(sin.(a))")
println("a .+ 10 = $(a .+ 10)")

# Fused broadcasting with @.
result = @. sin(a) + cos(b) * a^2
println("@. sin(a) + cos(b) * a^2 = $result")

# Broadcasting with matrices
A = [1 2; 3 4]
v = [10, 20]
println("A .+ v (column broadcast):")
display(A .+ v)
println()

println("A .+ v' (row broadcast):")
display(A .+ v')
println()

println("A .> 2:")
display(A .> 2)
println()

# ============================================================
# Section: Common array operations
# ============================================================

println("\n=== Common Array Operations ===")

v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

println("sum(v) = $(sum(v))")
println("prod(v) = $(prod(v))")
println("minimum(v), maximum(v) = $(minimum(v)), $(maximum(v))")
println("extrema(v) = $(extrema(v))")
println("mean(v) = $(mean(v))")
println("std(v) = $(std(v))")

# Sorting
println("sort(v) = $(sort(v))")
println("sortperm(v) = $(sortperm(v))")

# Searching
println("5 in v = $(5 in v)")
println("count(isodd, v) = $(count(isodd, v))")
println("any(x -> x > 8, v) = $(any(x -> x > 8, v))")
println("all(x -> x > 0, v) = $(all(x -> x > 0, v))")

# Mutation
v2 = copy(v)
push!(v2, 99)
println("push!(v2, 99) → $v2")
pop!(v2)
println("pop!(v2) → $v2")

# Concatenation
println("vcat([1,2],[3,4]) = $(vcat([1, 2], [3, 4]))")
println("hcat([1,2],[3,4]) = ")
display(hcat([1, 2], [3, 4]))
println()

# ============================================================
# Section: Linear algebra
# ============================================================

println("\n=== Linear Algebra ===")

A = [4.0 1.0; 2.0 3.0]
b = [1.0, 2.0]

println("A' (adjoint):")
display(A')
println()

println("det(A) = $(det(A))")
println("tr(A) = $(tr(A))")
println("rank(A) = $(rank(A))")

# Solving linear systems: Ax = b
x = A \ b
println("A \\ b = $x")
println("A*x ≈ b: $(A * x ≈ b)")

# Eigenvalues and eigenvectors
vals, vecs = eigen(A)
println("Eigenvalues: $vals")

# SVD
U, S, V = svd(A)
println("Singular values: $S")

# Norms
println("norm(b) = $(norm(b))")
println("norm(b, 1) = $(norm(b, 1))")
println("norm(b, Inf) = $(norm(b, Inf))")

# Dot product and cross product
println("dot([1,2,3],[4,5,6]) = $(dot([1, 2, 3], [4, 5, 6]))")
println("cross([1,0,0],[0,1,0]) = $(cross([1, 0, 0], [0, 1, 0]))")

# Special matrix types
D = Diagonal([1, 2, 3])
println("Diagonal([1,2,3]):")
display(D)
println()

# ============================================================
# Section: Matrix factorizations
# ============================================================

println("\n=== Matrix Factorizations ===")

A = rand(5, 5)
A = A + A'  # make symmetric
A += 5I     # ensure positive definiteness

# LU factorization
F = lu(A)
println("LU: L*U ≈ A[p,:] → $(F.L * F.U ≈ A[F.p, :])")

# Cholesky factorization
C = cholesky(A)
println("Cholesky: L*L' ≈ A → $(C.L * C.L' ≈ A)")

# QR factorization
Q, R = qr(A)
println("QR factorization computed successfully")

# Solve with factorizations
b1 = rand(5)
b2 = rand(5)
F = lu(A)
x1 = F \ b1
x2 = F \ b2
println("Solved 2 systems with same LU factorization")

# ============================================================
# Section: Sparse arrays
# ============================================================

println("\n=== Sparse Arrays ===")

# Create sparse matrices
S = sparse([1, 2, 3, 1], [1, 2, 3, 3], [10, 20, 30, 5], 3, 3)
println("Sparse matrix:")
display(S)
println()

# Convert dense to sparse
A_dense = [1 0 0; 0 2 0; 0 0 3]
A_sparse = sparse(A_dense)
println("Dense → Sparse conversion done")

# Sparse identity
I_sparse = spdiagm(0 => ones(100))
println("Sparse identity 100x100: nnz = $(nnz(I_sparse))")

# Memory comparison
A_dense_big = zeros(1000, 1000)
A_dense_big[1,1] = 1.0; A_dense_big[500,500] = 2.0; A_dense_big[1000,1000] = 3.0
A_sparse_big = sparse(A_dense_big)

println("Dense 1000x1000: $(Base.summarysize(A_dense_big)) bytes")
println("Sparse 1000x1000 (3 nnz): $(Base.summarysize(A_sparse_big)) bytes")

# Operations work the same
b = rand(1000)
x_sparse = A_sparse_big \ b
println("Sparse solve completed")

# ============================================================
# Exercises
# ============================================================

println("\n=== Exercises ===")

# Exercise 1: Random vector stats
v = rand(1:100, 10)
println("Random vector: $v")
println("Mean: $(mean(v)), Median: $(median(v)), Std: $(std(v))")

# Exercise 2: Solve Ax = b and verify
A = rand(5, 5)
b = rand(5)
x = A \ b
println("||Ax - b|| = $(norm(A*x - b)) (< 1e-10: $(norm(A*x - b) < 1e-10))")

# Exercise 3: sin²(x) + cos²(x) = 1
x_vals = 0:0.1:2π
identity_check = @. sin(x_vals)^2 + cos(x_vals)^2
println("sin²+cos² ≈ 1 for all x? $(all(x -> isapprox(x, 1.0), identity_check))")

# Exercise 6: Hilbert matrix condition numbers
println("Hilbert matrix condition numbers:")
for n in [5, 10, 15, 20]
    H = [1.0/(i+j-1) for i in 1:n, j in 1:n]
    println("  n=$n: cond(H) = $(cond(H))")
end
