#!/usr/bin/env python3
"""
generate_graph.py
Generate Graphviz DOT graphs for JSON Schemas or schema directories.

Capabilities:
    - Convert a single JSON Schema → DOT graph
    - Convert all schemas in a directory → combined DOT graph
    - Visualize nested object structures (one level deep)
    - Stdlib-only, no external dependencies

Usage:
    python generate_graph.py schema path/to/schema.json > schema.dot
    python generate_graph.py dir path/to/schemas/ > all_schemas.dot
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


def resolve_within_base(user_input: str, base: Path) -> Path:
    """Resolve a user-supplied path and ensure it stays within `base`."""
    candidate = (base / user_input).resolve()
    try:
        candidate.relative_to(base)
    except ValueError:
        print(f"[ERROR] Path escapes allowed root: {user_input}")
        sys.exit(1)
    return candidate


def safe(name: str) -> str:
    """Make a string safe for DOT node names."""
    return name.replace("-", "_").replace(" ", "_")


# ------------------------------------------------------------
# DOT Helpers
# ------------------------------------------------------------

def dot_header():
    return "digraph Schemas {\n  rankdir=LR;\n  node [shape=box, fontsize=10];\n"


def dot_footer():
    return "}\n"


def dot_node(name, label):
    return f'  {safe(name)} [label="{label}"];\n'


def dot_edge(src, dst):
    return f"  {safe(src)} -> {safe(dst)};\n"


# ------------------------------------------------------------
# Schema → DOT
# ------------------------------------------------------------

def schema_to_dot(schema_path: Path):
    schema = load_json(schema_path)

    title = schema.get("title", schema_path.stem)
    root = safe(title)

    out = []
    out.append(dot_node(root, title))

    props = schema.get("properties", {})

    for pname, pdef in props.items():
        node = f"{root}_{pname}"
        ptype = pdef.get("type", "object")
        label = f"{pname}\\n({ptype})"

        out.append(dot_node(node, label))
        out.append(dot_edge(root, node))

        # Nested object (one level)
        if ptype == "object" and "properties" in pdef:
            for nname, ndef in pdef["properties"].items():
                nnode = f"{node}_{nname}"
                ntype = ndef.get("type", "—")
                nlabel = f"{nname}\\n({ntype})"

                out.append(dot_node(nnode, nlabel))
                out.append(dot_edge(node, nnode))

    return "".join(out)


# ------------------------------------------------------------
# Directory → DOT
# ------------------------------------------------------------

def directory_to_dot(root: Path):
    out = []
    schema_paths = sorted(root.rglob("*.schema.json"))

    for path in schema_paths:
        out.append(schema_to_dot(path))

    return "".join(out)


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python generate_graph.py schema path/to/schema.json")
        print("  python generate_graph.py dir path/to/schemas/")
        sys.exit(1)

    mode = sys.argv[1]
    base_dir = Path.cwd().resolve()
    target = resolve_within_base(sys.argv[2], base_dir)

    print(dot_header(), end="")

    if mode == "schema":
        if not target.exists():
            print(f"[ERROR] Schema not found: {target}")
            sys.exit(1)
        print(schema_to_dot(target), end="")

    elif mode == "dir":
        if not target.exists():
            print(f"[ERROR] Directory not found: {target}")
            sys.exit(1)
        print(directory_to_dot(target), end="")

    else:
        print(f"[ERROR] Unknown mode: {mode}")
        sys.exit(1)

    print(dot_footer(), end="")


if __name__ == "__main__":
    main()

