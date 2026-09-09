You got it, here is the **canon‑aligned, repo‑safe, domain‑bundle generator** that automatically creates **all three domain‑level artifacts**:

- `domain_overview.md`  
- `module_graph.md`  
- `domain_graph.svg`  

This script is designed to live exactly where your active tab is pointing:

```
docs/tools/
```

It walks your entire `/docs` tree, detects domain directories, builds the module graph, renders the SVG, and generates the domain overview — **all in one pass**, never overwriting existing files.

This is the **TriadicFrameworks Domain Bundle Generator**.

---

# ⭐ Domain Bundle Generator  
Save as:

```
docs/tools/generate_domain_bundle.py
```

Run from repo root:

```
python3 docs/tools/generate_domain_bundle.py
```

---

# 🟦 **generate_domain_bundle.py (Final Canon Version)**

```python
import os
import subprocess
import json

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

# ---------------------------------------------------------
# DISCOVERY
# ---------------------------------------------------------
def find_domains():
    domains = []
    for item in os.listdir(ROOT):
        path = os.path.join(ROOT, item)
        if os.path.isdir(path) and item not in EXCLUDED_DIRS:
            domains.append(path)
    return domains

def find_modules(domain_path):
    modules = []
    for root, dirs, files in os.walk(domain_path):
        if "module.json" in files:
            modules.append(root)
    return modules

# ---------------------------------------------------------
# module_graph.md
# ---------------------------------------------------------
def generate_module_graph(domain_path, modules):
    out_path = os.path.join(domain_path, "module_graph.md")

    if os.path.exists(out_path):
        print(f"❌ module_graph.md already exists in {domain_path}, skipping.")
        return

    domain_name = os.path.basename(domain_path)

    mermaid_lines = [
        "```mermaid",
        "flowchart TD",
        f"    A[Domain: {domain_name}]"
    ]

    for m in modules:
        module_name = os.path.basename(m)
        mermaid_lines.append(f"    A --> {module_name}[{module_name}]")

    mermaid_lines.append("```")

    content = f"""# {domain_name} — Module Graph

This file provides a domain‑level module graph for **{domain_name}**.

---

## Module Graph (Mermaid)

{'\n'.join(mermaid_lines)}

---

Generated automatically by `generate_domain_bundle.py`.
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# domain_graph.svg
# ---------------------------------------------------------
def extract_mermaid(md_path):
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

    return "".join(block).strip()

def generate_domain_svg(domain_path):
    md_path = os.path.join(domain_path, "module_graph.md")
    svg_path = os.path.join(domain_path, "domain_graph.svg")

    if not os.path.exists(md_path):
        print(f"❌ No module_graph.md found in {domain_path}, skipping SVG.")
        return

    if os.path.exists(svg_path):
        print(f"❌ domain_graph.svg already exists in {domain_path}, skipping.")
        return

    mermaid_code = extract_mermaid(md_path)
    if not mermaid_code:
        print(f"❌ No Mermaid block found in {md_path}, skipping.")
        return

    temp_mmd = os.path.join(domain_path, "_temp_domain_graph.mmd")

    with open(temp_mmd, "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    try:
        subprocess.run(["mmdc", "-i", temp_mmd, "-o", svg_path], check=True)
        print(f"✔ Created {svg_path}")
    except Exception as e:
        print(f"❌ Failed to generate SVG for {domain_path}: {e}")

    os.remove(temp_mmd)

# ---------------------------------------------------------
# domain_overview.md
# ---------------------------------------------------------
def generate_domain_overview(domain_path, modules):
    out_path = os.path.join(domain_path, "domain_overview.md")

    if os.path.exists(out_path):
        print(f"❌ domain_overview.md already exists in {domain_path}, skipping.")
        return

    domain_name = os.path.basename(domain_path)

    module_lines = []
    for m in modules:
        module_name = os.path.basename(m)
        module_lines.append(f"- **{module_name}**")

    module_list = "\n".join(module_lines)

    content = f"""# {domain_name} — Domain Overview

## Purpose
This document provides a domain‑level overview for **{domain_name}**, summarizing its structural role within the TriadicFrameworks canon and listing all modules contained within this domain.

---

## Modules in This Domain
{module_list}

---

## Canon Context
This domain inherits the full TriadicFrameworks canon:

- RTT triads  
- TFT triads  
- Session context  
- RTT frozen source  
- AI initialization rules  

Canon reference: `/docs/spine/spine.json`

---

Generated automatically by `generate_domain_bundle.py`.
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Domain Bundle Generator ===\n")

    domains = find_domains()

    for domain in domains:
        modules = find_modules(domain)

        if not modules:
            continue

        generate_domain_overview(domain, modules)
        generate_module_graph(domain, modules)
        generate_domain_svg(domain)

    print("\n✨ Domain bundle generation complete.\n")

if __name__ == "__main__":
    main()
```

---

# ⭐ What This Script Gives You

### ✔ Creates `domain_overview.md`  
### ✔ Creates `module_graph.md`  
### ✔ Creates `domain_graph.svg`  
### ✔ Never overwrites existing files  
### ✔ Canon‑aligned  
### ✔ RTT‑aligned  
### ✔ Works across your entire `/docs` tree  
### ✔ Produces consistent domain‑level documentation bundles  

This is the **complete domain‑bundle generator** — the domain‑level equivalent of your full module bundle generator.
