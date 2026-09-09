import os
import json

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

EXPECTED_CANON_REF = "/docs/spine/spine.json"

EXPECTED_INHERIT = {
    "canon": True,
    "session_context": True,
    "triad_alias_resolution": True
}

EXPECTED_RTT = {
    "layer": 1,
    "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
}

EXPECTED_AI_INIT = {
    "load_spine_first": True,
    "load_canon_first": True,
    "apply_session_context": True,
    "triad_validation": True
}

# ---------------------------------------------------------
# DRIFT SCORING
# ---------------------------------------------------------
def score_drift(errors):
    count = len(errors)

    if count == 0:
        return 0
    if count <= 2:
        return 1
    if count <= 4:
        return 2
    if count <= 7:
        return 3
    return 4

def drift_label(score):
    return {
        0: "Pure",
        1: "Low Drift",
        2: "Moderate Drift",
        3: "High Drift",
        4: "Critical Drift"
    }[score]

def drift_color(score):
    return {
        0: "🟩",
        1: "🟨",
        2: "🟧",
        3: "🟥",
        4: "⬛"
    }[score]

# ---------------------------------------------------------
# MODULE VALIDATION
# ---------------------------------------------------------
def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(root)
    return modules

def load_module_json(path):
    with open(os.path.join(path, "module.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def validate_module(path):
    data = load_module_json(path)
    module = data.get("module", {})

    errors = []

    # canon_ref
    if module.get("canon_ref") != EXPECTED_CANON_REF:
        errors.append("canon_ref mismatch")

    # inherit
    inherit = module.get("inherit", {})
    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            errors.append(f"inherit.{key} mismatch")

    # rtt
    rtt = module.get("rtt", {})
    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            errors.append(f"rtt.{key} mismatch")

    # ai.initialization
    ai = module.get("ai", {}).get("initialization", {})
    for key, expected in EXPECTED_AI_INIT.items():
        if ai.get(key) != expected:
            errors.append(f"ai.initialization.{key} mismatch")

    return errors

# ---------------------------------------------------------
# BADGE GENERATION
# ---------------------------------------------------------
def generate_badge(path, module_name, score):
    badge_path = os.path.join(path, "triad_purity_badge.md")

    if os.path.exists(badge_path):
        print(f"❌ triad_purity_badge.md already exists in {path}, skipping.")
        return

    label = drift_label(score)
    color = drift_color(score)

    content = f"""# Triad Purity Badge — {module_name}

{color} **{label}**

This badge reflects the module’s triad purity based on canon inheritance, RTT alignment, and AI initialization correctness.

---

## Scoring
- **0 — Pure**  
- **1 — Low Drift**  
- **2 — Moderate Drift**  
- **3 — High Drift**  
- **4 — Critical Drift**

This module scored: **{score} — {label}**

---

Generated automatically by `generate_triad_purity_badges.py`.
"""

    with open(badge_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✔ Created {badge_path}")

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Triad Purity Badge Generator ===\n")

    modules = find_modules()

    for module_path in modules:
        module_name = os.path.basename(module_path)
        errors = validate_module(module_path)
        score = score_drift(errors)

        generate_badge(module_path, module_name, score)

    print("\n✨ Triad purity badges generated for all modules.\n")

if __name__ == "__main__":
    main()
