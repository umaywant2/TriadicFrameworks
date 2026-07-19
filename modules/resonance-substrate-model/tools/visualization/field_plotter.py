"""
field_plotter.py
General visualization utilities for SET (Spin–Charge–Temperature) fields.

Provides:
    - scalar field plotting
    - vector field plotting
    - magnitude maps
    - gradient maps

Dependencies:
    - numpy
    - matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Scalar Field Plotting
# ------------------------------------------------------------

def plot_scalar(field, title="Scalar Field", cmap="viridis"):
    """
    Plot a 2D scalar field using imshow.
    """
    plt.figure(figsize=(6, 5))
    im = plt.imshow(field.T, origin="lower", cmap=cmap)
    plt.colorbar(im)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def plot_scalar_gradient(field, dx=1.0, dy=1.0, title="Scalar Gradient Magnitude"):
    """
    Plot |∇field| for a scalar field.
    """
    dfx = np.gradient(field, dx, axis=0)
    dfy = np.gradient(field, dy, axis=1)
    mag = np.sqrt(dfx**2 + dfy**2)

    plot_scalar(mag, title=title, cmap="magma")


# ------------------------------------------------------------
# Vector Field Plotting
# ------------------------------------------------------------

def plot_vector(field, stride=6, title="Vector Field"):
    """
    Quiver plot for a 2D vector field with shape (nx, ny, 2).
    """
    Vx = field[..., 0]
    Vy = field[..., 1]

    nx, ny = Vx.shape
    X, Y = np.meshgrid(np.arange(nx), np.arange(ny), indexing="ij")

    plt.figure(figsize=(6, 6))
    plt.quiver(
        X[::stride, ::stride],
        Y[::stride, ::stride],
        Vx[::stride, ::stride],
        Vy[::stride, ::stride],
        color="black",
        scale=50
    )
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()


def plot_vector_magnitude(field, title="Vector Magnitude", cmap="inferno"):
    """
    Plot |field| for a vector field.
    """
    mag = np.sqrt(np.sum(field**2, axis=-1))
    plot_scalar(mag, title=title, cmap=cmap)


# ------------------------------------------------------------
# SET-Specific Helpers
# ------------------------------------------------------------

def plot_spin(S, title="Spin Field", stride=6):
    """
    Visualize the Spin field S(x,y,3) using its x,y components.
    """
    plot_vector(S[..., :2], stride=stride, title=title)


def plot_spin_magnitude(S, title="Spin Magnitude"):
    """
    Visualize |S|.
    """
    mag = np.sqrt(np.sum(S**2, axis=-1))
    plot_scalar(mag, title=title, cmap="plasma")


def plot_charge(C, title="Charge Field"):
    plot_scalar(C, title=title, cmap="RdBu")


def plot_temperature(T, title="Temperature Field"):
    plot_scalar(T, title=title, cmap="inferno")

