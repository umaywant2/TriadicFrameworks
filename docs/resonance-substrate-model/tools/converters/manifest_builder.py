"""
manifest_builder.py
Scan the schemas/ directory and build a manifest.json file that indexes
all JSON Schema files with their metadata.

Usage:
    python manifest_builder.py path/to/schemas > manifest.json

Features:
    - Recursively scans for *.schema.json files
    - Extracts title, description, version, required fields
    - Outputs a clean JSON manifest for documentation and tooling
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# Schema Metadata Extraction
# ------------------------------------------------------------

def extract_schema_metadata(path: Path):
    """
    Load a JSON Schema and extract key metadata fields.
    """
    with open(path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    return {
        "file": str(path.as_posix()),
        "title": schema.get("title", path.stem),
        "description": schema.get("description", ""),
        "version": schema.get("$version", schema.get("version", "")),
        "required": schema.get("required", []),
        "properties": list(schema.get("properties", {}).keys())
    }


# ------------------------------------------------------------
# Directory Scanning
# ------------------------------------------------------------

def scan_schemas(root: Path):
    """
    Recursively scan for *.schema.json files under root.
    """
    return sorted(root.rglob("*.schema.json"))


# ------------------------------------------------------------
# Manifest Construction
# ------------------------------------------------------------

def build_manifest(schema_paths):
    """
    Build a manifest dictionary from a list of schema paths.
    """
    manifest = {
        "schema_count": len(schema_paths),
        "schemas": []
    }

    for path in schema_paths:
        meta = extract_schema_metadata(path)
        manifest["schemas"].append(meta)

    return manifest


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python manifest_builder.py path/to/schemas")
        sys.exit(1)

    safe_base = Path.cwd().resolve()
    candidate = Path(sys.argv[1]).resolve()

    try:
        candidate.relative_to(safe_base)
    except ValueError:
        print(f"Error: path is outside allowed base directory: {safe_base}")
        sys.exit(1)

    root = candidate
    if not root.exists() or not root.is_dir():
        print(f"Error: directory not found: {root}")
        sys.exit(1)

    schema_paths = scan_schemas(root)
    manifest = build_manifest(schema_paths)

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

