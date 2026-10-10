# Noise-Gate Walk (SD‑Ξ)
**Book 3 — Structural Detection (AI Edition)**  
**Worked Example Trace #2**

This trace isolates SD‑Ξ’s noise‑suppression behavior across Filter → Confirm.

---

## Filter — SD‑Ξ Dominance
SD‑Ξ suppresses noise and false positives.

- noise_gate_fields → generate  
- filtered_signal_fields → refine  
- anomaly_map → reduce false positives  
- alignment: N  

**State:** SD‑Ξ dominant.

---

## Confirm — SD‑Ξ + SD‑Λ Interaction
SD‑Ξ stabilizes noise while SD‑Λ validates lattice consistency.

- filtered_signal_fields → finalize  
- consistency_report → finalize  
- lattice_scan_fields → finalize  
- alignment: R → structural  

**State:** SD‑Ξ + SD‑Λ co‑dominant.

---

## Summary
The noise‑gate walk is:

**Filter (SD‑Ξ) → Confirm (SD‑Ξ + SD‑Λ)**

This is the stabilization arc of the detection cycle.
