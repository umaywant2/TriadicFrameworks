"""
substrate_solver.py
Core numerical solver for the SET (Spin–Charge–Temperature) resonance substrate model.

Implements:
    ∂t S = D_S ∇²S - γ_S S + λ_SC ∇C - λ_ST ∇T
    ∂t C = D_C ∇²C - γ_C C + β_CS ∇·S
    ∂t T = D_T ∇²T - γ_T (T - T0) + η_S |S|² + η_C |∇C|²

This is a reference implementation intended for:
    - reproducible experiments
    - baseline simulations
    - further numerical refinement
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class SubstrateParams:
    # diffusion coefficients
    D_S: float = 1.0
    D_C: float = 1.0
    D_T: float = 1.0

    # relaxation coefficients
    gamma_S: float = 0.1
    gamma_C: float = 0.1
    gamma_T: float = 0.1

    # coupling coefficients
    lambda_SC: float = 1.0
    lambda_ST: float = 1.0
    beta_CS: float = 1.0
    eta_S: float = 0.1
    eta_C: float = 0.1

    # background temperature
    T0: float = 0.0


@dataclass
class Grid:
    nx: int
    ny: int
    dx: float
    dy: float


class SubstrateState:
    """
    Holds the fields:
        S: (nx, ny, 3)  Spin field (vector)
        C: (nx, ny)     Charge field (scalar)
        T: (nx, ny)     Temperature field (scalar)
    """

    def __init__(self, grid: Grid):
        self.grid = grid
        self.S = np.zeros((grid.nx, grid.ny, 3), dtype=float)
        self.C = np.zeros((grid.nx, grid.ny), dtype=float)
        self.T = np.zeros((grid.nx, grid.ny), dtype=float)


def laplacian_scalar(field: np.ndarray, grid: Grid) -> np.ndarray:
    """2D Laplacian for scalar field with periodic boundaries."""
    dx2 = grid.dx ** 2
    dy2 = grid.dy ** 2

    f = field
    lap = (
        (np.roll(f, 1, axis=0) - 2.0 * f + np.roll(f, -1, axis=0)) / dx2
        + (np.roll(f, 1, axis=1) - 2.0 * f + np.roll(f, -1, axis=1)) / dy2
    )
    return lap


def laplacian_vector(field: np.ndarray, grid: Grid) -> np.ndarray:
    """2D Laplacian for vector field (applied component-wise)."""
    lap = np.zeros_like(field)
    for k in range(field.shape[2]):
        lap[..., k] = laplacian_scalar(field[..., k], grid)
    return lap


def gradient_scalar(field: np.ndarray, grid: Grid) -> np.ndarray:
    """2D gradient of scalar field: returns (nx, ny, 2)."""
    dx = grid.dx
    dy = grid.dy

    fx = (np.roll(field, -1, axis=0) - np.roll(field, 1, axis=0)) / (2.0 * dx)
    fy = (np.roll(field, -1, axis=1) - np.roll(field, 1, axis=1)) / (2.0 * dy)

    grad = np.stack([fx, fy], axis=-1)
    return grad


def divergence_vector(field: np.ndarray, grid: Grid) -> np.ndarray:
    """2D divergence of vector field with last axis = 2 (x,y)."""
    dx = grid.dx
    dy = grid.dy

    fx = field[..., 0]
    fy = field[..., 1]

    dfx = (np.roll(fx, -1, axis=0) - np.roll(fx, 1, axis=0)) / (2.0 * dx)
    dfy = (np.roll(fy, -1, axis=1) - np.roll(fy, 1, axis=1)) / (2.0 * dy)

    return dfx + dfy


def step(state: SubstrateState, params: SubstrateParams, dt: float) -> None:
    """
    Advance S, C, T by one explicit time step dt using the draft field equations.
    Periodic boundary conditions are assumed.
    """

    g = state.grid

    # unpack fields
    S = state.S
    C = state.C
    T = state.T

    # Laplacians
    lap_S = laplacian_vector(S, g)
    lap_C = laplacian_scalar(C, g)
    lap_T = laplacian_scalar(T, g)

    # Gradients
    grad_C = gradient_scalar(C, g)      # (nx, ny, 2)
    grad_T = gradient_scalar(T, g)      # (nx, ny, 2)

    # For S, we only use x,y components for divergence coupling
    S_xy = S[..., :2]                   # (nx, ny, 2)
    div_S = divergence_vector(S_xy, g)  # (nx, ny)

    # |S|^2
    S_mag2 = np.sum(S ** 2, axis=-1)

    # |∇C|^2
    grad_C_mag2 = np.sum(grad_C ** 2, axis=-1)

    # --- Spin evolution ---
    dS_dt = (
        params.D_S * lap_S
        - params.gamma_S * S
    )

    # λ_SC ∇C term: lift grad_C (2D) into 3D by padding z=0
    grad_C_3 = np.zeros_like(S)
    grad_C_3[..., 0:2] = grad_C
    dS_dt += params.lambda_SC * grad_C_3

    # -λ_ST ∇T term: same lifting
    grad_T_3 = np.zeros_like(S)
    grad_T_3[..., 0:2] = grad_T
    dS_dt -= params.lambda_ST * grad_T_3

    # --- Charge evolution ---
    dC_dt = (
        params.D_C * lap_C
        - params.gamma_C * C
        + params.beta_CS * div_S
    )

    # --- Temperature evolution ---
    dT_dt = (
        params.D_T * lap_T
        - params.gamma_T * (T - params.T0)
        + params.eta_S * S_mag2
        + params.eta_C * grad_C_mag2
    )

    # explicit Euler update
    state.S = S + dt * dS_dt
    state.C = C + dt * dC_dt
    state.T = T + dt * dT_dt


def initialize_example(grid: Grid) -> SubstrateState:
    """
    Example initializer:
    - small localized perturbation in C
    - zero S and T
    """
    state = SubstrateState(grid)

    x = np.linspace(0, grid.nx * grid.dx, grid.nx, endpoint=False)
    y = np.linspace(0, grid.ny * grid.dy, grid.ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    # Gaussian bump in C
    cx = 0.5 * grid.nx * grid.dx
    cy = 0.5 * grid.ny * grid.dy
    sigma = 0.1 * min(grid.nx * grid.dx, grid.ny * grid.dy)

    state.C = np.exp(-(((X - cx) ** 2 + (Y - cy) ** 2) / (2.0 * sigma ** 2)))

    return state


def run_demo(steps: int = 1000, dt: float = 0.01) -> SubstrateState:
    """
    Minimal demo run for testing the solver.
    Returns the final state.
    """
    grid = Grid(nx=64, ny=64, dx=1.0, dy=1.0)
    params = SubstrateParams()
    state = initialize_example(grid)

    for _ in range(steps):
        step(state, params, dt)

    return state


if __name__ == "__main__":
    # simple smoke test
    final_state = run_demo(steps=100, dt=0.01)
    print("Final field norms:")
    print("||S|| =", np.linalg.norm(final_state.S))
    print("||C|| =", np.linalg.norm(final_state.C))
    print("||T|| =", np.linalg.norm(final_state.T))
