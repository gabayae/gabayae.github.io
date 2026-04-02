# Julia Programming

A 30-hour practical course on the Julia programming language, covering fundamentals through scientific computing, machine learning, and real-world capstone projects.

## Structure

| Chapter | Topic | Hours | Key packages |
|---------|-------|-------|-------------|
| 1 | Getting started with Julia | 3h | Pkg, Pluto |
| 2 | Types, variables, and control flow | 3h | - |
| 3 | Functions and multiple dispatch | 3h | - |
| 4 | Arrays and linear algebra | 3h | LinearAlgebra, SparseArrays |
| 5 | DataFrames and data wrangling | 3h | DataFrames.jl, CSV.jl |
| 6 | Visualization | 3h | Plots.jl, Makie.jl, AlgebraOfGraphics.jl |
| 7 | Performance and optimization | 3h | BenchmarkTools.jl, Profile |
| 8 | Scientific computing | 3h | DifferentialEquations.jl, Optimization.jl, ModelingToolkit.jl |
| 9 | Machine learning with Julia | 3h | MLJ.jl, Flux.jl |
| 10 | Capstone projects | 3h | All of the above |

## Datasets used

All datasets in this course are freely available:

- **RDatasets.jl:** Built-in classic datasets (iris, mtcars, etc.)
- **Our World in Data:** https://ourworldindata.org/
- **UCI ML Repository:** https://archive.ics.uci.edu/
- **MLDatasets.jl:** MNIST, CIFAR-10, and other standard ML datasets
- **CSV files from GitHub:** Various open-source datasets

## Prerequisites

Basic programming experience in any language. No prior Julia knowledge required. Familiarity with linear algebra and calculus is helpful for the scientific computing chapters.

## Tools

- Julia 1.10+
- VS Code with Julia extension
- Pluto.jl reactive notebooks
- IJulia for Jupyter integration

## Key packages

```julia
using Pkg
Pkg.add([
    "Pluto", "DataFrames", "CSV", "Plots", "Makie", "CairoMakie",
    "AlgebraOfGraphics", "BenchmarkTools", "DifferentialEquations",
    "Optimization", "ModelingToolkit", "MLJ", "Flux", "MLDatasets",
    "RDatasets", "LinearAlgebra", "SparseArrays", "Statistics"
])
```

## Languages

- `en/` -- English lecture notes (LaTeX + PDF)
- `code/julia/` -- Julia scripts per chapter
- `code/notebooks/` -- Jupyter notebooks per chapter (IJulia kernel)
