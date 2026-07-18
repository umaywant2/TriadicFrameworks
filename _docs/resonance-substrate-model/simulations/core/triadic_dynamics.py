"""
triadic_dynamics.py
Core dynamical rules for SET (Spin–Charge–Temperature) field evolution
in the Resonance Substrate Model.

This module defines:
    - local interaction terms
    - coupling operators
    - dissipation terms
    - alignment and destabilization rules
    - temperature feedback

These functions are used by substrate_solver.py to compute dS/dt, dC/dt, dT/dt.
"""

import numpy as np


# ------------------------------------------------------------
# Utility Operators
# ------------------------------------------------------------

def gradient(field, dx, dy):
    """Compute ∇field for a scalar field."""
    dfx = np.gradient(field, dx, axis=0)
    dfy = np.gradient(field, dy, axis=1)
    return dfx, dfy


def divergence(Fx, Fy, dx, dy):
    """Compute ∇·F for a vector field."""
    dFx = np.gradient(Fx, dx, axis=0)
    dFy = np.gradient(Fy, dy, axis=1)
    return dFx + dFy


def laplacian(field, dx, dy):
    """Compute ∇²field for scalar or vector fields."""
    d2x = np.gradient(np.gradient(field, dx, axis=0), dx, axis=0)
    d2y = np.gradient(np.gradient(field, dy, axis=1), dy, axis=1)
    return d2x + d2y


# ------------------------------------------------------------
# Core Dynamics
# ------------------------------------------------------------

def spin_alignment_term(S, C, params, dx, dy):
    """
    Spin aligns with ∇C.
    Term: λ_SC * ∇C
    """
    dCx, dCy = gradient(C, dx, dy)
    G = np.stack([dCx, dCy, np.zeros_like(dCx)], axis=-1)
    return params.lambda_SC * G


def spin_temperature_destabilization(S, T, params, dx, dy):
    """
    Temperature gradients destabilize Spin.
    Term: -λ_ST * ∇T
    """
    dTx, dTy = gradient(T, dx, dy)
    G = np.stack([dTx, dTy, np.zeros_like(dTx)], axis=-1)
    return -params.lambda_ST * G


def charge_from_spin(S, params):
    """
    Spin divergence induces Charge.
    Term: β_CS * ∇·S_xy
    """
    Sx = S[..., 0]
    Sy = S[..., 1]
    divS = divergence(Sx, Sy, params.dx, params.dy)
    return params.beta_CS * divS


def temperature_relaxation(T, params):
    """
    Temperature relaxes toward T0.
    Term: -γ_T (T - T0)
    """
    return -params.gamma_T * (T - params.T0)


# ------------------------------------------------------------
# Time Derivatives
# ------------------------------------------------------------

def dS_dt(S, C, T, params, dx, dy):
    """
    Compute time derivative of Spin field.
    dS/dt = D_S ∇²S - γ_S S + alignment - destabilization
    """
    diff = params.D_S * laplacian(S, dx, dy)
    decay = -params.gamma_S * S
    align = spin_alignment_term(S, C, params, dx, dy)
    destab = spin_temperature_destabilization(S, T, params, dx, dy)

    return diff + decay + align + destab


def dC_dt(S, C, params, dx, dy):
    """
    Compute time derivative of Charge field.
    dC/dt = D_C ∇²C - γ_C C + β_CS ∇·S
    """
    diff = params.D_C * laplacian(C, dx, dy)
    decay = -params.gamma_C * C
    induced = charge_from_spin(S, params)

    return diff + decay + induced


def dT_dt(S, C, T, params, dx, dy):
    """
    Compute time derivative of Temperature field.
    dT/dt = D_T ∇²T - γ_T (T - T0)
    """
    diff = params.D_T * laplacian(T, dx, dy)
    relax = temperature_relaxation(T, params)

    return diff + relax


# ------------------------------------------------------------
# Unified Dynamics Wrapper
# ------------------------------------------------------------

def compute_dynamics(state, params, grid):
    """
    Compute (dS/dt, dC/dt, dT/dt) for the current state.
    Used by substrate_solver.step().
    """
    S = state.S
    C = state.C
    T = state.T

    dS = dS_dt(S, C, T, params, grid.dx, grid.dy)
    dC = dC_dt(S, C, params, grid.dx, grid.dy)
    dT = dT_dt(S, C, T, params, grid.dx, grid.dy)

    return dS, dC, dT

