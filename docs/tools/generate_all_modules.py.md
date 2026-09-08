Here it is, the **bulk module.json generator**, built to sweep your entire TriadicFrameworks repo and automatically create canon‑aligned `module.json` files for every module directory that *does not already have one*.

This script is:

- **Safe** — never overwrites existing module.json files  
- **Canon‑aligned** — uses your template + spine inheritance  
- **Repo‑aware** — walks your `/docs` tree exactly the way TriadicFrameworks is structured  
- **Flexible** — works for maps, operators, examples, references, engines, profiles, signatures, diagnostics, etc.  
- **Fast** — generates all missing module.json files in seconds  

And it’s designed to live right where your active tab is pointing:  
`docs/tools/` in your GitHub repo.

---

# ⭐ Bulk Module Generator  
Save as:

```
docs/tools/generate_all_modules.py
```

Run from repo root:

```
python3 docs/tools/generate_all_modules.py
```

---

# 🟦 **generate_all_modules.py (Final Canon Version)**

```python
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
```

---

# ⭐ What This Script Does

### ✔ Walks your entire `/docs` tree  
It finds every directory that contains content (maps, operators, examples, references, etc.).

### ✔ Skips directories that should not have module.json  
- `/docs/spine/`  
- `/docs/_template/`  
- `/docs/tools/`  
- `/docs/assets/`  
- `/docs/images/`  

### ✔ Creates module.json only where missing  
Never overwrites existing files.

### ✔ Auto‑fills canon inheritance  
Every generated module includes:

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

### ✔ Auto‑fills AI initialization  
Ensuring the module loads the spine first.

### ✔ Uses your actual template  
The script reads:

```
docs/_template/module.json
```

which you just created.

---

# ⭐ You now have:

- A **single‑module generator**  
- A **bulk generator for all modules**  
- A **canon spine**  
- A **drift audit workflow**  
- A **triad alias‑aware validator**

This is the foundation of your **canon purity milestone**.
