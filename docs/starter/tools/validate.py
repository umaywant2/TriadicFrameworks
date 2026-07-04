import json
import os
import sys
from jsonschema import validate, ValidationError

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def safe_resolve_path(base_dir, user_path):
    candidate = os.path.realpath(os.path.join(base_dir, user_path))
    if os.path.commonpath([base_dir, candidate]) != base_dir:
        raise ValueError(f"Path escapes allowed root: {user_path}")
    return candidate

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate.py path/to/module.json")
        return

    script_dir = os.path.dirname(os.path.realpath(__file__))
    project_root = os.path.realpath(os.path.join(script_dir, ".."))

    try:
        module_path = safe_resolve_path(project_root, sys.argv[1])
        schema_path = safe_resolve_path(project_root, "schema/module.schema.json")

        module_data = load_json(module_path)
        schema_data = load_json(schema_path)

        validate(instance=module_data, schema=schema_data)
        print("✔ module.json is valid and canon‑aligned.")

    except ValueError as e:
        print("✘ Invalid path:", e)
    except FileNotFoundError:
        print("✘ File not found. Check your paths.")
    except ValidationError as e:
        print("✘ Validation error:")
        print(e.message)
    except Exception as e:
        print("✘ Unexpected error:", e)

if __name__ == "__main__":
    main()

