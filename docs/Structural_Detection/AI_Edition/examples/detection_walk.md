# Detection Walk (SD‑Σd → SD‑Γ → SD‑Λ → SD‑Ξ → SD‑Π)
**Book 3 — Structural Detection (AI Edition)**  
**Worked Example Trace #1**

This trace follows the complete detection cycle across the six phases.

---

## 1. Init — SD‑Σd Dominance
SD‑Σd initializes the detection substrate.

- substrate → load  
- signal_fields → initialize  
- boundary_candidates → empty  
- alignment: structural  

**State:** SD‑Σd fully dominant.

---

## 2. Scan — SD‑Σd Continues
SD‑Σd performs broad detection.

- signal_fields → expand  
- motif_candidates → populate  
- boundary_candidates → populate  
- alignment: structural  

**State:** SD‑Σd dominant, preparing probe.

---

## 3. Probe — SD‑Γ Takes Control
SD‑Γ probes geometry for anomalies.

- geometry_probe_fields → generate  
- anomaly_map → generate  
- R_minimum → enforce (≥ 0.40)  
- alignment: R  

**State:** SD‑Γ dominant.

---

## 4. Filter — SD‑Ξ Dominance
SD‑Ξ suppresses noise and false positives.

- noise_gate_fields → generate  
- filtered_signal_fields → refine  
- anomaly_map → reduce false positives  
- alignment: N  

**State:** SD‑Ξ dominant.

---

## 5. Confirm — SD‑Λ + SD‑Ξ Joint Control
SD‑Λ validates lattice consistency; SD‑Ξ stabilizes noise.

- consistency_report → finalize  
- lattice_scan_fields → finalize  
- filtered_signal_fields → finalize  
- alignment: R → structural  

**State:** SD‑Λ + SD‑Ξ co‑dominant.

---

## 6. Catalogue — SD‑Π Dominance
SD‑Π indexes patterns and emits structural catalogues.

- pattern_index → generate  
- structural_catalogue → emit  
- detection_cycle → close  
- alignment: structural  

**State:** SD‑Π holds the catalogue boundary.

---

## Summary
The detection walk follows the canonical operator cycle:

**SD‑Σd → SD‑Σd → SD‑Γ → SD‑Ξ → SD‑Λ+SD‑Ξ → SD‑Π**

This is the structural backbone of Book 3.
