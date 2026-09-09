Here’s a compact **Tools Status HTML Dashboard** generator for `/docs/spine`.

Save as:

```text
docs/tools/generate_tools_status_dashboard.py
```

Run from repo root:

```bash
python3 docs/tools/generate_tools_status_dashboard.py
```

It will create:

```text
docs/spine/tools_status.html
```

---

```python
import os
import json

ROOT = "docs"
TOOLS_DIR = os.path.join(ROOT,"tools")
OUTPUT = os.path.join(ROOT,"spine","tools_status.html")

EXPECTED_TOOLS = [
    "generate_module_bundle.py",
    "generate_domain_bundle.py",
    "enforce_module_schema.py",
    "local_module_guardian.py",
    "repair_module_json.py",
    "validate_canon_purity.py",
    "generate_canon_purity_dashboard.py",
    "generate_canon_sitemap.py",
    "auto_fix_drift.py",
    "generate_canon_purity_heatmap.py",
    "repair_module_schema.py",
    "validate_module_dependencies.py",
    "triad_purity_auditor.py"
]

def list_tools():
    if not os.path.isdir(TOOLS_DIR):
        return []
    return sorted(f for f in os.listdir(TOOLS_DIR) if f.endswith(".py"))

def build_dashboard(existing):
    rows = []
    for name in sorted(set(EXPECTED_TOOLS + existing)):
        status = "Present" if name in existing else "Missing"
        rows.append(f"""
        <tr>
          <td>{name}</td>
          <td>{status}</td>
        </tr>
        """)

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>TriadicFrameworks Tools Status Dashboard</title>
  <style>
    body {{ font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif; margin: 2rem; }}
    h1 {{ margin-bottom: 0.5rem; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
    th, td {{ border: 1px solid #ddd; padding: 0.5rem; }}
    th {{ background: #f5f5f5; }}
  </style>
</head>
<body>
  <h1>Tools Status Dashboard — /docs/spine</h1>
  <p>This dashboard reflects the status of core canon tools in <code>/docs/tools</code>.</p>

  <table>
    <thead>
      <tr>
        <th>Tool Script</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
</body>
</html>
"""
    return html

def main():
    print("\n=== TriadicFrameworks Tools Status Dashboard Generator ===\n")

    existing = list_tools()
    html = build_dashboard(existing)

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT,"w",encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Created {OUTPUT}")
    print("\n✨ Tools status dashboard ready.\n")

if __name__=="__main__":
    main()
```
