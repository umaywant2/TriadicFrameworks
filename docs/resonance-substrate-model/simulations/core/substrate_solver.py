"""
substrate_solver.py
Numerical solver for SET (Spin–Charge–Temperature) field evolution
in the Resonance Substrate Model.

This module provides:
    - Grid definition
    - Substrate parameter container
    - Substrate state container
    - Forward‑Euler time stepping
    - Boundary handling (zero‑flux / Neumann)

The actual dynamics are defined in triadic_dynamics.py.
"""

import numpy as np
from dataclasses import dataclass

from .triadic_dynamics import compute_dynamics


# ------------------------------------------------------------
# Grid Definition
# ------------------------------------------------------------

@dataclass
class Grid:
    nx: int
    ny: int
    dx: float
    dy: float


# ------------------------------------------------------------
# Parameter Container
# ------------------------------------------------------------

@dataclass
class SubstrateParams:
    # Diffusion coefficients
    D_S: float
    D_C: float
    D_T: float

    # Decay rates
    gamma_S: float
    gamma_C: float
    gamma_T: float

    # Coupling strengths
    lambda_SC: float   # Spin aligns with ∇C
    lambda_ST: float   # Spin destabilized by ∇T
    beta_CS: float     # Charge induced by ∇·S

    # Noise / perturbation strengths
    eta_S: float
    eta_C: float

    # Temperature baseline
    T0: float = 0.0


# ------------------------------------------------------------
# State Container
# ------------------------------------------------------------

@dataclass
class SubstrateState:
    grid: Grid

    def __post_init__(self):
        nx, ny = self.grid.nx, self.grid.ny

        # Spin field S(x,y,3)
        self.S = np.zeros((nx, ny, 3), dtype=float)

        # Charge field C(x,y)
        self.C = np.zeros((nx, ny), dtype=float)

        # Temperature field T(x,y)
        self.T = np.zeros((nx, ny), dtype=float)


# ------------------------------------------------------------
# Boundary Conditions
# ------------------------------------------------------------

def apply_neumann_bc(field):
    """
    Zero‑flux (Neumann) boundary conditions.
    Copies the nearest interior value to the boundary.
    Works for scalar or vector fields.
    """
    if field.ndim == 2:
        # Scalar field
        field[0, :] = field[1, :]
        field[-1, :] = field[-2, :]
        field[:, 0] = field[:, 1]
        field[:, -1] = field[:, -2]

    elif field.ndim == 3:
        # Vector field
        field[0, :, :] = field[1, :, :]
        field[-1, :, :] = field[-2, :, :]
        field[:, 0, :] = field[:, 1, :]
        field[:, -1, :] = field[:, -2, :]

    else:
        raise ValueError("Unsupported field dimensionality")


# ------------------------------------------------------------
# Time Stepping
# ------------------------------------------------------------

def step(state: SubstrateState, params: SubstrateParams, dt: float):
    """
    Advance the SET fields by one time step using forward‑Euler integration.

    dS/dt, dC/dt, dT/dt are computed by triadic_dynamics.compute_dynamics().
    """

    grid = state.grid

    # Compute derivatives
    dS, dC, dT = compute_dynamics(state, params, grid)

    # Update fields
    state.S += dt * dS
    state.C += dt * dC
    state.T += dt * dT

    # Apply boundary conditions
    apply_neumann_bc(state.S)
    apply_neumann_bc(state.C)
    apply_neumann_bc(state.T)

    # Optional: add small noise (if eta_S, eta_C > 0)
    if params.eta_S > 0:
        state.S += params.eta_S * np.random.normal(scale=1.0, size=state.S.shape)

    if params.eta_C > 0:
        state.C += params.eta_C * np.random.normal(scale=1.0, size=state.C.shape)
