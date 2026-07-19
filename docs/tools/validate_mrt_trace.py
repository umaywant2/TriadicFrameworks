import json
import sys
from jsonschema import validate, ValidationError

def load(path):
    with open(path, "r") as f:
        return json.load(f)

def main(trace_path):
    trace = load(trace_path)

    schemas = {
        "operators": load("docs/schemas/rtt-micro-core/v1/mrt_operators.schema.json"),
        "envelopes": load("docs/schemas/rtt-micro-core/v1/mrt_envelopes.schema.json"),
        "transforms": load("docs/schemas/rtt-micro-core/v1/mrt_transforms.schema.json")
    }

    try:
        for step in trace["steps"]:
            validate(step.get("omega_mu", {}), schemas["operators"])
            validate(step.get("f_mu", {}), schemas["operators"])
            validate(step.get("s_mu", {}), schemas["operators"])
            validate(step.get("delta_mu", {}), schemas["operators"])

        print("MRT trace is VALID.")
        return 0

    except ValidationError as e:
        print("MRT trace is INVALID:")
        print(e)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
