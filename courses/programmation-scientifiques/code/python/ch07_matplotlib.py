"""
Chapter 7: Matplotlib — Scientific Visualization
"""
import numpy as np
import matplotlib.pyplot as plt

# === Line plot ===
x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, np.sin(x), 'b-', lw=2, label='sin(x)')
ax.plot(x, np.cos(x), 'r--', lw=2, label='cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('ch07_trig.pdf')
plt.show()

# === Scatter plot ===
np.random.seed(42)
x = np.random.normal(0, 1, 200)
y = 2 * x + np.random.normal(0, 0.5, 200)
fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(x, y, alpha=0.5, c='steelblue', s=20)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter Plot with Linear Trend')
plt.savefig('ch07_scatter.pdf')
plt.show()

# === Histogram ===
data = np.random.normal(170, 10, 1000)
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(data, bins=30, edgecolor='black', alpha=0.7, color='steelblue')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Count')
ax.set_title('Height Distribution (simulated)')
ax.axvline(np.mean(data), color='red', linestyle='--', label=f'Mean = {np.mean(data):.1f}')
ax.legend()
plt.savefig('ch07_hist.pdf')
plt.show()

# === Subplots ===
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
t = np.linspace(0, 5, 200)
axes[0, 0].plot(t, np.exp(-t), 'b-')
axes[0, 0].set_title('Exponential Decay')
axes[0, 1].plot(t, np.exp(-0.5*t) * np.sin(5*t), 'r-')
axes[0, 1].set_title('Damped Oscillation')
axes[1, 0].plot(t, t**2, 'g-')
axes[1, 0].set_title('Quadratic')
axes[1, 1].plot(t, np.log(1 + t), 'm-')
axes[1, 1].set_title('Logarithm')
for ax in axes.flat:
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ch07_subplots.pdf')
plt.show()

# === Projectile motion ===
g = 9.81
v0 = 20.0
fig, ax = plt.subplots(figsize=(8, 5))
for angle_deg in [30, 45, 60, 75]:
    theta = np.radians(angle_deg)
    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.linspace(0, t_flight, 100)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    ax.plot(x, y, label=f'{angle_deg}°')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title(f'Projectile Motion (v₀ = {v0} m/s)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim(bottom=0)
plt.savefig('ch07_projectile.pdf')
plt.show()
