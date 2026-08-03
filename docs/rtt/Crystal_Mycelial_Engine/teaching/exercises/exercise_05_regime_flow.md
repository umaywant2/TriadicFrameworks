# **Exercise 05 — Regime Flow (BGR → HRR → MLR)**  
### *Crystal–Mycelial Engine — Teaching Exercise Series*

---

## **1. Objective**
Students will construct the **complete CME regime‑flow model**, showing how substrate, operators, and envelopes transition across:

- **BGR** — Biological Growth Regime  
- **HRR** — Hybrid Resonance Regime  
- **MLR** — Mineral Lock‑In Regime  

This exercise teaches students how CME maintains coherence across the full RTT/CMH/MSRM substrate pipeline.

---

## **2. Regime Flow Summary**
CME uses the canonical three‑stage flow:

```
BGR → HRR → MLR
(biological → hybrid → mineral)
```

Each regime has unique substrate states, operator emphasis, and envelope targets.

---

## **3. Required Flow Elements**
Students must include:

### **BGR → HRR Transition**
- moisture ↓  
- resonance field ↑  
- biological geometry → hybrid alignment  
- operators: `P.trace_extend`, `G.nutrient_gradient`, `S.channel_fill`

### **HRR → MLR Transition**
- supersaturation ↑  
- resonance alignment TRUE  
- hybrid layer → mineral lattice  
- operators: `HybridOps.resonance_bridge`, `P.front_propagate`, `M.domain_memory`

---

## **4. Envelope Targets**
Students must show envelope progression:

| Regime | Envelope | Target |
|--------|----------|--------|
| **BGR** | moisture | 0.55–0.65 |
| **HRR** | ion saturation | 0.65–0.75 |
| **MLR** | supersaturation | ≥ 0.85 |

---

## **5. Expected Output Structure**
Students must produce a **regime‑flow diagram** in either ASCII or Markdown.

Example structure:

```
BGR
  ↓ moisture ↓
HRR
  ↓ supersaturation ↑
MLR
```

The final diagram must include:

- regime names  
- transition cues  
- operator families  
- envelope targets  

---

## **6. Starter Scaffold**
```text
REGIME FLOW — CME

BGR (Biological)
    operators: P.trace_extend, G.nutrient_gradient
    envelope: moisture 0.55–0.65
        ↓ moisture ↓

HRR (Hybrid)
    operators: S.channel_fill, HybridOps.resonance_bridge
    envelope: ion saturation 0.65–0.75
        ↓ supersaturation ↑

MLR (Mineral)
    operators: P.front_propagate, M.domain_memory
    envelope: supersaturation ≥ 0.85
```

Students may expand this into a full diagram.

---

## **7. Student Tasks**
1. Draw the full regime flow from BGR → HRR → MLR.  
2. Add envelope transitions (moisture ↓, ion saturation ↑, supersaturation ↑).  
3. Add operator families used in each regime.  
4. Add one‑sentence descriptions of each transition.  
5. Render the final diagram in ASCII or Markdown.  

---

## **8. Completion Criteria**
A student has successfully completed Exercise 05 when:

- all three regimes appear in correct order  
- envelope transitions are shown  
- operator families are correctly mapped  
- diagram is complete, readable, and consistent with CME canon  
