"""
plot_heatmap.py
RTT-Inside Heatmap Plotting for Datacenter Reports
--------------------------------------------------
Provides heatmap visualizations for RTT structural and dimensional tensors
used in the Datacenter Reports module.

Design goals:
- Operator-first, drift-bounded
- Student-accessible, AI-parsable
- Minimal but extensible
"""

from typing import Any, Dict, List, Optional

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def _reshape_tensor(values: List[Any], shape: List[int]) -> np.ndarray:
    """
    Reshape flattened tensor values into the declared shape.
    """
    expected_size = 1
    for dim in shape:
        expected_size *= dim

    if len(values) != expected_size:
        raise ValueError(
            f"Tensor size mismatch: expected {expected_size}, got {len(values)}"
        )

    return np.array(values).reshape(shape)


def generate_heatmap(
    tensor: Dict[str, Any],
    title: Optional[str] = None,
    cmap: str = "viridis",
    figsize: tuple = (8, 6),
    annotate: bool = False,
) -> Figure:
    """
    Generate a static heatmap from a 2D RTT tensor.

    Expected tensor structure (aligned with tensor_export.schema.json):
    - tensor["name"]
    - tensor["description"]
    - tensor["shape"] (must be 2D)
    - tensor["values"] (flattened)
    - tensor["rtt_metadata"]["regime"]
    - tensor["rtt_metadata"]["coherence"]
    - tensor["rtt_metadata"]["drift"]
    """

    shape = tensor.get("shape", [])
    values = tensor.get("values", [])
    name = tensor.get("name", "RTT Tensor")
    description = tensor.get("description", "")
    rtt_meta = tensor.get("rtt_metadata", {})

    if len(shape) != 2:
        raise ValueError(
            f"Heatmap requires a 2D tensor, but shape={shape} was provided."
        )

    matrix = _reshape_tensor(values, shape)

    fig, ax = plt.subplots(figsize=figsize)
    heatmap = ax.imshow(matrix, cmap=cmap, aspect="auto")

    ax.set_title(title or f"{name} — Structural Heatmap")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    cbar = plt.colorbar(heatmap, ax=ax)
    cbar.set_label("Value")

    if annotate:
        for i in range(shape[0]):
            for j in range(shape[1]):
                ax.text(
                    j,
                    i,
                    f"{matrix[i, j]:.2f}",
                    ha="center",
                    va="center",
                    color="white",
                    fontsize=8,
                )

    # RTT metadata annotation
    regime = rtt_meta.get("regime", "unknown")
    coherence = rtt_meta.get("coherence", None)
    drift = rtt_meta.get("drift", None)

    annotation_text = f"Regime: {regime}"
    if coherence is not None:
        annotation_text += f" | Coherence: {coherence:.2f}"
    if drift is not None:
        annotation_text += f" | Drift: {drift:.2f}"

    fig.text(
        0.02,
        -0.05,
        annotation_text,
        fontsize=9,
        color="gray",
    )

    fig.tight_layout()
    return fig

