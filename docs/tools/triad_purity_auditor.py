import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# Canonical triad structure
EXPECTED_TRIADS = {
    "structural_triads": {
        "generative": ["resonance_source","structural_seed","temporal_onset"],
        "transformational": ["resonant_input","structural_transformation","temporal_modulation"],
        "coherence": ["resonant_field","structural_alignment","temporal_continuity"]
    }
}

def find_modules():
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

def audit_triads(path):
    with open(path,"r",encoding="utf-8") as f:
        try:
            data=json.load(f)
        except:
            return ["invalid JSON"]

    module=data.get("module",{})
    triads=module.get("triads")

    errs=[]

    # triads block must exist
    if not isinstance(triads,dict):
        errs.append("triads block missing")
        return errs

    # structural_triads must exist
    st=triads.get("structural_triads")
    if not isinstance(st,dict):
        errs.append("structural_triads block missing")
        return errs

    # check each canonical triad family
    for triad_name, keys in EXPECTED_TRIADS["structural_triads"].items():
        t=st.get(triad_name)
        if not isinstance(t,dict):
            errs.append(f"{triad_name} triad missing")
            continue
        # check required keys
        for k in keys:
            if k not in t:
                errs.append(f"{triad_name}.{k} missing")
        # check no extra keys
        for k in t.keys():
            if k not in keys:
                errs.append(f"{triad_name}.{k} is not a canonical key")

    return errs

def main():
    print("\n=== TriadicFrameworks Triad‑Purity Structural Auditor ===\n")

    modules=find_modules()
    total=len(modules)
    failures=0

    for m in modules:
        name=os.path.basename(os.path.dirname(m))
        errs=audit_triads(m)

        if errs:
            failures+=1
            print(f"❌ {name} — triad‑purity FAIL")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"✔ {name} — triad‑pure")

    print("\n=== Summary ===")
    print(f"Modules scanned: {total}")
    print(f"Triad‑pure: {total-failures}")
    print(f"Triad‑impure: {failures}")

    if failures==0:
        print("\n✨ All modules structurally triad‑pure.")
    else:
        print("\n⚠ Triad structural violations detected.")

if __name__=="__main__":
    main()
