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
        return None

def check_schema(data):
    if not isinstance(data,dict): return ["invalid JSON"]
    m=data.get("module")
    if not isinstance(m,dict): return ["module block missing"]
    errs=[]
    if m.get("canon_ref")!=EXPECTED_CANON_REF:
        errs.append("canon_ref mismatch")
    inh=m.get("inherit",{})
    for k,v in EXPECTED_INHERIT.items():
        if inh.get(k)!=v:
            errs.append(f"inherit.{k} mismatch")
    rtt=m.get("rtt",{})
    for k,v in EXPECTED_RTT.items():
        if rtt.get(k)!=v:
            errs.append(f"rtt.{k} mismatch")
    ai=m.get("ai",{}).get("initialization",{})
    for k,v in EXPECTED_AI_INIT.items():
        if ai.get(k)!=v:
            errs.append(f"ai.initialization.{k} mismatch")
    return errs

def check_block(block, expected):
    errs=[]
    if not isinstance(block,dict):
        return ["block missing"]
    for triad_name, keys in expected.items():
        t=block.get(triad_name)
        if not isinstance(t,dict):
            errs.append(f"{triad_name} triad missing")
            continue
        for k in keys:
            if k not in t:
                errs.append(f"{triad_name}.{k} missing")
        for k in t.keys():
            if k not in keys:
                errs.append(f"{triad_name}.{k} not canonical")
    return errs

def check_triads(data):
    m=data.get("module",{})
    triads=m.get("triads")
    if not isinstance(triads,dict):
        return ["triads block missing"]
    errs=[]
    errs+=check_block(triads.get("structural_triads"),STRUCTURAL_KEYS)
    errs+=check_block(triads.get("harmonic_triads"),HARMONIC_KEYS)
    errs+=check_block(triads.get("coherence_triads"),COHERENCE_KEYS)
    return errs

def get_dependencies(data):
    m=data.get("module",{})
    deps=m.get("dependencies",[])
    if isinstance(deps,dict):
        deps=deps.get("modules",[])
    if not isinstance(deps,list):
        return []
    return [d for d in deps if isinstance(d,str)]

def detect_cycles(edges):
    graph={}
    for a,b in edges:
        graph.setdefault(a,[]).append(b)
    visited=set()
    stack=set()
    cycles=[]
    def dfs(n,path):
        if n in stack:
            idx=path.index(n)
            cycles.append(path[idx:])
            return
        if n in visited: return
        visited.add(n)
        stack.add(n)
        for nxt in graph.get(n,[]):
            dfs(nxt,path+[nxt])
        stack.remove(n)
    for n in graph.keys():
        dfs(n,[n])
    uniq=[]
    seen=set()
    for c in cycles:
        t=tuple(c)
        if t not in seen:
            seen.add(t)
            uniq.append(c)
    return uniq

def score_layer(errs):
    if len(errs)==0: return "ok"
    if len(errs)<=2: return "warn"
    return "fail"

def color(layer):
    return {
        "ok":"#2ecc71",
        "warn":"#f1c40f",
        "fail":"#e74c3c"
    }[layer]

def build_html(rows):
    out=os.path.join(ROOT,"spine","consistency_atlas.html")
    os.makedirs(os.path.dirname(out),exist_ok=True)

    html=f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TriadicFrameworks Multi‑Layer Consistency Atlas</title>
<style>
body {{ font-family: system-ui; margin: 2rem; }}
table {{ border-collapse: collapse; width: 100%; }}
th,td {{ border:1px solid #ddd; padding:0.5rem; text-align:center; }}
th {{ background:#f5f5f5; }}
</style>
</head>
<body>
<h1>Multi‑Layer Consistency Atlas</h1>
<table>
<thead>
<tr>
<th>Module</th>
<th>Schema</th>
<th>Triads</th>
<th>Dependencies</th>
<th>Composite</th>
</tr>
</thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
</body>
</html>
"""
    with open(out,"w",encoding="utf-8") as f:
        f.write(html)
    print(f"✔ Created {out}")

def main():
    print("\n=== TriadicFrameworks Multi‑Layer Consistency Atlas Generator ===\n")

    modules=find_modules()
    names={os.path.basename(os.path.dirname(m)):m for m in modules}

    edges=[]
    missing=[]
    schema_errs={}
    triad_errs={}
    dep_missing={}

    for path in modules:
        name=os.path.basename(os.path.dirname(path))
        data=load_json(path)
        s=check_schema(data)
        t=check_triads(data)
        deps=get_dependencies(data)

        schema_errs[name]=s
        triad_errs[name]=t
        dep_missing[name]=[]

        for d in deps:
            edges.append((name,d))
            if d not in names:
                missing.append((name,d))
                dep_missing[name].append(d)

    cycles=detect_cycles(edges)
    cycles_by_module={}
    for c in cycles:
        for m in c:
            cycles_by_module.setdefault(m,[]).append(c)

    rows=[]
    for path in modules:
        name=os.path.basename(os.path.dirname(path))
        s_layer=score_layer(schema_errs[name])
        t_layer=score_layer(triad_errs[name])
        d_layer=score_layer(dep_missing[name] + cycles_by_module.get(name,[]))

        composite="ok"
        if "fail" in (s_layer,t_layer,d_layer):
            composite="fail"
        elif "warn" in (s_layer,t_layer,d_layer):
            composite="warn"

        rows.append(f"""
        <tr>
          <td>{name}</td>
          <td style="background:{color(s_layer)}">{s_layer}</td>
          <td style="background:{color(t_layer)}">{t_layer}</td>
          <td style="background:{color(d_layer)}">{d_layer}</td>
          <td style="background:{color(composite)}">{composite}</td>
        </tr>
        """)

    build_html(rows)
    print("\n✨ Multi‑layer consistency atlas generated.\n")

if __name__=="__main__":
    main()
