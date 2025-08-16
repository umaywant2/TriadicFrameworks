# 🧪 Lab 1: Casimir Resonance

## 🎯 Objective  
Demonstrate how Casimir forces emerge from triadic boundary conditions—interpreting vacuum fluctuations as phase-locked standing waves.

---

## 📐 Core Equation



\[
F = -\frac{\pi^2 \hbar c}{240 d^4}
\]



- \( F \): Casimir force  
- \( d \): plate separation  
- Interpreted as: destructive interference of virtual modes outside the plates

---

## 🧰 Prototype: Casimir Visualizer

```python
import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0.1e-6, 2e-6, 100)  # plate separation in meters
F = - (np.pi**2 * 1.0545718e-34 * 3e8) / (240 * d**4)

plt.figure(figsize=(8,4))
plt.plot(d * 1e6, F, color='indigo')
plt.title('Casimir Force vs Plate Separation')
plt.xlabel('Separation (μm)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.tight_layout()
plt.show()
