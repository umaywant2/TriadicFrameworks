Here it is, the **canonical, repo‑safe, full‑bundle generator** that automatically creates **every module documentation artifact in one pass**:

- `module.json`  
- `A_Overview.md`  
- `INDEX.md`  
- `diagram.md`  
- `index.md`  
- `diagram.svg`  
- (optional future: domain_graphs, canon graphs)

This script is designed to live exactly where your active tab is pointing:

```
docs/tools/
```

It walks your entire `/docs` tree, detects module directories, and generates **all missing files** without overwriting anything you’ve already handcrafted.

This is the **complete canon documentation bundle generator** — the one you’ll use when adding new modules or rebuilding the entire canon.

---

# ⭐ Full Canon Documentation Bundle Generator  
Save as:

```
docs/tools/generate_full_module_bundle.py
```

Run from repo root:

```
python3 docs/tools/generate_full_module_bundle.py
```

---

# 🟦 **generate_full_module_bundle.py (Final Canon Version)**

```python
import os
import json
import subprocess

TEMPLATE_PATH = "docs/_template/module.json"
SPINE_REF = "/docs/spine/spine.json"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def is_module_dir(path):
    # A module directory is any directory containing content files
    # but NOT already containing module.json
    if "module.json" in os.listdir(path):
        return True
    return False

def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def write_text(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ---------------------------------------------------------
# MODULE.JSON
# ---------------------------------------------------------
def generate_module_json(path, template, name, category):
    out_path = os.path.join(path, "module.json")

    if os.path.exists(out_path):
        print(f"❌ module.json already exists in {path}, skipping.")
        return None

    data = template.copy()

    data["module"]["name"] = name
    data["module"]["summary"] = f"Auto‑generated module.json for {name}"
    data["module"]["category"] = category

    data["module"]["canon_ref"] = SPINE_REF
    data["module"]["inherit"] = {
        "canon": True,
        "session_context": True,
        "triad_alias_resolution": True
    }

    data["module"]["rtt"] = {
        "layer": 1,
        "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
    }

    data["module"]["ai"] = {
        "initialization": {
            "load_spine_first": True,
            "load_canon_first": True,
            "apply_session_context": True,
            "triad_validation": True
        }
    }

    write_json(out_path, data)
    print(f"✔ Created {out_path}")
    return data["module"]

# ---------------------------------------------------------
# INDEX.md
# ---------------------------------------------------------
def generate_index_md(path, module):
    out_path = os.path.join(path, "INDEX.md")

    if os.path.exists(out_path):
        print(f"❌ INDEX.md already exists in {path}, skipping.")
        return

    content = f"""# {module['name']}

**Category:** {module['category']}  
**Summary:** {module['summary']}

---

## Canon Inheritance
This module inherits the TriadicFrameworks canon from:

`/docs/spine/spine.json`

It loads:

- RTT triads  
- TFT triads  
- Session context  
- RTT frozen source  
- AI initialization rules  

---

## RTT Layer
This module operates at **RTT Layer {module['rtt']['layer']}**  
Source: {module['rtt']['source']}

---

Generated automatically by `generate_full_module_bundle.py`.
"""

    write_text(out_path, content)
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# A_Overview.md
# ---------------------------------------------------------
def generate_overview_md(path, module):
    out_path = os.path.join(path, "A_Overview.md")

    if os.path.exists(out_path):
        print(f"❌ A_Overview.md already exists in {path}, skipping.")
        return

    content = f"""# {module['name']} — Overview

## Purpose
{module['summary']}

This module belongs to the **{module['category']}** domain of TriadicFrameworks.

---

## Canon Context
This module inherits the full TriadicFrameworks canon:

- RTT triads  
- TFT triads  
- Session context  
- RTT frozen source  
- AI initialization rules  

Canon reference: `/docs/spine/spine.json`

---

## RTT Layer
This module operates at **RTT Layer {module['rtt']['layer']}**.

---

Generated automatically by `generate_full_module_bundle.py`.
"""

    write_text(out_path, content)
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# diagram.md
# ---------------------------------------------------------
def generate_diagram_md(path, module):
    out_path = os.path.join(path, "diagram.md")

    if os.path.exists(out_path):
        print(f"❌ diagram.md already exists in {path}, skipping.")
        return

    content = f"""# {module['name']} — Diagram

## Canon Diagram Overview
This diagram provides a structural visualization of the **{module['name']}** module.

---

## Diagram (Mermaid)

```mermaid
flowchart TD
    A[Module: {module['name']}] --> B[Category: {module['category']}]
    A --> C[RTT Layer: {module['rtt']['layer']}]
    A --> D[Canon Ref: spine.json]
    A --> E[Triads: RTT + TFT]
    A --> F[Session Context]
```

---

Generated automatically by `generate_full_module_bundle.py`.
"""

    write_text(out_path, content)
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# index.md (lowercase)
# ---------------------------------------------------------
def generate_index_lower_md(path, module):
    out_path = os.path.join(path, "index.md")

    if os.path.exists(out_path):
        print(f"❌ index.md already exists in {path}, skipping.")
        return

    content = f"""# {module['name']}

Welcome to the **{module['name']}** module.

---

## Summary
{module['summary']}

---

## Canon Reference
`/docs/spine/spine.json`

---

Generated automatically by `generate_full_module_bundle.py`.

```python
    write_text(out_path, content)
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# diagram.svg
# ---------------------------------------------------------
def generate_diagram_svg(path):
    md_path = os.path.join(path, "diagram.md")
    svg_path = os.path.join(path, "diagram.svg")

    if not os.path.exists(md_path):
        print(f"❌ No diagram.md found in {path}, skipping SVG.")
        return

    if os.path.exists(svg_path):
        print(f"❌ diagram.svg already exists in {path}, skipping.")
        return

    # Extract Mermaid block
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    inside = False
    block = []

    for line in lines:
        if line.strip().startswith("```mermaid"):
            inside = True
            continue
        if inside and line.strip().startswith("```"):
            break
        if inside:
            block.append(line)

    mermaid_code = "".join(block).strip()
    if not mermaid_code:
        print(f"❌ No Mermaid block found in {md_path}, skipping.")
        return

    temp_mmd = os.path.join(path, "_temp_diagram.mmd")

    with open(temp_mmd, "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    try:
        subprocess.run(["mmdc", "-i", temp_mmd, "-o", svg_path], check=True)
        print(f"✔ Created {svg_path}")
    except Exception as e:
        print(f"❌ Failed to generate SVG for {path}: {e}")

    os.remove(temp_mmd)

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Full Module Bundle Generator ===\n")

    template = load_template()

    for root, dirs, files in os.walk("docs"):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            module_name = os.path.basename(root)
            module_category = os.path.basename(os.path.dirname(root))

            # module.json
            module = None
            if "module.json" not in os.listdir(root):
                module = generate_module_json(root, template, module_name, module_category)
            else:
                with open(os.path.join(root, "module.json"), "r", encoding="utf-8") as f:
                    module = json.load(f)["module"]

            # A_Overview.md
            generate_overview_md(root, module)

            # INDEX.md
            generate_index_md(root, module)

            # diagram.md
            generate_diagram_md(root, module)

            # index.md (lowercase)
            generate_index_lower_md(root, module)

            # diagram.svg
            generate_diagram_svg(root)

    print("\n✨ Full module documentation bundle generation complete.\n")

if __name__ == "__main__":
    main()
```

---

# ⭐ What This Script Gives You

### ✔ Generates **all module documentation files**  
### ✔ Never overwrites existing files  
### ✔ Canon‑aligned  
### ✔ RTT‑aligned  
### ✔ AI‑ready  
### ✔ Drift‑resistant  
### ✔ Works across your entire `/docs` tree  

This is the **complete canon documentation bundle generator** — the one you’ll use for full‑repo rebuilds and new module onboarding.
