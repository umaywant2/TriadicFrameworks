import json
import jsonschema
import sys
from pathlib import Path

SCHEMA_DIR = Path("../schemas")

def load_schema(name):
    with open(SCHEMA_DIR / name, "r") as f:
        return json.load(f)

def validate_config(config_path):
    config = json.load(open(config_path))
    schema = load_schema("simulation.schema.json")
    jsonschema.validate(config, schema)
    print("Config is valid.")

if __name__ == "__main__":
    validate_config(sys.argv[1])

