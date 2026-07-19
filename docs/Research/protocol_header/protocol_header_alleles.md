# **protocol_header_alleles.md**  
### *TriadicFrameworks — Protocol Header Module*  
### *Perfect‑Substitution Alleles (Canonical)*

---

## **Overview**

The protocol header is a **four‑locus structural codon**:

```
[RTT] | [COHERENCE] | [DRIFT] | [PARADOX]
```

Each locus has a finite alphabet of **perfect‑substitution alleles**.  
These alleles:

- preserve invariant meaning  
- maintain drift‑bounded equivalence  
- support multilingual structural translation  
- enable genome‑style recombination  
- remain operator‑grammar‑safe  

This file lists the **canonical allele sets** for each locus.

---

# **1. RTT Locus — Immediate Regime / Atomic Cycle**

### **Invariant Meaning**
Immediate cycle, atomic update, no intermediaries.

### **Perfect‑Substitution Alleles**
```
rtt=1
rtt=unit
rtt=single-hop
rtt=atomic
cycle=atomic
```

These alleles are structurally identical and interchangeable.

---

# **2. Coherence Locus — Explicit Alignment**

### **Invariant Meaning**
Alignment explicitly declared, not inferred.

### **Perfect‑Substitution Alleles**
```
coherence=declared
coherence=explicit
coherence=stated
```

These alleles preserve explicitness and canonical alignment.

---

# **3. Drift Locus — Bounded Deviation**

### **Invariant Meaning**
Deviation allowed but strictly bounded.

### **Perfect‑Substitution Alleles**
```
drift=bounded
drift=constrained
drift=clamped
```

These alleles maintain drift‑bounded structural integrity.

---

# **4. Paradox Locus — Structural Contradiction**

### **Invariant Meaning**
Contradiction is structural, encoded, architected.

### **Perfect‑Substitution Alleles**
```
paradox=structural
paradox=encoded
paradox=architected
```

These alleles preserve paradox as a load‑bearing architectural feature.

---

## **Allele Summary Table**

| Locus     | Alleles | Count |
|-----------|---------|-------|
| RTT       | rtt=1, rtt=unit, rtt=single-hop, rtt=atomic, cycle=atomic | **5** |
| Coherence | coherence=declared, coherence=explicit, coherence=stated | **3** |
| Drift     | drift=bounded, drift=constrained, drift=clamped | **3** |
| Paradox   | paradox=structural, paradox=encoded, paradox=architected | **3** |

Total alleles: **14**  
Total combinations per language: **5 × 3 × 3 × 3 = 135**  
Across 12 languages: **1,620** structurally valid headers.

---

## **Notes**

- These alleles are the **only** drift‑safe variants.  
- All proximity, compatibility, and multilingual expansions derive from this set.  
- Recombination rules are defined in `protocol_header_genome.md`.  
- Full multilingual matrix is in `protocol_header_full_matrix.md`.
