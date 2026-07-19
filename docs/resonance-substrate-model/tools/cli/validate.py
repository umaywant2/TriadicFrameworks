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
import os
import sys
from pathlib import Path


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def ensure_within_root(path: Path, root: Path, label: str) -> Path:
    # Normalize incoming value defensively before validation.
    raw_value = str(path).strip()
    normalized_value = os.path.normpath(raw_value.replace("\\", "/"))

    if normalized_value in ("", "."):
        error(f"{label} must not be empty: {normalized_value}")

    # Treat user-provided paths as repository-relative only.
    if normalized_value.startswith("/") or os.path.isabs(normalized_value):
        error(f"{label} must be a relative path: {normalized_value}")

    # Block Windows drive-qualified paths (e.g. C:/...).
    drive, _ = os.path.splitdrive(normalized_value)
    if drive:
        error(f"{label} must not include a drive prefix: {normalized_value}")

    # Block explicit traversal attempts before touching the filesystem.
    parts = [part for part in normalized_value.split("/") if part not in ("", ".")]
    if any(part == ".." for part in parts):
        error(f"{label} must not contain parent directory traversal: {normalized_value}")

    safe_candidate = Path(*parts)

    resolved_root = root.resolve()
    resolved = (resolved_root / safe_candidate).resolve(strict=False)
    if not resolved.is_relative_to(resolved_root):
        error(f"{label} escapes repository root: {normalized_value}")
    return resolved


def ensure_allowed_json_location(path: Path, root: Path, label: str) -> Path:
    resolved_root = root.resolve()
    # `path` is expected to be pre-sanitized by `ensure_within_root`.
    resolved_path = path

    allowed_dirs = (
        resolved_root / "schemas",
        resolved_root / "data",
        resolved_root / "manifests",
        resolved_root / "docs",
    )

    for allowed_dir in allowed_dirs:
        allowed_dir_resolved = allowed_dir.resolve(strict=False)
        try:
            resolved_path.relative_to(allowed_dir_resolved)
            return resolved_path
        except ValueError:
            continue

    error(f"{label} is not in an allowed JSON directory: {resolved_path}")


def load_json(path: Path, root: Path):
    safe_path = ensure_within_root(path, root, "JSON path")
    if safe_path.suffix.lower() != ".json":
        error(f"JSON path must point to a .json file: {safe_path}")
    safe_path = ensure_allowed_json_location(safe_path, root, "JSON path")
    try:
        with safe_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {safe_path}: {e}")
        sys.exit(1)


def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def ok(msg):
    print(f"[OK] {msg}")


# ------------------------------------------------------------
# Schema Validation
# ------------------------------------------------------------

def validate_schema(schema_path: Path, repo_root: Path):
    schema = load_json(schema_path, repo_root)

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

def validate_manifest(manifest_path: Path, repo_root: Path):
    manifest = load_json(manifest_path, repo_root)
    manifest_dir = manifest_path.resolve().parent

    if "schemas" not in manifest:
        error("Manifest missing 'schemas' list")

    for entry in manifest["schemas"]:
        if "file" not in entry:
            error("Manifest entry missing 'file' field")
        if not isinstance(entry["file"], str):
            error("Manifest entry 'file' field must be a string")

        raw_schema_path = Path(entry["file"])
        schema_path = ensure_within_root(raw_schema_path, manifest_dir, "Schema path")

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
        validate_schema(target, repo_root)

    elif mode == "data":
        if "--schema" not in sys.argv:
            error("Missing --schema argument for data validation")

        schema_index = sys.argv.index("--schema") + 1
        if schema_index >= len(sys.argv):
            error("Missing schema path after --schema")
        schema_path = ensure_within_root(Path(sys.argv[schema_index]), repo_root, "Schema path")
        validate_data(target, schema_path)

    elif mode == "manifest":
        validate_manifest(target, repo_root)

    else:
        error(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()

