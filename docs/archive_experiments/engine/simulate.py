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

def _safe_join_under_root(root, filename):
    safe_name = _validate_output_filename(filename)
    root_resolved = Path(root).resolve()
    candidate = (root_resolved / safe_name).resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError:
        raise ValueError("Invalid output filename: output path escapes docs/reports")
    return candidate

def _safe_manifest_path(manifest_path):
    if not manifest_path:
        raise ValueError("Invalid manifest path: empty path is not allowed")

    user_path = Path(str(manifest_path))
    if user_path.is_absolute():
        raise ValueError("Invalid manifest path: absolute paths are not allowed")
    if ".." in user_path.parts:
        raise ValueError("Invalid manifest path: parent directory traversal is not allowed")

    manifests_root = Path("docs/manifests").resolve()
    candidate = (manifests_root / user_path).resolve()
    try:
        candidate.relative_to(manifests_root)
    except ValueError:
        raise ValueError("Invalid manifest path: path escapes docs/manifests")
    if candidate.suffix.lower() not in {".yaml", ".yml"}:
        raise ValueError("Invalid manifest path: expected a .yaml or .yml file")
    if not candidate.is_file():
        raise ValueError("Invalid manifest path: file does not exist")
    return candidate

def run_simulation(manifest_path):
    safe_manifest_path = _safe_manifest_path(manifest_path)
    with open(safe_manifest_path, 'r') as f:
        manifest = yaml.safe_load(f)

    label = manifest['label']
    safe_label = _sanitize_label(label)
    forces = manifest['forces']
    fluids = manifest['fluids']
    frequency = manifest['frequency']

    signals = generate_triphasic_signals(forces, fluids, frequency, cycles=3500)

    reports_root = Path("docs/reports").resolve()
    output_filename = "simulation_cycles.csv"
    output_path = _safe_join_under_root(reports_root, output_filename)

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
