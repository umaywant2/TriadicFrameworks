"""
plot_interactive.py
RTT-Inside Interactive Plotting for Datacenter Reports
------------------------------------------------------
Provides interactive visualizations for RTT dimensional and structural tensors
used in the Datacenter Reports module.

Design goals:
- Operator-first, drift-bounded
- Student-accessible, AI-parsable
- Minimal but extensible
"""

from typing import Any, Dict, List, Optional

import plotly.express as px
import plotly.graph_objects as go


def _flatten_tensor(values: List[Any], shape: List[int]) -> List[Any]:
    """
    Flatten or validate tensor values against shape.
    For now, assumes values are already flattened in row-major order.
    """
    expected_size = 1
    for dim in shape:
        expected_size *= dim

    if len(values) != expected_size:
        raise ValueError(
            f"Tensor size mismatch: expected {expected_size}, got {len(values)}"
        )

    return values


def generate_interactive_plot(
    tensor: Dict[str, Any],
    title: Optional[str] = None,
    color_scale: str = "Viridis",
) -> go.Figure:
    """
    Generate an interactive Plotly figure from a dimensional RTT tensor.

    Expected tensor structure (aligned with tensor_export.schema.json):
    - tensor["name"]
    - tensor["description"]
    - tensor["shape"] (e.g., [n, m])
    - tensor["values"] (flattened)
    - tensor["rtt_metadata"]["dimensional_fields"]
    - tensor["rtt_metadata"]["regime"]
    - tensor["rtt_metadata"]["coherence"]
    - tensor["rtt_metadata"]["drift"]

    For 2D tensors, renders an interactive heatmap.
    For 1D tensors, renders an interactive bar chart.
    """

    shape = tensor.get("shape", [])
    values = tensor.get("values", [])
    name = tensor.get("name", "RTT Tensor")
    description = tensor.get("description", "")
    rtt_meta = tensor.get("rtt_metadata", {})

    flattened = _flatten_tensor(values, shape)

    if len(shape) == 2:
        n_rows, n_cols = shape
        z = [
            flattened[i * n_cols : (i + 1) * n_cols] for i in range(n_rows)
        ]

        fig = px.imshow(
            z,
            color_continuous_scale=color_scale,
            aspect="auto",
        )

        fig.update_layout(
            title=title or f"{name} — Interactive Dimensional Map",
            xaxis_title="Column",
            yaxis_title="Row",
            coloraxis_colorbar_title="Value",
            hoverlabel=dict(bgcolor="black", font_color="white"),
        )

    elif len(shape) == 1:
        indices = list(range(len(flattened)))
        fig = px.bar(
            x=indices,
            y=flattened,
        )

        fig.update_layout(
            title=title or f"{name} — Interactive 1D Tensor",
            xaxis_title="Index",
            yaxis_title="Value",
            hoverlabel=dict(bgcolor="black", font_color="white"),
        )

    else:
        raise NotImplementedError(
            f"Interactive plotting for shape {shape} is not yet implemented."
        )

    # RTT metadata annotation in figure
    regime = rtt_meta.get("regime", "unknown")
    coherence = rtt_meta.get("coherence", None)
    drift = rtt_meta.get("drift", None)
    dimensional_fields = rtt_meta.get("dimensional_fields", [])

    annotation_text = (
        f"Regime: {regime} | "
        f"Dimensional: {', '.join(dimensional_fields) or 'n/a'}"
    )
    if coherence is not None:
        annotation_text += f" | Coherence: {coherence:.2f}"
    if drift is not None:
        annotation_text += f" | Drift: {drift:.2f}"

    fig.add_annotation(
        text=annotation_text,
        xref="paper",
        yref="paper",
        x=0.0,
        y=-0.15,
        showarrow=False,
        font=dict(size=10, color="gray"),
    )

    fig.update_layout(
        margin=dict(l=40, r=40, t=60, b=80),
    )

    return fig

