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

def find_modules():
    """Return all module directories containing module.json."""
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

def main():
    print("\n=== TriadicFrameworks module.json Inheritance Validator ===\n")

    modules = find_modules()
    total = len(modules)
    failures = 0

    for module_path in modules:
        module_name = os.path.basename(module_path)
        errors = validate_module(module_path)

        if errors:
            failures += 1
            print(f"❌ {module_name} — FAIL")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✔ {module_name} — PASS")

    print("\n=== Summary ===")
    print(f"Total modules checked: {total}")
    print(f"Passed: {total - failures}")
    print(f"Failed: {failures}")

    if failures == 0:
        print("\n✨ All modules are canon‑aligned. Perfect inheritance.")
    else:
        print("\n⚠ Some modules need correction. See errors above.")

if __name__ == "__main__":
    main()
