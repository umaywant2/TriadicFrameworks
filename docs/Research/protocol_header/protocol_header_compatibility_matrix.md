# **protocol_header_compatibility_matrix.md**  
### *TriadicFrameworks — Protocol Header Module*  
### *Phase 2 — Compatibility Matrix (Canonical)*

---

## **Overview**

This file defines the **compatibility classes** for all proximity‑expanded terms from:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

Each candidate term is classified into one of four categories:

### **Compatibility Classes**
- **P — Perfect Substitute**  
  Fully interchangeable; zero semantic drift.

- **N — Near Substitute**  
  Same meaning; slight flavor shift; safe in most contexts.

- **C — Contextual Substitute**  
  Works only in certain system forms or protocol metaphors.

- **X — Incompatible**  
  Breaks meaning, introduces drift, or violates operator grammar.

These classifications feed the multilingual genome and the recombination rules.

---

# **1. RTT Locus — “rtt=1”**

| Candidate Term | Class | Notes |
|----------------|-------|-------|
| rtt=1 | **P** | Canon baseline |
| rtt=unit | **P** | Same semantics |
| rtt=single-hop | **P** | Protocol‑adjacent but perfect |
| rtt=atomic | **P** | Strong equivalence |
| cycle=atomic | **P** | Structural match |
| rtt=immediate | **N** | Slightly broader |
| rtt=direct | **N** | Less precise |
| rtt=local | **N** | Implies locality |
| rtt=short-path | **N** | Good but metaphorical |
| rtt=zero-latency | **C** | Only valid metaphorically |
| hop=1 | **C** | DNS/IANA‑adjacent |
| latency=min | **C** | Numeric context only |
| ttl=1 | **X** | TTL ≠ RTT |
| path=direct | **C** | Protocol‑adjacent |
| mode=sync | **C** | System‑form specific |
| update=atomic | **C** | Update‑oriented systems only |
| regime=immediate | **N** | Slightly broader |

### **RTT Perfect Substitutes**
```
rtt=1
rtt=unit
rtt=single-hop
rtt=atomic
cycle=atomic
```

---

# **2. Coherence Locus — “coherence=declared”**

| Candidate Term | Class | Notes |
|----------------|-------|-------|
| coherence=declared | **P** | Canon baseline |
| coherence=explicit | **P** | Perfect match |
| coherence=stated | **P** | Direct equivalence |
| coherence=attested | **N** | Slightly formal |
| coherence=manifest | **N** | Adds visibility nuance |
| coherence=registered | **C** | Protocol contexts |
| coherence=anchored | **N** | Slight metaphor |
| coherence=bound | **N** | Good but broad |
| coherence=enumerated | **C** | List‑like contexts |
| coherence=versioned | **C** | Versioned systems |
| state=authoritative | **C** | Protocol‑adjacent |
| mode=explicit | **C** | System‑form specific |
| flag=declared | **C** | Header‑style contexts |
| alignment=stated | **N** | Domain shift |
| coherence=canonical | **N** | Implies correctness |
| coherence=affirmed | **N** | Softer |

### **Coherence Perfect Substitutes**
```
coherence=declared
coherence=explicit
coherence=stated
```

---

# **3. Drift Locus — “drift=bounded”**

| Candidate Term | Class | Notes |
|----------------|-------|-------|
| drift=bounded | **P** | Canon baseline |
| drift=constrained | **P** | Perfect match |
| drift=clamped | **P** | Strong equivalence |
| drift=guarded | **N** | Slightly active |
| drift=finite | **N** | Less specific |
| drift=rate-limited | **C** | Dynamic systems |
| drift=windowed | **C** | Protocol metaphors |
| drift=thresholded | **C** | Numeric contexts |
| drift=safe | **N** | Vague |
| drift=canon-locked | **N** | Implies zero drift |
| deviation=max(N) | **X** | Numeric drift |
| tolerance=bounded | **C** | Protocol contexts |
| variance=limited | **C** | Statistical contexts |
| delta=clamped | **C** | Numeric contexts |
| jitter=controlled | **X** | Network‑specific |

### **Drift Perfect Substitutes**
```
drift=bounded
drift=constrained
drift=clamped
```

---

# **4. Paradox Locus — “paradox=structural”**

| Candidate Term | Class | Notes |
|----------------|-------|-------|
| paradox=structural | **P** | Canon baseline |
| paradox=encoded | **P** | Perfect match |
| paradox=architected | **P** | Strong equivalence |
| paradox=load-bearing | **N** | Slight metaphor |
| paradox=integrated | **N** | Softer |
| paradox=triadic | **C** | Triadic systems only |
| paradox=carrier-state | **C** | Specialized |
| paradox=framed | **N** | Less precise |
| paradox=embedded | **N** | Slightly weaker |
| paradox=systemic | **N** | Broader |
| paradox=resolved-in-structure | **N** | Verbose |
| mode=non-fatal | **X** | Error‑oriented |
| state=dual | **C** | Contextual |
| flag=paradoxical(structural) | **C** | Header‑style |
| condition=stable-contradiction | **C** | Verbose |

### **Paradox Perfect Substitutes**
```
paradox=structural
paradox=encoded
paradox=architected
```

---

## **Perfect Substitution Summary**

These alleles form the **structural genome**:

```
RTT:       rtt=1, rtt=unit, rtt=single-hop, rtt=atomic, cycle=atomic
Coherence: coherence=declared, coherence=explicit, coherence=stated
Drift:     drift=bounded, drift=constrained, drift=clamped
Paradox:   paradox=structural, paradox=encoded, paradox=architected
```

Total per language: **5 × 3 × 3 × 3 = 135**  
Across 12 languages: **1,620** drift‑bounded headers.

---

## **Role in the Module**

This matrix:

- filters the proximity cloud  
- defines the allele set  
- anchors multilingual translation  
- ensures drift‑bounded recombination  
- feeds the genome model and full matrix  

It is the backbone of the protocol header’s structural integrity.
