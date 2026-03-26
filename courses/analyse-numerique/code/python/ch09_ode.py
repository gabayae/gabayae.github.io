"""
Chapter 9: Numerical Solution of ODEs
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(f, t0, T, y0, h):
    t = np.arange(t0, T+h, h)
    y = np.zeros((len(t), len(np.atleast_1d(y0))))
    y[0] = y0
    for n in range(len(t)-1):
        y[n+1] = y[n] + h * np.array(f(t[n], y[n]))
    return t, y

def rk4(f, t0, T, y0, h):
    t = np.arange(t0, T+h, h)
    y = np.zeros((len(t), len(np.atleast_1d(y0))))
    y[0] = y0
    for n in range(len(t)-1):
        k1 = np.array(f(t[n], y[n]))
        k2 = np.array(f(t[n]+h/2, y[n]+h*k1/2))
        k3 = np.array(f(t[n]+h/2, y[n]+h*k2/2))
        k4 = np.array(f(t[n]+h, y[n]+h*k3))
        y[n+1] = y[n] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return t, y

# Test: y' = -y, y(0) = 1
f = lambda t, y: -y
print("=== y' = -y, y(0) = 1 ===")
print(f"{'h':>8} {'Euler':>12} {'Err Euler':>12} {'RK4':>15} {'Err RK4':>12}")
for h in [0.1, 0.05, 0.01]:
    t_e, y_e = euler(f, 0, 1, [1.0], h)
    t_r, y_r = rk4(f, 0, 1, [1.0], h)
    exact_val = np.exp(-1)
    print(f"{h:8.3f} {y_e[-1,0]:12.6f} {abs(y_e[-1,0]-exact_val):12.2e} "
          f"{y_r[-1,0]:15.10f} {abs(y_r[-1,0]-exact_val):12.2e}")

# Plot
t_e, y_e = euler(f, 0, 1, [1.0], 0.1)
t_r, y_r = rk4(f, 0, 1, [1.0], 0.1)
exact = np.exp(-t_e)

plt.figure(figsize=(8, 5))
plt.plot(t_e, exact, 'k-', lw=2, label='Exact')
plt.plot(t_e, y_e, 'ro--', label='Euler')
plt.plot(t_r, y_r, 'bs-', label='RK4')
plt.legend(); plt.xlabel('t'); plt.ylabel('y')
plt.title("Euler vs RK4"); plt.savefig("ch09_ode.pdf"); plt.show()

# Lorenz system
def lorenz(t, y, sigma=10, rho=28, beta=8/3):
    return np.array([
        sigma * (y[1] - y[0]),
        y[0] * (rho - y[2]) - y[1],
        y[0] * y[1] - beta * y[2]
    ])

t_lor, y_lor = rk4(lorenz, 0, 50, [1.0, 1.0, 1.0], 0.01)
print(f"\nLorenz at t=50: x={y_lor[-1,0]:.4f}, y={y_lor[-1,1]:.4f}, z={y_lor[-1,2]:.4f}")
