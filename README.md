# QuantumBreaths1D

A numerical simulation of the one-dimensional Gross–Pitaevskii equation (GPE) under a periodic potential using the split-step Fourier method. This project models the evolution of a normalised Bose–Einstein condensate wavefunction in a nonlinear and spatially modulated environment.

## 💡 Features

- Spatial domain: \([-L/2, L/2]\)
- Time evolution via the split-step Fourier method
- Periodic potential: \( V(x) = V_0 \cos^2\left( \frac{\pi x}{a} \right) \)
- Gaussian initial wavefunction
- Normalisation maintained at each time step
- Final density visualisation

## 🧮 Parameters

- `N`: Number of spatial grid points
- `L`: Length of the spatial domain
- `dx`: Spatial resolution
- `dt`: Time step
- `g`: Interaction coefficient
- `V0`: Depth of the periodic potential
- `a`: Period of the potential
- `steps`: Total number of time steps

## 📊 Output

A plot showing the final probability density \( |\psi(x)|^2 \), revealing modulations due to the nonlinear dynamics and external periodic potential.

## 📁 Requirements

- `numpy`
- `matplotlib`

Install via:
```bash
pip install numpy matplotlib
