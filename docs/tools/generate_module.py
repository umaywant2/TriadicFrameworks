import os
import json

TEMPLATE_PATH = "docs/_template/module.json"
SPINE_REF = "/docs/spine/spine.json"

def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_module_json(module_dir, data):
    path = os.path.join(module_dir, "module.json")

    if os.path.exists(path):
        print(f"❌ module.json already exists in {module_dir}, skipping.")
        return

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"✔ Created {path}")

def main():
    print("\n=== TriadicFrameworks Module Generator ===\n")

    module_name = input("Module name: ").strip()
    module_summary = input("Module summary: ").strip()
    module_category = input("Module category: ").strip()
    module_dir = input("Module directory (e.g., docs/atmosphere/maps): ").strip()

    if not os.path.isdir(module_dir):
        print(f"❌ Directory does not exist: {module_dir}")
        return

    template = load_template()

    # Fill in module fields
    template["module"]["name"] = module_name
    template["module"]["summary"] = module_summary
    template["module"]["category"] = module_category

    # Ensure canon inheritance is correct
    template["module"]["canon_ref"] = SPINE_REF
    template["module"]["inherit"] = {
        "canon": True,
        "session_context": True,
        "triad_alias_resolution": True
    }

    # Ensure RTT block is correct
    template["module"]["rtt"] = {
        "layer": 1,
        "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
    }

    # Ensure AI initialization block is correct
    template["module"]["ai"] = {
        "initialization": {
            "load_spine_first": True,
            "load_canon_first": True,
            "apply_session_context": True,
            "triad_validation": True
        }
    }

    write_module_json(module_dir, template)

    print("\n✨ Done. Your module.json is canon‑aligned and ready.\n")

if __name__ == "__main__":
    main()
