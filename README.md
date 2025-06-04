# 1D-GPE-Periodic-Lattice-Simulation

**Simulation of Nonlinear Quantum Dynamics in a Periodic Lattice via the 1D Gross–Pitaevskii Equation**

A spectral simulation of the 1D time-dependent Gross–Pitaevskii equation (GPE) in a periodic potential. Models condensate dynamics with nonlinear interaction and lattice modulation via the split-step Fourier method.

## 📐 Physical Model

We simulate the following dimensionless form of the GPE:

\[
i \frac{\partial \psi(x,t)}{\partial t} = \left[ -\frac{1}{2} \frac{\partial^2}{\partial x^2} + V_0 \cos^2\left( \frac{\pi x}{a} \right) + g |\psi(x,t)|^2 \right] \psi(x,t)
\]

Where:
- \( \psi(x, t) \): condensate wavefunction, normalised to 1
- \( V_0 \): depth of the periodic potential
- \( a \): period of the lattice
- \( g \): nonlinear interaction coefficient

## 🧪 Numerical Method

- **Spatial discretisation:** \( N = 1024 \) grid points over domain \( x \in [-L/2, L/2] \)
- **Time evolution:** split-step Fourier method (second-order)
- **Renormalisation:** wavefunction norm preserved at each step

## 🔧 Parameters (defaults)

| Parameter | Meaning                            | Value   |
|-----------|------------------------------------|---------|
| N         | Number of spatial grid points      | 1024    |
| L         | Spatial domain size                | 10.0    |
| dx        | Spatial step size                  | L / N   |
| dt        | Time step                          | 0.0005  |
| g         | Nonlinearity coefficient           | 1.0     |
| V0        | Potential depth                    | 10.0    |
| a         | Potential period                   | 2.0     |
| steps     | Time steps for evolution           | 5000    |

## 📈 Output

- Plots the final density profile \( |\psi(x)|^2 \)
- Reveals nonlinear density modulation due to interaction and lattice effects

![density_plot](example_output.png)

## ▶️ Usage

Install dependencies:

```bash
pip install numpy matplotlib
```
## Run the simulation:
```bash
python gpe_1d_periodic.py
```

