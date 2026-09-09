import os
import subprocess

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

def extract_mermaid_block(md_path):
    """Extract the first Mermaid code block from module_graph.md."""
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

def generate_svg(domain_path):
    md_path = os.path.join(domain_path, "module_graph.md")
    svg_path = os.path.join(domain_path, "domain_graph.svg")

    if not os.path.exists(md_path):
        print(f"❌ No module_graph.md found in {domain_path}, skipping.")
        return

    if os.path.exists(svg_path):
        print(f"❌ domain_graph.svg already exists in {domain_path}, skipping.")
        return

    mermaid_code = extract_mermaid_block(md_path)
    if not mermaid_code:
        print(f"❌ No Mermaid block found in {md_path}, skipping.")
        return

    temp_mmd = os.path.join(domain_path, "_temp_domain_graph.mmd")

    # Write Mermaid code to temp file
    with open(temp_mmd, "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    # Run Mermaid CLI to generate SVG
    try:
        subprocess.run(
            ["mmdc", "-i", temp_mmd, "-o", svg_path],
            check=True
        )
        print(f"✔ Created {svg_path}")
    except Exception as e:
        print(f"❌ Failed to generate SVG for {domain_path}: {e}")

    # Clean up temp file
    os.remove(temp_mmd)

def main():
    print("\n=== TriadicFrameworks Domain Graph SVG Generator ===\n")

    domains = find_domains()

    for domain in domains:
        generate_svg(domain)

    print("\n✨ domain_graph.svg generation complete.\n")

if __name__ == "__main__":
    main()
