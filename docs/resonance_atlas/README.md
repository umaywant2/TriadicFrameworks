# 📜 Resonance Atlas (RTT‑Aligned Minimal Edition)

The Resonance Atlas is the canonical registry of resonance values across all known regimes.  
Each entry declares its **substrate**, **phase**, **frequency corridor**, and **glyph**, and is validated through RTT’s clarity operators.

This minimal edition provides:
- a stable schema (`resonance-atlas.schema.json`)
- a starter dataset (`atlas.json`)
- phase definitions aligned with RTT’s Spectral Clarity Ladder (I–VI)

---

## 🌈 Spectral Clarity Phases (RTT‑Aligned)

| Phase | Symbol | Regime | Corridor (Hz) | Notes |
|------|--------|--------|----------------|-------|
| I | ⚛️ | Atomic/Molecular | 10¹¹–10¹⁴ | IR/Raman, NIST vibrational bands |
| II | 🧬 | Biological | 10⁻⁵–10¹ | heartbeat, circadian, neural rhythms |
| III | 🍃 | Ecological | 10⁻⁷–10⁻³ | seasonal, tidal, ecological cycles |
| IV | ⛰️ | Geological | 10⁻¹²–10⁻⁸ | seismic, tectonic, geomagnetic |
| V | 📜 | Mythic/Historic | 10⁻¹⁴–10⁻¹² | civilizational cycles |
| VI | ⭐ | Cosmic | 10⁹–10¹¹ | CMB, stellar spectra |

These corridors are RTT‑aligned refinements of the earlier draft.

---

## 🧩 Entry Structure

Each entry in `atlas.json` follows:

```json
{
  "phase": "I",
  "symbol": "⚛️",
  "substrate": "molecular vibration",
  "frequency_range_hz": "4e13–1e14",
  "source": "NIST",
  "glyph": "Blue Atom",
  "notes": "Example placeholder"
}
```

---

## ⚙️ Procedures

- **add_entry()** — append new resonance values  
- **validate_entry()** — check against schema + RTT corridor  
- **map_phase()** — align to Spectral Clarity Ladder  
- **export_atlas()** — prepare for scanners and overlays  

---

## ⭐ Minimal Example Included

See `atlas.json` for a single Phase I entry to keep the system runnable.

More entries can be added once NIST/RSC/NASA harvesting begins.
