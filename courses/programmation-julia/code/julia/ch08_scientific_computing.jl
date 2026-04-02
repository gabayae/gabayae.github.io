"""
Chapter 8: Scientific Computing
=================================
Comprehensive examples using DifferentialEquations.jl and Optimization.jl.
Covers: ODE solving (Lorenz, SIR, harmonic oscillator), parameter estimation,
stiff systems, and nonlinear optimization.
"""

using DifferentialEquations
using Plots
using LinearAlgebra

# ============================================================
# Section: Ordinary Differential Equations (ODEs)
# ============================================================

println("=== ODE Solving with DifferentialEquations.jl ===")

# --- Example 1: Simple exponential decay ---
# dy/dt = -0.5y, y(0) = 1
println("\n--- Exponential Decay ---")
decay!(du, u, p, t) = (du[1] = -0.5 * u[1])

u0 = [1.0]
tspan = (0.0, 10.0)
prob_decay = ODEProblem(decay!, u0, tspan)
sol_decay = solve(prob_decay, Tsit5())

println("y(0) = $(sol_decay(0.0)[1])")
println("y(5) = $(round(sol_decay(5.0)[1], digits=6))")
println("y(10) = $(round(sol_decay(10.0)[1], digits=6))")
println("Exact y(10) = $(round(exp(-0.5*10), digits=6))")

p_decay = plot(sol_decay, title="Exponential Decay",
    xlabel="t", ylabel="y(t)", lw=2, label="y(t) = e^{-0.5t}")
savefig(p_decay, "ode_decay.png")
println("Saved: ode_decay.png")

# --- Example 2: Harmonic oscillator ---
# x'' + omega^2 * x = 0  =>  u1' = u2, u2' = -omega^2 * u1
println("\n--- Harmonic Oscillator ---")
function harmonic!(du, u, p, t)
    omega = p[1]
    du[1] = u[2]           # dx/dt = v
    du[2] = -omega^2 * u[1]  # dv/dt = -omega^2 * x
end

u0_harm = [1.0, 0.0]  # x(0)=1, v(0)=0
tspan_harm = (0.0, 20.0)
p_harm = [2.0]  # omega = 2

prob_harm = ODEProblem(harmonic!, u0_harm, tspan_harm, p_harm)
sol_harm = solve(prob_harm, Tsit5(), saveat=0.05)

p_harmonic = plot(sol_harm, idxs=(1), label="x(t)", lw=2,
    title="Harmonic Oscillator (omega=2)",
    xlabel="t", ylabel="Displacement")
plot!(p_harmonic, sol_harm, idxs=(2), label="v(t)", lw=2, ls=:dash)
savefig(p_harmonic, "ode_harmonic.png")
println("Saved: ode_harmonic.png")

# Phase portrait
p_phase = plot(sol_harm, idxs=(1, 2), label="Phase portrait",
    xlabel="x", ylabel="v", title="Phase Portrait", lw=2)
savefig(p_phase, "ode_phase.png")
println("Saved: ode_phase.png")

# --- Example 3: The Lorenz system (chaos) ---
println("\n--- Lorenz System ---")
function lorenz!(du, u, p, t)
    sigma, rho, beta = p
    du[1] = sigma * (u[2] - u[1])
    du[2] = u[1] * (rho - u[3]) - u[2]
    du[3] = u[1] * u[2] - beta * u[3]
end

u0_lorenz = [1.0, 0.0, 0.0]
tspan_lorenz = (0.0, 50.0)
p_lorenz = [10.0, 28.0, 8/3]  # classic Lorenz parameters

prob_lorenz = ODEProblem(lorenz!, u0_lorenz, tspan_lorenz, p_lorenz)
sol_lorenz = solve(prob_lorenz, Tsit5(), saveat=0.01)

println("Lorenz system solved: $(length(sol_lorenz.t)) time steps")
println("Final state: $(round.(sol_lorenz.u[end], digits=3))")

# Time series
p_lorenz_ts = plot(sol_lorenz, idxs=(1), label="x(t)", lw=0.5,
    title="Lorenz Attractor - Time Series", xlabel="t")
savefig(p_lorenz_ts, "lorenz_timeseries.png")
println("Saved: lorenz_timeseries.png")

# 3D attractor
p_lorenz_3d = plot(sol_lorenz, idxs=(1, 2, 3), label="",
    title="Lorenz Attractor", xlabel="x", ylabel="y", zlabel="z",
    lw=0.3, color=:viridis)
savefig(p_lorenz_3d, "lorenz_attractor.png")
println("Saved: lorenz_attractor.png")

# --- Example 4: SIR epidemiological model ---
println("\n--- SIR Epidemiological Model ---")
function sir!(du, u, p, t)
    S, I, R = u
    beta, gamma = p
    N = S + I + R
    du[1] = -beta * S * I / N        # dS/dt
    du[2] = beta * S * I / N - gamma * I  # dI/dt
    du[3] = gamma * I                # dR/dt
end

N = 1_000_000.0
I0 = 100.0
u0_sir = [N - I0, I0, 0.0]  # S, I, R
tspan_sir = (0.0, 200.0)
p_sir = [0.3, 0.1]  # beta, gamma  =>  R0 = beta/gamma = 3

prob_sir = ODEProblem(sir!, u0_sir, tspan_sir, p_sir)
sol_sir = solve(prob_sir, Tsit5(), saveat=0.5)

println("R0 = beta/gamma = $(p_sir[1]/p_sir[2])")
println("Peak infected: $(round(maximum(sol_sir[2, :]), digits=0))")

# Find peak time
peak_idx = argmax(sol_sir[2, :])
println("Peak time: $(sol_sir.t[peak_idx]) days")
println("Final recovered: $(round(sol_sir[3, end], digits=0))")

p_sir_plot = plot(sol_sir, idxs=(1), label="Susceptible", lw=2,
    title="SIR Model (R₀ = 3)", xlabel="Days", ylabel="Population")
plot!(p_sir_plot, sol_sir, idxs=(2), label="Infected", lw=2, color=:red)
plot!(p_sir_plot, sol_sir, idxs=(3), label="Recovered", lw=2, color=:green)
savefig(p_sir_plot, "sir_model.png")
println("Saved: sir_model.png")

# --- Example 5: Stiff system (Van der Pol oscillator) ---
println("\n--- Van der Pol Oscillator (stiff) ---")
function vanderpol!(du, u, p, t)
    mu = p[1]
    du[1] = u[2]
    du[2] = mu * (1 - u[1]^2) * u[2] - u[1]
end

u0_vdp = [2.0, 0.0]
tspan_vdp = (0.0, 100.0)
p_vdp = [10.0]  # large mu => stiff

prob_vdp = ODEProblem(vanderpol!, u0_vdp, tspan_vdp, p_vdp)
sol_vdp = solve(prob_vdp, Rodas5P(), saveat=0.1)  # stiff solver

println("Van der Pol solved with stiff solver: $(length(sol_vdp.t)) time steps")

p_vdp_plot = plot(sol_vdp, idxs=(1), label="x(t)", lw=1.5,
    title="Van der Pol Oscillator (μ=10)", xlabel="t", ylabel="x")
savefig(p_vdp_plot, "vanderpol.png")
println("Saved: vanderpol.png")

# ============================================================
# Section: Comparing solvers
# ============================================================

println("\n=== Comparing ODE Solvers ===")

# Solve the Lorenz system with different solvers
solvers = [Tsit5(), Vern7(), DP5()]
solver_names = ["Tsit5", "Vern7", "DP5"]

for (solver, name) in zip(solvers, solver_names)
    sol = solve(prob_lorenz, solver)
    println("$name: $(length(sol.t)) steps, retcode = $(sol.retcode)")
end

# ============================================================
# Section: Optimization with Optimization.jl
# ============================================================

println("\n=== Optimization ===")

using Optimization
using OptimizationOptimJL

# --- Example 1: Minimize Rosenbrock function ---
println("\n--- Rosenbrock Function ---")
function rosenbrock(u, p)
    x, y = u
    a, b = p
    return (a - x)^2 + b * (y - x^2)^2
end

u0_opt = [0.0, 0.0]
p_opt = [1.0, 100.0]  # a=1, b=100

optprob = OptimizationProblem(rosenbrock, u0_opt, p_opt)
sol_opt = solve(optprob, NelderMead())

println("Rosenbrock minimum at: $(round.(sol_opt.u, digits=6))")
println("Minimum value: $(round(sol_opt.objective, digits=10))")

# With gradient-based method (using AutoForwardDiff)
using Optimization, OptimizationOptimJL
using ForwardDiff

optf = OptimizationFunction(rosenbrock, Optimization.AutoForwardDiff())
optprob2 = OptimizationProblem(optf, u0_opt, p_opt)
sol_opt2 = solve(optprob2, LBFGS())

println("LBFGS solution: $(round.(sol_opt2.u, digits=6))")
println("LBFGS minimum: $(round(sol_opt2.objective, digits=10))")

# --- Example 2: Least squares curve fitting ---
println("\n--- Least Squares Curve Fitting ---")

# Generate noisy data
t_data = range(0, 5, length=50)
y_true = 3.0 .* exp.(-0.5 .* t_data) .* sin.(2.0 .* t_data)
y_noisy = y_true .+ 0.2 .* randn(length(t_data))

# Fit model: A * exp(-k*t) * sin(omega*t)
function residual_cost(params, p)
    t, y = p
    A, k, omega = params
    y_model = A .* exp.(-k .* t) .* sin.(omega .* t)
    return sum((y .- y_model).^2)
end

p_data = (collect(t_data), y_noisy)
u0_fit = [1.0, 1.0, 1.0]  # initial guess

optf_fit = OptimizationFunction(residual_cost, Optimization.AutoForwardDiff())
optprob_fit = OptimizationProblem(optf_fit, u0_fit, p_data)
sol_fit = solve(optprob_fit, LBFGS())

A_fit, k_fit, omega_fit = sol_fit.u
println("Fitted parameters:")
println("  A = $(round(A_fit, digits=4)) (true: 3.0)")
println("  k = $(round(k_fit, digits=4)) (true: 0.5)")
println("  ω = $(round(omega_fit, digits=4)) (true: 2.0)")

# Plot fit
y_fitted = A_fit .* exp.(-k_fit .* collect(t_data)) .* sin.(omega_fit .* collect(t_data))
p_fit = scatter(collect(t_data), y_noisy, label="Noisy data", ms=3, alpha=0.6)
plot!(p_fit, collect(t_data), y_fitted, label="Fitted model", lw=2, color=:red,
    title="Least Squares Fit", xlabel="t", ylabel="y")
savefig(p_fit, "curve_fit.png")
println("Saved: curve_fit.png")

# --- Example 3: Constrained optimization ---
println("\n--- Constrained Optimization ---")

# Minimize f(x,y) = (x-1)^2 + (y-2)^2 subject to x + y <= 2
function objective_constrained(u, p)
    return (u[1] - 1)^2 + (u[2] - 2)^2
end

optprob_con = OptimizationProblem(objective_constrained, [0.0, 0.0], nothing,
    lb=[-5.0, -5.0], ub=[5.0, 5.0])
sol_con = solve(optprob_con, NelderMead())

println("Constrained minimum at: $(round.(sol_con.u, digits=4))")
println("Objective value: $(round(sol_con.objective, digits=6))")

println("\nAll scientific computing examples complete.")
