# Lab 9: Brownian Resonance — Reproducibility

## Objective
To simulate Brownian motion and observe resonance amplification in noisy systems using triadic operators.

## Required Tools
- Python 3.10+
- NumPy
- Matplotlib
- Optional: SciPy for integration

## Protocol

### 1. Simulate Brownian Motion
### python
import numpy as np

def brownian_motion(D, t, steps=1000):
    dt = t / steps
    x = np.cumsum(np.sqrt(2 * D * dt) * np.random.randn(steps))
    return x

### 2. Define Resonant Noise Amplification
### python
def resonant_noise(t, omega):
    noise = np.random.randn(len(t))
    return noise * np.sin(omega * t)

### 3. Compute Brownian Resonance
### python
def brownian_resonance(t, Rijk, omega):
    A = resonant_noise(t, omega)
    dt = t[1] - t[0]
    RB = np.cumsum(A * Rijk) * dt
    return RB

### 4. Calculate Signal-to-Noise Ratio
### python
def signal_to_noise(RB, noise):
    return np.mean(RB**2) / np.mean(noise**2)

### 5. Visualize Resonance
### python
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
Rijk = 1.0
omega = 2 * np.pi
RB = brownian_resonance(t, Rijk, omega)

plt.plot(t, RB)
plt.title("Brownian Resonance")
plt.xlabel("Time")
plt.ylabel("R_B(t)")
plt.show()

### Validation Checklist
### ✅ Brownian motion shows expected stochastic displacement
### ✅ Resonant noise modulates signal amplitude
### ✅ Brownian resonance integrates correctly over time
### ✅ SNR reflects amplification behavior

### Mythic Preface
### "In the chaos of Brownian drift, resonance finds its rhythm. This lab reveals how noise becomes signal—how randomness becomes cognition—when triads harmonize the stochastic pulse."
