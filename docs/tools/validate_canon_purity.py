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
# DRIFT SCORING
# ---------------------------------------------------------
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

def drift_color(score):
    return {
        0: "🟩",
        1: "🟨",
        2: "🟧",
        3: "🟥",
        4: "⬛"
    }[score]

# ---------------------------------------------------------
# MODULE DISCOVERY
# ---------------------------------------------------------
def find_modules():
    modules = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED_DIRS):
            continue
        if "module.json" in files:
            modules.append(os.path.join(root, "module.json"))
    return modules

# ---------------------------------------------------------
# VALIDATION HELPERS
# ---------------------------------------------------------
def validate_schema(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=MODULE_SCHEMA)
        return []
    except ValidationError as e:
        return [str(e)]

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

# ---------------------------------------------------------
# MAIN PURITY VALIDATOR
# ---------------------------------------------------------
def main():
    print("\n=== TriadicFrameworks Canon Purity Validator ===\n")

    modules = find_modules()
    total = len(modules)

    purity_report = []
    failures = 0

    for module_path in modules:
        name = os.path.basename(os.path.dirname(module_path))

        schema_errors = validate_schema(module_path)
        drift_errors = validate_drift(module_path)
        drift_score = score_drift(drift_errors)

        purity_report.append((name, schema_errors, drift_errors, drift_score))

        if schema_errors or drift_score > 0:
            failures += 1

    # Print detailed report
    for name, schema_errors, drift_errors, drift_score in purity_report:
        if schema_errors or drift_score > 0:
            print(f"❌ {name} — FAIL — {drift_color(drift_score)} {drift_label(drift_score)}")
            for e in schema_errors:
                print(f"   SCHEMA: {e}")
            for e in drift_errors:
                print(f"   DRIFT: {e}")
            print()
        else:
            print(f"✔ {name} — PASS — 🟩 Pure")

    # Summary
    print("\n=== Summary ===")
    print(f"Total modules checked: {total}")
    print(f"Pure modules: {total - failures}")
    print(f"Impure modules: {failures}")

    if failures == 0:
        print("\n✨ Canon purity is perfect across the entire framework.")
    else:
        print("\n⚠ Canon purity violations detected. Review impure modules above.")

if __name__ == "__main__":
    main()
