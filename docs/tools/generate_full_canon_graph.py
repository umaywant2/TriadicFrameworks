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

def generate_full_graph(domains):
    """Create module_graph.mermaid for the entire canon."""
    out_path = os.path.join(ROOT, "module_graph.mermaid")

    if os.path.exists(out_path):
        print(f"❌ module_graph.mermaid already exists, skipping.")
        return

    mermaid_lines = [
        "flowchart TD",
        "    CANON[TriadicFrameworks Canon]"
    ]

    for domain in domains:
        domain_name = os.path.basename(domain)
        mermaid_lines.append(f"    CANON --> {domain_name}[Domain: {domain_name}]")

        modules = find_modules(domain)
        for m in modules:
            module_name = os.path.basename(m)
            mermaid_lines.append(f"    {domain_name} --> {module_name}[{module_name}]")

    content = "\n".join(mermaid_lines)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {out_path}")

def main():
    print("\n=== TriadicFrameworks Full Canon Graph Generator ===\n")

    domains = find_domains()
    generate_full_graph(domains)

    print("\n✨ Full canon module_graph.mermaid generation complete.\n")

if __name__ == "__main__":
    main()
