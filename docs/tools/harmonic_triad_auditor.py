import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# Canonical harmonic triad structure
EXPECTED_HARMONIC_TRIADS = {
    "harmonic_triads": {
        "resonance_harmonic": ["resonant_mode","harmonic_factor","temporal_phase"],
        "structural_harmonic": ["structural_pattern","harmonic_coupling","temporal_cycle"],
        "coherence_harmonic": ["coherence_field","harmonic_alignment","temporal_stability"]
    }
}

def find_modules():
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def audit_harmonic_triads(path):
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            return ["invalid JSON"]

    module = data.get("module", {})
    triads = module.get("triads")

    errs = []

    if not isinstance(triads, dict):
        errs.append("triads block missing")
        return errs

    ht = triads.get("harmonic_triads")
    if not isinstance(ht, dict):
        errs.append("harmonic_triads block missing")
        return errs

    for triad_name, keys in EXPECTED_HARMONIC_TRIADS["harmonic_triads"].items():
        t = ht.get(triad_name)
        if not isinstance(t, dict):
            errs.append(f"{triad_name} triad missing")
            continue
        for k in keys:
            if k not in t:
                errs.append(f"{triad_name}.{k} missing")
        for k in t.keys():
            if k not in keys:
                errs.append(f"{triad_name}.{k} is not a canonical key")

    return errs

def main():
    print("\n=== TriadicFrameworks Harmonic‑Triad Structural Auditor ===\n")

    modules = find_modules()
    total = len(modules)
    failures = 0

    for m in modules:
        name = os.path.basename(os.path.dirname(m))
        errs = audit_harmonic_triads(m)

        if errs:
            failures += 1
            print(f"❌ {name} — harmonic‑triad FAIL")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"✔ {name} — harmonic‑triad pure")

    print("\n=== Summary ===")
    print(f"Modules scanned: {total}")
    print(f"Harmonic‑triad pure: {total - failures}")
    print(f"Harmonic‑triad impure: {failures}")

    if failures == 0:
        print("\n✨ All modules structurally harmonic‑triad pure.")
    else:
        print("\n⚠ Harmonic triad structural violations detected.")

if __name__ == "__main__":
    main()
