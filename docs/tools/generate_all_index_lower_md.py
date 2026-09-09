import os
import json

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

def load_module_json(path):
    module_json_path = os.path.join(path, "module.json")
    if not os.path.exists(module_json_path):
        return None

    with open(module_json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def is_module_dir(path):
    return "module.json" in os.listdir(path)

def generate_index_lower_md(path, module):
    index_path = os.path.join(path, "index.md")

    if os.path.exists(index_path):
        print(f"❌ index.md already exists in {path}, skipping.")
        return

    name = module["name"]
    summary = module["summary"]
    category = module["category"]

    content = f"""# {name}

Welcome to the **{name}** module within the **{category}** domain of TriadicFrameworks.

This page provides a simple, lowercase entry point for static site generators and AI navigation systems.

---

## Summary
{summary}

---

## Canon Reference
This module inherits the full TriadicFrameworks canon from:

`/docs/spine/spine.json`

It loads:

- RTT triads  
- TFT triads  
- Session context  
- RTT frozen source  
- AI initialization rules  

---

## RTT Layer
This module operates at **RTT Layer {module['rtt']['layer']}**  
Source: {module['rtt']['source']}

---

## Files in This Module
This module may contain:

- Maps  
- Operators  
- Examples  
- References  

(Actual files vary by module.)

---

Generated automatically by `generate_all_index_lower_md.py`.
"""

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {index_path}")

def main():
    print("\n=== TriadicFrameworks Bulk lowercase index.md Generator ===\n")

    for root, dirs, files in os.walk("docs"):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            module_data = load_module_json(root)
            if module_data:
                module = module_data["module"]
                generate_index_lower_md(root, module)

    print("\n✨ Bulk lowercase index.md generation complete.\n")

if __name__ == "__main__":
    main()
