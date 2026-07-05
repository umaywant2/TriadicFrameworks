#!/usr/bin/env python3
"""
rtt-schema
Unified CLI tool for working with JSON Schemas in the Resonance Substrate Model.

Capabilities:
    - Inspect schema metadata
    - Validate schema structure
    - Validate data files against schemas
    - Convert schema → Markdown
    - Convert schema → Graphviz DOT
    - List all schemas in a directory

Usage:
    rtt-schema inspect path/to/schema.json
    rtt-schema validate-schema path/to/schema.json
    rtt-schema validate-data path/to/data.json --schema path/to/schema.json
    rtt-schema to-markdown path/to/schema.json
    rtt-schema to-graphviz path/to/schema.json
    rtt-schema list path/to/schemas/

Dependencies:
    - Python standard library only
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# Utility
# ------------------------------------------------------------

def constrain_to_base(path: Path, base: Path) -> Path:
    base_resolved = base.expanduser().resolve()
    user_path = path
    candidate = user_path if user_path.is_absolute() else (base_resolved / user_path)
    candidate = candidate.resolve(strict=False)
    try:
        candidate.relative_to(base_resolved)
    except ValueError:
        error(f"Path escapes allowed root: {path}")
    return candidate


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
# Inspect
# ------------------------------------------------------------

def inspect_schema(path: Path):
    schema = load_json(path)

    print("Schema Metadata")
    print("---------------")
    print(f"File:        {path}")
    print(f"Title:       {schema.get('title', '(none)')}")
    print(f"Description: {schema.get('description', '(none)')}")
    print(f"Version:     {schema.get('$version', schema.get('version', '(none)'))}")

    props = schema.get("properties", {})
    print(f"Properties:  {len(props)}")
    for p in props:
        print(f"  - {p}")

    required = schema.get("required", [])
    print(f"Required:    {required if required else '(none)'}")


# ------------------------------------------------------------
# Schema Validation
# ------------------------------------------------------------

def validate_schema(path: Path):
    schema = load_json(path)

    if "properties" not in schema:
        error("Schema missing 'properties'")

    if not isinstance(schema["properties"], dict):
        error("'properties' must be an object")

    ok("Schema is valid")


# ------------------------------------------------------------
# Data Validation
# ------------------------------------------------------------

def validate_data(data_path: Path, schema_path: Path):
    data = load_json(data_path)
    schema = load_json(schema_path)

    props = schema.get("properties", {})
    required = schema.get("required", [])

    # Required fields
    for field in required:
        if field not in data:
            error(f"Missing required field '{field}'")

    # Type checking (simple)
    for key, value in data.items():
        if key not in props:
            print(f"[WARN] Extra field '{key}' not in schema")
            continue

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

    ok("Data file is valid")


# ------------------------------------------------------------
# Markdown Conversion
# ------------------------------------------------------------

def to_markdown(path: Path):
    schema = load_json(path)

    title = schema.get("title", "Schema")
    print(f"# {title}\n")

    if "description" in schema:
        print(schema["description"], "\n")

    required = schema.get("required", [])
    if required:
        print("## Required Fields")
        print(", ".join(required), "\n")

    props = schema.get("properties", {})
    if props:
        print("## Properties")
        print("| Name | Type | Description | Default |")
        print("|------|------|-------------|---------|")
        for name, prop in props.items():
            ptype = prop.get("type", "—")
            desc = prop.get("description", "—")
            default = prop.get("default", "—")
            print(f"| {name} | {ptype} | {desc} | {default} |")


# ------------------------------------------------------------
# Graphviz Conversion
# ------------------------------------------------------------

def to_graphviz(path: Path):
    schema = load_json(path)

    title = schema.get("title", "Schema")
    root = title.replace(" ", "_")

    print("digraph Schema {")
    print("  rankdir=LR;")
    print("  node [shape=box, fontsize=10];")
    print(f'  {root} [label="{title}"];')

    props = schema.get("properties", {})
    for pname, pdef in props.items():
        node = f"{root}_{pname}"
        ptype = pdef.get("type", "object")
        print(f'  {node} [label="{pname}\\n({ptype})"];')
        print(f"  {root} -> {node};")

        # Nested object
        if ptype == "object" and "properties" in pdef:
            for nname, ndef in pdef["properties"].items():
                nnode = f"{node}_{nname}"
                ntype = ndef.get("type", "—")
                print(f'  {nnode} [label="{nname}\\n({ntype})"];')
                print(f"  {node} -> {nnode};")

    print("}")


# ------------------------------------------------------------
# List Schemas
# ------------------------------------------------------------

def list_schemas(root: Path):
    paths = sorted(root.rglob("*.schema.json"))
    for p in paths:
        print(p.as_posix())


# ------------------------------------------------------------
# CLI Dispatcher
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  rtt-schema inspect path/to/schema.json")
        print("  rtt-schema validate-schema path/to/schema.json")
        print("  rtt-schema validate-data path/to/data.json --schema path/to/schema.json")
        print("  rtt-schema to-markdown path/to/schema.json")
        print("  rtt-schema to-graphviz path/to/schema.json")
        print("  rtt-schema list path/to/schemas/")
        sys.exit(1)

    cmd = sys.argv[1]
    base_dir = Path.cwd()
    target = constrain_to_base(Path(sys.argv[2]), base_dir)

    if cmd == "inspect":
        inspect_schema(target)
    elif cmd == "validate-schema":
        validate_schema(target)
    elif cmd == "validate-data":
        if "--schema" not in sys.argv:
            error("Missing --schema argument")
        schema_path = constrain_to_base(Path(sys.argv[sys.argv.index("--schema") + 1]), base_dir)
        validate_data(target, schema_path)
    elif cmd == "to-markdown":
        to_markdown(target)
    elif cmd == "to-graphviz":
        to_graphviz(target)
    elif cmd == "list":
        list_schemas(target)
    else:
        error(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()

