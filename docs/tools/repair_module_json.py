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
# AUTO‑REPAIR LOGIC
# ---------------------------------------------------------
def repair_module_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    module = data.setdefault("module", {})
    fixes = []

    # canon_ref
    if module.get("canon_ref") != EXPECTED_CANON_REF:
        module["canon_ref"] = EXPECTED_CANON_REF
        fixes.append("canon_ref corrected")

    # inherit block
    inherit = module.setdefault("inherit", {})
    for key, expected in EXPECTED_INHERIT.items():
        if inherit.get(key) != expected:
            inherit[key] = expected
            fixes.append(f"inherit.{key} corrected")

    # rtt block
    rtt = module.setdefault("rtt", {})
    for key, expected in EXPECTED_RTT.items():
        if rtt.get(key) != expected:
            rtt[key] = expected
            fixes.append(f"rtt.{key} corrected")

    # ai.initialization block
    ai = module.setdefault("ai", {}).setdefault("initialization", {})
    for key, expected in EXPECTED_AI_INIT.items():
        if ai.get(key) != expected:
            ai[key] = expected
            fixes.append(f"ai.initialization.{key} corrected")

    # Write back if fixes occurred
    if fixes:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return fixes

    return []

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Module.json Auto‑Repair Engine ===\n")

    modules = find_modules()
    total = len(modules)
    repaired = 0

    for module_path in modules:
        name = os.path.basename(os.path.dirname(module_path))
        fixes = repair_module_json(module_path)

        if fixes:
            repaired += 1
            print(f"✔ {name} — repaired:")
            for fix in fixes:
                print(f"   - {fix}")
        else:
            print(f"✔ {name} — already pure")

    print("\n=== Summary ===")
    print(f"Total modules scanned: {total}")
    print(f"Modules repaired: {repaired}")
    print(f"Modules already pure: {total - repaired}")

    if repaired == 0:
        print("\n✨ All modules are canon‑pure. No repairs needed.")
    else:
        print("\n✨ Canon purity restored across all modules.")

if __name__ == "__main__":
    main()
