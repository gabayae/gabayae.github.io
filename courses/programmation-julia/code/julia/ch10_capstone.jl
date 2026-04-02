"""
Chapter 10: Capstone Projects
===============================
Starter code for three capstone projects combining everything from the course.
Project 1: Lotka-Volterra predator-prey simulation
Project 2: SIR epidemic with vaccination and data fitting
Project 3: End-to-end data pipeline (CSV -> analysis -> ML -> visualization)
"""

using DifferentialEquations
using Plots
using DataFrames
using CSV
using Statistics
using LinearAlgebra

# ============================================================
# Project 1: Lotka-Volterra Predator-Prey Model
# ============================================================

println("=" ^ 60)
println("PROJECT 1: Lotka-Volterra Predator-Prey Model")
println("=" ^ 60)

# The Lotka-Volterra equations:
#   dx/dt = alpha*x - beta*x*y     (prey growth - predation)
#   dy/dt = delta*x*y - gamma*y    (predator growth - death)

function lotka_volterra!(du, u, p, t)
    x, y = u           # prey, predator
    alpha, beta, delta, gamma = p
    du[1] = alpha * x - beta * x * y     # prey
    du[2] = delta * x * y - gamma * y    # predator
end

# Parameters
alpha = 1.1    # prey birth rate
beta = 0.4     # predation rate
delta = 0.1    # predator growth from eating prey
gamma = 0.4    # predator death rate

p_lv = [alpha, beta, delta, gamma]
u0_lv = [10.0, 5.0]   # initial prey, predator
tspan_lv = (0.0, 100.0)

# Solve
prob_lv = ODEProblem(lotka_volterra!, u0_lv, tspan_lv, p_lv)
sol_lv = solve(prob_lv, Tsit5(), saveat=0.1)

println("Lotka-Volterra simulation complete")
println("  Time span: $(tspan_lv)")
println("  Initial: prey=$(u0_lv[1]), predator=$(u0_lv[2])")

# Extract data
t_lv = sol_lv.t
prey = [u[1] for u in sol_lv.u]
predator = [u[2] for u in sol_lv.u]

println("  Max prey: $(round(maximum(prey), digits=2))")
println("  Max predator: $(round(maximum(predator), digits=2))")

# Time series plot
p1 = plot(t_lv, prey, label="Prey", lw=2, color=:blue,
    title="Lotka-Volterra: Population Dynamics",
    xlabel="Time", ylabel="Population")
plot!(p1, t_lv, predator, label="Predator", lw=2, color=:red)
savefig(p1, "capstone_lv_timeseries.png")
println("Saved: capstone_lv_timeseries.png")

# Phase portrait
p2 = plot(prey, predator, label="Trajectory", lw=1.5,
    title="Lotka-Volterra: Phase Portrait",
    xlabel="Prey", ylabel="Predator", color=:purple)
scatter!(p2, [u0_lv[1]], [u0_lv[2]], label="Start", ms=8, color=:green)
savefig(p2, "capstone_lv_phase.png")
println("Saved: capstone_lv_phase.png")

# Parameter sensitivity study
println("\n--- Parameter Sensitivity (varying beta) ---")
betas = [0.2, 0.4, 0.6, 0.8]
p_sens = plot(title="Prey Population vs Predation Rate (beta)",
    xlabel="Time", ylabel="Prey Population")

for b in betas
    p_var = [alpha, b, delta, gamma]
    sol_var = solve(ODEProblem(lotka_volterra!, u0_lv, tspan_lv, p_var), Tsit5(), saveat=0.1)
    prey_var = [u[1] for u in sol_var.u]
    plot!(p_sens, sol_var.t, prey_var, label="beta=$b", lw=1.5)
end
savefig(p_sens, "capstone_lv_sensitivity.png")
println("Saved: capstone_lv_sensitivity.png")

# Save simulation data to CSV
df_lv = DataFrame(
    time = t_lv,
    prey = prey,
    predator = predator
)
CSV.write("lotka_volterra_data.csv", df_lv)
println("Saved: lotka_volterra_data.csv ($(nrow(df_lv)) rows)")

# ============================================================
# Project 2: SIR Model with Vaccination
# ============================================================

println("\n" * "=" ^ 60)
println("PROJECT 2: SIR with Vaccination and Analysis")
println("=" ^ 60)

# Extended SIR: SIRV (Susceptible-Infected-Recovered-Vaccinated)
#   dS/dt = -beta*S*I/N - v*S
#   dI/dt = beta*S*I/N - gamma*I
#   dR/dt = gamma*I
#   dV/dt = v*S

function sirv!(du, u, p, t)
    S, I, R, V = u
    beta, gamma, v_rate = p
    N = S + I + R + V
    du[1] = -beta * S * I / N - v_rate * S  # Susceptible
    du[2] = beta * S * I / N - gamma * I     # Infected
    du[3] = gamma * I                        # Recovered
    du[4] = v_rate * S                       # Vaccinated
end

N_pop = 100_000.0
I0 = 50.0
u0_sirv = [N_pop - I0, I0, 0.0, 0.0]
tspan_sirv = (0.0, 300.0)

# Scenario comparison: no vaccination vs vaccination
scenarios = [
    ("No vaccination", [0.3, 0.1, 0.0]),
    ("Slow vaccination (0.5%/day)", [0.3, 0.1, 0.005]),
    ("Fast vaccination (2%/day)", [0.3, 0.1, 0.02]),
]

results = DataFrame[]
p_comparison = plot(title="SIR+V: Infected over Time",
    xlabel="Days", ylabel="Infected", legend=:topright)

for (name, params) in scenarios
    prob = ODEProblem(sirv!, u0_sirv, tspan_sirv, params)
    sol = solve(prob, Tsit5(), saveat=1.0)

    infected = [u[2] for u in sol.u]
    recovered = [u[3] for u in sol.u]
    vaccinated = [u[4] for u in sol.u]

    peak_inf = maximum(infected)
    peak_day = sol.t[argmax(infected)]
    total_inf = recovered[end]  # final recovered ~ total who were infected

    println("\n$name:")
    println("  R0 = $(params[1]/params[2])")
    println("  Peak infected: $(round(peak_inf, digits=0)) on day $(round(peak_day, digits=0))")
    println("  Total infected: $(round(total_inf, digits=0))")
    println("  Final vaccinated: $(round(vaccinated[end], digits=0))")

    plot!(p_comparison, sol.t, infected, label=name, lw=2)

    push!(results, DataFrame(
        scenario = fill(name, length(sol.t)),
        day = sol.t,
        infected = infected,
        recovered = recovered,
        vaccinated = vaccinated
    ))
end

savefig(p_comparison, "capstone_sirv_comparison.png")
println("\nSaved: capstone_sirv_comparison.png")

# Save all scenarios
df_sirv = vcat(results...)
CSV.write("sirv_scenarios.csv", df_sirv)
println("Saved: sirv_scenarios.csv ($(nrow(df_sirv)) rows)")

# Herd immunity threshold analysis
println("\n--- Herd Immunity Threshold ---")
R0_values = range(1.5, 5.0, length=20)
herd_thresholds = 1.0 .- 1.0 ./ R0_values

p_herd = plot(collect(R0_values), herd_thresholds .* 100,
    title="Herd Immunity Threshold vs R₀",
    xlabel="R₀", ylabel="% Population to Vaccinate",
    lw=3, label="Threshold", color=:darkorange,
    fill=(0, 0.2, :orange))
savefig(p_herd, "capstone_herd_immunity.png")
println("Saved: capstone_herd_immunity.png")

# ============================================================
# Project 3: End-to-End Data Pipeline
# ============================================================

println("\n" * "=" ^ 60)
println("PROJECT 3: End-to-End Data Pipeline")
println("=" ^ 60)

# Step 1: Generate realistic synthetic data (city weather dataset)
println("\n--- Step 1: Data Generation ---")

using Random
Random.seed!(2026)

n_cities = 8
cities = ["Nairobi", "Lagos", "Cairo", "Casablanca",
          "Johannesburg", "Dakar", "Addis Ababa", "Tunis"]
n_months = 12
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Base temperatures (Celsius) and rainfall (mm) for each city
base_temps = [25, 27, 22, 18, 16, 25, 20, 18]
base_rain = [50, 150, 5, 60, 80, 20, 100, 50]

records = DataFrame[]
for (i, city) in enumerate(cities)
    for (j, month) in enumerate(months)
        # Seasonal variation
        seasonal = 5 * sin(2π * (j - 1) / 12)
        temp = base_temps[i] + seasonal + 2 * randn()
        rain = max(0, base_rain[i] + 30 * sin(2π * (j - 3) / 12) + 20 * randn())
        humidity = clamp(40 + rain / 5 + 10 * randn(), 10, 100)
        wind = max(0, 15 + 5 * randn())

        push!(records, DataFrame(
            city = city,
            month = month,
            month_num = j,
            temperature = round(temp, digits=1),
            rainfall_mm = round(rain, digits=1),
            humidity_pct = round(humidity, digits=1),
            wind_kmh = round(wind, digits=1)
        ))
    end
end

df_weather = vcat(records...)
CSV.write("african_cities_weather.csv", df_weather)
println("Generated weather dataset: $(nrow(df_weather)) rows x $(ncol(df_weather)) cols")
println("Cities: $(join(cities, ", "))")

# Step 2: Data exploration and cleaning
println("\n--- Step 2: Data Exploration ---")
println("Summary statistics:")
display(describe(df_weather))
println()

# Check for anomalies
println("Temperature range: $(minimum(df_weather.temperature)) - $(maximum(df_weather.temperature)) C")
println("Rainfall range: $(minimum(df_weather.rainfall_mm)) - $(maximum(df_weather.rainfall_mm)) mm")

# Group statistics
city_stats = combine(groupby(df_weather, :city),
    :temperature => mean => :avg_temp,
    :temperature => std => :std_temp,
    :rainfall_mm => mean => :avg_rain,
    :humidity_pct => mean => :avg_humidity
)
println("\nCity-level statistics:")
display(sort(city_stats, :avg_temp, rev=true))
println()

# Step 3: Feature engineering
println("\n--- Step 3: Feature Engineering ---")
transform!(df_weather,
    [:temperature, :humidity_pct] =>
        ByRow((t, h) -> t * h / 100) => :heat_index_approx,
    :rainfall_mm =>
        ByRow(r -> r > 100 ? "Heavy" : r > 30 ? "Moderate" : "Light") => :rain_category
)
println("Added heat_index_approx and rain_category columns")

# Step 4: Visualization
println("\n--- Step 4: Visualization ---")

# Temperature heatmap by city and month
temp_wide = unstack(select(df_weather, :city, :month_num, :temperature),
    :city, :month_num, :temperature)
temp_matrix = Matrix(select(temp_wide, Not(:city)))

p_temp = heatmap(months, cities, temp_matrix,
    title="Monthly Temperature by City (C)",
    xlabel="Month", ylabel="City",
    color=:thermal, size=(900, 500))
savefig(p_temp, "capstone_temp_heatmap.png")
println("Saved: capstone_temp_heatmap.png")

# Rainfall bar chart
rain_avg = combine(groupby(df_weather, :city), :rainfall_mm => mean => :avg_rain)
sort!(rain_avg, :avg_rain, rev=true)

p_rain = bar(rain_avg.city, rain_avg.avg_rain,
    title="Average Monthly Rainfall by City",
    xlabel="City", ylabel="Rainfall (mm)",
    color=:steelblue, legend=false, rotation=45)
savefig(p_rain, "capstone_rainfall_bar.png")
println("Saved: capstone_rainfall_bar.png")

# Temperature time series for all cities
p_ts = plot(title="Monthly Temperature Trends",
    xlabel="Month", ylabel="Temperature (C)", legend=:outertopright)
for city in cities
    city_data = filter(:city => ==(city), df_weather)
    plot!(p_ts, city_data.month_num, city_data.temperature,
        label=city, lw=2, marker=:circle, ms=3)
end
savefig(p_ts, "capstone_temp_trends.png")
println("Saved: capstone_temp_trends.png")

# Step 5: Simple prediction model
println("\n--- Step 5: Prediction Model ---")

# Predict temperature from month_num, rainfall, humidity, wind
# Using simple multivariate linear regression (manual)
X_mat = hcat(
    ones(nrow(df_weather)),
    Float64.(df_weather.month_num),
    sin.(2π .* df_weather.month_num ./ 12),
    cos.(2π .* df_weather.month_num ./ 12),
    df_weather.rainfall_mm,
    df_weather.humidity_pct,
    df_weather.wind_kmh
)
y_vec = df_weather.temperature

# Split 80/20
n_train = Int(round(0.8 * nrow(df_weather)))
idx_perm = randperm(nrow(df_weather))
train_perm = idx_perm[1:n_train]
test_perm = idx_perm[n_train+1:end]

X_tr = X_mat[train_perm, :]
y_tr = y_vec[train_perm]
X_te = X_mat[test_perm, :]
y_te = y_vec[test_perm]

# Ordinary least squares
beta_hat = X_tr \ y_tr
y_pred = X_te * beta_hat

rmse = sqrt(mean((y_pred .- y_te).^2))
r2 = 1 - sum((y_pred .- y_te).^2) / sum((y_te .- mean(y_te)).^2)

println("Linear Regression Results:")
println("  RMSE: $(round(rmse, digits=2)) C")
println("  R²:   $(round(r2, digits=4))")

# Predicted vs actual plot
p_pred = scatter(y_te, y_pred, label="Predictions",
    xlabel="Actual Temperature (C)", ylabel="Predicted Temperature (C)",
    title="Predicted vs Actual Temperature",
    ms=4, alpha=0.7)
plot!(p_pred, [minimum(y_te), maximum(y_te)], [minimum(y_te), maximum(y_te)],
    label="Perfect prediction", lw=2, ls=:dash, color=:red)
savefig(p_pred, "capstone_pred_vs_actual.png")
println("Saved: capstone_pred_vs_actual.png")

# Step 6: Summary report
println("\n--- Step 6: Summary Report ---")
println("=" ^ 50)
println("CAPSTONE DATA PIPELINE SUMMARY")
println("=" ^ 50)
println("Dataset: African Cities Weather (synthetic)")
println("  $(nrow(df_weather)) observations, $(ncol(df_weather)) features")
println("  $(n_cities) cities, $(n_months) months")
println()
println("Key findings:")
hottest = city_stats[argmax(city_stats.avg_temp), :]
wettest = city_stats[argmax(city_stats.avg_rain), :]
println("  Hottest city: $(hottest.city) ($(round(hottest.avg_temp, digits=1)) C avg)")
println("  Wettest city: $(wettest.city) ($(round(wettest.avg_rain, digits=1)) mm avg)")
println()
println("Prediction model: Linear regression")
println("  RMSE = $(round(rmse, digits=2)) C, R² = $(round(r2, digits=4))")
println()
println("Output files:")
println("  african_cities_weather.csv")
println("  lotka_volterra_data.csv")
println("  sirv_scenarios.csv")
println("  capstone_*.png (6 figures)")
println("=" ^ 50)

println("\nAll capstone projects complete.")
