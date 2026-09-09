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
    # A module directory is any directory containing module.json
    return "module.json" in os.listdir(path)

def generate_index_md(path, module_data):
    index_path = os.path.join(path, "INDEX.md")

    if os.path.exists(index_path):
        print(f"❌ INDEX.md already exists in {path}, skipping.")
        return

    module = module_data["module"]
    name = module["name"]
    summary = module["summary"]
    category = module["category"]

    content = f"""# {name}

**Category:** {category}  
**Summary:** {summary}

---

## Canon Inheritance
This module inherits the TriadicFrameworks canon from:

`/docs/spine/spine.json`

It loads:

- RTT triads  
- TFT triads  
- Session context  
- RTT frozen source  
- AI initialization rules  

---

## Files
This module contains:

- Maps  
- Operators  
- Examples  
- References  

(Actual files vary by module.)

---

## RTT Layer
This module operates at **RTT Layer {module['rtt']['layer']}**  
Source: {module['rtt']['source']}

---

## AI Initialization
This module is AI‑ready and initializes with:

- load_spine_first  
- load_canon_first  
- apply_session_context  
- triad_validation  

---

Generated automatically by `generate_all_index_md.py`.
"""

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {index_path}")

def main():
    print("\n=== TriadicFrameworks Bulk INDEX.md Generator ===\n")

    for root, dirs, files in os.walk("docs"):
        # Skip excluded directories
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue

        if is_module_dir(root):
            module_data = load_module_json(root)
            if module_data:
                generate_index_md(root, module_data)

    print("\n✨ Bulk INDEX.md generation complete.\n")

if __name__ == "__main__":
    main()
