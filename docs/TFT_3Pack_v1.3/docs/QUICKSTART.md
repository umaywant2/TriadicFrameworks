## ⚡ `docs/QUICKSTART.md` — Ritual Activation

```markdown
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
