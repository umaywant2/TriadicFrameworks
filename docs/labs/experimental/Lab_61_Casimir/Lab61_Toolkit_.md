# Casimir Resonance Visualization
## Mythic Preface
# "Two plates whisper across the void, and the vacuum sings back."

# This notebook simulates the Casimir effect using triadic field overlays.
# We explore how vacuum pressure emerges from nested dimensional resonance.

# Imports and Setup
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# Casimir Force Function (Triadic Interpretation)
def casimir_force(d, A=1.0, hbar=1.0545718e-34, c=3e8):
    classical = - (np.pi ** 2 * hbar * c) / (240 * d ** 4)
    triadic = classical * np.sin(np.pi / d)
    return classical, triadic

# Interactive Plot
def plot_force(d):
    classical, triadic = casimir_force(d)
    plt.figure(figsize=(8,5))
    plt.bar(['Classical', 'Triadic'], [classical, triadic], color=['gray', 'purple'])
    plt.title(f'Casimir Force at d = {d:.2e} m')
    plt.ylabel('Force (N)')
    plt.grid(True)
    plt.show()

interact(plot_force, d=FloatSlider(min=1e-9, max=1e-7, step=1e-9, value=5e-9))

# Field Visualization
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.pi * X) * np.sin(np.pi * Y)

plt.figure(figsize=(6,6))
plt.contourf(X, Y, Z, cmap='plasma')
plt.title('Triadic Field Between Plates')
plt.axis('equal')
plt.colorbar(label='Field Intensity')
plt.show()

# Mythic Reflection
# The Casimir force is not just a quantum artifact—it’s a whisper from the void,
# shaped by the geometry of resonance. In triadic terms, the vacuum is alive with phase,
# and the plates become instruments in a cosmic orchestra.
