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

def generate_inversions(x, y, modes=["negate", "flip", "harmonic"]):
    """
    Generate inverted views using multiple symbolic modes.
    """
    inversions = {}
    for mode in modes:
        ix, iy = invert_geometry(x, y, mode)
        inversions[mode] = (ix, iy)
    return inversions

def visualize_inversions(inversions, title="Inverted Symbolic Views"):
    plt.figure(figsize=(8, 8))
    for mode, (x, y) in inversions.items():
        plt.plot(x, y, label=f"Inversion: {mode}")
    plt.title(title)
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    x, y = generate_spiral(a=1, b=0.15, turns=3)
    inversions = generate_inversions(x, y)
    visualize_inversions(inversions)
