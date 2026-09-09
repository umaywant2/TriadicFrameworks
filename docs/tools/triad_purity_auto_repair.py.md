Here’s your **triad‑purity auto‑repair engine**, aligned with the rest of your canon tooling and safe to paste into your active `docs/tools` tab.

Save as:

```text
docs/tools/triad_purity_auto_repair.py
```

Run from repo root:

```bash
python3 docs/tools/triad_purity_auto_repair.py
```

It will **modify module.json files in place**, repairing structural, harmonic, and coherence triads to canonical shape.

---

```python
import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

STRUCTURAL_KEYS = {
    "generative": ["resonance_source","structural_seed","temporal_onset"],
    "transformational": ["resonant_input","structural_transformation","temporal_modulation"],
    "coherence": ["resonant_field","structural_alignment","temporal_continuity"],
}

HARMONIC_KEYS = {
    "resonance_harmonic": ["resonant_mode","harmonic_factor","temporal_phase"],
    "structural_harmonic": ["structural_pattern","harmonic_coupling","temporal_cycle"],
    "coherence_harmonic": ["coherence_field","harmonic_alignment","temporal_stability"],
}

COHERENCE_KEYS = {
    "coherence_core": ["coherence_field","coherence_alignment","coherence_stability"],
    "coherence_harmonic": ["harmonic_alignment","harmonic_balance","harmonic_resonance"],
    "coherence_temporal": ["temporal_continuity","temporal_stability","temporal_resonance"],
}

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
        return {"module": {}}

def ensure_block(parent, key):
    blk = parent.get(key)
    if not isinstance(blk, dict):
        blk = {}
        parent[key] = blk
    return blk

def repair_family(triads, family_name, expected):
    fixes = []
    fam = ensure_block(triads, family_name)
    for triad_name, keys in expected.items():
        t = ensure_block(fam, triad_name)
        # add missing canonical keys
        for k in keys:
            if k not in t:
                t[k] = f"auto_repaired_{k}"
                fixes.append(f"{family_name}.{triad_name}.{k} added")
        # remove non‑canonical keys
        for k in list(t.keys()):
            if k not in keys:
                del t[k]
                fixes.append(f"{family_name}.{triad_name}.{k} removed")
    return fixes

def repair_triads(module):
    fixes = []
    triads = ensure_block(module, "triads")

    fixes += repair_family(triads, "structural_triads", STRUCTURAL_KEYS)
    fixes += repair_family(triads, "harmonic_triads", HARMONIC_KEYS)
    fixes += repair_family(triads, "coherence_triads", COHERENCE_KEYS)

    return fixes

def main():
    print("\n=== TriadicFrameworks Triad‑Purity Auto‑Repair Engine ===\n")

    modules = find_modules()
    repaired = 0

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        data = safe_load(path)
        module = data.setdefault("module", {})

        fixes = repair_triads(module)

        if fixes:
            repaired += 1
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"✔ {name} — triad‑purity repaired:")
            for fmsg in fixes:
                print(f"   - {fmsg}")
        else:
            print(f"✔ {name} — already triad‑pure")

    print("\n=== Summary ===")
    print(f"Modules scanned: {len(modules)}")
    print(f"Modules triad‑repaired: {repaired}")
    print(f"Modules already triad‑pure: {len(modules) - repaired}")

    if repaired:
        print("\n✨ Triad‑purity restored across modules.")
    else:
        print("\n✨ All modules already structurally triad‑pure.")

if __name__ == "__main__":
    main()
```
