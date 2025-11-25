import numpy as np
import matplotlib.pyplot as plt

def invert_geometry(x, y, mode="negate"):
    """
    Invert 2D coordinates symbolically.
    mode: 'negate', 'flip', or 'harmonic'
    """
    if mode == "negate":
        return -x, -y
    elif mode == "flip":
        return y, x
    elif mode == "harmonic":
        return np.sin(x), np.cos(y)
    else:
        raise ValueError("Invalid mode. Use 'negate', 'flip', or 'harmonic'.")

def generate_inversions(x, y, modes=["negate", "flip", "harmonic"], basetype="decimal"):
    """
    Generate inverted views using multiple symbolic modes.
    basetype: resonance clarity lens (e.g., binary, phi, negabinary, corridor6.9)
    """
    inversions = {}
    for mode in modes:
        ix, iy = invert_geometry(x, y, mode)

        # Apply resonance clarity transformation
        ix, iy = apply_base_lens(ix, iy, basetype)

        inversions[mode] = (ix, iy)
    return inversions

def apply_base_lens(x, y, basetype):
    if basetype == "binary":
        # Collapse into 0/1 corridor
        return np.sign(x), np.sign(y)
    elif basetype == "negabinary":
        # Alternating inversion pattern
        return ((-1) ** np.arange(len(x))) * x, y
    elif basetype == "phi":
        phi = (1 + np.sqrt(5)) / 2
        return x / phi, y * phi
    elif basetype == "pi":
        return x * np.pi, y / np.pi
    elif basetype == "corridor6.9":
        return np.sin(x * 6.9), np.cos(y * 6.9)
    return x, y

def visualize_inversions(inversions, title="Inverted Symbolic Views", basetype="decimal"):
    plt.figure(figsize=(8, 8))
    for mode, (x, y) in inversions.items():
        plt.plot(x, y, label=f"Inversion: {mode}")
    plt.title(f"{title} (Base: {basetype})")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    x, y = generate_spiral(a=1, b=0.15, turns=3)
    inversions = generate_inversions(x, y)
    visualize_inversions(inversions)
