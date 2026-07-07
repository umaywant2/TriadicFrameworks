"""
schema_to_graphviz.py
Convert a JSON Schema file into a Graphviz DOT graph.

Usage:
    python schema_to_graphviz.py path/to/schema.json > schema.dot

Features:
    - Visualizes schema properties as nodes
    - Draws edges for nested objects
    - Supports one-level nested structures
    - Outputs clean DOT format for Graphviz

Dependencies:
    - Python standard library only
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# DOT Helpers
# ------------------------------------------------------------

def dot_header():
    return "digraph Schema {\n  rankdir=LR;\n  node [shape=box, fontsize=10];\n"


def dot_footer():
    return "}\n"


def dot_node(name, label):
    safe = name.replace("-", "_")
    return f'  {safe} [label="{label}"];\n'


def dot_edge(src, dst):
    s = src.replace("-", "_")
    d = dst.replace("-", "_")
    return f"  {s} -> {d};\n"


# ------------------------------------------------------------
# Schema Parsing
# ------------------------------------------------------------

def load_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_schema_path(raw_path):
    base_dir = Path(__file__).resolve().parent

    raw = str(raw_path).strip()
    if not raw:
        raise ValueError("path must not be empty")

    user_path = Path(raw).expanduser()
    if user_path.is_absolute():
        raise ValueError(f"absolute paths are not allowed: {user_path}")
    if ".." in user_path.parts:
        raise ValueError(f"path traversal is not allowed: {user_path}")

    candidate = base_dir / user_path
    try:
        schema_path = candidate.resolve(strict=True)
    except FileNotFoundError:
        raise ValueError(f"file not found: {candidate}")
    try:
        schema_path.relative_to(base_dir)
    except ValueError:
        raise ValueError(f"path escapes allowed directory: {schema_path}")
    if not schema_path.is_file():
        raise ValueError(f"not a file: {schema_path}")
    if schema_path.suffix.lower() != ".json":
        raise ValueError(f"expected a .json file: {schema_path}")
    return schema_path


def extract_properties(schema):
    return schema.get("properties", {})


# ------------------------------------------------------------
# Graph Construction
# ------------------------------------------------------------

def schema_to_dot(schema):
    out = []
    out.append(dot_header())

    title = schema.get("title", "Schema")
    root_name = title.replace(" ", "_")

    # Root node
    out.append(dot_node(root_name, title))

    props = extract_properties(schema)

    for pname, pdef in props.items():
        pnode = f"{root_name}_{pname}"
        ptype = pdef.get("type", "object")
        label = f"{pname}\\n({ptype})"

        # Add property node
        out.append(dot_node(pnode, label))

        # Connect root → property
        out.append(dot_edge(root_name, pnode))

        # Nested object?
        if ptype == "object" and "properties" in pdef:
            nested = pdef["properties"]
            for nname, ndef in nested.items():
                nnode = f"{pnode}_{nname}"
                ntype = ndef.get("type", "—")
                nlabel = f"{nname}\\n({ntype})"

                out.append(dot_node(nnode, nlabel))
                out.append(dot_edge(pnode, nnode))

    out.append(dot_footer())
    return "".join(out)


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python schema_to_graphviz.py path/to/schema.json")
        sys.exit(1)

    try:
        schema_path = validate_schema_path(sys.argv[1])
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    schema = load_schema(schema_path)
    dot = schema_to_dot(schema)
    print(dot)


if __name__ == "__main__":
    main()

