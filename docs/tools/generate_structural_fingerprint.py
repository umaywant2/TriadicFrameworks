import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

def find_modules():
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def safe_load(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def structural_fingerprint_for_module(path):
    data = safe_load(path)
    m = data.get("module", {})

    name = m.get("name") or os.path.basename(os.path.dirname(path))
    category = m.get("category", "uncategorized")

    # high‑level blocks present
    blocks = {
        "has_inherit": isinstance(m.get("inherit"), dict),
        "has_rtt": isinstance(m.get("rtt"), dict),
        "has_ai": isinstance(m.get("ai"), dict),
        "has_triads": isinstance(m.get("triads"), dict),
        "has_dependencies": m.get("dependencies") is not None,
    }

    # triad presence + shapes
    triads = m.get("triads", {})
    structural = triads.get("structural_triads", {})
    harmonic = triads.get("harmonic_triads", {})
    coherence = triads.get("coherence_triads", {})

    def triad_shape(block):
        if not isinstance(block, dict):
            return {"families": 0, "keys_per_family": {}}
        families = list(block.keys())
        keys_per_family = {}
        for fam, obj in block.items():
            if isinstance(obj, dict):
                keys_per_family[fam] = sorted(obj.keys())
            else:
                keys_per_family[fam] = []
        return {
            "families": len(families),
            "keys_per_family": keys_per_family,
        }

    fp = {
        "name": name,
        "category": category,
        "path": path,
        "blocks": blocks,
        "triads": {
            "structural": triad_shape(structural),
            "harmonic": triad_shape(harmonic),
            "coherence": triad_shape(coherence),
        },
        "dependencies": {
            "modules": []
        }
    }

    deps = m.get("dependencies", [])
    if isinstance(deps, dict):
        deps = deps.get("modules", [])
    if isinstance(deps, list):
        fp["dependencies"]["modules"] = [d for d in deps if isinstance(d, str)]

    return fp

def main():
    print("\n=== TriadicFrameworks Canon‑Wide Structural Fingerprint Generator ===\n")

    modules = find_modules()
    fingerprint = {}

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        fp = structural_fingerprint_for_module(path)
        fingerprint[name] = fp
        print(f"✔ fingerprinted {name}")

    out_path = os.path.join(ROOT, "spine", "structural_fingerprint.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(fingerprint, f, indent=2)

    print(f"\n✔ Created {out_path}")
    print("\n✨ Canon‑wide structural fingerprint captured.\n")

if __name__ == "__main__":
    main()
