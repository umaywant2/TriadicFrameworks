## Time Crystal Emitter · Bill of Materials (BOM)

| **Group**            | **Item**                                      | **Notes**                                           |
|----------------------|-----------------------------------------------|-----------------------------------------------------|
| Resonance Substrate  | Thin‑film ferromagnet sample                  | RF‑driven magnon layer, MOKE compatible             |
| Resonance Substrate  | Josephson junction array (LN2‑class)          | Accessible superconducting oscillator               |
| Chamber              | Optical‑grade transparent housing             | Supports MOKE / laser access                        |
| Chamber              | Modular resonator mounts                      | Swap ferromagnet / JJ modules                       |
| Chamber              | EM shielding (mu‑metal or equivalent)         | Reduces external interference                       |
| Actuation            | RF signal generator                           | Drives ferromagnet / JJ oscillations                |
| Actuation            | Piezo stack or actuator                       | Mechanical / force channel                          |
| Actuation            | Small electromagnets / coils                  | Local field modulation                              |
| Actuation            | Acoustic transducer (optional)                | Fluids/fields perturbation channel                  |
| Sensing              | MOKE optical setup (laser + detector)         | Thin‑film ferromagnet readout                       |
| Sensing              | SQUID magnetometer (or equivalent)            | Superconducting circuit readout                     |
| Control & Logging    | DAQ / oscilloscope / digitizer                | Time‑series capture                                 |
| Control & Logging    | Host machine with RTT‑Inside stack            | Converts signals → RTTcode packets                  |
| Safety & Support     | Cryogenic handling gear (for JJ arrays)       | LN2 or appropriate cryogen                          |
| Safety & Support     | Laser safety eyewear & beam enclosures        | For MOKE / optical diagnostics                      |
| Safety & Support     | RF shielding and grounding hardware           | Prevents leakage and noise                          |

> **RTT‑Inside note:**  
> Each logged experiment should include a corresponding RTTcode packet with `experiment.experiment_id`, `seed`, `trial`, and `provenance` fields populated for deterministic replay.
