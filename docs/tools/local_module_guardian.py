import os
import json
import sys
from jsonschema import validate, ValidationError

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

# Canonical schema
MODULE_SCHEMA = {
    "type": "object",
    "properties": {
        "module": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "summary": {"type": "string"},
                "category": {"type": "string"},

                "canon_ref": {
                    "type": "string",
                    "enum": ["/docs/spine/spine.json"]
                },

                "inherit": {
                    "type": "object",
                    "properties": {
                        "canon": {"type": "boolean"},
                        "session_context": {"type": "boolean"},
                        "triad_alias_resolution": {"type": "boolean"}
                    },
                    "required": [
                        "canon",
                        "session_context",
                        "triad_alias_resolution"
                    ]
                },

                "rtt": {
                    "type": "object",
                    "properties": {
                        "layer": {"type": "integer"},
                        "source": {"type": "string"}
                    },
                    "required": ["layer", "source"]
                },

                "ai": {
                    "type": "object",
                    "properties": {
                        "initialization": {
                            "type": "object",
                            "properties": {
                                "load_spine_first": {"type": "boolean"},
                                "load_canon_first": {"type": "boolean"},
                                "apply_session_context": {"type": "boolean"},
                                "triad_validation": {"type": "boolean"}
                            },
                            "required": [
                                "load_spine_first",
                                "load_canon_first",
                                "apply_session_context",
                                "triad_validation"
                            ]
                        }
                    },
                    "required": ["initialization"]
                }
            },
            "required": [
                "name",
                "summary",
                "category",
                "canon_ref",
                "inherit",
                "rtt",
                "ai"
            ]
        }
    },
    "required": ["module"]
}

# Drift scoring rules
def score_drift(errors):
    count = len(errors)
    if count == 0: return 0
    if count <= 2: return 1
    if count <= 4: return 2
    if count <= 7: return 3
    return 4

def drift_label(score):
    return {
        0: "Pure",
        1: "Low Drift",
        2: "Moderate Drift",
        3: "High Drift",
        4: "Critical Drift"
    }[score]

# Validate schema
def validate_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=MODULE_SCHEMA)
        return []
    except ValidationError as e:
        return [str(e)]

# Validate drift
def validate_drift(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    module = data.get("module", {})
    errors = []

    # Canon ref
    if module.get("canon_ref") != "/docs/spine/spine.json":
        errors.append("canon_ref mismatch")

    # Inherit
    inherit = module.get("inherit", {})
    for key in ["canon", "session_context", "triad_alias_resolution"]:
        if inherit.get(key) != True:
            errors.append(f"inherit.{key} mismatch")

    # RTT
    rtt = module.get("rtt", {})
    if rtt.get("layer") != 1:
        errors.append("rtt.layer mismatch")
    if rtt.get("source") != "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html":
        errors.append("rtt.source mismatch")

    # AI init
    ai = module.get("ai", {}).get("initialization", {})
    for key in ["load_spine_first", "load_canon_first", "apply_session_context", "triad_validation"]:
        if ai.get(key) != True:
            errors.append(f"ai.initialization.{key} mismatch")

    return errors

# Discover modules
def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(os.path.join(root, "module.json"))
    return modules

# Main
def main():
    modules = find_modules()
    fatal = False

    for module_path in modules:
        name = os.path.basename(os.path.dirname(module_path))

        schema_errors = validate_schema(module_path)
        drift_errors = validate_drift(module_path)
        drift_score = score_drift(drift_errors)

        if schema_errors or drift_score > 0:
            fatal = True
            print(f"❌ {name} — BLOCKED")
            for e in schema_errors:
                print(f"   SCHEMA: {e}")
            for e in drift_errors:
                print(f"   DRIFT: {e}")
            print(f"   Drift Severity: {drift_score} ({drift_label(drift_score)})\n")
        else:
            print(f"✔ {name} — OK")

    if fatal:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
