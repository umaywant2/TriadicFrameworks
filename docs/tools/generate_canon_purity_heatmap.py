import os
import json
from jsonschema import validate, ValidationError

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# ---------------- Schema ----------------
MODULE_SCHEMA = {
    "type":"object",
    "properties":{
        "module":{
            "type":"object",
            "properties":{
                "name":{"type":"string"},
                "summary":{"type":"string"},
                "category":{"type":"string"},
                "canon_ref":{"type":"string","enum":["/docs/spine/spine.json"]},
                "inherit":{
                    "type":"object",
                    "properties":{
                        "canon":{"type":"boolean"},
                        "session_context":{"type":"boolean"},
                        "triad_alias_resolution":{"type":"boolean"}
                    },
                    "required":["canon","session_context","triad_alias_resolution"]
                },
                "rtt":{
                    "type":"object",
                    "properties":{
                        "layer":{"type":"integer"},
                        "source":{"type":"string"}
                    },
                    "required":["layer","source"]
                },
                "ai":{
                    "type":"object",
                    "properties":{
                        "initialization":{
                            "type":"object",
                            "properties":{
                                "load_spine_first":{"type":"boolean"},
                                "load_canon_first":{"type":"boolean"},
                                "apply_session_context":{"type":"boolean"},
                                "triad_validation":{"type":"boolean"}
                            },
                            "required":[
                                "load_spine_first",
                                "load_canon_first",
                                "apply_session_context",
                                "triad_validation"
                            ]
                        }
                    },
                    "required":["initialization"]
                }
            },
            "required":[
                "name","summary","category",
                "canon_ref","inherit","rtt","ai"
            ]
        }
    },
    "required":["module"]
}

# ---------------- Drift scoring ----------------
def score_drift(errors):
    c=len(errors)
    if c==0: return 0
    if c<=2: return 1
    if c<=4: return 2
    if c<=7: return 3
    return 4

def drift_color(score):
    return {
        0:"#2ecc71",
        1:"#f1c40f",
        2:"#e67e22",
        3:"#e74c3c",
        4:"#2c3e50"
    }[score]

# ---------------- Discovery ----------------
def find_modules():
    out=[]
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            out.append(os.path.join(root,"module.json"))
    return out

# ---------------- Validation ----------------
def validate_schema(path):
    with open(path,"r",encoding="utf-8") as f:
        data=json.load(f)
    try:
        validate(instance=data,schema=MODULE_SCHEMA)
        return []
    except ValidationError as e:
        return [str(e)]

def validate_drift(path):
    with open(path,"r",encoding="utf-8") as f:
        data=json.load(f)
    m=data.get("module",{})
    errs=[]

    if m.get("canon_ref")!="/docs/spine/spine.json":
        errs.append("canon_ref mismatch")

    inh=m.get("inherit",{})
    for k in ["canon","session_context","triad_alias_resolution"]:
        if inh.get(k)!=True:
            errs.append(f"inherit.{k} mismatch")

    rtt=m.get("rtt",{})
    if rtt.get("layer")!=1:
        errs.append("rtt.layer mismatch")
    if rtt.get("source")!="https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html":
        errs.append("rtt.source mismatch")

    ai=m.get("ai",{}).get("initialization",{})
    for k in ["load_spine_first","load_canon_first","apply_session_context","triad_validation"]:
        if ai.get(k)!=True:
            errs.append(f"ai.initialization.{k} mismatch")

    return errs

# ---------------- Heatmap SVG ----------------
def build_heatmap(report):
    svg_path=os.path.join(ROOT,"canon_purity_heatmap.svg")

    cell=20
    pad=5
    cols=20
    rows=(len(report)+cols-1)//cols
    width=cols*cell+pad*2
    height=rows*cell+pad*2

    rects=[]
    for i,r in enumerate(report):
        row=i//cols
        col=i%cols
        x=pad+col*cell
        y=pad+row*cell
        color=drift_color(r["drift_score"])
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell-2}" height="{cell-2}" '
            f'fill="{color}" stroke="#333" stroke-width="0.5">'
            f'<title>{r["name"]} — drift {r["drift_score"]}</title>'
            f'</rect>'
        )

    svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>
{''.join(rects)}
</svg>
"""
    with open(svg_path,"w",encoding="utf-8") as f:
        f.write(svg)
    print(f"✔ Created {svg_path}")

# ---------------- Main ----------------
def main():
    print("\n=== TriadicFrameworks Canon Purity Heatmap Generator ===\n")

    modules=find_modules()
    report=[]

    for path in modules:
        name=os.path.basename(os.path.dirname(path))
        schema_err=validate_schema(path)
        drift_err=validate_drift(path)
        drift_score=score_drift(drift_err)

        report.append({
            "name":name,
            "schema_errors":schema_err,
            "drift_errors":drift_err,
            "drift_score":drift_score
        })

    build_heatmap(report)
    print("\n✨ Canon purity heatmap generated.\n")

if __name__=="__main__":
    main()
