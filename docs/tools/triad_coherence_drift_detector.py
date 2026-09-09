import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# Canonical coherence triad structure
EXPECTED_COHERENCE = {
    "coherence_triads": {
        "coherence_core": ["coherence_field","coherence_alignment","coherence_stability"],
        "coherence_harmonic": ["harmonic_alignment","harmonic_balance","harmonic_resonance"],
        "coherence_temporal": ["temporal_continuity","temporal_stability","temporal_resonance"]
    }
}

def find_modules():
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

def score_drift(errs):
    c=len(errs)
    if c==0: return 0
    if c<=2: return 1
    if c<=4: return 2
    if c<=7: return 3
    return 4

def drift_label(score):
    return {
        0:"Pure",
        1:"Low Drift",
        2:"Moderate Drift",
        3:"High Drift",
        4:"Critical Drift"
    }[score]

def audit_coherence(path):
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

    coh=triads.get("coherence_triads")
    if not isinstance(coh,dict):
        errs.append("coherence_triads block missing")
        return errs

    # Validate each coherence triad family
    for triad_name, keys in EXPECTED_COHERENCE["coherence_triads"].items():
        t=coh.get(triad_name)
        if not isinstance(t,dict):
            errs.append(f"{triad_name} triad missing")
            continue

        # required keys
        for k in keys:
            if k not in t:
                errs.append(f"{triad_name}.{k} missing")

        # no extra keys
        for k in t.keys():
            if k not in keys:
                errs.append(f"{triad_name}.{k} is not canonical")

    return errs

def main():
    print("\n=== TriadicFrameworks Triad‑Coherence Drift Detector ===\n")

    modules=find_modules()
    total=len(modules)
    failures=0

    for m in modules:
        name=os.path.basename(os.path.dirname(m))
        errs=audit_coherence(m)
        score=score_drift(errs)

        if errs:
            failures+=1
            print(f"❌ {name} — {drift_label(score)}")
            for e in errs:
                print(f"   - {e}")
        else:
            print(f"✔ {name} — Pure")

    print("\n=== Summary ===")
    print(f"Modules scanned: {total}")
    print(f"Coherence‑pure: {total-failures}")
    print(f"Coherence‑drifted: {failures}")

    if failures==0:
        print("\n✨ All modules coherence‑pure.")
    else:
        print("\n⚠ Coherence drift detected across modules.")

if __name__=="__main__":
    main()
