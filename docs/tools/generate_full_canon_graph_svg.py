import os
import subprocess

MERMAID_PATH = "docs/module_graph.mermaid"
SVG_PATH = "docs/module_graph.svg"

def generate_svg():
    if not os.path.exists(MERMAID_PATH):
        print(f"❌ Mermaid file not found: {MERMAID_PATH}")
        return

    if os.path.exists(SVG_PATH):
        print(f"❌ module_graph.svg already exists, skipping.")
        return

    try:
        subprocess.run(
            ["mmdc", "-i", MERMAID_PATH, "-o", SVG_PATH],
            check=True
        )
        print(f"✔ Created {SVG_PATH}")
    except Exception as e:
        print(f"❌ Failed to generate SVG: {e}")

def main():
    print("\n=== TriadicFrameworks Full Canon Graph SVG Generator ===\n")
    generate_svg()
    print("\n✨ module_graph.svg generation complete.\n")

if __name__ == "__main__":
    main()
