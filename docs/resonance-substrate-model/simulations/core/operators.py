"""
operators.py
Low‑level numerical operators for the SET (Spin–Charge–Temperature)
Resonance Substrate Model.

This module provides:
    - gradient
    - divergence
    - laplacian
    - vector magnitude
    - normalization
    - curl (2D → pseudo‑scalar)
    - jacobian (for advanced analysis)

All operators are implemented using numpy and assume uniform grid spacing.
"""

import numpy as np


# ------------------------------------------------------------
# Basic Differential Operators
# ------------------------------------------------------------

def gradient(field, dx, dy):
    """
    Compute ∇field for a scalar field.
    Returns (df/dx, df/dy).
    """
    dfx = np.gradient(field, dx, axis=0)
    dfy = np.gradient(field, dy, axis=1)
    return dfx, dfy


def divergence(Fx, Fy, dx, dy):
    """
    Compute ∇·F for a 2D vector field F = (Fx, Fy).
    """
    dFx = np.gradient(Fx, dx, axis=0)
    dFy = np.gradient(Fy, dy, axis=1)
    return dFx + dFy


def laplacian(field, dx, dy):
    """
    Compute ∇²field for scalar or vector fields.
    """
    d2x = np.gradient(np.gradient(field, dx, axis=0), dx, axis=0)
    d2y = np.gradient(np.gradient(field, dy, axis=1), dy, axis=1)
    return d2x + d2y


# ------------------------------------------------------------
# Vector Utilities
# ------------------------------------------------------------

def magnitude(vec):
    """
    Compute |vec| for a vector field vec(x,y,3).
    """
    return np.sqrt(np.sum(vec**2, axis=-1))


def normalize(vec):
    """
    Normalize a vector field.
    Returns vec / |vec| with numerical stability.
    """
    mag = magnitude(vec)[..., None] + 1e-9
    return vec / mag


# ------------------------------------------------------------
# Curl (2D)
# ------------------------------------------------------------

def curl_2d(Fx, Fy, dx, dy):
    """
    Compute 2D curl:
        curl(F) = dFy/dx - dFx/dy
    Returns a scalar field.
    """
    dFy_dx = np.gradient(Fy, dx, axis=0)
    dFx_dy = np.gradient(Fx, dy, axis=1)
    return dFy_dx - dFx_dy


# ------------------------------------------------------------
# Jacobian (Advanced Analysis)
# ------------------------------------------------------------

def jacobian(field, dx, dy):
    """
    Compute the Jacobian matrix of a vector field:
        J[i,j] = d(field_i) / d(x_j)
    For a 3‑component field, returns shape (nx, ny, 3, 2).
    """
    dfx_dx = np.gradient(field[..., 0], dx, axis=0)
    dfx_dy = np.gradient(field[..., 0], dy, axis=1)

    dfy_dx = np.gradient(field[..., 1], dx, axis=0)
    dfy_dy = np.gradient(field[..., 1], dy, axis=1)

    dfz_dx = np.gradient(field[..., 2], dx, axis=0)
    dfz_dy = np.gradient(field[..., 2], dy, axis=1)

    return np.stack([
        np.stack([dfx_dx, dfx_dy], axis=-1),
        np.stack([dfy_dx, dfy_dy], axis=-1),
        np.stack([dfz_dx, dfz_dy], axis=-1)
    ], axis=-2)

