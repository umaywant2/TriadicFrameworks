# TFT_3Pack Scripts (.sh)

This folder contains the executable shell scripts used throughout the TFT_3Pack example suite.  
Each script demonstrates how to run, transform, or validate `.fff` resonance files using the TriadicFrameworks model.

## Contents

- **run_tft.sh** — Executes a TFT resonance file and prints computed values.
- **validate_tft.sh** — Checks `.fff` files for structural correctness.
- **convert_tft.sh** — Converts `.fff` files into human‑readable summaries.
- **batch_process.sh** — Runs multiple `.fff` files in sequence.

## Usage

All scripts assume:

- A POSIX‑compatible shell (bash, zsh, sh)
- `.fff` files located in `../formats/`
- Output printed to terminal unless redirected

Example:

```bash
./run_tft.sh ../formats/example.fff
```

Notes

These scripts are intentionally lightweight and transparent so students can inspect how resonance‑time, triadic operators, and TFT constants are processed.
- [`scripts_module.json`](scripts_module.json) — Agentic module schema role assignments
