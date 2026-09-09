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
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None

def check_schema(data):
    if not isinstance(data, dict):
        return ["invalid JSON"]
    m = data.get("module")
    if not isinstance(m, dict):
        return ["module block missing"]
    errs = []
    if m.get("canon_ref") != EXPECTED_CANON_REF:
        errs.append("canon_ref mismatch")
    inh = m.get("inherit", {})
    for k, v in EXPECTED_INHERIT.items():
        if inh.get(k) != v:
            errs.append(f"inherit.{k} mismatch")
    rtt = m.get("rtt", {})
    for k, v in EXPECTED_RTT.items():
        if rtt.get(k) != v:
            errs.append(f"rtt.{k} mismatch")
    ai = m.get("ai", {}).get("initialization", {})
    for k, v in EXPECTED_AI_INIT.items():
        if ai.get(k) != v:
            errs.append(f"ai.initialization.{k} mismatch")
    return errs

def check_block(block, expected):
    errs = []
    if not isinstance(block, dict):
        return ["block missing"]
    for triad_name, keys in expected.items():
        t = block.get(triad_name)
        if not isinstance(t, dict):
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
    m = data.get("module", {})
    triads = m.get("triads")
    if not isinstance(triads, dict):
        return ["triads block missing"]
    errs = []
    errs += check_block(triads.get("structural_triads"), STRUCTURAL_KEYS)
    errs += check_block(triads.get("harmonic_triads"), HARMONIC_KEYS)
    errs += check_block(triads.get("coherence_triads"), COHERENCE_KEYS)
    return errs

def get_dependencies(data):
    m = data.get("module", {})
    deps = m.get("dependencies", [])
    if isinstance(deps, dict):
        deps = deps.get("modules", [])
    if not isinstance(deps, list):
        return []
    return [d for d in deps if isinstance(d, str)]

def detect_cycles(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
    visited = set()
    stack = set()
    cycles = []

    def dfs(n, path):
        if n in stack:
            idx = path.index(n)
            cycles.append(path[idx:])
            return
        if n in visited:
            return
        visited.add(n)
        stack.add(n)
        for nxt in graph.get(n, []):
            dfs(nxt, path + [nxt])
        stack.remove(n)

    for n in graph.keys():
        dfs(n, [n])

    uniq = []
    seen = set()
    for c in cycles:
        t = tuple(c)
        if t not in seen:
            seen.add(t)
            uniq.append(c)
    return uniq

def score_module(schema_errs, triad_errs, dep_missing, dep_cycles_for_module):
    c = len(schema_errs) + len(triad_errs) + len(dep_missing) + len(dep_cycles_for_module)
    if c == 0: return 0
    if c <= 2: return 1
    if c <= 4: return 2
    if c <= 7: return 3
    return 4

def color_for_score(score):
    return {
        0: "#2ecc71",  # pure
        1: "#f1c40f",  # low issues
        2: "#e67e22",  # moderate
        3: "#e74c3c",  # high
        4: "#2c3e50",  # critical
    }[score]

def build_svg(report):
    svg_path = os.path.join(ROOT, "spine", "consistency_map.svg")
    os.makedirs(os.path.dirname(svg_path), exist_ok=True)

    cell = 20
    pad = 5
    cols = 20
    rows = (len(report) + cols - 1) // cols
    width = cols * cell + pad * 2
    height = rows * cell + pad * 2

    rects = []
    for i, r in enumerate(report):
        row = i // cols
        col = i % cols
        x = pad + col * cell
        y = pad + row * cell
        color = color_for_score(r["score"])
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell-2}" height="{cell-2}" '
            f'fill="{color}" stroke="#333" stroke-width="0.5">'
            f'<title>{r["name"]} — consistency score {r["score"]}</title>'
            f'</rect>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>
{''.join(rects)}
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✔ Created {svg_path}")

def main():
    print("\n=== TriadicFrameworks Consistency‑Map SVG Visualizer ===\n")

    modules = find_modules()
    names = {os.path.basename(os.path.dirname(m)): m for m in modules}

    edges = []
    missing = []
    report = []

    # First pass: collect edges and basic errors
    per_module_schema = {}
    per_module_triads = {}
    per_module_missing = {}

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        data = load_json(path)
        schema_errs = check_schema(data)
        triad_errs = check_triads(data)
        deps = get_dependencies(data)

        per_module_schema[name] = schema_errs
        per_module_triads[name] = triad_errs
        per_module_missing[name] = []

        for d in deps:
            edges.append((name, d))
            if d not in names:
                missing.append((name, d))
                per_module_missing[name].append(d)

    cycles = detect_cycles(edges)

    # Map cycles to modules
    cycles_by_module = {}
    for c in cycles:
        for m in c:
            cycles_by_module.setdefault(m, []).append(c)

    # Build report with scores
    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        schema_errs = per_module_schema.get(name, [])
        triad_errs = per_module_triads.get(name, [])
        dep_missing = per_module_missing.get(name, [])
        dep_cycles_for_module = cycles_by_module.get(name, [])
        score = score_module(schema_errs, triad_errs, dep_missing, dep_cycles_for_module)
        report.append({"name": name, "score": score})

    build_svg(report)
    print("\n✨ Consistency‑map SVG visualization generated.\n")

if __name__ == "__main__":
    main()
