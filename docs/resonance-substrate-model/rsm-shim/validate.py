import json
import jsonschema
import sys
from pathlib import Path

SCHEMA_DIR = Path("../schemas")
CONFIG_DIR = Path(".")

def resolve_safe_path(base_dir, user_path):
    base = Path(base_dir).resolve()
    user_path_obj = Path(user_path)
    if user_path_obj.is_absolute() or ".." in user_path_obj.parts:
        raise ValueError(f"Config path escapes allowed directory: {user_path}")
    candidate = (base / user_path_obj).resolve()
    if base != candidate and base not in candidate.parents:
        raise ValueError(f"Config path escapes allowed directory: {user_path}")
    return candidate

def load_schema(name):
    safe_schema_path = resolve_safe_path(SCHEMA_DIR, name)
    with open(safe_schema_path, "r") as f:
        return json.load(f)

def validate_config(config_path):
    safe_config_path = resolve_safe_path(CONFIG_DIR, config_path)
    with open(safe_config_path, "r") as config_file:
        config = json.load(config_file)
    schema = load_schema("simulation.schema.json")
    jsonschema.validate(config, schema)
    print("Config is valid.")

if __name__ == "__main__":
    validate_config(sys.argv[1])

