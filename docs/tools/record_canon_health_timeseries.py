import os
import json
import datetime

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}
SPINE = os.path.join(ROOT, "spine")
TIMESERIES_FILE = os.path.join(SPINE, "canon_health_timeseries.json")

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

def load_timeseries():
    if not os.path.isfile(TIMESERIES_FILE):
        return []
    try:
        with open(TIMESERIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_timeseries(ts):
    os.makedirs(SPINE, exist_ok=True)
    with open(TIMESERIES_FILE, "w", encoding="utf-8") as f:
        json.dump(ts, f, indent=2)

def main():
    print("\n=== TriadicFrameworks Canon‑Health Time‑Series Recorder ===\n")

    modules = find_modules()
    names = {os.path.basename(os.path.dirname(m)): m for m in modules}

    edges = []
    missing = []

    per_schema = {}
    per_triads = {}
    per_missing = {}

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        data = load_json(path)
        schema_errs = check_schema(data)
        triad_errs = check_triads(data)
        deps = get_dependencies(data)

        per_schema[name] = schema_errs
        per_triads[name] = triad_errs
        per_missing[name] = []

        for d in deps:
            edges.append((name, d))
            if d not in names:
                missing.append((name, d))
                per_missing[name].append(d)

    cycles = detect_cycles(edges)
    cycles_by_module = {}
    for c in cycles:
        for m in c:
            cycles_by_module.setdefault(m, []).append(c)

    # Aggregate health metrics
    total_modules = len(modules)
    schema_ok = sum(1 for n in per_schema if len(per_schema[n]) == 0)
    triads_ok = sum(1 for n in per_triads if len(per_triads[n]) == 0)
    deps_ok = sum(1 for n in per_missing if len(per_missing[n]) == 0 and len(cycles_by_module.get(n, [])) == 0)

    scores = []
    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        s_errs = per_schema.get(name, [])
        t_errs = per_triads.get(name, [])
        d_missing = per_missing.get(name, [])
        d_cycles = cycles_by_module.get(name, [])
        score = score_module(s_errs, t_errs, d_missing, d_cycles)
        scores.append(score)

    avg_score = sum(scores) / total_modules if total_modules else 0.0
    max_score = max(scores) if scores else 0

    snapshot = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "totals": {
            "modules": total_modules,
            "schema_ok": schema_ok,
            "triads_ok": triads_ok,
            "dependencies_ok": deps_ok,
        },
        "scores": {
            "average_consistency_score": avg_score,
            "max_consistency_score": max_score,
        },
        "issues": {
            "missing_dependencies": missing,
            "cycles": cycles,
        }
    }

    ts = load_timeseries()
    ts.append(snapshot)
    save_timeseries(ts)

    print(f"✔ Recorded snapshot at {snapshot['timestamp']}")
    print(f"   Modules: {total_modules}")
    print(f"   Schema OK: {schema_ok}")
    print(f"   Triads OK: {triads_ok}")
    print(f"   Dependencies OK: {deps_ok}")
    print(f"   Avg score: {avg_score:.2f}, Max score: {max_score}")
    print(f"\n✔ Updated {TIMESERIES_FILE}")
    print("\n✨ Canon‑health time‑series point captured.\n")

if __name__ == "__main__":
    main()
