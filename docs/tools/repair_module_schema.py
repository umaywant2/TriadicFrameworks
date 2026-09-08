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

# ---------------------------------------------------------
# DISCOVERY
# ---------------------------------------------------------
def find_modules():
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

# ---------------------------------------------------------
# STRUCTURAL + VALUE REPAIR
# ---------------------------------------------------------
def repair(path):
    fixes=[]
    try:
        with open(path,"r",encoding="utf-8") as f:
            data=json.load(f)
    except:
        data={"module":{}}
        fixes.append("module.json was invalid JSON — rebuilt")

    if not isinstance(data.get("module"),dict):
        data["module"]={}
        fixes.append("module object created")

    module=data["module"]
    dirname=os.path.basename(os.path.dirname(path))

    # Identity fields
    if not isinstance(module.get("name"),str):
        module["name"]=dirname
        fixes.append("module.name created")
    if not isinstance(module.get("summary"),str):
        module["summary"]=f"{dirname} module (auto‑repaired)"
        fixes.append("module.summary created")
    if not isinstance(module.get("category"),str):
        module["category"]="uncategorized"
        fixes.append("module.category created")

    # canon_ref
    if module.get("canon_ref")!=EXPECTED_CANON_REF:
        module["canon_ref"]=EXPECTED_CANON_REF
        fixes.append("canon_ref corrected")

    # inherit
    inherit=module.get("inherit")
    if not isinstance(inherit,dict):
        inherit={}
        module["inherit"]=inherit
        fixes.append("inherit object created")
    for k,v in EXPECTED_INHERIT.items():
        if inherit.get(k)!=v:
            inherit[k]=v
            fixes.append(f"inherit.{k} corrected")

    # rtt
    rtt=module.get("rtt")
    if not isinstance(rtt,dict):
        rtt={}
        module["rtt"]=rtt
        fixes.append("rtt object created")
    for k,v in EXPECTED_RTT.items():
        if rtt.get(k)!=v:
            rtt[k]=v
            fixes.append(f"rtt.{k} corrected")

    # ai.initialization
    ai=module.get("ai")
    if not isinstance(ai,dict):
        ai={}
        module["ai"]=ai
        fixes.append("ai object created")

    init=ai.get("initialization")
    if not isinstance(init,dict):
        init={}
        ai["initialization"]=init
        fixes.append("ai.initialization object created")

    for k,v in EXPECTED_AI_INIT.items():
        if init.get(k)!=v:
            init[k]=v
            fixes.append(f"ai.initialization.{k} corrected")

    # Write back
    if fixes:
        with open(path,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=2)
    return fixes

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Schema‑Repair Engine ===\n")
    modules=find_modules()
    repaired=0

    for m in modules:
        name=os.path.basename(os.path.dirname(m))
        fixes=repair(m)
        if fixes:
            repaired+=1
            print(f"✔ {name} — repaired:")
            for f in fixes:
                print(f"   - {f}")
        else:
            print(f"✔ {name} — already valid")

    print("\n=== Summary ===")
    print(f"Modules scanned: {len(modules)}")
    print(f"Modules repaired: {repaired}")
    print(f"Modules already valid: {len(modules)-repaired}")

    if repaired:
        print("\n✨ Schema structure normalized across all modules.")
    else:
        print("\n✨ All modules structurally canon‑valid.")

if __name__=="__main__":
    main()
