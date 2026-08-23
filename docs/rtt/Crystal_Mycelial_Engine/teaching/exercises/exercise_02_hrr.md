# **Exercise 02 — HRR (Hybrid Resonance Regime)**  
### *Crystal–Mycelial Engine — Teaching Exercise Series*

---

## **1. Objective**
Students will implement the **Hybrid Resonance Regime (HRR)** stage of the CME pipeline by:

- filling biological channels  
- bridging resonance fields  
- producing the canonical `hybrid_layer` substrate  

This exercise introduces **S** and **HybridOps** operator families in their hybrid‑layer context.

---

## **2. Regime Summary — HRR**
**HRR** models the transition from biological geometry to resonance‑aligned hybrid substrate:

- mineral precursor infiltration  
- resonance field alignment  
- hybrid memory transfer  
- dual‑substrate coherence  

**Envelope Targets**
- ion saturation: **0.65–0.75**  
- coherence field: **0.8–1.4 kHz**  
- moisture: **0.35–0.45**

---

## **3. Required Operators**
Students must use:

- `S.channel_fill` — fill biological channels with hybrid substrate  
- `HybridOps.resonance_bridge` — align biological geometry with resonance fields  

These produce the canonical `hybrid_layer` structure.

---

## **4. Expected Output Structure**
The student’s agent should return:

```python
hybrid_layer = {
    "channels": <data>,
    "alignment": <data>
}
```

Values may be placeholders or simulated data depending on lesson level.

---

## **5. Starter Scaffold**
```python
class HybridAlignmentAgent:
    def align(self, bio_map):
        """
        Implement the Hybrid Resonance Regime (HRR).
        Required:
            S.channel_fill
            HybridOps.resonance_bridge
        Output:
            hybrid_layer
        """
        hybrid_layer = {
            "channels": None,
            "alignment": None
        }

        # TODO: call S.channel_fill
        # TODO: call HybridOps.resonance_bridge

        return hybrid_layer
```

---

## **6. Student Tasks**
1. Accept `bio_map` from Exercise 01.  
2. Implement `S.channel_fill` to fill biological channels.  
3. Implement `HybridOps.resonance_bridge` to align geometry with resonance fields.  
4. Store results in `hybrid_layer`.  
5. Print the resulting `hybrid_layer` for inspection.  
6. Verify envelope targets (ion saturation 0.65–0.75, coherence field 0.8–1.4 kHz).  

---

## **7. Completion Criteria**
A student has successfully completed Exercise 02 when:

- `hybrid_layer["channels"]` contains a filled‑channel structure  
- `hybrid_layer["alignment"]` contains resonance alignment data  
- envelope targets are acknowledged  
- code runs without errors  
