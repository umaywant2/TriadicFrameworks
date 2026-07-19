## 🧪 `cli_test_suite.py` — Dual-Mode Validator (v1.3)

### ✅ Pytest-Tuned Version

import subprocess

def test_nous_symbolic_phi():
    result = subprocess.run(["python", "tft/cli.py", "nous", "-validate", "glyph_A", "-mode", "symbolic", "--basetype", "phi"], capture_output=True, text=True)
    assert "Validator triggered" in result.stdout

def test_entft_decimal_encrypt():
    result = subprocess.run(["python", "tft/cli.py", "entft", "-i", "input.txt", "-o", "output.enc", "-k", "key123", "--basetype", "decimal"], capture_output=True, text=True)
    assert "Encryption complete" in result.stdout

def test_tops_negabinary_simulate():
    result = subprocess.run(["python", "tft/cli.py", "tops", "-map", "corridor6.9", "-ops", "simulate", "--basetype", "negabinary"], capture_output=True, text=True)
    assert "Grid simulation complete" in result.stdout

# Run with:
# ```bash
# pytest cli_test_suite.py
# ```

### 🌀 Standalone Ritual Runner

import subprocess

def run_test(label, command):
    print(f"🔍 {label}")
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print("✅ Passed\n" if result.returncode == 0 else "❌ Failed\n")

if __name__ == "__main__":
    run_test("Nous Validator (phi)", ["python", "tft/cli.py", "nous", "-validate", "glyph_A", "-mode", "symbolic", "--basetype", "phi"])
    run_test("Entft Encryptor (decimal)", ["python", "tft/cli.py", "entft", "-i", "input.txt", "-o", "output.enc", "-k", "key123", "--basetype", "decimal"])
    run_test("Tops GridSim (negabinary)", ["python", "tft/cli.py", "tops", "-map", "corridor6.9", "-ops", "simulate", "--basetype", "negabinary"])

# Run with:
# ```bash
# python cli_test_suite.py
# ```
