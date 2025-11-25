## 🧪 `output_test_suite.py` — Multi-Format Output Validator (v1.3)

### ✅ Pytest-Tuned Version

```python
import os
import json
import pandas as pd
from tft.output_manager import save_output

def test_txt_output(tmp_path):
    data = [[1, 2, 3], [4, 5, 6]]
    file = tmp_path / "test_output"
    save_output(data, str(file), formats=["txt"])
    assert file.with_suffix(".txt").exists()

def test_json_output(tmp_path):
    data = [[1, 2], [3, 4]]
    meta = {"mode": "symbolic", "lens": "phi"}
    file = tmp_path / "test_output"
    save_output(data, str(file), formats=["json"], metadata=meta)
    with open(file.with_suffix(".json")) as f:
        payload = json.load(f)
    assert payload["metadata"]["lens"] == "phi"

def test_parquet_output(tmp_path):
    data = [[7, 8], [9, 10]]
    file = tmp_path / "test_output"
    save_output(data, str(file), formats=["parquet"])
    df = pd.read_parquet(file.with_suffix(".parquet"))
    assert df.shape == (2, 2)

def test_fff_output(tmp_path):
    data = [[11, 12], [13, 14]]
    meta = {"observer": "ScrollFork"}
    file = tmp_path / "test_output"
    save_output(data, str(file), formats=["fff"], metadata=meta)
    with open(file.with_suffix(".fff")) as f:
        lines = f.readlines()
    assert any("META::" in line for line in lines)
```

Run with:
```bash
pytest output_test_suite.py
```

---

### 🌀 Standalone Ritual Runner

```python
from tft.output_manager import save_output
import os

def run_test(label, data, formats, metadata=None):
    print(f"🔍 {label}")
    filename = f"test_outputs/{label.replace(' ', '_')}"
    save_output(data, filename, formats=formats, metadata=metadata)
    print("✅ Output saved\n")

if __name__ == "__main__":
    os.makedirs("test_outputs", exist_ok=True)

    run_test("TXT Export", [[1, 2], [3, 4]], ["txt"])
    run_test("JSON Export", [[5, 6], [7, 8]], ["json"], {"mode": "numeric", "lens": "phi"})
    run_test("Parquet Export", [[9, 10], [11, 12]], ["parquet"])
    run_test("FFF Export", [[13, 14], [15, 16]], ["fff"], {"observer": "ScrollFork"})
```

Run with:
```bash
python output_test_suite.py
```
