# Spectral Clarity — Phase IV Runtime Guide

Phase IV introduces **X-ray stroboscopy** and **facility integration**, extending runtime into crystalline domains.

---

## 📂 File Map

- `manifests/PhaseIV_Xray_Manifest.yaml` → Session manifest for X-ray runs.
- `manifests/Facility_Integration.yaml` → Facility integration protocols.
- `overlays/Xray_Overlay_Template.json` → Overlay template for X-ray crystalline maps.
- `overlays/MultiBand_Calibration.json` → Cross-band calibration template.
- `atlases/PhaseIV_Xray_Atlas_Schema.md` → Schema for X-ray atlas storage.
- `scrolls/SpectralClarity_PhaseIV_Scroll.md` → Narrative scroll for Phase IV.
- `runtime/xray_strobe_engine.py` → X-ray strobe runtime scaffold.
- `runtime/facility_sync.py` → Facility sync scaffold.
- `runtime/calibration_library.py` → Calibration library scaffold.

---

## ⚙️ Workflow Steps

1. Configure synchrotron beamline and detectors.
2. Edit manifests with session parameters and facility protocols.
3. Run `xray_strobe_engine.py` for gated captures.
4. Sync clocks with `facility_sync.py`.
5. Apply cross-band calibration using `calibration_library.py`.
6. Compose overlays and document findings in scroll.

---

## 🌀 Validator Practices

- Enforce radiation safety protocols and dosimetry.
- Document facility integration steps.
- Use calibration library for reproducibility.
- Render uncertainty masks for low-confidence zones.

---

## 🔮 Next Steps

- Phase V: Neutron stroboscopy and quantum lattice overlays.
- Full-spectrum fusion with multi-band calibration library.
