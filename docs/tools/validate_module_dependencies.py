import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# ---------------------------------------------------------
# DISCOVERY
# ---------------------------------------------------------
def find_modules():
    modules = {}
    for root,dirs,files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED): continue
        if "module.json" in files:
            path = os.path.join(root,"module.json")
            name = os.path.basename(root)
            modules[name] = path
    return modules

# ---------------------------------------------------------
# LOAD + EXTRACT DEPENDENCIES
# ---------------------------------------------------------
def get_dependencies(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            data = json.load(f)
    except:
        return []

    m = data.get("module",{})
    deps = m.get("dependencies",[])
    if isinstance(deps,dict):
        # allow {"modules":[...]} style
        deps = deps.get("modules",[])
    if not isinstance(deps,list):
        return []
    return [d for d in deps if isinstance(d,str)]

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------
def validate_dependencies(modules):
    missing = []
    edges = []

    # build edges
    for name,path in modules.items():
        deps = get_dependencies(path)
        for d in deps:
            edges.append((name,d))
            if d not in modules:
                missing.append((name,d))

    return edges, missing

# simple cycle detection on name graph
def detect_cycles(edges):
    graph = {}
    for a,b in edges:
        graph.setdefault(a,[]).append(b)

    visited = set()
    stack = set()
    cycles = []

    def dfs(node, path):
        if node in stack:
            # cycle found
            idx = path.index(node)
            cycles.append(path[idx:])
            return
        if node in visited:
            return
        visited.add(node)
        stack.add(node)
        for nxt in graph.get(node,[]):
            dfs(nxt, path+[nxt])
        stack.remove(node)

    for n in graph.keys():
        dfs(n,[n])

    # dedupe cycles by sorted tuple
    seen = set()
    uniq = []
    for c in cycles:
        key = tuple(c)
        if key not in seen:
            seen.add(key)
            uniq.append(c)
    return uniq

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Cross‑Module Dependency Validator ===\n")

    modules = find_modules()
    edges, missing = validate_dependencies(modules)
    cycles = detect_cycles(edges)

    # Missing targets
    if missing:
        print("❌ Missing dependency targets:")
        for src,dst in missing:
            print(f"   - {src} → {dst} (not found)")
    else:
        print("✔ No missing dependency targets.")

    # Cycles
    if cycles:
        print("\n⚠ Cyclic dependencies detected:")
        for c in cycles:
            chain = " → ".join(c + [c[0]])
            print(f"   - {chain}")
    else:
        print("\n✔ No cyclic dependencies detected.")

    print("\n=== Summary ===")
    print(f"Modules scanned: {len(modules)}")
    print(f"Dependency edges: {len(edges)}")
    print(f"Missing targets: {len(missing)}")
    print(f"Cycles: {len(cycles)}\n")

    if not missing and not cycles:
        print("✨ Cross‑module dependencies are consistent and acyclic.")
    else:
        print("⚠ Review missing targets and cycles for canon consistency.")

if __name__=="__main__":
    main()
