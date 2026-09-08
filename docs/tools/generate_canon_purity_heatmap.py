import os
import json
from jsonschema import validate, ValidationError

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

MODULE_SCHEMA = {
    "type": "object",
    "properties": {
        "module": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "summary": {"type": "string"},
                "category": {"type": "string"},
                "canon_ref": {
                    "type": "string",
                    "enum": ["/docs/spine/spine.json"]
                },
                "inherit": {
                    "type": "object",
                    "properties": {
                        "canon": {"type": "boolean"},
                        "session_context": {"type": "boolean"},
                        "triad_alias_resolution": {"type": "boolean"}
                    },
                    "required": [
                        "canon",
                        "session_context",
                        "triad_alias_resolution"
                    ]
                },
                "rtt": {
                    "type": "object",
                    "properties": {
                        "layer": {"type": "integer"},
                        "source": {"type": "string"}
                    },
                    "required": ["layer", "source"]
                },
                "ai": {
                    "type": "object",
                    "properties": {
                        "initialization": {
                            "type": "object",
                            "properties": {
                                "load_spine_first": {"type": "boolean"},
                                "load_canon_first": {"type": "boolean"},
                                "apply_session_context": {"type": "boolean"},
                                "triad_validation": {"type": "boolean"}
                            },
                            "required": [
                                "load_spine_first",
                                "load_canon_first",
                                "apply_session_context",
                                "triad_validation"
                            ]
                        }
                    },
                    "required": ["initialization"]
                }
            },
            "required": [
                "name",
                "summary",
                "category",
                "canon_ref",
                "inherit",
                "rtt",
                "ai"
            ]
        }
    },
    "required": ["module"]
}

def score_drift(errors):
    count = len(errors)
    if count == 0: return 0
    if count <= 2: return 1
    if count <= 4: return 2
    if count <= 7: return 3
    return 4

def drift_color(score):
    return {
        0: "#2ecc71",  # green
        1: "#f1c40f",  # yellow
        2: "#e67e22",  # orange
        3: "#e74c3c",  # red
        4: "#2c3e50"   # dark
    }[score]

def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(os.path.join(root, "module.json"))
    return modules

def validate_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=MODULE_SCHEMA)
        return []
    except ValidationError as e:
        return [str(e)]

def validate_drift(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    module = data.get("module", {})
    errors = []

    if module.get("canon_ref") != "/docs/spine/spine.json":
        errors.append("canon_ref mismatch")

    inherit = module.get("inherit", {})
    for key in ["canon", "session_context", "triad_alias_resolution"]:
        if inherit.get(key) != True:
            errors.append(f"inherit.{key} mismatch")

    rtt = module.get("rtt", {})
    if rtt.get("layer") != 1:
        errors.append("rtt.layer mismatch")
    if rtt.get("source") != "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html":
        errors.append("rtt.source mismatch")

    ai = module.get("ai", {}).get("initialization", {})
    for key in ["load_spine_first", "load_canon_first", "apply_session_context", "triad_validation"]:
        if ai.get(key) != True:
            errors.append(f"ai.initialization.{key} mismatch")

    return errors

def build_heatmap_svg(report):
    svg_path = os.path.join(ROOT, "canon_purity_heatmap.svg")

    cell_size = 20
    padding = 5
    cols = 20
    rows = (len(report) + cols - 1) // cols
    width = cols * cell_size + padding * 2
    height = rows * cell_size + padding * 2

    cells = []
    for idx, r in enumerate(report):
        row = idx // cols
        col = idx % cols
        x = padding + col * cell_size
        y = padding + row * cell_size
        color = drift_color(r["drift_score"])
        cells.append(
            f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" '
            f'fill="{color}" stroke="#333" stroke-width="0.5">'
            f'<title>{r["name"]} — drift {r["drift_score"]}</title>'
            f'</rect>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>
  {"".join(cells)}
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✔ Created {svg_path}")

def main():
    print("\n=== TriadicFrameworks Canon Purity Heatmap Generator ===\n")

    modules = find_modules()
    report = []

    for module_path in modules:
        with open(module_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        module = data.get("module", {})
        name = os.path.basename(os.path.dirname(module_path))

        schema_errors = validate_schema(module_path)
        drift_errors = validate_drift(module_path)
        drift_score = score_drift(drift_errors)

        report.append({
            "name": name,
            "schema_errors": schema_errors,
            "drift_errors": drift_errors,
            "drift_score": drift_score
        })

    build_heatmap_svg(report)

    print("\n✨ Canon purity heatmap generated.\n")

if __name__ == "__main__":
    main()
