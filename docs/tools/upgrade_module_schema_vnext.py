import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

VNEXT_SCHEMA_VERSION = "2.0"

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
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def upgrade(path):
    fixes = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return ["invalid JSON — skipped"]

    if not isinstance(data.get("module"), dict):
        data["module"] = {}
        fixes.append("module object created")

    module = data["module"]

    # vNext schema_version
    meta = module.get("metadata")
    if not isinstance(meta, dict):
        meta = {}
        module["metadata"] = meta
        fixes.append("metadata object created")

    if meta.get("schema_version") != VNEXT_SCHEMA_VERSION:
        meta["schema_version"] = VNEXT_SCHEMA_VERSION
        fixes.append(f"metadata.schema_version set to {VNEXT_SCHEMA_VERSION}")

    # inherit normalization
    inherit = module.get("inherit")
    if not isinstance(inherit, dict):
        inherit = {}
        module["inherit"] = inherit
        fixes.append("inherit object created")

    for k, v in EXPECTED_INHERIT.items():
        if inherit.get(k) != v:
            inherit[k] = v
            fixes.append(f"inherit.{k} normalized")

    # rtt normalization
    rtt = module.get("rtt")
    if not isinstance(rtt, dict):
        rtt = {}
        module["rtt"] = rtt
        fixes.append("rtt object created")

    for k, v in EXPECTED_RTT.items():
        if rtt.get(k) != v:
            rtt[k] = v
            fixes.append(f"rtt.{k} normalized")

    # ai.initialization normalization
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

    for k, v in EXPECTED_AI_INIT.items():
        if init.get(k) != v:
            init[k] = v
            fixes.append(f"ai.initialization.{k} normalized")

    # vNext triads scaffold
    triads = module.get("triads")
    if not isinstance(triads, dict):
        triads = {}
        module["triads"] = triads
        fixes.append("triads scaffold created for vNext")

    # Write back
    if fixes:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return fixes

def main():
    print("\n=== TriadicFrameworks Module.json vNext Schema Upgrader ===\n")

    modules = find_modules()
    upgraded = 0

    for m in modules:
        name = os.path.basename(os.path.dirname(m))
        fixes = upgrade(m)
        if fixes:
            upgraded += 1
            print(f"✔ {name} — upgraded:")
            for f in fixes:
                print(f"   - {f}")
        else:
            print(f"✔ {name} — already vNext")

    print("\n=== Summary ===")
    print(f"Modules scanned: {len(modules)}")
    print(f"Modules upgraded: {upgraded}")
    print(f"Modules already vNext: {len(modules) - upgraded}")

    if upgraded:
        print("\n✨ vNext schema applied across module.json files.")
    else:
        print("\n✨ All modules already on vNext schema.")

if __name__ == "__main__":
    main()
