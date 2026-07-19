"""
validate_module_tensors.py
RTT-Inside Tensor Validator for Datacenter Reports
--------------------------------------------------
Validates all tensors defined in tensor_registry.py against:

- tensor_export.schema.json
- RTT drift + coherence rules
- semantic versioning
- lineage requirements
- AI-parsable metadata
- shape + dtype correctness

This validator is operator-first, drift-bounded, and safe for AI ingestion.
"""

import json
import re
from typing import Dict, Any, List

from jsonschema import validate, ValidationError

from .tensor_registry import TENSOR_REGISTRY


# ------------------------------------------------------------
# Load schema
# ------------------------------------------------------------

def load_schema(path: str = "docs/datacenter_reports/schemas/tensor_export.schema.json") -> Dict[str, Any]:
    """
    Load the canonical RTT tensor export schema.
    """
    with open(path, "r") as f:
        return json.load(f)


# ------------------------------------------------------------
# RTT Rules
# ------------------------------------------------------------

SEMVER_PATTERN = re.compile(r"^v[0-9]+\.[0-9]+\.[0-9]+$")

def validate_semver(version: str):
    if not SEMVER_PATTERN.match(version):
        raise ValueError(f"Invalid semantic version: {version}")


def validate_rtt_metadata(meta: Dict[str, Any]):
    """
    Validate RTT-specific metadata fields.
    """
    if "coherence" in meta:
        c = meta["coherence"]
        if not (0 <= c <= 1):
            raise ValueError(f"Coherence must be between 0 and 1, got {c}")

    if "drift" in meta:
        d = meta["drift"]
        if not (0 <= d <= 1):
            raise ValueError(f"Drift must be between 0 and 1, got {d}")

    if "regime" in meta:
        if meta["regime"] not in ["stable", "transitional", "chaotic", "emergent"]:
            raise ValueError(f"Invalid regime: {meta['regime']}")

    if "dimensional_fields" in meta:
        if not isinstance(meta["dimensional_fields"], list):
            raise ValueError("dimensional_fields must be a list")


def validate_lineage(meta: Dict[str, Any]):
    """
    Ensure lineage is present and non-empty.
    """
    if "lineage" not in meta or not meta["lineage"]:
        raise ValueError("Tensor must include lineage information.")


def validate_ai_metadata(ai: Dict[str, Any]):
    """
    Validate AI-parsable metadata.
    """
    if "parsable" in ai and not isinstance(ai["parsable"], bool):
        raise ValueError("ai.parsable must be a boolean")

    if "cross_module_propagation" in ai:
        if not isinstance(ai["cross_module_propagation"], list):
            raise ValueError("ai.cross_module_propagation must be a list")


# ------------------------------------------------------------
# Tensor Validation
# ------------------------------------------------------------

def validate_tensor(tensor_id: str, tensor: Dict[str, Any], schema: Dict[str, Any]):
    """
    Validate a single tensor against schema + RTT rules.
    """
    print(f"Validating tensor: {tensor_id}")

    # 1. JSON Schema validation
    try:
        validate(instance=tensor, schema=schema)
    except ValidationError as e:
        raise ValueError(f"Schema validation failed for {tensor_id}: {e.message}")

    # 2. Semantic versioning
    validate_semver(tensor["version"])

    # 3. RTT metadata
    validate_rtt_metadata(tensor["rtt_metadata"])

    # 4. Lineage
    validate_lineage(tensor["rtt_metadata"])

    # 5. AI metadata
    validate_ai_metadata(tensor["ai"])

    print(f"✓ {tensor_id} passed validation.")


# ------------------------------------------------------------
# Module-Level Validation
# ------------------------------------------------------------

def validate_all_tensors(schema_path: str = "docs/datacenter_reports/schemas/tensor_export.schema.json"):
    """
    Validate every tensor in the registry.
    """
    schema = load_schema(schema_path)

    print("=== RTT Tensor Validation ===")
    for tensor_id, tensor in TENSOR_REGISTRY.items():
        validate_tensor(tensor_id, tensor, schema)

    print("All tensors validated successfully.")


if __name__ == "__main__":
    validate_all_tensors()

