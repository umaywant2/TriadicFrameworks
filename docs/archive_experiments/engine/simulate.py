import yaml
import csv
import re
from pathlib import Path

from triphasic import generate_triphasic_signals

def _sanitize_label(label):
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", str(label).strip())
    safe = safe.strip("._-")
    if not safe:
        raise ValueError("Invalid manifest label: label must contain at least one safe character")
    return safe

def _validate_output_filename(filename):
    if not filename:
        raise ValueError("Invalid output filename: empty filename is not allowed")
    filename_path = Path(filename)
    if filename_path.is_absolute() or filename_path.name != filename:
        raise ValueError("Invalid output filename: path separators are not allowed")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", filename):
        raise ValueError("Invalid output filename: contains unsafe characters")
    return filename

def run_simulation(manifest_path):
    with open(manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    label = manifest['label']
    safe_label = _sanitize_label(label)
    forces = manifest['forces']
    fluids = manifest['fluids']
    frequency = manifest['frequency']

    signals = generate_triphasic_signals(forces, fluids, frequency, cycles=3500)

    reports_root = Path("docs/reports").resolve()
    output_filename = _validate_output_filename(f"{safe_label}_cycles.csv")
    output_path = (reports_root / output_filename).resolve()
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
