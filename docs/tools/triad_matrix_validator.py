import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# Canonical triad matrix structure
EXPECTED_MATRIX = {
    "triad_matrix": {
        "generative": ["resonance_harmonic","structural_seed","temporal_onset"],
        "transformational": ["resonant_input","structural_transformation","temporal_modulation"],
        "coherence": ["coherence_field","structural_alignment","temporal_continuity"]
    }
}

def find_modules():
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

def audit_matrix(path):
    with open(path,"r",encoding="utf-8") as f:
        try:
            data=json.load(f)
        except:
            return ["invalid JSON"]

    module=data.get("module",{})
    triads=module.get("triads")
    errs=[]

    if not isinstance(triads,dict):
        errs.append("triads block missing")
        return errs

    matrix=triads.get("triad_matrix")
    if not isinstance(matrix,dict):
        errs.append("triad_matrix block missing")
        return errs

    # Validate rows
    for row, cols in EXPECTED_MATRIX["triad_matrix"].items():
        r=matrix.get(row)
        if not isinstance(r,dict):
            errs.append(f"row {row} missing")
            continue

        # required columns
        for c in cols:
            if c not in r:
                errs.append(f"{row}.{c} missing")

        # no extra columns
        for c in r.keys():
            if c not in cols:
                errs.append(f"{row}.{c} is not canonical")

    return errs

def main():
    print("\n=== TriadicFrameworks Triad‑Matrix Validator ===\n")

    modules=find_modules()
    total=len(modules)
    failures=0

    for m in modules:
        name=os.path.basename(os.path.dirname(m))
        errs=audit_matrix(m)

        if errs:
            failures+=1
            print(f"❌ {name} — triad‑matrix FAIL")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"✔ {name} — triad‑matrix pure")

    print("\n=== Summary ===")
    print(f"Modules scanned: {total}")
    print(f"Matrix‑pure: {total-failures}")
    print(f"Matrix‑impure: {failures}")

    if failures==0:
        print("\n✨ All modules are triad‑matrix pure.")
    else:
        print("\n⚠ Triad‑matrix structural violations detected.")

if __name__=="__main__":
    main()
