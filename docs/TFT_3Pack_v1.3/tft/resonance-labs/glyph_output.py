import matplotlib.pyplot as plt
import numpy as np

def render_overlay(x, y, field, title="Spiral Resonance Overlay"):
    """
    Render spiral geometry with harmonic field overlay.
    x, y: spiral coordinates
    field: temporal distortion field (from time_shift)
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="#0077cc", label="Spiral Geometry")
    plt.scatter(x, y, c=field, cmap="plasma", s=2, label="Resonance Field")
    plt.title(title)
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    from resonance_model import generate_harmonic_field
    from time_shift import simulate_time_shift

    x, y = generate_spiral(a=1, b=0.15, turns=6)
    _, field = generate_harmonic_field(base_freq=1.0, loops=5)
    shifted = simulate_time_shift(field, entropy_mode="recursive", delay_factor=0.2)
    render_overlay(x, y, shifted)
