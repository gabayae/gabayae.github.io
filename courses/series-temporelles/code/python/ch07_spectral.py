"""
Chapter 7: Spectral Analysis
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram, welch

# Simulate AR(2) with spectral peak
np.random.seed(42)
n = 1024
eps = np.random.normal(0, 1, n)
x = np.zeros(n)
phi1, phi2 = 1.5, -0.85
for t in range(2, n):
    x[t] = phi1*x[t-1] + phi2*x[t-2] + eps[t]

# Raw periodogram
freq_p, Pxx_p = periodogram(x, fs=1, scaling='density')

# Smoothed periodogram (Welch)
freq_w, Pxx_w = welch(x, fs=1, nperseg=256, scaling='density')

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].semilogy(freq_p, Pxx_p, lw=0.5)
axes[0].set_title('Raw Periodogram')
axes[0].set_xlabel('Frequency')

axes[1].semilogy(freq_w, Pxx_w, lw=1.5, color='red')
axes[1].set_title('Smoothed Periodogram (Welch)')
axes[1].set_xlabel('Frequency')
plt.tight_layout()
plt.savefig('ch07_spectral.pdf')
plt.show()

# Theoretical AR(2) spectrum
omega = np.linspace(0.01, np.pi, 500)
phi_z = 1 - phi1*np.exp(-1j*omega) - phi2*np.exp(-2j*omega)
f_theo = 1 / (2*np.pi * np.abs(phi_z)**2)

plt.figure(figsize=(8, 4))
plt.plot(omega, f_theo, 'b-', label='Theoretical')
plt.title('Theoretical AR(2) Spectrum')
plt.xlabel('omega'); plt.ylabel('f(omega)')
plt.legend()
plt.savefig('ch07_spectrum_theo.pdf')
plt.show()
