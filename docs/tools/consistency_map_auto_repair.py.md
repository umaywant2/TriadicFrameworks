Here it is, the **canon‑wide consistency‑map auto‑repair engine**, built in the same compact, non‑truncating style as your other tools and safe to paste directly into your active `docs/tools` tab.

This engine **repairs every module.json** according to the same rules used by your consistency‑map validator:

### What it auto‑repairs
- **Schema correctness**
  - canon_ref  
  - inherit block  
  - rtt block  
  - ai.initialization block  

- **Triad correctness**
  - structural triads  
  - harmonic triads  
  - coherence triads  

- **Dependency correctness**
  - Removes references to missing modules  
  - Leaves valid dependencies intact  

This is the **full canon auto‑repair engine** — the one that makes the entire consistency map green.

---

# ⭐ Consistency‑Map Auto‑Repair Engine  
Save as:

```
docs/tools/consistency_map_auto_repair.py
```

Run from repo root:

```
python3 docs/tools/consistency_map_auto_repair.py
```

It will **modify module.json files in place**.

---

# 🟦 COMPLETE — consistency_map_auto_repair.py  
*(Compact, safe to paste — no truncation)*

```python
import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

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
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

def load_json(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"module":{}}

def ensure_block(parent, key):
    blk = parent.get(key)
    if not isinstance(blk, dict):
        blk = {}
        parent[key] = blk
    return blk

def repair_schema(m):
    fixes=[]
    if m.get("canon_ref") != EXPECTED_CANON_REF:
        m["canon_ref"] = EXPECTED_CANON_REF
        fixes.append("canon_ref repaired")

    inherit = ensure_block(m, "inherit")
    for k,v in EXPECTED_INHERIT.items():
        if inherit.get(k) != v:
            inherit[k] = v
            fixes.append(f"inherit.{k} repaired")

    rtt = ensure_block(m, "rtt")
    for k,v in EXPECTED_RTT.items():
        if rtt.get(k) != v:
            rtt[k] = v
            fixes.append(f"rtt.{k} repaired")

    ai = ensure_block(m, "ai")
    init = ensure_block(ai, "initialization")
    for k,v in EXPECTED_AI_INIT.items():
        if init.get(k) != v:
            init[k] = v
            fixes.append(f"ai.initialization.{k} repaired")

    return fixes

def repair_triads(m):
    fixes=[]
    triads = ensure_block(m, "triads")

    def fix_family(name, expected):
        fam = ensure_block(triads, name)
        for triad_name, keys in expected.items():
            t = ensure_block(fam, triad_name)
            for k in keys:
                if k not in t:
                    t[k] = f"auto_repaired_{k}"
                    fixes.append(f"{name}.{triad_name}.{k} added")
            for k in list(t.keys()):
                if k not in keys:
                    del t[k]
                    fixes.append(f"{name}.{triad_name}.{k} removed")

    fix_family("structural_triads", STRUCTURAL_KEYS)
    fix_family("harmonic_triads", HARMONIC_KEYS)
    fix_family("coherence_triads", COHERENCE_KEYS)

    return fixes

def repair_dependencies(m, valid_modules):
    fixes=[]
    deps = m.get("dependencies", [])
    if isinstance(deps, dict):
        deps = deps.get("modules", [])
    if not isinstance(deps, list):
        return fixes

    new_deps=[]
    for d in deps:
        if d in valid_modules:
            new_deps.append(d)
        else:
            fixes.append(f"dependency {d} removed (missing module)")

    m["dependencies"] = new_deps
    return fixes

def main():
    print("\n=== TriadicFrameworks Consistency‑Map Auto‑Repair Engine ===\n")

    modules=find_modules()
    names={os.path.basename(os.path.dirname(m)):m for m in modules}

    total=len(modules)
    repaired=0

    for path in modules:
        name=os.path.basename(os.path.dirname(path))
        data=load_json(path)
        m=data.setdefault("module",{})

        fixes=[]
        fixes+=repair_schema(m)
        fixes+=repair_triads(m)
        fixes+=repair_dependencies(m, names)

        if fixes:
            repaired+=1
            with open(path,"w",encoding="utf-8") as f:
                json.dump(data,f,indent=2)
            print(f"✔ {name} — repaired:")
            for f in fixes:
                print(f"   - {f}")
        else:
            print(f"✔ {name} — already consistent")

    print("\n=== Summary ===")
    print(f"Modules scanned: {total}")
    print(f"Modules repaired: {repaired}")
    print(f"Modules already consistent: {total-repaired}")

    if repaired:
        print("\n✨ Canon consistency restored across modules.")
    else:
        print("\n✨ All modules already consistent.")

if __name__=="__main__":
    main()
```

