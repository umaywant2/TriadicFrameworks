"""
triadic_space_mapper.py
Visualization utilities for mapping SET (Spin–Charge–Temperature) fields
into combined triadic space representations.

This module provides:
    - 2D scalar field plots (Charge, Temperature)
    - 2D vector field plots (Spin)
    - combined triadic overlays
    - magnitude and gradient visualizations

Dependencies:
    - numpy
    - matplotlib

Intended for use with:
    simulations/core/substrate_solver.py
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def compute_spin_magnitude(S):
    """
    Compute |S| for a Spin field S(x,y,3).
    """
    return np.sqrt(np.sum(S**2, axis=-1))


def compute_charge_gradient(C, dx, dy):
    """
    Compute |∇C| for a scalar Charge field.
    """
    dCx = np.gradient(C, dx, axis=0)
    dCy = np.gradient(C, dy, axis=1)
    return np.sqrt(dCx**2 + dCy**2)


# ------------------------------------------------------------
# Visualization Functions
# ------------------------------------------------------------

def plot_spin_field(S, X=None, Y=None, stride=6, title="Spin Field"):
    """
    Quiver plot of the Spin field (Sx, Sy).
    Only the first two components are visualized.
    """
    Sx = S[..., 0]
    Sy = S[..., 1]

    nx, ny = Sx.shape

    if X is None or Y is None:
        x = np.arange(nx)
        y = np.arange(ny)
        X, Y = np.meshgrid(x, y, indexing="ij")

    plt.figure(figsize=(6, 6))
    plt.quiver(
        X[::stride, ::stride],
        Y[::stride, ::stride],
        Sx[::stride, ::stride],
        Sy[::stride, ::stride],
        color="black",
        scale=50
    )
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()


def plot_scalar_field(field, title="Scalar Field", cmap="viridis"):
    """
    Generic 2D scalar field visualization.
    """
    plt.figure(figsize=(6, 5))
    im = plt.imshow(field.T, origin="lower", cmap=cmap)
    plt.colorbar(im)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def plot_triadic_overlay(S, C, T, dx=1.0, dy=1.0, title="Triadic Overlay"):
    """
    Combined visualization:
        - Spin magnitude → red channel
        - Charge gradient magnitude → green channel
        - Temperature → blue channel

    Produces an RGB composite image.
    """
    S_mag = compute_spin_magnitude(S)
    C_grad = compute_charge_gradient(C, dx, dy)
    T_norm = T.copy()

    # Normalize each component to [0,1]
    def normalize(arr):
        arr = arr - arr.min()
        if arr.max() > 0:
            arr = arr / arr.max()
        return arr

    R = normalize(S_mag)
    G = normalize(C_grad)
    B = normalize(T_norm)

    rgb = np.stack([R, G, B], axis=-1)

    plt.figure(figsize=(6, 6))
    plt.imshow(rgb, origin="lower")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# ------------------------------------------------------------
# High-Level Convenience Wrapper
# ------------------------------------------------------------

def visualize_triadic_state(state, grid, prefix="Triadic State"):
    """
    Convenience function to visualize all three SET fields:
        - Spin vector field
        - Charge scalar field
        - Temperature scalar field
        - Combined triadic overlay
    """
    S = state.S
    C = state.C
    T = state.T

    # Spin field
    plot_spin_field(S, title=f"{prefix}: Spin Field")

    # Charge field
    plot_scalar_field(C, title=f"{prefix}: Charge Field", cmap="RdBu")

    # Temperature field
    plot_scalar_field(T, title=f"{prefix}: Temperature Field", cmap="inferno")

    # Combined triadic overlay
    plot_triadic_overlay(
        S, C, T,
        dx=grid.dx,
        dy=grid.dy,
        title=f"{prefix}: Triadic Overlay"
    )

