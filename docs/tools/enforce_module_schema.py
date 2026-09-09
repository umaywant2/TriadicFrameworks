import os
import json
from jsonschema import validate, ValidationError

ROOT = "docs"

EXCLUDED_DIRS = {
    "spine",
    "_template",
    "assets",
    "images",
    "tools"
}

# ---------------------------------------------------------
# CANONICAL MODULE.JSON SCHEMA
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# MODULE DISCOVERY
# ---------------------------------------------------------
def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(root)
    return modules

# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------
def validate_schema(path):
    with open(os.path.join(path, "module.json"), "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        validate(instance=data, schema=MODULE_SCHEMA)
        return []
    except ValidationError as e:
        return [str(e)]

# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Module.json Schema Enforcer ===\n")

    modules = find_modules()
    total = len(modules)
    failures = 0

    for module_path in modules:
        module_name = os.path.basename(module_path)
        errors = validate_schema(module_path)

        if errors:
            failures += 1
            print(f"❌ {module_name} — SCHEMA FAIL")
            for err in errors:
                print(f"   - {err}")
        else:
            print(f"✔ {module_name} — SCHEMA PASS")

    print("\n=== Summary ===")
    print(f"Total modules checked: {total}")
    print(f"Schema‑valid: {total - failures}")
    print(f"Schema‑invalid: {failures}")

    if failures == 0:
        print("\n✨ All modules conform to the canonical module.json schema.")
    else:
        print("\n⚠ Schema violations detected. Fix required for full canon purity.")

if __name__ == "__main__":
    main()
