#!/usr/bin/env python
import sys
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]  # docs/MCP
PROTOCOL_DIR = BASE / "protocol"
SRC_DIR = BASE / "src"
ROOT_MODULE_REGISTRY = BASE / "module_registry.json"
EXAMPLE_REGISTRY = PROTOCOL_DIR / "examples.registry.json"
TOOLS_CATALOG = PROTOCOL_DIR / "tools.catalog.json"
SERVER_MANIFEST = PROTOCOL_DIR / "server.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def rpc_error(code: int, message: str, data=None):
    err = {"code": code, "message": message}
    if data is not None:
        err["data"] = data
    return err


def handle_initialize(params):
    return {
        "serverName": "TriadicFrameworks-MCP",
        "serverVersion": "0.1.0",
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "tools": True,
            "resources": True,
            "prompts": True
        }
    }


def handle_tools_list(params):
    catalog = load_json(TOOLS_CATALOG)
    return {"tools": catalog}


def handle_getCapabilities(params):
    manifest = load_json(SERVER_MANIFEST)
    return manifest


def _load_module_registry():
    return load_json(ROOT_MODULE_REGISTRY)


def handle_listModules(params):
    registry = _load_module_registry()
    layer = params.get("layer")
    modules = registry.get("modules", [])
    if layer:
        modules = [m for m in modules if m.get("layer") == layer]
    return {"modules": modules}


def handle_getModule(params):
    module_id = params.get("id")
    if not module_id:
        raise ValueError("id is required")
    registry = _load_module_registry()
    for m in registry.get("modules", []):
        if m.get("id") == module_id:
            return {"module": m}
    raise FileNotFoundError(f"Module {module_id} not found")


def handle_getOperator(params):
    operator_id = params.get("id")
    if not operator_id:
        raise ValueError("id is required")
    op_registry_path = BASE / "L3_Forces_Unseen" / "registry" / "operator_registry.json"
    registry = load_json(op_registry_path)
    operators = registry.get("operators", [])
    for op in operators:
        if op.get("id") == operator_id or op.get("name") == operator_id:
            return {"operator": op}
    raise FileNotFoundError(f"Operator {operator_id} not found")


def handle_searchOperators(params):
    term = params.get("query", "").lower()
    op_registry_path = BASE / "L3_Forces_Unseen" / "registry" / "operator_registry.json"
    registry = load_json(op_registry_path)
    operators = registry.get("operators", [])
    if term:
        operators = [
            op for op in operators
            if term in (op.get("name", "").lower() or "") or term in (op.get("definition", "").lower() or "")
        ]
    return {"results": operators}


def handle_traceLineage(params):
    module_id = params.get("moduleId")
    registry = _load_module_registry()
    for m in registry.get("modules", []):
        if m.get("id") == module_id:
            return {"lineage": m.get("lineage")}
    raise FileNotFoundError(f"Lineage for {module_id} not found")


def handle_diagnoseDrift(params):
    # Stub: returns a neutral drift diagnostic
    return {
        "drift": {
            "status": "unknown",
            "severity": "none",
            "notes": "Drift diagnostics not yet implemented."
        }
    }


def handle_mapRegime(params):
    module_id = params.get("moduleId")
    registry = _load_module_registry()
    for m in registry.get("modules", []):
        if m.get("id") == module_id:
            return {"regime": m.get("regime")}
    return {"regime": None}


def handle_resolveCoherence(params):
    module_id = params.get("moduleId")
    registry = _load_module_registry()
    for m in registry.get("modules", []):
        if m.get("id") == module_id:
            return {
                "coherent": m.get("coherent", False),
                "freezeTable": m.get("freezeTable")
            }
    return {"coherent": False}


def handle_renderSessionContext(params):
    session_id = params.get("sessionId")
    return {
        "sessionId": session_id,
        "context": {
            "modules": [],
            "examples": [],
            "notes": "Session context rendering not yet fully implemented."
        }
    }


def _load_example_registry():
    return load_json(EXAMPLE_REGISTRY)


def handle_listExamples(params):
    registry = _load_example_registry()
    examples = registry.get("examples", [])
    return {"examples": examples}


def handle_getExample(params):
    example_id = params.get("id")
    if not example_id:
        raise ValueError("id is required")
    registry = _load_example_registry()
    for row in registry.get("examples", []):
        if row.get("id") == example_id:
            path = BASE / row["path"]
            envelope = load_json(path)
            return {"example": envelope}
    raise FileNotFoundError(f"Example {example_id} not found")


def handle_searchExamples(params):
    module = params.get("module")
    layer = params.get("layer")
    kind = params.get("kind")
    registry = _load_example_registry()
    results = []
    for row in registry.get("examples", []):
        if module and row.get("module") != module:
            continue
        if layer and row.get("layer") != layer:
            continue
        if kind and row.get("kind") != kind:
            continue
        path = BASE / row["path"]
        envelope = load_json(path)
        results.append(envelope)
    return {"results": results}


def dispatch(method, params):
    if method == "initialize":
        return handle_initialize(params)
    if method == "tools/list":
        return handle_tools_list(params)
    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "getCapabilities":
            return handle_getCapabilities(args)
        if name == "listModules":
            return handle_listModules(args)
        if name == "getModule":
            return handle_getModule(args)
        if name == "getOperator":
            return handle_getOperator(args)
        if name == "searchOperators":
            return handle_searchOperators(args)
        if name == "traceLineage":
            return handle_traceLineage(args)
        if name == "diagnoseDrift":
            return handle_diagnoseDrift(args)
        if name == "mapRegime":
            return handle_mapRegime(args)
        if name == "resolveCoherence":
            return handle_resolveCoherence(args)
        if name == "renderSessionContext":
            return handle_renderSessionContext(args)
        if name == "listExamples":
            return handle_listExamples(args)
        if name == "getExample":
            return handle_getExample(args)
        if name == "searchExamples":
            return handle_searchExamples(args)

        raise ValueError(f"Unknown tool: {name}")

    raise ValueError(f"Unknown method: {method}")


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            params = req.get("params", {})
            req_id = req.get("id")

            try:
                result = dispatch(method, params)
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": result
                }
            except Exception as e:
                err = rpc_error(-32000, str(e))
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": err
                }

            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            # malformed request; no id to reply to safely
            continue


if __name__ == "__main__":
    main()
