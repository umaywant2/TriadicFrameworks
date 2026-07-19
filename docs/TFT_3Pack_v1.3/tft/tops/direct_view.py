import numpy as np
import matplotlib.pyplot as plt

def rotate_object(x, y, angle_deg):
    """
    Rotate 2D coordinates by a given angle.
    x, y: original coordinates
    angle_deg: rotation angle in degrees
    """
    angle_rad = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    coords = np.vstack((x, y))
    rotated = rotation_matrix @ coords
    return rotated[0], rotated[1]

def generate_views(x, y, angles=[0, 90, 180, 270], basetype="decimal"):
    """
    Generate rotated views of an object.
    angles: list of angles in degrees
    basetype: resonance clarity lens (e.g., binary, phi, negabinary, corridor6.9)
    """
    views = {}
    for angle in angles:
        rx, ry = rotate_object(x, y, angle)

        # Apply resonance clarity transformation
        rx, ry = apply_base_lens(rx, ry, basetype)

        views[angle] = (rx, ry)
    return views

def apply_base_lens(x, y, basetype):
    """
    Transform coordinates according to the chosen base lens.
    """
    if basetype == "binary":
        # Collapse into 0/1 corridor
        return np.sign(x), np.sign(y)

    elif basetype == "negabinary":
        # Alternate inversion pattern
        return ((-1) ** np.arange(len(x))) * x, y

    elif basetype == "phi":
        # Golden ratio scaling
        phi = (1 + np.sqrt(5)) / 2
        return x / phi, y * phi

    elif basetype == "pi":
        return x * np.pi, y / np.pi

    elif basetype == "corridor6.9":
        # Speculative resonance corridor
        return np.sin(x * 6.9), np.cos(y * 6.9)

    # Default: no transformation
    return x, y

def visualize_views(views, title="Direct Multi-Angle Views", basetype="decimal"):
    plt.figure(figsize=(8, 8))
    for angle, (x, y) in views.items():
        plt.plot(x, y, label=f"{angle}°")
    plt.title(f"{title} (Base: {basetype})")
    plt.axis("equal")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    x, y = generate_spiral(a=1, b=0.15, turns=3)
    views = generate_views(x, y)
    visualize_views(views)
