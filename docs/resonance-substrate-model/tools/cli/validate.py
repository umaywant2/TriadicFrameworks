"""
validate.py
Command‑line validation tool for the Resonance Substrate Model repository.

Capabilities:
    - Validate JSON Schema syntax
    - Validate JSON data files against schemas
    - Check schema manifest consistency
    - Report missing or malformed fields

Usage:
    python validate.py schema path/to/schema.json
    python validate.py data path/to/data.json --schema path/to/schema.json
    python validate.py manifest path/to/manifest.json

Dependencies:
    - Python standard library only
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def ensure_within_root(path: Path, root: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        error(f"{label} escapes repository root: {path}")
    return resolved


def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}")
        sys.exit(1)


def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def ok(msg):
    print(f"[OK] {msg}")


# ------------------------------------------------------------
# Schema Validation
# ------------------------------------------------------------

def validate_schema(schema_path: Path):
    schema = load_json(schema_path)

    # Basic required fields for a JSON Schema
    if "properties" not in schema:
        error(f"Schema missing 'properties': {schema_path}")

    if not isinstance(schema["properties"], dict):
        error(f"'properties' must be an object: {schema_path}")

    ok(f"Schema is valid: {schema_path}")


# ------------------------------------------------------------
# Data Validation Against Schema
# ------------------------------------------------------------

def validate_data(data_path: Path, schema_path: Path):
    data = load_json(data_path)
    schema = load_json(schema_path)

    props = schema.get("properties", {})
    required = schema.get("required", [])

    # Check required fields
    for field in required:
        if field not in data:
            error(f"Missing required field '{field}' in {data_path}")

    # Check field types (simple version)
    for key, value in data.items():
        if key not in props:
            print(f"[WARN] Extra field '{key}' not in schema")

        else:
            expected = props[key].get("type")
            if expected:
                if expected == "object" and not isinstance(value, dict):
                    error(f"Field '{key}' should be object")
                if expected == "array" and not isinstance(value, list):
                    error(f"Field '{key}' should be array")
                if expected == "string" and not isinstance(value, str):
                    error(f"Field '{key}' should be string")
                if expected == "number" and not isinstance(value, (int, float)):
                    error(f"Field '{key}' should be number")
                if expected == "integer" and not isinstance(value, int):
                    error(f"Field '{key}' should be integer")
                if expected == "boolean" and not isinstance(value, bool):
                    error(f"Field '{key}' should be boolean")

    ok(f"Data file is valid: {data_path}")


# ------------------------------------------------------------
# Manifest Validation
# ------------------------------------------------------------

def validate_manifest(manifest_path: Path):
    manifest = load_json(manifest_path)
    manifest_dir = manifest_path.resolve().parent

    if "schemas" not in manifest:
        error("Manifest missing 'schemas' list")

    for entry in manifest["schemas"]:
        if "file" not in entry:
            error("Manifest entry missing 'file' field")
        if not isinstance(entry["file"], str):
            error("Manifest entry 'file' field must be a string")

        raw_schema_path = Path(entry["file"])
        if raw_schema_path.is_absolute():
            error(f"Schema path must be relative to manifest directory: {raw_schema_path}")

        schema_path = (manifest_dir / raw_schema_path).resolve()
        try:
            schema_path.relative_to(manifest_dir)
        except ValueError:
            error(f"Schema path escapes manifest directory: {raw_schema_path}")

        if not schema_path.exists():
            error(f"Schema listed in manifest not found: {schema_path}")

    ok("Manifest is valid")


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python validate.py schema path/to/schema.json")
        print("  python validate.py data path/to/data.json --schema path/to/schema.json")
        print("  python validate.py manifest path/to/manifest.json")
        sys.exit(1)

    mode = sys.argv[1]
    repo_root = Path(__file__).resolve().parents[2]
    target = ensure_within_root(Path(sys.argv[2]), repo_root, "Target path")

    if mode == "schema":
        validate_schema(target)

    elif mode == "data":
        if "--schema" not in sys.argv:
            error("Missing --schema argument for data validation")

        schema_index = sys.argv.index("--schema") + 1
        schema_path = ensure_within_root(Path(sys.argv[schema_index]), repo_root, "Schema path")
        validate_data(target, schema_path)

    elif mode == "manifest":
        validate_manifest(target)

    else:
        error(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()

