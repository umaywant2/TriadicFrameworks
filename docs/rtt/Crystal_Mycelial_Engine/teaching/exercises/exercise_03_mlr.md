# **Exercise 03 — MLR (Mineral Lock‑In Regime)**  
### *Crystal–Mycelial Engine — Teaching Exercise Series*

---

## **1. Objective**
Students will implement the **Mineral Lock‑In Regime (MLR)** stage of the CME pipeline by:

- propagating mineral lattice fronts  
- encoding domain memory  
- producing the canonical `mineral_map` substrate  

This exercise introduces **P** and **M** operator families in their mineral‑domain context.

---

## **2. Regime Summary — MLR**
**MLR** models the final transition into mineral lattice logic:

- crystal lattice propagation  
- domain formation  
- impurity‑band memory encoding  
- resonance‑locked geometry  

**Envelope Targets**
- supersaturation: **≥ 0.85**  
- thermal shift: **−3 to −5 °C**  
- resonance alignment: **TRUE**

---

## **3. Required Operators**
Students must use:

- `P.front_propagate` — propagate the mineral lattice front  
- `M.domain_memory` — encode memory into mineral domains  

These produce the canonical `mineral_map` structure.

---

## **4. Expected Output Structure**
The student’s agent should return:

```python
mineral_map = {
    "lattice": <data>,
    "domains": <data>
}
```

Values may be placeholders or simulated data depending on lesson level.

---

## **5. Starter Scaffold**
```python
class MineralDomainAgent:
    def crystallize(self, hybrid_layer):
        """
        Implement the Mineral Lock-In Regime (MLR).
        Required:
            P.front_propagate
            M.domain_memory
        Output:
            mineral_map
        """
        mineral_map = {
            "lattice": None,
            "domains": None
        }

        # TODO: call P.front_propagate
        # TODO: call M.domain_memory

        return mineral_map
```

---

## **6. Student Tasks**
1. Accept `hybrid_layer` from Exercise 02.  
2. Implement `P.front_propagate` to generate lattice propagation.  
3. Implement `M.domain_memory` to encode domain memory.  
4. Store results in `mineral_map`.  
5. Print the resulting `mineral_map` for inspection.  
6. Verify envelope targets (supersaturation ≥ 0.85, thermal shift −3 to −5 °C).  

---

## **7. Completion Criteria**
A student has successfully completed Exercise 03 when:

- `mineral_map["lattice"]` contains a lattice propagation structure  
- `mineral_map["domains"]` contains domain memory data  
- envelope targets are acknowledged  
- code runs without errors  
