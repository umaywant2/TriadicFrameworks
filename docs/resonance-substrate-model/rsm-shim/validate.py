import json
import jsonschema
import sys
from pathlib import Path

SCHEMA_DIR = Path("../schemas")
CONFIG_DIR = Path(".")

def resolve_safe_path(base_dir, user_path):
    base = Path(base_dir).resolve()
    user_path_obj = Path(user_path)
    if user_path_obj.is_absolute():
        raise ValueError(f"Config path escapes allowed directory: {user_path}")

    candidate = (base / user_path_obj).resolve()
    try:
        candidate.relative_to(base)
    except ValueError:
        raise ValueError(f"Config path escapes allowed directory: {user_path}")
    return candidate

def sanitize_config_filename(config_path):
    config_name = Path(config_path).name
    if config_name != config_path:
        raise ValueError(f"Config path must be a file in the current directory: {config_path}")
    if config_name in ("", ".", ".."):
        raise ValueError(f"Invalid config filename: {config_path}")
    if Path(config_name).suffix.lower() != ".json":
        raise ValueError(f"Config file must be a .json file: {config_path}")
    return config_name

def load_schema(name):
    safe_schema_path = resolve_safe_path(SCHEMA_DIR, name)
    with open(safe_schema_path, "r") as f:
        return json.load(f)

def validate_config(config_path):
    safe_config_name = sanitize_config_filename(config_path)
    with open(safe_config_name, "r") as config_file:
        config = json.load(config_file)
    schema = load_schema("simulation.schema.json")
    jsonschema.validate(config, schema)
    print("Config is valid.")

if __name__ == "__main__":
    validate_config(sys.argv[1])

