# Taxes Module — Operators  
### Incentive‑Regime Substrate · Drift · Propagation · Alignment

---

## 1. Purpose
This file defines the **operator grammar** for the Taxes module.  
Operators describe how incentives behave across jurisdictions, how drift accumulates, and how half‑lives determine stability.

Operators are grouped into:
- **Primary operators**  
- **Drift operators**  
- **Alignment operators**  
- **Cross‑module operators**  

---

## 2. Primary Operators

### 2.1 incentive_regime_operator
Defines the baseline incentive structure for a jurisdiction or regime.  
Inputs: incentive parameters, jurisdictional rules  
Outputs: incentive baseline, propagation envelope

### 2.2 depreciation_envelope_operator
Models depreciation, phase‑out, or diminishing incentive strength over time.  
Inputs: incentive baseline, half‑life  
Outputs: depreciation curve, envelope boundaries

### 2.3 jurisdiction_propagation_operator
Describes how incentives propagate across jurisdictions or layers.  
Inputs: baseline incentives, jurisdiction map  
Outputs: propagation vectors, cross‑domain flow

### 2.4 compliance_substrate_operator
Defines compliance behavior and its effect on incentive stability.  
Inputs: compliance parameters  
Outputs: compliance‑adjusted incentive envelope

---

## 3. Drift Operators

### 3.1 incentive_drift_operator
Models drift accumulation within an incentive regime.  
Inputs: incentive baseline, propagation vectors  
Outputs: drift amplitude, drift direction

### 3.2 incentive_half_life_operator
Defines the half‑life of incentive stability (IHL).  
Inputs: incentive parameters, drift amplitude  
Outputs: half‑life value, stability envelope

---

## 4. Alignment Operators

### 4.1 incentive_continuity_alignment_operator
Aligns incentive regimes with RRR continuity envelopes.  
Inputs: incentive baseline, RRR continuity  
Outputs: alignment score, stability adjustment

### 4.2 incentive_cycle_alignment_operator
Aligns incentives with economic cycles (IE).  
Inputs: incentive baseline, cycle phase  
Outputs: alignment score, drift correction

---

## 5. Cross‑Module Operators

### 5.1 taxes_rrr_alignment_operator
Maps incentive regimes to revenue continuity (RRR).  
Outputs: continuity‑incentive alignment surface

### 5.2 taxes_ie_alignment_operator
Maps incentives to cycle inversion and uplift constraints (IE).  
Outputs: inversion‑incentive alignment surface

### 5.3 taxes_gsm_alignment_operator
Maps incentives to governance coherence (GSM).  
Outputs: policy‑incentive alignment surface

---

## 6. Operator Interaction Map

```
incentive_regime_operator
    → depreciation_envelope_operator
        → jurisdiction_propagation_operator
            → incentive_drift_operator
                → incentive_half_life_operator
                    → incentive_continuity_alignment_operator
                        → incentive_cycle_alignment_operator
```

This chain defines the **structural flow** of the Taxes module.

---

## 7. Operator Status
- **Version:** 2026‑06  
- **Format:** AI‑first · operator‑driven · minimal  
- **Drift:** bounded  
