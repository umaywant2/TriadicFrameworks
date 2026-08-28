#!/usr/bin/env python3
import sys
import json
import traceback

# ------------------------------------------------------------
# Load protocol catalogs
# ------------------------------------------------------------

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

TOOLS = load_json("docs/MCP/protocol/tools.catalog.json")["tools"]
RESOURCES = load_json("docs/MCP/protocol/resources.catalog.json")["resources"]
PROMPTS = load_json("docs/MCP/protocol/prompts.catalog.json")["prompts"]
EXAMPLES = load_json("docs/MCP/protocol/examples.registry.json")["examples"]

# ------------------------------------------------------------
# JSON-RPC helpers
# ------------------------------------------------------------

def rpc_reply(id, result=None, error=None):
    return json.dumps({
        "jsonrpc": "2.0",
        "id": id,
        "result": result,
        "error": error
    })

def rpc_error(id, message):
    return rpc_reply(id, error={"code": -1, "message": message})

# ------------------------------------------------------------
# Tool implementations (stubs)
# ------------------------------------------------------------

def getCapabilities(params):
    return {
        "version": "0.1.0",
        "tools": [t["name"] for t in TOOLS],
        "resources": [r["name"] for r in RESOURCES]
    }

def listModules(params):
    # In v0: read module_registry.json
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/module_registry.json")
    layer = params.get("layer")
    modules = registry["modules"]

    if layer:
        modules = [m for m in modules if m["layer"] == layer]

    return {"modules": modules}

def getModule(params):
    module_id = params["id"]
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/module_registry.json")

    for m in registry["modules"]:
        if m["id"] == module_id:
            return m

    return rpc_error(None, f"Module not found: {module_id}")

def getOperator(params):
    operator = params["operator"]
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/operator_registry.json")

    if operator in registry:
        return registry[operator]

    return rpc_error(None, f"Operator not found: {operator}")

def searchOperators(params):
    query = params["query"].lower()
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/operator_registry.json")

    results = []
    for name, meta in registry.items():
        if query in name.lower() or query in meta.get("definition", "").lower():
            results.append({
                "operator": name,
                "definition": meta.get("definition", ""),
                "layer": meta.get("layer", "")
            })

    return {"results": results}

def traceLineage(params):
    module_id = params["id"]
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/module_registry.json")

    for m in registry["modules"]:
        if m["id"] == module_id:
            return {"lineage": m.get("lineage", [])}

    return rpc_error(None, f"Module not found: {module_id}")

def diagnoseDrift(params):
    # Minimal stub — real math comes later
    phase = params.get("phaseHistory", [])
    drift_index = len(phase) * 0.1
    instability = drift_index * 0.5

    return {
        "driftIndex": drift_index,
        "instability": instability,
        "notes": "Stub implementation — replace with real drift math."
    }

def mapRegime(params):
    module_id = params["id"]
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/module_registry.json")

    for m in registry["modules"]:
        if m["id"] == module_id:
            return {"regime": m.get("regime", "unknown")}

    return rpc_error(None, f"Module not found: {module_id}")

def resolveCoherence(params):
    # Minimal stub — real coherence checks come later
    return {
        "coherent": True,
        "issues": []
    }

def renderSessionContext(params):
    module_id = params["id"]
    registry = load_json("docs/MCP/L3_Forces_Unseen/registry/module_registry.json")

    for m in registry["modules"]:
        if m["id"] == module_id:
            return {"context": m.get("sessionContext", {})}

    return rpc_error(None, f"Module not found: {module_id}")

# ------------------------------------------------------------
# Example tools
# ------------------------------------------------------------

def listExamples(params):
    module = params.get("module")
    kind = params.get("kind")

    results = EXAMPLES

    if module:
        results = [e for e in results if e["module"] == module]

    if kind:
        results = [e for e in results if kind in e["kind"]]

    return {"examples": results}

def getExample(params):
    example_id = params["id"]

    for e in EXAMPLES:
        if e["id"] == example_id:
            path = e["path"]
            return load_json(path)

    return rpc_error(None, f"Example not found: {example_id}")

def searchExamples(params):
    query = params["query"].lower()
    results = []

    for e in EXAMPLES:
        if query in e["id"].lower() or query in e["module"].lower():
            results.append(e)

    return {"results": results}

# ------------------------------------------------------------
# Tool dispatch table
# ------------------------------------------------------------

TOOL_IMPL = {
    "getCapabilities": getCapabilities,
    "listModules": listModules,
    "getModule": getModule,
    "getOperator": getOperator,
    "searchOperators": searchOperators,
    "traceLineage": traceLineage,
    "diagnoseDrift": diagnoseDrift,
    "mapRegime": mapRegime,
    "resolveCoherence": resolveCoherence,
    "renderSessionContext": renderSessionContext,
    "listExamples": listExamples,
    "getExample": getExample,
    "searchExamples": searchExamples
}

# ------------------------------------------------------------
# Main JSON-RPC loop
# ------------------------------------------------------------

def main():
    for line in sys.stdin:
        try:
            req = json.loads(line)
            method = req.get("method")
            id = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                result = {"tools": [t["name"] for t in TOOLS]}
                print(rpc_reply(id, result))
                continue

            if method == "resources/list":
                result = {"resources": [r["name"] for r in RESOURCES]}
                print(rpc_reply(id, result))
                continue

            if method == "prompts/list":
                result = {"prompts": [p["name"] for p in PROMPTS]}
                print(rpc_reply(id, result))
                continue

            if method == "tools/call":
                tool_name = params.get("name")
                tool_params = params.get("arguments", {})

                if tool_name not in TOOL_IMPL:
                    print(rpc_error(id, f"Unknown tool: {tool_name}"))
                    continue

                result = TOOL_IMPL[tool_name](tool_params)
                print(rpc_reply(id, result))
                continue

            print(rpc_error(id, f"Unknown method: {method}"))

        except Exception as e:
            traceback.print_exc()
            print(rpc_error(None, f"Server error: {str(e)}"))

if __name__ == "__main__":
    main()

