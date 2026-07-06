import yaml
import csv
from pathlib import Path

from triphasic import generate_triphasic_signals

def run_simulation(manifest_path):
    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    label = manifest['label']
    forces = manifest['forces']
    fluids = manifest['fluids']
    frequency = manifest['frequency']

    signals = generate_triphasic_signals(forces, fluids, frequency, cycles=3500)

    reports_root = Path("docs/reports").resolve()
    output_path = (reports_root / f"{label}_cycles.csv").resolve()
    try:
        output_path.relative_to(reports_root)
    except ValueError:
        raise ValueError("Invalid manifest label: output path escapes docs/reports")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=signals[0].keys())
        writer.writeheader()
        writer.writerows(signals)

    print(f"✅ Simulation complete: {output_path}")

# Example usage:
# run_simulation("docs/manifests/S1.yaml")

if __name__ == "__main__":
    import sys
    run_simulation(sys.argv[1])
