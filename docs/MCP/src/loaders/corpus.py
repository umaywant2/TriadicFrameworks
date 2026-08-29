"""
TriadicFrameworks Corpus Loader (R5 Canon)
-----------------------------------------
This loader indexes all MCP layers (L0–L4), their modules, dimensions,
examples, registries, and cosmology/continuity metadata.

It exposes a unified corpus dictionary for MCP tools.
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]   # docs/MCP/src/loaders → docs/MCP
MCP = ROOT / "MCP"


def load_json(path: Path):
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def load_layer(layer_name: str):
    """Load a single MCP layer directory."""
    layer_path = MCP / layer_name
    if not layer_path.exists():
        return None

    layer = {
        "name": layer_name,
        "path": str(layer_path),
        "module": load_json(layer_path / "module.json"),
        "dimensions": {},
        "docs": {},
        "registry": {},
        "examples": {},
        "sitemap": load_json(layer_path / "sitemap.json"),
    }

    # Load dimension_index.json if present
    dim_index = layer_path / "dimensions" / "dimension_index.json"
    if dim_index.exists():
        layer["dimensions"]["index"] = load_json(dim_index)

    # Load all dimension JSON files
    dims_dir = layer_path / "dimensions"
    if dims_dir.exists():
        for f in dims_dir.glob("*.json"):
            if f.name != "dimension_index.json":
                layer["dimensions"][f.stem] = load_json(f)

    # Load docs (md + json)
    for ext in ("*.md", "*.json"):
        for f in layer_path.glob(ext):
            if f.name not in ("module.json", "sitemap.json"):
                layer["docs"][f.stem] = f.read_text(encoding="utf-8")

    # Load registry files
    reg_dir = layer_path / "registry"
    if reg_dir.exists():
        for f in reg_dir.glob("*.json"):
            layer["registry"][f.stem] = load_json(f)

    # Load examples
    ex_dir = layer_path / "examples"
    if ex_dir.exists():
        for f in ex_dir.glob("*.json"):
            layer["examples"][f.stem] = load_json(f)

    return layer


def build_corpus():
    """Build the full MCP corpus across all layers."""
    layers = [
        "L0_QMROOT",
        "L1_Frequency_Unseen",
        "L2_Fluids_Seen",
        "L3_Forces_Unseen",
        "L4_Continuity_Mechanics",
    ]

    corpus = {
        "layers": {},
        "sitemap": load_json(MCP / "sitemap.json"),
        "examples": load_json(MCP / "examples.registry.json"),
        "protocol": {
            "server": load_json(MCP / "protocol" / "server.json"),
            "tools": load_json(MCP / "protocol" / "tools.catalog.json"),
            "resources": load_json(MCP / "protocol" / "resources.catalog.json"),
            "prompts": load_json(MCP / "protocol" / "prompts.catalog.json"),
        }
    }

    for layer in layers:
        corpus["layers"][layer] = load_layer(layer)

    return corpus


# Exposed corpus object
CORPUS = build_corpus()


def get_layer(name: str):
    return CORPUS["layers"].get(name)


def get_dimension(layer: str, dim: str):
    lyr = get_layer(layer)
    if not lyr:
        return None
    return lyr["dimensions"].get(dim)


def list_layers():
    return list(CORPUS["layers"].keys())


def list_dimensions(layer: str):
    lyr = get_layer(layer)
    if not lyr:
        return []
    return list(lyr["dimensions"].keys())


def get_corpus():
    return CORPUS

