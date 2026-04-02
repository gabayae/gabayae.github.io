"""
Chapter 6: Data Visualization with Plots.jl and Makie.jl
=========================================================
Comprehensive examples of data visualization in Julia using
Plots.jl (with GR backend) and CairoMakie.jl.
"""

# ============================================================
# Part 1: Plots.jl
# ============================================================

using Plots

println("=== Plots.jl Examples ===")

# --- Basic line plot ---
x = range(0, 2π, length=200)
y1 = sin.(x)
y2 = cos.(x)

p1 = plot(x, y1, label="sin(x)", lw=2, title="Trigonometric Functions")
plot!(p1, x, y2, label="cos(x)", lw=2, ls=:dash)
xlabel!(p1, "x")
ylabel!(p1, "y")
savefig(p1, "plots_line.png")
println("Saved: plots_line.png")

# --- Scatter plot ---
n = 100
x_scatter = randn(n)
y_scatter = 2 .* x_scatter .+ 0.5 .* randn(n)
groups = rand(["A", "B", "C"], n)

p2 = scatter(x_scatter, y_scatter, group=groups,
    title="Scatter Plot with Groups",
    xlabel="x", ylabel="y",
    markersize=5, alpha=0.7)
savefig(p2, "plots_scatter.png")
println("Saved: plots_scatter.png")

# --- Bar chart ---
categories = ["Julia", "Python", "R", "Matlab", "C++"]
values = [92, 88, 75, 65, 78]

p3 = bar(categories, values,
    title="Language Scores",
    ylabel="Score",
    color=:steelblue,
    legend=false)
savefig(p3, "plots_bar.png")
println("Saved: plots_bar.png")

# --- Histogram ---
data = randn(1000)
p4 = histogram(data, bins=30,
    title="Normal Distribution (n=1000)",
    xlabel="Value", ylabel="Count",
    fillalpha=0.6, color=:teal, legend=false)
savefig(p4, "plots_histogram.png")
println("Saved: plots_histogram.png")

# --- Heatmap ---
using LinearAlgebra
A = [1/(i+j-1) for i in 1:10, j in 1:10]  # Hilbert matrix
p5 = heatmap(A, title="Hilbert Matrix Heatmap",
    xlabel="Column", ylabel="Row",
    color=:viridis)
savefig(p5, "plots_heatmap.png")
println("Saved: plots_heatmap.png")

# --- Contour plot ---
f(x, y) = sin(x) * cos(y)
x_grid = range(-π, π, length=100)
y_grid = range(-π, π, length=100)
z = [f(xi, yi) for yi in y_grid, xi in x_grid]

p6 = contourf(x_grid, y_grid, z,
    title="Contour: sin(x)cos(y)",
    xlabel="x", ylabel="y",
    color=:coolwarm, levels=20)
savefig(p6, "plots_contour.png")
println("Saved: plots_contour.png")

# --- Subplots layout ---
p_layout = plot(p1, p2, p3, p4, layout=(2, 2), size=(1000, 800))
savefig(p_layout, "plots_layout.png")
println("Saved: plots_layout.png")

# --- 3D surface plot ---
x3d = range(-2, 2, length=50)
y3d = range(-2, 2, length=50)
z3d = [exp(-(xi^2 + yi^2)) for yi in y3d, xi in x3d]

p7 = surface(x3d, y3d, z3d,
    title="Gaussian Surface",
    xlabel="x", ylabel="y", zlabel="z",
    color=:plasma)
savefig(p7, "plots_surface.png")
println("Saved: plots_surface.png")

# --- Animation ---
println("Creating animation...")
anim = @animate for t in range(0, 2π, length=60)
    plot(x, sin.(x .+ t), label="sin(x + t)",
         ylims=(-1.5, 1.5), title="t = $(round(t, digits=2))",
         lw=2, color=:crimson)
end
gif(anim, "plots_wave.gif", fps=15)
println("Saved: plots_wave.gif")

# ============================================================
# Part 2: CairoMakie.jl
# ============================================================

using CairoMakie

println("\n=== CairoMakie Examples ===")

# --- Basic line plot ---
fig1 = Figure(size=(800, 500))
ax1 = Axis(fig1[1, 1],
    title="Trigonometric Functions (Makie)",
    xlabel="x", ylabel="y")
lines!(ax1, collect(x), sin.(collect(x)), label="sin(x)", linewidth=2)
lines!(ax1, collect(x), cos.(collect(x)), label="cos(x)",
       linewidth=2, linestyle=:dash)
axislegend(ax1)
save("makie_line.png", fig1)
println("Saved: makie_line.png")

# --- Scatter plot with colormap ---
fig2 = Figure(size=(800, 600))
ax2 = Axis(fig2[1, 1], title="Scatter with Colormap",
    xlabel="x", ylabel="y")
xs = randn(200)
ys = randn(200)
cs = sqrt.(xs.^2 .+ ys.^2)
sc = scatter!(ax2, xs, ys, color=cs, colormap=:viridis,
    markersize=10)
Colorbar(fig2[1, 2], sc, label="Distance from origin")
save("makie_scatter.png", fig2)
println("Saved: makie_scatter.png")

# --- Bar plot ---
fig3 = Figure(size=(700, 500))
ax3 = Axis(fig3[1, 1], title="Language Popularity",
    xlabel="Language", ylabel="Score",
    xticks=(1:5, ["Julia", "Python", "R", "Matlab", "C++"]))
barplot!(ax3, 1:5, [92, 88, 75, 65, 78],
    color=[:royalblue, :gold, :forestgreen, :coral, :purple])
save("makie_bar.png", fig3)
println("Saved: makie_bar.png")

# --- Heatmap ---
fig4 = Figure(size=(700, 600))
ax4 = Axis(fig4[1, 1], title="Correlation Heatmap",
    xlabel="Variable", ylabel="Variable")
data_matrix = randn(5, 100)
corr = [sum(data_matrix[i, :] .* data_matrix[j, :]) /
        (norm(data_matrix[i, :]) * norm(data_matrix[j, :])) for i in 1:5, j in 1:5]
hm = heatmap!(ax4, corr, colormap=:RdBu)
Colorbar(fig4[1, 2], hm, label="Correlation")
save("makie_heatmap.png", fig4)
println("Saved: makie_heatmap.png")

# --- Multi-panel figure ---
fig5 = Figure(size=(1200, 800))

# Panel 1: Line plot
ax_a = Axis(fig5[1, 1], title="(a) Damped Oscillation")
t_vals = range(0, 10, length=300)
lines!(ax_a, collect(t_vals), exp.(-0.3 .* collect(t_vals)) .* sin.(5 .* collect(t_vals)),
       linewidth=2, color=:crimson)

# Panel 2: Histogram
ax_b = Axis(fig5[1, 2], title="(b) Distribution")
hist!(ax_b, randn(5000), bins=50, color=(:steelblue, 0.7))

# Panel 3: Surface
ax_c = Axis3(fig5[2, 1], title="(c) 3D Surface",
    xlabel="x", ylabel="y", zlabel="z")
xg = range(-3, 3, length=50)
yg = range(-3, 3, length=50)
zg = [sin(sqrt(xi^2 + yi^2)) for xi in xg, yi in yg]
surface!(ax_c, collect(xg), collect(yg), zg, colormap=:turbo)

# Panel 4: Contour
ax_d = Axis(fig5[2, 2], title="(d) Filled Contour")
contourf!(ax_d, collect(xg), collect(yg), zg, colormap=:thermal, levels=15)

save("makie_multipanel.png", fig5)
println("Saved: makie_multipanel.png")

# --- Statistical visualization ---
fig6 = Figure(size=(900, 400))

# Box plot
ax_box = Axis(fig6[1, 1], title="Box Plot",
    xticks=(1:3, ["Group A", "Group B", "Group C"]))
for (i, mu) in enumerate([0, 1, 2])
    boxplot!(ax_box, fill(i, 50), randn(50) .+ mu)
end

# Violin plot
ax_viol = Axis(fig6[1, 2], title="Violin Plot",
    xticks=(1:3, ["X", "Y", "Z"]))
for (i, sigma) in enumerate([0.5, 1.0, 2.0])
    violin!(ax_viol, fill(i, 200), sigma .* randn(200))
end

save("makie_stats.png", fig6)
println("Saved: makie_stats.png")

println("\nAll visualization examples complete.")
println("Generated PNG files in the current directory.")
