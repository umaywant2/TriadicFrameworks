import os
import json

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
        return False

    for f in os.listdir(path):
        if f.endswith((".md", ".txt", ".json")) and f != "module.json":
            return True

    return False

def generate_module_json(path, template):
    module_name = os.path.basename(path)

    data = template.copy()

    # Fill in module fields
    data["module"]["name"] = module_name
    data["module"]["summary"] = f"Auto‑generated module.json for {module_name}"
    data["module"]["category"] = os.path.basename(os.path.dirname(path))

    # Canon inheritance
    data["module"]["canon_ref"] = SPINE_REF
    data["module"]["inherit"] = {
        "canon": True,
        "session_context": True,
        "triad_alias_resolution": True
    }

    # RTT block
    data["module"]["rtt"] = {
        "layer": 1,
        "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
    }

    # AI initialization
    data["module"]["ai"] = {
        "initialization": {
            "load_spine_first": True,
            "load_canon_first": True,
            "apply_session_context": True,
            "triad_validation": True
        }
    }

    out_path = os.path.join(path, "module.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"✔ Created {out_path}")

def main():
    print("\n=== TriadicFrameworks Bulk Module Generator ===\n")

    template = load_template()

    for root, dirs, files in os.walk("docs"):
        # Skip excluded directories
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue

        # Check if this directory qualifies as a module
        if is_module_dir(root):
            generate_module_json(root, template)

    print("\n✨ Bulk generation complete — all missing module.json files created.\n")

if __name__ == "__main__":
    main()
