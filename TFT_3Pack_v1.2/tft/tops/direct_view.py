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

def generate_views(x, y, angles=[0, 90, 180, 270]):
    """
    Generate rotated views of an object.
    angles: list of angles in degrees
    """
    views = {}
    for angle in angles:
        rx, ry = rotate_object(x, y, angle)
        views[angle] = (rx, ry)
    return views

def visualize_views(views, title="Direct Multi-Angle Views"):
    plt.figure(figsize=(8, 8))
    for angle, (x, y) in views.items():
        plt.plot(x, y, label=f"{angle}°")
    plt.title(title)
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from mirror_geometry import generate_spiral
    x, y = generate_spiral(a=1, b=0.15, turns=3)
    views = generate_views(x, y)
    visualize_views(views)
