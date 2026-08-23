# **Exercise 04 — Operator Mapping (CME Operator Grammar)**  
### *Crystal–Mycelial Engine — Teaching Exercise Series*

---

## **1. Objective**
Students will construct the **operator‑mapping table** for the Crystal–Mycelial Engine (CME), showing how RTT operator families (**P, E, G, M, S, HybridOps**) apply across:

- Biological Growth Regime (BGR)  
- Hybrid Resonance Regime (HRR)  
- Mineral Lock‑In Regime (MLR)

This exercise teaches students how operator grammar shifts as substrates transition from **biological → hybrid → mineral**.

---

## **2. Operator Families**
CME uses the canonical RTT operator families:

- **P** — Propagation  
- **E** — Energy  
- **G** — Gradient  
- **M** — Memory  
- **S** — Substrate  
- **HybridOps** — Hybrid‑layer operators  

---

## **3. Regime‑Specific Operator Emphasis**
Students must understand the canonical operator emphasis:

**BGR:** P • E • G • M  
**HRR:** S • HybridOps • E • G  
**MLR:** P • M • E • S  

This pattern must appear in the mapping table.

---

## **4. Required Operators**
Students must include the following operators in their mapping:

### **BGR**
- `P.trace_extend`  
- `G.nutrient_gradient`  
- `M.route_memory`  
- `E.logic_pulse`

### **HRR**
- `S.channel_fill`  
- `HybridOps.resonance_bridge`  
- `HybridOps.memory_transfer`  
- `E.resonance_field`

### **MLR**
- `P.front_propagate`  
- `M.domain_memory`  
- `S.substrate_swap`  
- `E.domain_lock`

---

## **5. Expected Output Structure**
Students must produce a table with the following structure:

```
Operator Family | Regime | Operator | Role
```

Example row:

```
P | BGR | P.trace_extend | extend biological geometry
```

The final table should contain **all operators listed above**, each mapped to its regime and role.

---

## **6. Starter Scaffold**
```python
operator_map = [
    # BGR
    ("P", "BGR", "P.trace_extend", "extend biological geometry"),
    ("G", "BGR", "G.nutrient_gradient", "shape nutrient gradients"),
    ("M", "BGR", "M.route_memory", "encode routing memory"),
    ("E", "BGR", "E.logic_pulse", "generate biological pulses"),

    # HRR
    ("S", "HRR", "S.channel_fill", "infiltrate biological channels"),
    ("HybridOps", "HRR", "HybridOps.resonance_bridge", "align resonance fields"),
    ("HybridOps", "HRR", "HybridOps.memory_transfer", "transfer memory to hybrid layer"),
    ("E", "HRR", "E.resonance_field", "generate hybrid resonance field"),

    # MLR
    ("P", "MLR", "P.front_propagate", "advance crystal growth front"),
    ("M", "MLR", "M.domain_memory", "encode mineral domain memory"),
    ("S", "MLR", "S.substrate_swap", "finalize hybrid → mineral transition"),
    ("E", "MLR", "E.domain_lock", "stabilize resonance‑aligned domains")
]
```

Students may use Python, Markdown, or a simple text table.

---

## **7. Student Tasks**
1. Reproduce the operator‑mapping table using the scaffold.  
2. Add a one‑sentence role description for each operator.  
3. Verify regime emphasis matches the canonical pattern.  
4. Print or render the final table for inspection.  
5. Confirm that all operators appear exactly once.  

---

## **8. Completion Criteria**
A student has successfully completed Exercise 04 when:

- all operators are mapped to the correct regime  
- each operator has a clear role description  
- operator emphasis matches BGR → HRR → MLR pattern  
- table is complete, consistent, and readable  
