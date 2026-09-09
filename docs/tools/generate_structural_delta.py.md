Here’s your **structural delta engine**, Nawder—canon‑aligned and ready to drop into your active `docs/tools` tab.

It:

- Uses the existing `structural_fingerprint.json` as **baseline**  
- Recomputes the **current structural fingerprint**  
- Produces a **delta report** per module: added/removed blocks, triad families, keys, and dependencies  

Save as:

```text
docs/tools/generate_structural_delta.py
```

Run from repo root:

```bash
python3 docs/tools/generate_structural_delta.py
```

It will create:

```text
docs/spine/structural_delta.json
```

---

```python
import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}
SPINE = os.path.join(ROOT, "spine")

BASELINE_FP = os.path.join(SPINE, "structural_fingerprint.json")
OUT_PATH = os.path.join(SPINE, "structural_delta.json")

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

    blocks = {
        "has_inherit": isinstance(m.get("inherit"), dict),
        "has_rtt": isinstance(m.get("rtt"), dict),
        "has_ai": isinstance(m.get("ai"), dict),
        "has_triads": isinstance(m.get("triads"), dict),
        "has_dependencies": m.get("dependencies") is not None,
    }

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

def load_baseline():
    if not os.path.isfile(BASELINE_FP):
        return {}
    try:
        with open(BASELINE_FP, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def diff_blocks(old, new):
    out = {"added": [], "removed": []}
    old_keys = {k for k, v in old.items() if v}
    new_keys = {k for k, v in new.items() if v}
    out["added"] = sorted(list(new_keys - old_keys))
    out["removed"] = sorted(list(old_keys - new_keys))
    return out

def diff_triads(old, new):
    result = {}
    for family in ["structural", "harmonic", "coherence"]:
        o = old.get(family, {})
        n = new.get(family, {})
        fam_delta = {
            "families_added": [],
            "families_removed": [],
            "keys_added": {},
            "keys_removed": {},
        }

        o_fams = set(o.get("keys_per_family", {}).keys())
        n_fams = set(n.get("keys_per_family", {}).keys())

        fam_delta["families_added"] = sorted(list(n_fams - o_fams))
        fam_delta["families_removed"] = sorted(list(o_fams - n_fams))

        for fam in sorted(n_fams | o_fams):
            o_keys = set(o.get("keys_per_family", {}).get(fam, []))
            n_keys = set(n.get("keys_per_family", {}).get(fam, []))
            added = sorted(list(n_keys - o_keys))
            removed = sorted(list(o_keys - n_keys))
            if added or removed:
                fam_delta["keys_added"][fam] = added
                fam_delta["keys_removed"][fam] = removed

        result[family] = fam_delta
    return result

def diff_dependencies(old, new):
    o = set(old.get("modules", []))
    n = set(new.get("modules", []))
    return {
        "added": sorted(list(n - o)),
        "removed": sorted(list(o - n)),
    }

def main():
    print("\n=== TriadicFrameworks Structural Delta Engine ===\n")

    baseline = load_baseline()
    modules = find_modules()

    current_fp = {}
    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        fp = structural_fingerprint_for_module(path)
        current_fp[name] = fp
        print(f"✔ fingerprinted current {name}")

    delta = {
        "summary": {
            "baseline_modules": len(baseline),
            "current_modules": len(current_fp),
        },
        "modules": {}
    }

    all_names = set(baseline.keys()) | set(current_fp.keys())

    for name in sorted(all_names):
        old = baseline.get(name)
        new = current_fp.get(name)

        if old is None and new is not None:
            delta["modules"][name] = {
                "status": "added",
                "blocks_delta": {},
                "triads_delta": {},
                "dependencies_delta": {},
            }
            continue
        if old is not None and new is None:
            delta["modules"][name] = {
                "status": "removed",
                "blocks_delta": {},
                "triads_delta": {},
                "dependencies_delta": {},
            }
            continue

        blocks_delta = diff_blocks(old.get("blocks", {}), new.get("blocks", {}))
        triads_delta = diff_triads(old.get("triads", {}), new.get("triads", {}))
        deps_delta = diff_dependencies(old.get("dependencies", {}), new.get("dependencies", {}))

        status = "unchanged"
        if blocks_delta["added"] or blocks_delta["removed"] or \
           any(v["families_added"] or v["families_removed"] or v["keys_added"] or v["keys_removed"]
               for v in triads_delta.values()) or \
           deps_delta["added"] or deps_delta["removed"]:
            status = "modified"

        delta["modules"][name] = {
            "status": status,
            "blocks_delta": blocks_delta,
            "triads_delta": triads_delta,
            "dependencies_delta": deps_delta,
        }

    os.makedirs(SPINE, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(delta, f, indent=2)

    print(f"\n✔ Created {OUT_PATH}")
    print("\n✨ Structural delta report generated.\n")

if __name__ == "__main__":
    main()
```
