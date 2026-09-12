import os
import json
from copy import deepcopy

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
    """Load the canonical module.json template."""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def is_module_dir(path):
    """
    A module directory is any directory containing content files
    but NOT already containing module.json.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        return False

    if "module.json" in entries:
        return False

    for f in entries:
        if f.endswith((".md", ".txt", ".json")) and f != "module.json":
            return True

    return False

def write_json(path, data):
    """Write JSON with UTF‑8 encoding and indentation."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def write_text(path, content):
    """Write plain text with UTF‑8 encoding."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_module_json(path, template, name, category):
    """Create module.json if it does not already exist."""
    out_path = os.path.join(path, "module.json")

    if os.path.exists(out_path):
        print(f"❌ module.json already exists in {path}, skipping.")
        return None

    data = deepcopy(template)

    # Canon metadata
    data["module"]["name"] = name
    data["module"]["summary"] = f"Auto‑generated module.json for {name}"
    data["module"]["category"] = category
    data["module"]["canon_ref"] = SPINE_REF

    # Canon inheritance
    data["module"]["inherit"] = {
        "canon": True,
        "session_context": True,
        "triad_alias_resolution": True
    }

    # RTT metadata
    data["module"]["rtt"] = {
        "layer": 1,
        "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
    }

    # AI initialization metadata
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

def generate_index_md(path, module):
    """Create INDEX.md if missing."""
    out_path = os.path.join(path, "INDEX.md")

    if os.path.exists(out_path):
        print(f"❌ INDEX.md already exists in {path}, skipping.")
        return

    content = (
        f"# {module['name']}\n\n"
        f"**Category:** {module['category']}  \n"
        f"**Summary:** {module['summary']}\n\n"
        "---\n\n"
        "## Canon Inheritance\n"
        "This module inherits the TriadicFrameworks canon from:\n\n"
        "`/docs/spine/spine.json`\n\n"
        "It loads:\n\n"
        "- RTT triads  \n"
        "- TFT triads  \n"
        "- Session context  \n"
        "- RTT frozen source  \n"
        "- AI initialization rules  \n\n"
        "---\n\n"
        "## RTT Layer\n"
        f"This module operates at **RTT Layer {module['rtt']['layer']}**  \n"
        f"Source: {module['rtt']['source']}\n\n"
        "---\n\n"
        "Generated automatically by `generate_module_bundle.py`.\n"
    )

    write_text(out_path, content)
    print(f"✔ Created {out_path}")

def generate_overview_md(path, module):
    """Create A_Overview.md if missing."""
    out_path = os.path.join(path, "A_Overview.md")

    if os.path.exists(out_path):
        print(f"❌ A_Overview.md already exists in {path}, skipping.")
        return

    content = (
        f"# {module['name']} — Overview\n\n"
        "## Purpose\n"
        f"{module['summary']}\n\n"
        f"This module belongs to the **{module['category']}** domain of TriadicFrameworks.\n\n"
        "---\n\n"
        "## Canon Context\n"
        "This module inherits the full TriadicFrameworks canon:\n\n"
        "- RTT triads  \n"
        "- TFT triads  \n"
        "- Session context  \n"
        "- RTT frozen source  \n"
        "- AI initialization rules  \n\n"
        "Canon reference: `/docs/spine/spine.json`\n\n"
        "---\n\n"
        "## RTT Layer\n"
        f"This module operates at **RTT Layer {module['rtt']['layer']}**.\n\n"
        "---\n\n"
        "Generated automatically by `generate_module_bundle.py`.\n"
    )

    write_text(out_path, content)
    print(f"✔ Created {out_path}")

def main():
    print("\n=== TriadicFrameworks Module Bundle Generator ===\n")

    template = load_template()

    for root, dirs, files in os.walk("docs"):
        # Skip excluded directories
        if any(ex in root.split(os.sep) for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            module_name = os.path.basename(root)
            module_category = os.path.basename(os.path.dirname(root))

            module = generate_module_json(root, template, module_name, module_category)
            if module:
                generate_index_md(root, module)
                generate_overview_md(root, module)

    print("\n✨ Bundle generation complete — module.json, INDEX.md, and A_Overview.md created.\n")

if __name__ == "__main__":
    main()
