import numpy as np
import matplotlib.pyplot as plt

# 1) Parameters and Grid Definition
N  = 1024                      # Number of spatial points
L  = 10.0                      # Spatial domain: [-L/2, L/2]
dx = L / N                     # Spatial step size
x  = np.linspace(-L/2, L/2, N) # Spatial axis
dt = 0.0005                    # Time step
g  = 1.0                       # Polariton–polariton interaction coefficient
V0 = 10.0                      # Depth of the periodic potential
a  = 2.0                       # Period of the periodic potential
steps = 5000                   # Total number of time evolution steps

# 2) Definition of the Periodic Potential
# V(x) = V0 * cos^2(pi x / a)
V = V0 * np.cos(np.pi * x / a)**2

# 3) Initial Wavefunction: Gaussian Profile, to be normalised
psi = np.exp(-x**2).astype(np.complex128)
psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)

# 4) Fourier Space Definition
k  = 2 * np.pi * np.fft.fftfreq(N, d=dx)
k2 = k**2

# 5) Time Evolution (Split-Step Fourier Method)
for _ in range(steps):
    # 5a) Nonlinear + Potential Step (half step)
    psi *= np.exp(-1j * (V + g * np.abs(psi)**2) * dt / 2)

    # 5b) Kinetic Step (in Fourier space, half step)
    psi_k = np.fft.fft(psi)
    psi_k *= np.exp(-1j * k2 * dt / 2)
    psi = np.fft.ifft(psi_k)

    # 5c) Nonlinear + Potential Step (second half step)
    psi *= np.exp(-1j * (V + g * np.abs(psi)**2) * dt / 2)

    # 5d) Norm Preservation (Renormalisation)
    psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)

# 6) Compute and Visualise the Density
density = np.abs(psi)**2

plt.figure(figsize=(8, 4))
plt.plot(x, density, color='tab:blue', linewidth=1.5)
plt.title("1D GPE: Density Modulation in a Periodic Potential")
plt.xlabel("Position $x$")
plt.ylabel("Density $|\psi(x)|^2$")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
