"""
Test Harness for Scroll Batch Orchestrator
TriadicFrameworks • Workflows Subsystem

Covers:
- file‑path inputs
- in‑memory scroll objects
- mixed input lists
- deterministic batch report structure

🧭 Optional extension: “Golden File” test
Ensures long‑term stability of the batch report schema across refactors.

import yaml
from pathlib import Path

def test_report_schema_stability():
    s = sample_scroll_obj()
    report = batch_run([s])

    # load a golden schema from tests/golden/batch_schema.yml
    schema_path = Path(__file__).parent / "golden" / "batch_schema.yml"
    expected = yaml.safe_load(schema_path.read_text())

    assert set(report.keys()) == set(expected.keys())
"""


import tempfile
from pathlib import Path
from batch_orchestrator import batch_run


# --- Helpers ---------------------------------------------------------------

def make_temp_scroll(content: str) -> Path:
    """Create a temporary .fff scroll file with given content."""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".fff", mode="w", encoding="utf-8")
    tmp.write(content)
    tmp.close()
    return Path(tmp.name)


def sample_scroll_obj():
    """Return an in‑memory scroll object."""
    return """
    # Sample Scroll
    emitter: test
    frequency: 144
    """


# --- Tests ----------------------------------------------------------------

def test_paths_only():
    s1 = make_temp_scroll("scroll A")
    s2 = make_temp_scroll("scroll B")

    report = batch_run([s1, s2])

    assert report["count"] == 2
    assert len(report["results"]) == 2
    assert "output" in report["results"][0]


def test_objects_only():
    s1 = sample_scroll_obj()
    s2 = sample_scroll_obj()

    report = batch_run([s1, s2])

    assert report["count"] == 2
    assert all("output" in r for r in report["results"])


def test_mixed_inputs():
    s_path = make_temp_scroll("scroll from file")
    s_obj = sample_scroll_obj()

    report = batch_run([s_path, s_obj])

    assert report["count"] == 2
    assert any(isinstance(r["input"], str) for r in report["results"])
    assert any(not isinstance(r["input"], str) for r in report["results"])


def test_output_dir(tmp_path):
    s1 = make_temp_scroll("scroll X")

    report = batch_run([s1], output_dir=tmp_path)

    # ensure a YAML file was written
    files = list(tmp_path.glob("batch_*.yml"))
    assert len(files) == 1
    assert files[0].is_file()
