"""
resonance_field_solver.py
High‑level resonance field analysis for the SET (Spin–Charge–Temperature)
substrate model.

This module provides:
    - resonance envelope computation
    - resonance flux computation
    - resonance transport velocity
    - coherence metrics
    - high‑level wrappers for envelope evolution

It complements:
    - triadic_dynamics.py  (local field dynamics)
    - substrate_solver.py  (numerical integration)
"""

import numpy as np
from dataclasses import dataclass


# ------------------------------------------------------------
# Envelope Definition
# ------------------------------------------------------------

@dataclass
class EnvelopeParams:
    alpha: float = 1.0   # weight for |∇T|
    theta: float = 0.1   # threshold for resonance activation


def gradient(field, dx, dy):
    dfx = np.gradient(field, dx, axis=0)
    dfy = np.gradient(field, dy, axis=1)
    return dfx, dfy


def spin_gradient_magnitude(S, dx, dy):
    dSx = np.gradient(S[..., 0], dx, axis=0)
    dSy = np.gradient(S[..., 1], dy, axis=1)
    dSz = np.gradient(S[..., 2], dx, axis=0)
    return np.sqrt(dSx**2 + dSy**2 + dSz**2)


def scalar_gradient_magnitude(C, dx, dy):
    dCx, dCy = gradient(C, dx, dy)
    return np.sqrt(dCx**2 + dCy**2)


def temperature_gradient_magnitude(T, dx, dy):
    dTx, dTy = gradient(T, dx, dy)
    return np.sqrt(dTx**2 + dTy**2)


# ------------------------------------------------------------
# Envelope Computation
# ------------------------------------------------------------

def compute_envelope_field(S, C, T, grid, env: EnvelopeParams):
    """
    R(x,y) = |∇S| + |∇C| - α|∇T| - θ
    """
    gS = spin_gradient_magnitude(S, grid.dx, grid.dy)
    gC = scalar_gradient_magnitude(C, grid.dx, grid.dy)
    gT = temperature_gradient_magnitude(T, grid.dx, grid.dy)

    return gS + gC - env.alpha * gT - env.theta


def compute_envelope_mask(R):
    """Boolean mask of resonant regions."""
    return R > 0


# ------------------------------------------------------------
# Resonance Flux
# ------------------------------------------------------------

def compute_resonance_flux(S, C, T, grid, env: EnvelopeParams):
    """
    Resonance flux is defined as:
        F = ∇R
    where R is the resonance envelope field.
    """
    R = compute_envelope_field(S, C, T, grid, env)
    dRx, dRy = gradient(R, grid.dx, grid.dy)
    return dRx, dRy


# ------------------------------------------------------------
# Resonance Transport Velocity
# ------------------------------------------------------------

def compute_transport_velocity(S, C, T, grid, env: EnvelopeParams):
    """
    Transport velocity is defined as:
        v = F / |F|
    where F = ∇R.
    """
    dRx, dRy = compute_resonance_flux(S, C, T, grid, env)
    mag = np.sqrt(dRx**2 + dRy**2) + 1e-9
    return dRx / mag, dRy / mag


# ------------------------------------------------------------
# Coherence Metrics
# ------------------------------------------------------------

def compute_alignment_coherence(S, C, grid):
    """
    Coherence = mean( Ŝ · ∇Ĉ )
    """
    dCx, dCy = gradient(C, grid.dx, grid.dy)
    G = np.stack([dCx, dCy, np.zeros_like(dCx)], axis=-1)

    S_norm = S / (np.linalg.norm(S, axis=-1, keepdims=True) + 1e-9)
    G_norm = G / (np.linalg.norm(G, axis=-1, keepdims=True) + 1e-9)

    return np.mean(np.sum(S_norm * G_norm, axis=-1))


def compute_envelope_area(mask):
    """Total area of resonant regions."""
    return np.sum(mask)


# ------------------------------------------------------------
# High‑Level Wrapper
# ------------------------------------------------------------

def analyze_resonance(state, grid, env: EnvelopeParams):
    """
    Compute all resonance‑related quantities for the current state.
    Returns a dictionary with:
        - envelope field
        - envelope mask
        - flux
        - transport velocity
        - coherence
        - area
    """
    S = state.S
    C = state.C
    T = state.T

    R = compute_envelope_field(S, C, T, grid, env)
    mask = compute_envelope_mask(R)
    flux = compute_resonance_flux(S, C, T, grid, env)
    velocity = compute_transport_velocity(S, C, T, grid, env)
    coherence = compute_alignment_coherence(S, C, grid)
    area = compute_envelope_area(mask)

    return {
        "R": R,
        "mask": mask,
        "flux": flux,
        "velocity": velocity,
        "coherence": coherence,
        "area": area
    }

