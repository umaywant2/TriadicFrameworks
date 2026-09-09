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
# DRIFT SCORING RULES
# ---------------------------------------------------------
def score_drift(errors):
    """
    Drift severity scoring:
    0 = No drift
    1 = Minor drift (1–2 small mismatches)
    2 = Moderate drift (3–4 mismatches)
    3 = High drift (5–7 mismatches)
    4 = Critical drift (8+ mismatches or missing blocks)
    """

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
        0: "None",
        1: "Low",
        2: "Moderate",
        3: "High",
        4: "Critical"
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

    # Validate canon_ref
    if module.get("canon_ref") != EXPECTED_CANON_REF:
        errors.append(f"canon_ref mismatch: {module.get('canon_ref')}")

    # Validate inherit block
    inherit = module.get("inherit", {})
    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            errors.append(f"inherit.{key} mismatch: {inherit.get(key)}")

    # Validate RTT block
    rtt = module.get("rtt", {})
    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            errors.append(f"rtt.{key} mismatch: {rtt.get(key)}")

    # Validate AI initialization block
    ai = module.get("ai", {}).get("initialization", {})
    for key, expected in EXPECTED_AI_INIT.items():
        if ai.get(key) != expected:
            errors.append(f"ai.initialization.{key} mismatch: {ai.get(key)}")

    return errors

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Drift‑Severity Validator ===\n")

    modules = find_modules()
    total = len(modules)
    failures = 0

    for module_path in modules:
        module_name = os.path.basename(module_path)
        errors = validate_module(module_path)
        drift_score = score_drift(errors)
        drift_text = drift_label(drift_score)

        if errors:
            failures += 1
            print(f"❌ {module_name} — FAIL — Drift Severity: {drift_score} ({drift_text})")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✔ {module_name} — PASS — Drift Severity: 0 (None)")

    print("\n=== Summary ===")
    print(f"Total modules checked: {total}")
    print(f"Passed: {total - failures}")
    print(f"Failed: {failures}")

    if failures == 0:
        print("\n✨ All modules are canon‑aligned. Zero drift across the entire framework.")
    else:
        print("\n⚠ Drift detected. Review modules with High or Critical severity first.")

if __name__ == "__main__":
    main()
