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

def generate_diagram_md(path, module):
    diagram_path = os.path.join(path, "diagram.md")

    if os.path.exists(diagram_path):
        print(f"❌ diagram.md already exists in {path}, skipping.")
        return

    name = module["name"]
    category = module["category"]

    content = f"""# {name} — Diagram

## Canon Diagram Overview
This diagram provides a structural visualization of the **{name}** module within the **{category}** domain of TriadicFrameworks.

It is designed to be AI‑readable, drift‑resistant, and canon‑aligned.

---

## Module Position in Canon
- **RTT Layer:** {module['rtt']['layer']}
- **Canon Reference:** `/docs/spine/spine.json`
- **Triad Inheritance:** RTT + TFT triads
- **Session Context:** rtt=1 | coherence=declared | drift=bounded | paradox=structural

---

## Diagram (Mermaid Spec Placeholder)

```mermaid
flowchart TD
    A[Module: {name}] --> B[Category: {category}]
    A --> C[RTT Layer: {module['rtt']['layer']}]
    A --> D[Canon Ref: spine.json]
    A --> E[Triads: RTT + TFT]
    A --> F[Session Context]
