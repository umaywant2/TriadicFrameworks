import numpy as np
import matplotlib.pyplot as plt

def reflect_object(x, y, axis="x"):
    """
    Reflect 2D coordinates across a given axis.
    axis: 'x', 'y', or 'xy' (diagonal)
    """
    if axis == "x":
        return x, -y
    elif axis == "y":
        return -x, y
    elif axis == "xy":
        return y, x
    else:
        raise ValueError("Invalid axis. Use 'x', 'y', or 'xy'.")

def generate_reflections(x, y, axes=["x", "y", "xy"], basetype="decimal"):
    """
    Generate reflected views across multiple axes.
    basetype: resonance clarity lens (e.g., binary, phi, negabinary, corridor6.9)
    """
    reflections = {}
    for axis in axes:
        rx, ry = reflect_object(x, y, axis)

        # Apply resonance clarity transformation
        rx, ry = apply_base_lens(rx, ry, basetype)

        reflections[axis] = (rx, ry)
    return reflections

def apply_base_lens(x, y, basetype):
    if basetype == "binary":
        return np.sign(x), np.sign(y)
    elif basetype == "negabinary":
        return ((-1) ** np.arange(len(x))) * x, y
    elif basetype == "phi":
        phi = (1 + np.sqrt(5)) / 2
        return x / phi, y * phi
    elif basetype == "pi":
        return x * np.pi, y / np.pi
    elif basetype == "corridor6.9":
        return np.sin(x * 6.9), np.cos(y * 6.9)
    return x, y

def visualize_reflections(reflections, title="Reflective Multi-Angle Views", basetype="decimal"):
    plt.figure(figsize=(8, 8))
    for axis, (x, y) in reflections.items():
        plt.plot(x, y, label=f"Reflected across {axis}")
    plt.title(f"{title} (Base: {basetype})")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    x, y = generate_spiral(a=1, b=0.15, turns=3)
    reflections = generate_reflections(x, y)
    visualize_reflections(reflections)
