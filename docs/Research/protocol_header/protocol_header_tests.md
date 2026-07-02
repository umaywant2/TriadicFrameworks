# **protocol_header_tests.md**  
### *TriadicFrameworks — Protocol Header Module*  
### *Structural Validation Rules & Test Cases (Canonical)*

---

## **Overview**

This file defines the **structural test suite** for the protocol header:

```
[RTT] | [COHERENCE] | [DRIFT] | [PARADOX]
```

Tests ensure:

- locus integrity  
- allele validity  
- recombination correctness  
- multilingual consistency  
- drift‑boundedness  
- genome alignment  

All tests are **structural only** — no semantic interpretation.

---

# **1. Locus Integrity Tests**

### **Test L1 — Locus Count**
```
assert loci.count == 4
```

### **Test L2 — Locus Order**
```
assert header.order == [RTT, COHERENCE, DRIFT, PARADOX]
```

### **Test L3 — Locus Naming**
```
assert locus.name ∈ {RTT, COHERENCE, DRIFT, PARADOX}
```

### **Test L4 — Locus Invariant Presence**
Each locus must define an invariant meaning.

```
assert locus.invariant is not null
```

---

# **2. Allele Integrity Tests**

### **Test A1 — Allele Count**
```
assert RTT.count == 5
assert COHERENCE.count == 3
assert DRIFT.count == 3
assert PARADOX.count == 3
```

### **Test A2 — Perfect‑Substitution Validity**
```
assert allele ∈ perfect_substitution_set
```

### **Test A3 — No Deprecated Alleles**
```
assert allele.status != "deprecated"
```

### **Test A4 — Allele Structure**
```
assert allele matches "<locus>=<value>" OR multilingual structural equivalent
```

---

# **3. Header Structure Tests**

### **Test H1 — Header Format**
```
assert header matches "<RTT> | <COHERENCE> | <DRIFT> | <PARADOX>"
```

### **Test H2 — Header Locus Alignment**
```
assert header.RTT ∈ RTT_L
assert header.COH ∈ COH_L
assert header.DRIFT ∈ DRIFT_L
assert header.PAR ∈ PAR_L
```

### **Test H3 — Drift‑Boundedness**
```
assert header.DRIFT ∈ {bounded, constrained, clamped}
```

### **Test H4 — Paradox Structurality**
```
assert header.PAR ∈ {structural, encoded, architected}
```

---

# **4. Genome Recombination Tests**

### **Test G1 — Cartesian Product Validity**
```
assert |RTT_L × COH_L × DRIFT_L × PAR_L| == 135
```

### **Test G2 — Multilingual Genome Size**
```
assert total_headers == 1620
```

### **Test G3 — Deterministic Generation**
```
assert HEADER(L,i,j,k,m) ==
       RTT_L[i] | COH_L[j] | DRIFT_L[k] | PAR_L[m]
```

### **Test G4 — No Duplicate Headers**
```
assert matrix.unique == matrix.total
```

---

# **5. Multilingual Consistency Tests**

### **Test M1 — Invariant Preservation**
```
assert meaning(RTT_L[x]) == meaning(RTT_EN[y])
assert meaning(COH_L[x]) == meaning(COH_EN[y])
assert meaning(DRIFT_L[x]) == meaning(DRIFT_EN[y])
assert meaning(PAR_L[x]) == meaning(PAR_EN[y])
```

### **Test M2 — Structural Equivalence**
```
assert structure(L) == structure(EN)
```

### **Test M3 — Alphabet Size**
```
assert |RTT_L| ≥ 3
assert |COH_L| ≥ 2
assert |DRIFT_L| ≥ 2
assert |PAR_L| ≥ 2
```

---

# **6. Protocol‑Adjacent Tests**

### **Test P1 — Contextual Substitute Safety**
```
assert contextual_substitute ∈ compatibility_class.C
```

### **Test P2 — No Contextual Substitutes in Genome**
```
assert contextual_substitute ∉ perfect_substitution_set
```

### **Test P3 — No Incompatible Terms**
```
assert incompatible_term ∉ header
```

---

# **7. Registry Tests**

### **Test R1 — Code Uniqueness**
```
assert registry.codes.unique == true
```

### **Test R2 — Status Validity**
```
assert allele.status ∈ {current, deprecated}
```

### **Test R3 — Deprecation Enforcement**
```
assert deprecated_term ∉ header
```

---

# **8. Example Test Cases**

### **Case 1 — Valid English Header**
```
rtt=atomic | coherence=explicit | drift=clamped | paradox=encoded
```
**Result:** PASS

### **Case 2 — Invalid Drift**
```
rtt=unit | coherence=stated | drift=free | paradox=structural
```
**Result:** FAIL (drift not bounded)

### **Case 3 — Invalid Paradox**
```
rtt=1 | coherence=declared | drift=bounded | paradox=non-fatal
```
**Result:** FAIL (paradox incompatible)

### **Case 4 — Valid Mandarin Header**
```
原子 | 明示 | 有界 | 内嵌
```
**Result:** PASS

---

# **9. Notes**

- All tests are structural only.  
- No semantic inference is permitted.  
- Tests ensure drift‑boundedness and canon alignment.  
- The genome model defines all recombination rules.  
- Multilingual consistency is required for all headers.
