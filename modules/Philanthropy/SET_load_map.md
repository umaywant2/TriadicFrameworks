# SET Load Map — Philanthropy & Funding Transparency Module

This file defines the Structural Energy Theory (SET) load model for philanthropic funding flows.  
SET treats money, incentives, governance pressure, and reporting demands as **structural energy** moving through a multi-layer system.

The SET Load Map reveals:
- where energy accumulates  
- where it leaks  
- where it bottlenecks  
- where it destabilizes flows  
- where alignment is strong  
- where drift becomes inevitable  

---

# 1. Purpose of SET in Philanthropy

Philanthropy is not just money.  
It is **energy** moving through:

- donors  
- foundations  
- intermediaries  
- NGOs  
- subcontractors  
- local partners  
- beneficiaries  

Each node absorbs, transforms, or leaks energy.

SET provides a structural model for understanding these dynamics.

---

# 2. SET Components for Funding Flows

SET uses four core operators:

1. **SET_IN(node)** — energy entering  
2. **SET_OUT(node)** — energy leaving  
3. **SET_LEAK(node)** — energy lost  
4. **SET_BAL(node)** — balance between input and output  

These operators apply to:
- money  
- incentives  
- governance pressure  
- reporting load  
- compliance requirements  
- reputational energy  

---

# 3. SET_IN — Incoming Energy

SET_IN includes:

- funding received  
- donor intent  
- mandates  
- compliance requirements  
- reputational expectations  
- governance pressure  

Example:
```
SET_IN(NGO_C) = $2.4M + 3 mandates + high reporting load
```

High SET_IN is not inherently good — it can overload a node.

---

# 4. SET_OUT — Outgoing Energy

SET_OUT includes:

- grants disbursed  
- services delivered  
- outcomes produced  
- reports generated  
- compliance actions  
- community engagement  

Example:
```
SET_OUT(NGO_C) = $1.9M programs + 4 reports + 2 audits
```

---

# 5. SET_LEAK — Lost Energy

SET_LEAK includes:

- overhead  
- administrative inefficiency  
- fundraising costs  
- legal fees  
- intermediary extraction  
- narrative inflation  
- governance friction  

Example:
```
SET_LEAK(IntermediaryX) = 42%
```

High leakage is a structural red indicator.

---

# 6. SET_BAL — Energy Balance

SET_BAL measures whether a node is:

- overloaded  
- underloaded  
- balanced  
- leaking  
- bottlenecked  

Formula:
```
SET_BAL(node) = SET_OUT(node) / SET_IN(node)
```

Interpretation:
- **> 0.8** → high efficiency  
- **0.5–0.8** → moderate efficiency  
- **< 0.5** → structural drift  
- **< 0.3** → severe leakage or overload  

Example:
```
SET_BAL(NGO_C) = 0.79 (healthy)
```

---

# 7. SET Load Across the Funding Chain

Example chain:
```
DonorA → FoundationB → IntermediaryX → NGO_C → LocalPartnerD → Beneficiary
```

SET load map:
```
DonorA:
  SET_IN = intent + capital
  SET_OUT = grants
  SET_BAL = 1.00

FoundationB:
  SET_IN = $10M + donor mandates
  SET_OUT = $4.2M disbursed
  SET_LEAK = endowment preservation
  SET_BAL = 0.42

IntermediaryX:
  SET_IN = $4.2M
  SET_OUT = $2.4M
  SET_LEAK = 42%
  SET_BAL = 0.57

NGO_C:
  SET_IN = $2.4M
  SET_OUT = $1.9M
  SET_LEAK = 18%
  SET_BAL = 0.79

LocalPartnerD:
  SET_IN = $1.9M
  SET_OUT = $1.82M
  SET_LEAK = 4%
  SET_BAL = 0.96
```

---

# 8. SET Load Patterns in Philanthropy

Common patterns:

### **8.1 Upstream Overload**
Foundations overloaded with:
- donor mandates  
- governance pressure  
- reputational expectations  

Result: **slow disbursement**.

---

### **8.2 Midstream Leakage**
Intermediaries absorb:
- overhead  
- compliance  
- reporting  
- branding  

Result: **energy loss**.

---

### **8.3 Downstream Strain**
Local partners overloaded with:
- reporting  
- compliance  
- donor expectations  

Result: **reduced program capacity**.

---

### **8.4 Narrative Inflation**
Energy diverted into:
- storytelling  
- branding  
- donor relations  

Result: **signal-to-noise collapse**.

---

# 9. SET Load Integrity Score

Each node receives a SET integrity score:

```
SET_Integrity(node) =
  w1 * SET_BAL(node)
+ w2 * (1 - SET_LEAK(node))
+ w3 * VIS(node)
+ w4 * ACC(node)
```

Example:
```
SET_Integrity(IntermediaryX) = 0.41 (low)
```

---

# 10. AI Process Manager Agent (PMA) Integration

The PMA uses SET to:

- detect overload  
- identify leakage  
- map bottlenecks  
- recommend structural corrections  
- generate donor clarity reports  
- maintain system-wide coherence  

Operators used:
```
SET_IN, SET_OUT, SET_LEAK, SET_BAL
FLOW, TRACE, LEAK
GOV, ACC, VIS
DRF, ALN, COH
```

---

# 11. Summary

The SET Load Map reveals:

- where philanthropic energy accumulates  
- where it leaks  
- where it bottlenecks  
- where drift becomes inevitable  
- where alignment is strong  
- where structural corrections are needed  

SET transforms philanthropy from a **narrative-driven system** into a **structurally visible energy system**, enabling clarity, accountability, and alignment across the entire funding chain.
