"""
tensor_registry.py
RTT-Inside Tensor Registry for Datacenter Reports
-------------------------------------------------
Defines all tensors exposed by the Datacenter Reports module.

Each tensor entry includes:
- id: canonical unique identifier
- name: human-readable name
- module: module that owns the tensor
- description: structural explanation of what the tensor represents
- shape: tensor dimensionality
- dtype: data type
- units: optional units
- values: flattened tensor values (populated at runtime)
- rtt_metadata: analyzer layer, dimensional fields, regime, coherence, drift, lineage
- ai: AI-parsable metadata for cross-module propagation

This file is drift-bounded, operator-first, and safe for AI ingestion.
"""

from typing import Dict, Any, List


TENSOR_REGISTRY: Dict[str, Dict[str, Any]] = {

    # ------------------------------------------------------------
    # 1. Structural Field Tensor
    # ------------------------------------------------------------
    "structural_field_tensor": {
        "tensor_id": "structural_field_tensor",
        "name": "Structural Field Tensor",
        "module": "datacenter_reports",
        "version": "v1.0.0",
        "description": (
            "Normalized structural snapshot of the datacenter across the five RTT "
            "structural fields: facilities, governance, cultural substrate, "
            "standards, and human envelope."
        ),
        "shape": [5, 5],  # example shape; actual values populated at runtime
        "dtype": "float32",
        "units": "normalized",
        "values": [],  # populated by evaluator

        "rtt_metadata": {
            "analyzer_layer": "triadic_stack",
            "dimensional_fields": ["compute", "infrastructure", "governance"],
            "regime": "stable",
            "coherence": 0.92,
            "drift": 0.03,
            "role": "structural_field",
            "lineage": ["datacenter_evaluator.structural_field_tensor"]
        },

        "ai": {
            "parsable": True,
            "embedding_hint": "structural field tensor",
            "cross_module_propagation": ["governance_substrate", "NoS", "integrations"],
            "safety": {"sensitive": False}
        }
    },

    # ------------------------------------------------------------
    # 2. Dimensional Field Tensor
    # ------------------------------------------------------------
    "dimensional_field_tensor": {
        "tensor_id": "dimensional_field_tensor",
        "name": "Dimensional Field Tensor",
        "module": "datacenter_reports",
        "version": "v1.0.0",
        "description": (
            "Multi-site comparison of dimensional fields across datacenter regions. "
            "Encodes planetary, cultural, governance, economic, compute, and "
            "infrastructure dimensions."
        ),
        "shape": [6, 12],  # example shape
        "dtype": "float32",
        "units": "normalized",
        "values": [],

        "rtt_metadata": {
            "analyzer_layer": "planetary_layer",
            "dimensional_fields": ["planetary", "cultural", "economic"],
            "regime": "emergent",
            "coherence": 0.88,
            "drift": 0.05,
            "role": "dimensional_field",
            "lineage": ["datacenter_evaluator.dimensional_field_tensor"]
        },

        "ai": {
            "parsable": True,
            "embedding_hint": "dimensional field tensor",
            "cross_module_propagation": [
                "framework_field_theory",
                "low_dimensional_structures"
            ],
            "safety": {"sensitive": False}
        }
    },

    # ------------------------------------------------------------
    # 3. qCompute Tensor
    # ------------------------------------------------------------
    "qcompute_tensor": {
        "tensor_id": "qcompute_tensor",
        "name": "qCompute Capacity Tensor",
        "module": "datacenter_reports",
        "version": "v1.0.0",
        "description": (
            "Normalized map of qCompute-related metrics including compute density, "
            "energy envelope, and thermal regime across datacenter sites."
        ),
        "shape": [12, 3],  # example shape
        "dtype": "float32",
        "units": "normalized",
        "values": [],

        "rtt_metadata": {
            "analyzer_layer": "compute_infrastructure",
            "dimensional_fields": ["compute", "infrastructure", "planetary"],
            "regime": "transitional",
            "coherence": 0.81,
            "drift": 0.07,
            "role": "compute_capacity",
            "lineage": ["datacenter_evaluator.qcompute_tensor"]
        },

        "ai": {
            "parsable": True,
            "embedding_hint": "compute capacity tensor",
            "cross_module_propagation": [
                "inverted_economics",
                "resilience_checker"
            ],
            "safety": {"sensitive": False}
        }
    }
}


# ------------------------------------------------------------
# Accessors
# ------------------------------------------------------------

def get_tensor_config(tensor_id: str) -> Dict[str, Any]:
    """
    Retrieve a tensor configuration by ID.
    """
    if tensor_id not in TENSOR_REGISTRY:
        raise KeyError(f"Tensor ID '{tensor_id}' not found in registry.")
    return TENSOR_REGISTRY[tensor_id]


def list_tensors() -> Dict[str, str]:
    """
    Return a dictionary of tensor_id -> name for all registered tensors.
    """
    return {tid: cfg["name"] for tid, cfg in TENSOR_REGISTRY.items()}

