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
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def is_module_dir(path):
    return "module.json" in os.listdir(path)

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

    data = deepcopy(template)

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

    lines = [
        f"# {module['name']}",
        "",
        f"**Category:** {module['category']}  ",
        f"**Summary:** {module['summary']}",
        "",
        "---",
        "",
        "## Canon Inheritance",
        "This module inherits the TriadicFrameworks canon from:",
        "",
        "`/docs/spine/spine.json`",
        "",
        "It loads:",
        "",
        "- RTT triads",
        "- TFT triads",
        "- Session context",
        "- RTT frozen source",
        "- AI initialization rules",
        "",
        "---",
        "",
        "## RTT Layer",
        f"This module operates at **RTT Layer {module['rtt']['layer']}**",
        f"Source: {module['rtt']['source']}",
        "",
        "---",
        "",
        "Generated automatically by `generate_full_module_bundle.py`."
    ]

    write_text(out_path, "\n".join(lines))
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# A_Overview.md
# ---------------------------------------------------------
def generate_overview_md(path, module):
    out_path = os.path.join(path, "A_Overview.md")

    if os.path.exists(out_path):
        print(f"❌ A_Overview.md already exists in {path}, skipping.")
        return

    lines = [
        f"# {module['name']} — Overview",
        "",
        "## Purpose",
        module["summary"],
        "",
        f"This module belongs to the **{module['category']}** domain of TriadicFrameworks.",
        "",
        "---",
        "",
        "## Canon Context",
        "This module inherits the full TriadicFrameworks canon:",
        "",
        "- RTT triads",
        "- TFT triads",
        "- Session context",
        "- RTT frozen source",
        "- AI initialization rules",
        "",
        "Canon reference: `/docs/spine/spine.json`",
        "",
        "---",
        "",
        "## RTT Layer",
        f"This module operates at **RTT Layer {module['rtt']['layer']}**.",
        "",
        "---",
        "",
        "Generated automatically by `generate_full_module_bundle.py`."
    ]

    write_text(out_path, "\n".join(lines))
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# diagram.md
# ---------------------------------------------------------
def generate_diagram_md(path, module):
    out_path = os.path.join(path, "diagram.md")

    if os.path.exists(out_path):
        print(f"❌ diagram.md already exists in {path}, skipping.")
        return

    lines = [
        f"# {module['name']} — Diagram",
        "",
        "## Canon Diagram Overview",
        f"This diagram provides a structural visualization of the **{module['name']}** module.",
        "",
        "---",
        "",
        "## Diagram (Mermaid)",
        "",
        "```mermaid",
        "flowchart TD",
        f"    A[Module: {module['name']}] --> B[Category: {module['category']}]",
        f"    A --> C[RTT Layer: {module['rtt']['layer']}]",
        "    A --> D[Canon Ref: spine.json]",
        "    A --> E[Triads: RTT + TFT]",
        "    A --> F[Session Context]",
        "```",
        "",
        "---",
        "",
        "Generated automatically by `generate_full_module_bundle.py`."
    ]

    write_text(out_path, "\n".join(lines))
    print(f"✔ Created {out_path}")

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Full Module Bundle Generator ===\n")

    template = load_template()

    for root, dirs, files in os.walk("docs"):
        if any(ex in root.split(os.sep) for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            module_name = os.path.basename(root)
            module_category = os.path.basename(os.path.dirname(root))

            module = generate_module_json(root, template, module_name, module_category)
            if module:
                generate_index_md(root, module)
                generate_overview_md(root, module)
                generate_diagram_md(root, module)

    print("\n✨ Full bundle generation complete.\n")

if __name__ == "__main__":
    main()
