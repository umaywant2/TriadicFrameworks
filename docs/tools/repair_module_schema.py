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
# DISCOVERY
# ---------------------------------------------------------
def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(os.path.join(root, "module.json"))
    return modules

# ---------------------------------------------------------
# STRUCTURAL + VALUE REPAIR
# ---------------------------------------------------------
def repair_module_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # Hard reset to minimal valid structure
            data = {}

    fixes = []

    # Ensure top-level module object
    if not isinstance(data.get("module"), dict):
        data["module"] = {}
        fixes.append("module object created")

    module = data["module"]

    # Basic identity fields
    dirname = os.path.basename(os.path.dirname(path))

    if not isinstance(module.get("name"), str):
        module["name"] = dirname
        fixes.append("module.name set to directory name")

    if not isinstance(module.get("summary"), str):
        module["summary"] = f"{dirname} module (auto‑repaired summary)"
        fixes.append("module.summary created")

    if not isinstance(module.get("category"), str):
        module["category"] = "uncategorized"
        fixes.append("module.category created")

    # canon_ref
    if module.get("canon_ref") != EXPECTED_CANON_REF:
        module["canon_ref"] = EXPECTED_CANON_REF
        fixes.append("canon_ref corrected/created")

    # inherit block
    inherit = module.get("inherit")
    if not isinstance(inherit, dict):
        inherit = {}
        module["inherit"] = inherit
        fixes.append("inherit object created")

    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            inherit[key] = expected
            fixes.append(f"inherit.{key} corrected/created")

    # rtt block
    rtt = module.get("rtt")
    if not isinstance(rtt, dict):
        rtt = {}
        module["rtt"] = rtt
        fixes.append("rtt object created")

    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            rtt[key] = expected
            fixes.append(f"rtt.{key} corrected/created")

    # ai.initialization block
    ai = module.get("ai")
    if not isinstance(ai, dict):
        ai = {}
        module["ai"] = ai
        fixes.append("ai object created")

    init = ai.get("initialization")
    if not isinstance(init, dict):
        init = {}
        ai["initialization"] = init
        fixes.append("ai.initialization object created")

    for key, expected in EXPECTED_AI_INIT.items():
        if init.get(key) != expected:
            init[key] = expected
            fixes.append(f"ai.initialization.{key} corrected/created")

    # Write back if anything changed
    if fixes:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return fixes

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Module.json Schema‑Repair Engine ===\n")

    modules = find_modules()
    total = len(modules)
    repaired = 0

    for module_path in modules:
        name = os.path.basename(os.path.dirname(module_path))
        fixes = repair_module_schema(module_path)

        if fixes:
            repaired += 1
            print(f"✔ {name} — schema repaired:")
            for fix in fixes:
                print(f"   - {fix}")
        else:
            print(f"✔ {name} — already structurally valid")

    print("\n=== Summary ===")
    print(f"Total modules scanned: {total}")
    print(f"Modules repaired: {repaired}")
    print(f"Modules already valid: {total - repaired}")

    if repaired == 0:
        print("\n✨ All module.json files are structurally canon‑valid.")
    else:
        print("\n✨ Schema structure normalized across all modules.")

if __name__ == "__main__":
    main()
