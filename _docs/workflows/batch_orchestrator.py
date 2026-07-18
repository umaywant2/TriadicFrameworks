"""
Scroll Batch Orchestrator
Part of the TriadicFrameworks Workflows subsystem.

Runs a batch of scrolls (.fff files or in‑memory scroll objects)
through the Python scroll pipeline and aggregates results into
a structured batch report.

This engine is substrate‑agnostic and contains no external service
dependencies. It is the batch counterpart to scroll_pipeline.py.
"""

from pathlib import Path
from datetime import datetime
import yaml

from scroll_pipeline import run_scroll


def is_path(x):
    return isinstance(x, str) and x.endswith(".fff")


def load_scroll(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def process_scroll(scroll_obj):
    return run_scroll(scroll_obj)


def batch_run(items, output_dir=None):
    """
    items: list of file paths OR in‑memory scroll objects.
    output_dir: optional directory for writing a timestamped YAML report.
    """
    batch_results = []

    for item in items:
        scroll = load_scroll(item) if is_path(item) else item
        output = process_scroll(scroll)

        batch_results.append({
            "input": item,
            "output": output
        })

    report = {
        "timestamp": datetime.now().isoformat(),
        "count": len(batch_results),
        "results": batch_results
    }

    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        outfile = Path(output_dir) / f"batch_{ts}.yml"
        with open(outfile, "w", encoding="utf-8") as f:
            yaml.dump(report, f, sort_keys=False)

    return report
