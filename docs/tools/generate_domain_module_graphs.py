import os

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

def find_domains():
    """Return all top-level domain directories under /docs."""
    domains = []
    for item in os.listdir(ROOT):
        path = os.path.join(ROOT, item)
        if os.path.isdir(path) and item not in EXCLUDED_DIRS:
            domains.append(path)
    return domains

def find_modules(domain_path):
    """Return all module directories inside a domain."""
    modules = []
    for root, dirs, files in os.walk(domain_path):
        if "module.json" in files:
            modules.append(root)
    return modules

def generate_graph(domain_path, modules):
    """Create module_graph.md inside the domain directory."""
    out_path = os.path.join(domain_path, "module_graph.md")

    if os.path.exists(out_path):
        print(f"❌ module_graph.md already exists in {domain_path}, skipping.")
        return

    domain_name = os.path.basename(domain_path)

    # Build Mermaid graph
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

It lists all modules detected under:

`{domain_path}`

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

## Module Graph (Mermaid)

{'\n'.join(mermaid_lines)}

---

Generated automatically by `generate_domain_module_graphs.py`.
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {out_path}")

def main():
    print("\n=== TriadicFrameworks Domain Module Graph Generator ===\n")

    domains = find_domains()

    for domain in domains:
        modules = find_modules(domain)
        if modules:
            generate_graph(domain, modules)

    print("\n✨ Domain module_graph.md generation complete.\n")

if __name__ == "__main__":
    main()
