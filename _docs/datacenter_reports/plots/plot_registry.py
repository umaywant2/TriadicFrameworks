"""
plot_registry.py
RTT-Inside Plot Registry for Datacenter Reports
------------------------------------------------
This registry defines all plot types available to the Datacenter Reports
module. Each plot entry includes:

- id: canonical unique identifier
- name: human-readable name
- module: module that owns the plot
- description: structural description of what the plot visualizes
- generator: Python function responsible for rendering the plot
- inputs: tensors or fields required to generate the plot
- rtt_metadata: analyzer layer, dimensional fields, regime, drift, coherence
- ai: AI-parsable metadata for cross-module propagation

This file is drift-bounded, operator-first, and safe for AI ingestion.
"""

from typing import Dict, Any
from .plot_heatmap import generate_heatmap
from .plot_interactive import generate_interactive_plot
from .palette_rtt import RTT_PALETTE


PLOT_REGISTRY: Dict[str, Dict[str, Any]] = {

    "heatmap_structural_fields": {
        "id": "heatmap_structural_fields",
        "name": "Structural Field Heatmap",
        "module": "datacenter_reports",
        "description": (
            "Heatmap visualization of structural fields across datacenter layers. "
            "Displays normalized values for facilities, governance, cultural substrate, "
            "standards, human envelope, triadic stack, planetary layer, compute infrastructure, "
            "taxes, and resonance summary."
        ),
        "generator": generate_heatmap,
        "inputs": ["structural_field_tensor"],
        "palette": RTT_PALETTE["triadic"],
        "rtt_metadata": {
            "analyzer_layer": "triadic_stack",
            "dimensional_fields": ["compute", "infrastructure", "governance"],
            "regime": "stable",
            "coherence": 0.92,
            "drift": 0.03,
            "role": "visualization",
            "lineage": ["tensor_registry.structural_field_tensor"]
        },
        "ai": {
            "parsable": True,
            "embedding_hint": "heatmap structural visualization",
            "cross_module_propagation": ["governance_substrate", "NoS", "integrations"],
            "safety": {"sensitive": False}
        }
    },

    "interactive_dimensional_map": {
        "id": "interactive_dimensional_map",
        "name": "Interactive Dimensional Map",
        "module": "datacenter_reports",
        "description": (
            "Interactive visualization of dimensional fields across datacenter regimes. "
            "Allows exploration of planetary, cultural, governance, economic, compute, "
            "and infrastructure dimensions."
        ),
        "generator": generate_interactive_plot,
        "inputs": ["dimensional_field_tensor"],
        "palette": RTT_PALETTE["dimensional"],
        "rtt_metadata": {
            "analyzer_layer": "planetary_layer",
            "dimensional_fields": ["planetary", "cultural", "economic"],
            "regime": "emergent",
            "coherence": 0.88,
            "drift": 0.05,
            "role": "visualization",
            "lineage": ["tensor_registry.dimensional_field_tensor"]
        },
        "ai": {
            "parsable": True,
            "embedding_hint": "interactive dimensional visualization",
            "cross_module_propagation": ["framework_field_theory", "low_dimensional_structures"],
            "safety": {"sensitive": False}
        }
    },

    "qcompute_capacity_map": {
        "id": "qcompute_capacity_map",
        "name": "qCompute Capacity Map",
        "module": "datacenter_reports",
        "description": (
            "Visualization of qCompute capacity across datacenter sites. "
            "Displays normalized compute density, energy envelope, and thermal regime."
        ),
        "generator": generate_heatmap,
        "inputs": ["qcompute_tensor"],
        "palette": RTT_PALETTE["compute"],
        "rtt_metadata": {
            "analyzer_layer": "compute_infrastructure",
            "dimensional_fields": ["compute", "infrastructure", "planetary"],
            "regime": "transitional",
            "coherence": 0.81,
            "drift": 0.07,
            "role": "visualization",
            "lineage": ["tensor_registry.qcompute_tensor"]
        },
        "ai": {
            "parsable": True,
            "embedding_hint": "compute capacity visualization",
            "cross_module_propagation": ["inverted_economics", "resilience_checker"],
            "safety": {"sensitive": False}
        }
    }
}


def get_plot_config(plot_id: str) -> Dict[str, Any]:
    """
    Retrieve a plot configuration by ID.
    """
    if plot_id not in PLOT_REGISTRY:
        raise KeyError(f"Plot ID '{plot_id}' not found in registry.")
    return PLOT_REGISTRY[plot_id]


def list_plots() -> Dict[str, str]:
    """
    Return a dictionary of plot_id -> name for all registered plots.
    """
    return {pid: cfg["name"] for pid, cfg in PLOT_REGISTRY.items()}

