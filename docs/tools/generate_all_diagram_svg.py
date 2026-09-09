import os
import subprocess

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

def is_module_dir(path):
    return "diagram.md" in os.listdir(path)

def extract_mermaid_block(md_path):
    """Extract the first Mermaid code block from diagram.md."""
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

def generate_svg(path):
    md_path = os.path.join(path, "diagram.md")
    svg_path = os.path.join(path, "diagram.svg")

    if os.path.exists(svg_path):
        print(f"❌ diagram.svg already exists in {path}, skipping.")
        return

    mermaid_code = extract_mermaid_block(md_path)
    if not mermaid_code:
        print(f"❌ No Mermaid block found in {md_path}, skipping.")
        return

    temp_mmd = os.path.join(path, "_temp_diagram.mmd")

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
        print(f"❌ Failed to generate SVG for {path}: {e}")

    # Clean up temp file
    os.remove(temp_mmd)

def main():
    print("\n=== TriadicFrameworks Bulk diagram.svg Generator ===\n")

    for root, dirs, files in os.walk("docs"):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            generate_svg(root)

    print("\n✨ Bulk diagram.svg generation complete.\n")

if __name__ == "__main__":
    main()
