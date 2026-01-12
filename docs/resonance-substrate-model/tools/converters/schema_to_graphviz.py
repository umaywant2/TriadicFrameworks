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

    schema_path = Path(sys.argv[1])
    if not schema_path.exists():
        print(f"Error: file not found: {schema_path}")
        sys.exit(1)

    schema = load_schema(schema_path)
    dot = schema_to_dot(schema)
    print(dot)


if __name__ == "__main__":
    main()

