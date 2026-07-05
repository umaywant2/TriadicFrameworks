#!/usr/bin/env python3
"""
inspect_schema.py
Inspect and summarize a JSON Schema file.

Outputs:
    - file path
    - title
    - description
    - version (if present)
    - required fields
    - property list with types
    - nested object summaries (one level)

Usage:
    python inspect_schema.py path/to/schema.json
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# Utility
# ------------------------------------------------------------

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


def validate_schema_path(user_input: str) -> Path:
    # Restrict schema inspection to files under docs/resonance-substrate-model
    safe_root = Path(__file__).resolve().parents[2]
    candidate = Path(user_input).expanduser()
    candidate = candidate if candidate.is_absolute() else (Path.cwd() / candidate)
    resolved = candidate.resolve(strict=False)

    try:
        resolved.relative_to(safe_root)
    except ValueError:
        error(f"Path is outside allowed directory: {safe_root}")

    return resolved


# ------------------------------------------------------------
# Inspection Logic
# ------------------------------------------------------------

def inspect_schema(path: Path):
    schema = load_json(path)

    print("Schema Summary")
    print("--------------")
    print(f"File:        {path.as_posix()}")
    print(f"Title:       {schema.get('title', '(none)')}")
    print(f"Description: {schema.get('description', '(none)')}")
    print(f"Version:     {schema.get('$version', schema.get('version', '(none)'))}")

    # Required fields
    required = schema.get("required", [])
    print(f"Required:    {required if required else '(none)'}")

    # Properties
    props = schema.get("properties", {})
    print(f"\nProperties ({len(props)}):")
    for name, prop in props.items():
        ptype = prop.get("type", "—")
        desc = prop.get("description", "")
        print(f"  - {name} ({ptype})  {desc}")

    # Nested objects (one level)
    for name, prop in props.items():
        if prop.get("type") == "object" and "properties" in prop:
            nested = prop["properties"]
            print(f"\nNested Object: {name}")
            for nname, nprop in nested.items():
                ntype = nprop.get("type", "—")
                ndesc = nprop.get("description", "")
                print(f"  - {nname} ({ntype})  {ndesc}")


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python inspect_schema.py path/to/schema.json")
        sys.exit(1)

    path = validate_schema_path(sys.argv[1])
    if not path.exists():
        error(f"Schema file not found: {path}")

    inspect_schema(path)


if __name__ == "__main__":
    main()

