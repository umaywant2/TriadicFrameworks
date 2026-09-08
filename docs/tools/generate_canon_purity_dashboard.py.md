Here’s your **repo‑wide canon purity dashboard**, Nawder — HTML + SVG, wired straight into your `docs/tools` world.

It gives you:

- A single `canon_purity_dashboard.html`  
- A matching `canon_purity_heatmap.svg`  
- Per‑module purity table  
- Color‑coded drift severity  
- Summary stats at the top  

---

### 📁 File placement

Save as:

```text
docs/tools/generate_canon_purity_dashboard.py
```

Run from repo root:

```bash
python3 docs/tools/generate_canon_purity_dashboard.py
```

---

### 🟦 generate_canon_purity_dashboard.py

```python
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

def drift_label(score):
    return {
        0: "Pure",
        1: "Low",
        2: "Moderate",
        3: "High",
        4: "Critical"
    }[score]

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

def build_dashboard(report):
    out_path = os.path.join(ROOT, "canon_purity_dashboard.html")

    total = len(report)
    impure = sum(1 for r in report if r["drift_score"] > 0 or r["schema_errors"])
    pure = total - impure

    rows = []
    for r in report:
        color = drift_color(r["drift_score"])
        rows.append(f"""
        <tr style="background-color:{color}22">
          <td>{r['name']}</td>
          <td>{r['category']}</td>
          <td>{r['drift_score']}</td>
          <td>{drift_label(r['drift_score'])}</td>
          <td>{'OK' if not r['schema_errors'] else 'Invalid'}</td>
          <td><pre>{'<br>'.join(r['drift_errors'] + r['schema_errors']) or '&nbsp;'}</pre></td>
        </tr>
        """)

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>TriadicFrameworks Canon Purity Dashboard</title>
  <style>
    body {{ font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif; margin: 2rem; }}
    h1 {{ margin-bottom: 0.2rem; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
    th, td {{ border: 1px solid #ddd; padding: 0.5rem; vertical-align: top; }}
    th {{ background: #f5f5f5; }}
    pre {{ margin: 0; font-size: 0.8rem; }}
    .summary {{ margin-top: 0.5rem; }}
  </style>
</head>
<body>
  <h1>TriadicFrameworks Canon Purity Dashboard</h1>
  <div class="summary">
    <p><strong>Total modules:</strong> {total}</p>
    <p><strong>Pure modules:</strong> {pure}</p>
    <p><strong>Impure modules:</strong> {impure}</p>
    <p>Heatmap: <code>docs/canon_purity_heatmap.svg</code></p>
  </div>

  <table>
    <thead>
      <tr>
        <th>Module</th>
        <th>Category</th>
        <th>Drift Score</th>
        <th>Drift Level</th>
        <th>Schema</th>
        <th>Details</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>

</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✔ Created {out_path}")

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
            f'<title>{r["name"]} — {drift_label(r["drift_score"])}</title>'
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
    print("\n=== TriadicFrameworks Canon Purity Dashboard Generator ===\n")

    modules = find_modules()
    report = []

    for module_path in modules:
        with open(module_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        module = data.get("module", {})
        name = os.path.basename(os.path.dirname(module_path))
        category = module.get("category", "unknown")

        schema_errors = validate_schema(module_path)
        drift_errors = validate_drift(module_path)
        drift_score = score_drift(drift_errors)

        report.append({
            "name": name,
            "category": category,
            "schema_errors": schema_errors,
            "drift_errors": drift_errors,
            "drift_score": drift_score
        })

    build_dashboard(report)
    build_heatmap_svg(report)

    print("\n✨ Canon purity dashboard + heatmap generated.\n")

if __name__ == "__main__":
    main()
```

---

This gives you a **single HTML dashboard** plus a **visual heatmap SVG** you can drop straight into GitHub Pages or your internal docs.
