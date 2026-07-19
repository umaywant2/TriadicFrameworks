"""
envelope_viewer.py
Visualization tools for resonance envelope detection and mapping.

A resonance envelope is defined by:
    R(x,t) = |∇S| + |∇C| - α|∇T| - Θ

This module provides:
    - envelope computation
    - envelope mask visualization
    - overlay plots

Dependencies:
    - numpy
    - matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# Envelope Computation
# ------------------------------------------------------------

def compute_gradients(S, C, T, dx=1.0, dy=1.0):
    """
    Compute |∇S|, |∇C|, |∇T|.
    """
    # Spin gradient magnitude
    dSx = np.gradient(S[..., 0], dx, axis=0)
    dSy = np.gradient(S[..., 1], dy, axis=1)
    dSz = np.gradient(S[..., 2], dx, axis=0)
    grad_S = np.sqrt(dSx**2 + dSy**2 + dSz**2)

    # Charge gradient magnitude
    dCx = np.gradient(C, dx, axis=0)
    dCy = np.gradient(C, dy, axis=1)
    grad_C = np.sqrt(dCx**2 + dCy**2)

    # Temperature gradient magnitude
    dTx = np.gradient(T, dx, axis=0)
    dTy = np.gradient(T, dy, axis=1)
    grad_T = np.sqrt(dTx**2 + dTy**2)

    return grad_S, grad_C, grad_T


def compute_envelope(S, C, T, alpha=1.0, theta=0.1, dx=1.0, dy=1.0):
    """
    Compute resonance envelope field R(x,y).
    """
    grad_S, grad_C, grad_T = compute_gradients(S, C, T, dx, dy)
    R = grad_S + grad_C - alpha * grad_T - theta
    return R


def envelope_mask(R):
    """
    Boolean mask where resonance condition is satisfied.
    """
    return R > 0


# ------------------------------------------------------------
# Visualization
# ------------------------------------------------------------

def plot_envelope_field(R, title="Resonance Envelope Field"):
    """
    Plot the raw envelope field R(x,y).
    """
    plt.figure(figsize=(6, 5))
    im = plt.imshow(R.T, origin="lower", cmap="coolwarm")
    plt.colorbar(im)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def plot_envelope_mask(mask, title="Resonance Envelope Mask"):
    """
    Plot the binary mask of resonant regions.
    """
    plt.figure(figsize=(6, 5))
    plt.imshow(mask.T, origin="lower", cmap="gray_r")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def plot_overlay(C, mask, title="Charge Field with Resonance Overlay"):
    """
    Overlay resonance mask on top of Charge field.
    """
    plt.figure(figsize=(6, 5))
    im = plt.imshow(C.T, origin="lower", cmap="RdBu")
    plt.imshow(mask.T, origin="lower", cmap="Greens", alpha=0.4)
    plt.colorbar(im)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# ------------------------------------------------------------
# High-Level Wrapper
# ------------------------------------------------------------

def visualize_envelope(S, C, T, alpha=1.0, theta=0.1, dx=1.0, dy=1.0, prefix="Envelope"):
    """
    Compute and visualize:
        - envelope field R
        - envelope mask
        - overlay on Charge field
    """
    R = compute_envelope(S, C, T, alpha, theta, dx, dy)
    mask = envelope_mask(R)

    plot_envelope_field(R, title=f"{prefix}: Field")
    plot_envelope_mask(mask, title=f"{prefix}: Mask")
    plot_overlay(C, mask, title=f"{prefix}: Overlay")

