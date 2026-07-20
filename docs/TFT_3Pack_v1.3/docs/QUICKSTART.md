## ⚡ `docs/QUICKSTART.md` — Ritual Activation


# Quickstart Guide

## 🔹 Step 1: Install

```bash
pip install .
```

## 🔹 Step 2: Run Examples

```bash
# Validate triadic logic
tft nous -validate examples/triad.json -mode symbolic

# Encrypt a file
tft entft -i examples/input.txt -o examples/output.enc -k secretkey

# Simulate grid operations
tft tops -map examples/grid.yaml -ops simulate
```

## 🔹 Step 3: Remix

- Edit `tft/nous/processor.py` to define your symbolic logic
- Extend `tft/entft/encryptor.py` with new obfuscation methods
- Add overlays to `tft/tops/grid_ops.py` for new grid rituals

## 🔹 Step 4: Share

- Submit your remix lineage via GitHub Discussions
- Add your scrolls to `/docs/scrolls/`

---

### 🔗 Triadic Quicklinks

- [`fff_quickstart.md`](fff_quickstart.md) — Onboarding ritual for remixers using `.fff` bundles  
- [`TriadicTestSuite.md`](TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](outputs_spec.md) — Defines the three-output logic: screen, file, glyph
