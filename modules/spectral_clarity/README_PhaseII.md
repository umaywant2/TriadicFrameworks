# Spectral Clarity — Phase II Runtime Guide

Phase II introduces **RF lock-in overlays** and **chirp scans** to surface resonance corridors and bifurcations.

---

## 📂 File Map
- `manifests/PhaseII_RFChirp_Manifest.yaml` → Session manifest for RF lock-in and chirp runs.
- `manifests/SDR_Config_HPZ440.yaml` → SDR hardware configuration.
- `overlays/RF_Overlay_Template.json` → Overlay template for RF quadratures.
- `overlays/Chirp_Scan_Overlay.json` → Overlay template for chirp scans.
- `atlases/PhaseII_RFChirp_Atlas_Schema.md` → Schema for RF/chirp atlas storage.
- `scrolls/SpectralClarity_PhaseII_Scroll.md` → Narrative scroll for Phase II.
- `runtime/rf_lockin_engine.py` → RF lock-in runtime scaffold.
- `runtime/chirp_scan_engine.py` → Chirp scan runtime scaffold.

---

## ⚙️ Workflow Steps
1. Configure SDR and RF generator (`SDR_Config_HPZ440.yaml`).
2. Edit `PhaseII_RFChirp_Manifest.yaml` with session parameters.
3. Run `rf_lockin_engine.py` to capture quadratures and build overlays.
4. Run `chirp_scan_engine.py` to sweep frequencies and construct bifurcation atlases.
5. Compose overlays using JSON templates.
6. Document findings in `SpectralClarity_PhaseII_Scroll.md`.

---

## 🌀 Validator Practices
- Always log manifests and scrolls.
- Use schema for reproducibility.
- Document bifurcations and resonance corridors clearly.

---

## 🔮 Next Steps
- Phase III: UV/THz modules and advanced safety protocols.
- Cross-band calibration library for multi-spectrum overlays.
