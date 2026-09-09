Here you go, a **clean, canonical, repo‑ready auto‑generator script** that creates `module.json` files from your template. It’s designed specifically for your TriadicFrameworks repo structure (including the template you have open in your current tab: **docs/_template/module.json** ).

This script:

- Reads your **template module.json**
- Prompts for module name, summary, category
- Auto‑fills the inheritance + RTT blocks
- Writes the new module.json into the correct module directory
- Prevents overwriting existing module.json files
- Ensures every module inherits the canon spine

It’s safe, simple, and fully aligned with your canon purity workflow.

---

# ⭐ **module.json Auto‑Generator Script (Python)**

Save this as:

```
tools/generate_module.py
```

Run it from the repo root:

```
python3 tools/generate_module.py
```

Here is the full script:

```python
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
```

---

# 🔍 **Why This Script Is Canon‑Aligned**

### ✔ Uses your actual template  
It loads the file you have open in your GitHub tab (docs/_template/module.json) .

### ✔ Auto‑fills the canon inheritance  
Every generated module automatically includes:

```json
"canon_ref": "/docs/spine/spine.json",
"inherit": {
  "canon": true,
  "session_context": true,
  "triad_alias_resolution": true
}
```

### ✔ Auto‑fills RTT  
Every module declares:

```json
"rtt": {
  "layer": 1,
  "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
}
```

### ✔ Prevents overwriting existing modules  
No accidental drift.

### ✔ Works for all ~200 modules  
This is your bulk‑generation tool.
