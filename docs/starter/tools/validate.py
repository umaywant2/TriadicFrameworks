import json
import sys
from jsonschema import validate, ValidationError

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate.py path/to/module.json")
        return

    module_path = sys.argv[1]
    schema_path = "../schema/module.schema.json"

    try:
        module_data = load_json(module_path)
        schema_data = load_json(schema_path)

        validate(instance=module_data, schema=schema_data)
        print("✔ module.json is valid and canon‑aligned.")

    except FileNotFoundError:
        print("✘ File not found. Check your paths.")
    except ValidationError as e:
        print("✘ Validation error:")
        print(e.message)
    except Exception as e:
        print("✘ Unexpected error:", e)

if __name__ == "__main__":
    main()

