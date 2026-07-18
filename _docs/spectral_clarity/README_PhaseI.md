# Spectral Clarity — Phase I Runtime Guide

Welcome to **Phase I** of the Spectral Clarity runtime lens.  
This stage establishes the **Visible/IR strobe engine**, overlay compositor, and validator scroll workflow.

---

## 📂 File Map

- `manifests/PhaseI_VisibleIR_Manifest.yaml` → Session manifest (strobes, sensors, notes).
- `manifests/Hardware_Config_HPZ440.yaml` → Hardware configuration for HP Z440 workstation.
- `overlays/VisibleIR_Overlay_Template.json` → Overlay template linking phase maps and glyphs.
- `overlays/Glyph_Set_SpectralClarity.json` → Glyph definitions for resonance corridors and thresholds.
- `atlases/PhaseI_VisibleIR_Atlas_Schema.md` → Schema for NPZ/HDF5 phase atlas storage.
- `scrolls/SpectralClarity_PhaseI_Scroll.md` → Narrative scroll documenting intent, setup, findings, remix pathways.
- `runtime/strobe_engine_visibleIR.py` → Strobe engine scaffold for Visible/IR bands.
- `runtime/overlay_compositor.py` → Overlay compositor scaffold for phase atlases.

---

## ⚙️ Workflow Steps

1. **Setup hardware**
   - Connect visible LED strobe and IR diode source.
   - Sync visible strobe to actuator; detune IR strobe by Δf.
   - Attach CMOS and InGaAs sensors with gated exposure.

2. **Configure manifests**
   - Edit `PhaseI_VisibleIR_Manifest.yaml` with session parameters.
   - Update `Hardware_Config_HPZ440.yaml` to reflect current workstation specs.

3. **Run strobe engine**
   - Launch `runtime/strobe_engine_visibleIR.py`.
   - Verify pulses, duty cycles, and phase offsets.

4. **Capture phase maps**
   - Save outputs as `visible_phase.npy`, `ir_phase.npy`, etc.
   - Store amplitude and confidence arrays alongside.

5. **Compose overlays**
   - Use `runtime/overlay_compositor.py` to fuse Visible/IR maps.
   - Reference `VisibleIR_Overlay_Template.json` for layer structure.
   - Apply glyphs from `Glyph_Set_SpectralClarity.json`.

6. **Document scroll**
   - Record intent, setup, findings in `SpectralClarity_PhaseI_Scroll.md`.
   - Include resonance corridors, thresholds, and remix pathways.

---

## 🌀 Validator Practices

- **Artifact dignity:** Always log manifests and scrolls; never discard raw runs.
- **Phase atlas integrity:** Use schema in `atlases/PhaseI_VisibleIR_Atlas_Schema.md` for reproducibility.
- **Remix pathways:** Document extensions (RF lock-in, chirp scans) for future phases.

---

## 🔮 Next Steps

- Extend runtime to include RF lock-in overlays.
- Add chirp scanning for bifurcation mapping.
- Prepare Phase II manifests and schemas.

---

© 2025 TriadicFrameworks. Remix freely, honor lineage.
