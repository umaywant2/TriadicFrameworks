# Spectral Clarity — Phase III Runtime Guide

Phase III introduces **UV/THz strobe modules** and embeds **advanced safety protocols**.

---

## 📂 File Map

- `manifests/PhaseIII\_UVTHz\_Manifest.yaml` → Session manifest for UV/THz runs.
- `manifests/Safety\_Protocols.yaml` → Validator-grade safety definitions.
- `overlays/UV\_Overlay\_Template.json` → Overlay template for UV fluorescence.
- `overlays/THz\_Overlay\_Template.json` → Overlay template for THz hydration/structural maps.
- `atlases/PhaseIII\_UVTHz\_Atlas\_Schema.md` → Schema for UV/THz atlas storage.
- `scrolls/SpectralClarity\_PhaseIII\_Scroll.md` → Narrative scroll for Phase III.
- `runtime/uv\_strobe\_engine.py` → UV strobe runtime scaffold.
- `runtime/thz\_strobe\_engine.py` → THz strobe runtime scaffold.
- `runtime/safety\_monitor.py` → Safety monitor scaffold.

---

## ⚙️ Workflow Steps

1. Configure UV diode and THz antenna with manifests.
2. Run `uv\_strobe\_engine.py` and `thz\_strobe\_engine.py` for gated captures.
3. Apply safety checks via `safety\_monitor.py`.
4. Compose overlays using JSON templates.
5. Document findings in `SpectralClarity\_PhaseIII\_Scroll.md`.

---

## 🌀 Validator Practices

- Always enforce safety protocols before running strobes.
- Document duty cycles, pulse widths, and containment.
- Use atlas schema for reproducibility.
- Render uncertainty masks for low-confidence zones.

---

## 🔮 Next Steps

- Phase IV: X-ray stroboscopy and facility integration.
- Cross-band calibration library for full-spectrum fusion.


