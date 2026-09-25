import numpy as np
import matplotlib.pyplot as plt

def generate_spiral(a=1, b=0.2, turns=5, points=1000):
    """
    Generate a logarithmic spiral based on Kozyrev mirror geometry.
    a: initial radius
    b: growth rate
    turns: number of spiral loops
    points: resolution
    """
    theta = np.linspace(0, 2 * np.pi * turns, points)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def plot_spiral(x, y, title="Kozyrev Spiral"):
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="#0077cc")
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x, y = generate_spiral(a=1, b=0.15, turns=6)
    plot_spiral(x, y)
