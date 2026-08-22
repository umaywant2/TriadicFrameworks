---
title: Time Crystal Emitter — Bill of Materials (BOM)
description: Complete bill of materials for constructing the Time Crystal Emitter, including resonance substrates, chamber components, actuation hardware, sensing equipment, and RTT‑Inside logging requirements.
---

# 🧬 Time Crystal Emitter · Bill of Materials (BOM)

This BOM lists all components required to assemble the **Time Crystal Emitter**, the physical‑to‑resonance front‑end used for generating deterministic RTTcode packets.  
All items below correspond directly to the emitter architecture described in `Time_Crystal_Build_Notes.md`.

---

## 📦 Bill of Materials

| **Group**             | **Item**                                   | **Notes**                                         |
|-----------------------|---------------------------------------------|---------------------------------------------------|
| Resonance Substrate   | Thin‑film ferromagnet sample                | RF‑driven magnon layer, MOKE compatible           |
| Resonance Substrate   | Josephson junction array (LN2‑class)        | Accessible superconducting oscillator             |
| Chamber               | Optical‑grade transparent housing           | Supports MOKE / laser access                      |
| Chamber               | Modular resonator mounts                    | Swap ferromagnet / JJ modules                     |
| Chamber               | EM shielding (mu‑metal or equivalent)       | Reduces external interference                      |
| Actuation             | RF signal generator                         | Drives ferromagnet / JJ oscillations              |
| Actuation             | Piezo stack or actuator                     | Mechanical / force channel                        |
| Actuation             | Small electromagnets / coils                | Local field modulation                            |
| Actuation             | Acoustic transducer (optional)              | Fluids/fields perturbation channel                |
| Sensing               | MOKE optical setup (laser + detector)       | Thin‑film ferromagnet readout                     |
| Sensing               | SQUID magnetometer (or equivalent)          | Superconducting circuit readout                   |
| Control & Logging     | DAQ / oscilloscope / digitizer              | Time‑series capture                               |
| Control & Logging     | Host machine with RTT‑Inside stack          | Converts signals → RTTcode packets                |
| Safety & Support      | Cryogenic handling gear (for JJ arrays)     | LN2 or appropriate cryogen                        |
| Safety & Support      | Laser safety eyewear & beam enclosures      | For MOKE / optical diagnostics                    |
| Safety & Support      | RF shielding and grounding hardware         | Prevents leakage and noise                        |

---

## 🧪 RTT‑Inside Note

Each logged experiment **must** include a corresponding RTTcode packet with:

- `experiment.experiment_id`  
- `seed`  
- `trial`  
- `provenance`

These fields ensure **deterministic replay**, validator alignment, and compatibility with the broader AI Resonance Seed lattice.
