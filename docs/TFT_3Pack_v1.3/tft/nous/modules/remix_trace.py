import yaml
import json
from datetime import datetime

def load_yaml_trace(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def load_json_log(path):
    with open(path, 'r') as file:
        return json.load(file)

def parse_remix_events(trace):
    for entry in trace:
        print(f"[{entry['timestamp']}] {entry['declared_by']} → {entry['mutation_type']} mutation on {entry['coin_id']} ({entry['corridor']})")

def validate_lineage(entry):
    required_keys = ['coin_id', 'origin', 'mutation_type', 'declared_by', 'corridor', 'glyph', 'timestamp']
    return all(key in entry for key in required_keys)

if __name__ == "__main__":
    yaml_trace = load_yaml_trace("../outputs/remix_trace.yaml")
    json_log = load_json_log("../outputs/remix_mutation_log.json")

    print("🧬 Remix Trace — YAML")
    parse_remix_events(yaml_trace)

    print("\n🧬 Remix Log — JSON")
    for entry in json_log:
        if validate_lineage(entry):
            print(f"[{entry['timestamp']}] {entry['agent']} → {entry['mutation_type']} mutation on {entry['coin_id']}")

