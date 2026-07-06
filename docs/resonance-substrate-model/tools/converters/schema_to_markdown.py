"""
schema_to_markdown.py
Convert a JSON Schema file into a readable Markdown document.

Usage:
    python schema_to_markdown.py path/to/schema.json > schema.md

Features:
    - Title extraction
    - Description extraction
    - Property tables
    - Required fields listing
    - Nested object handling (one level)
"""

import json
import sys
from pathlib import Path


# ------------------------------------------------------------
# Markdown Helpers
# ------------------------------------------------------------

def md_header(text, level=1):
    return f"{'#' * level} {text}\n"


def md_table(headers, rows):
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out) + "\n"


# ------------------------------------------------------------
# Schema Parsing
# ------------------------------------------------------------

def load_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_properties(schema):
    return schema.get("properties", {})


def extract_required(schema):
    return schema.get("required", [])


def format_property(name, prop):
    ptype = prop.get("type", "—")
    desc = prop.get("description", "—")
    default = prop.get("default", "—")
    return [name, ptype, desc, str(default)]


# ------------------------------------------------------------
# Markdown Generation
# ------------------------------------------------------------

def schema_to_markdown(schema):
    md = []

    # Title
    title = schema.get("title", "Schema")
    md.append(md_header(title, level=1))

    # Description
    if "description" in schema:
        md.append(schema["description"] + "\n")

    # Required fields
    required = extract_required(schema)
    if required:
        md.append(md_header("Required Fields", level=2))
        md.append(", ".join(required) + "\n")

    # Properties
    props = extract_properties(schema)
    if props:
        md.append(md_header("Properties", level=2))

        rows = []
        for name, prop in props.items():
            rows.append(format_property(name, prop))

        md.append(md_table(["Name", "Type", "Description", "Default"], rows))

    # Nested objects (one level deep)
    for name, prop in props.items():
        if prop.get("type") == "object" and "properties" in prop:
            md.append(md_header(f"Object: {name}", level=2))

            nested_rows = []
            for nname, nprop in prop["properties"].items():
                nested_rows.append(format_property(nname, nprop))

            md.append(md_table(["Name", "Type", "Description", "Default"], nested_rows))

    return "\n".join(md)


# ------------------------------------------------------------
# CLI Entry Point
# ------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python schema_to_markdown.py path/to/schema.json")
        sys.exit(1)

    user_input_path = Path(sys.argv[1])
    if user_input_path.is_absolute():
        print(f"Error: absolute paths are not allowed: {user_input_path}")
        sys.exit(1)

    if ".." in user_input_path.parts:
        print(f"Error: parent directory traversal is not allowed: {user_input_path}")
        sys.exit(1)

    safe_root = Path.cwd().resolve()
    schema_path = (safe_root / user_input_path).resolve()

    try:
        schema_path.relative_to(safe_root)
    except ValueError:
        print(f"Error: path is outside allowed directory: {user_input_path}")
        sys.exit(1)

    if schema_path.suffix.lower() != ".json":
        print(f"Error: only .json schema files are allowed: {schema_path}")
        sys.exit(1)

    if not schema_path.exists() or not schema_path.is_file():
        print(f"Error: file not found: {schema_path}")
        sys.exit(1)

    schema = load_schema(schema_path)
    md = schema_to_markdown(schema)
    print(md)


if __name__ == "__main__":
    main()

