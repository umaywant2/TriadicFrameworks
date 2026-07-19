# **protocol_header_loci.md**  
### *TriadicFrameworks — Protocol Header Module*  
### *Locus Definitions (Canonical)*

---

## **Overview**

The protocol header is a **four‑locus structural codon** used across TriadicFrameworks to express drift‑bounded, canon‑aligned system states.

Each locus represents a **structural invariant**:

```
[RTT] | [COHERENCE] | [DRIFT] | [PARADOX]
```

Each locus has a finite alphabet of **perfect‑substitution alleles**, allowing multilingual, cross‑system recombination without semantic drift.

This file defines the **invariant meaning** of each locus.

---

# **1. RTT Locus — Immediate Regime / Atomic Cycle**

### **Invariant Meaning**
The RTT locus expresses **immediacy**:

- single cycle  
- atomic update  
- no intermediaries  
- no latency  
- direct regime response  

### **Structural Definition**
RTT describes how quickly a system responds or updates.  
It is always:

- immediate  
- atomic  
- single‑hop  
- non‑buffered  

### **Canonical Baseline**
```
rtt=1
```

### **Perfect‑Substitution Alleles**
Defined in `protocol_header_alleles.md`.

---

# **2. Coherence Locus — Explicit Alignment**

### **Invariant Meaning**
The Coherence locus expresses **declared alignment**:

- explicitly stated  
- not inferred  
- not emergent  
- not probabilistic  

### **Structural Definition**
Coherence describes how alignment is communicated:

- declared  
- explicit  
- stated  
- attested  

It is always **visible**, never implicit.

### **Canonical Baseline**
```
coherence=declared
```

### **Perfect‑Substitution Alleles**
Defined in `protocol_header_alleles.md`.

---

# **3. Drift Locus — Bounded Deviation**

### **Invariant Meaning**
The Drift locus expresses **controlled deviation**:

- bounded  
- constrained  
- clamped  
- guardrailed  

### **Structural Definition**
Drift describes how much movement or variation is allowed:

- deviation permitted  
- but strictly bounded  
- never unbounded  
- never free‑floating  

### **Canonical Baseline**
```
drift=bounded
```

### **Perfect‑Substitution Alleles**
Defined in `protocol_header_alleles.md`.

---

# **4. Paradox Locus — Structural Contradiction**

### **Invariant Meaning**
The Paradox locus expresses **architected contradiction**:

- structural  
- encoded  
- load‑bearing  
- non‑fatal  

### **Structural Definition**
Paradox describes contradictions that are:

- part of the architecture  
- intentionally encoded  
- stable  
- non‑error states  

It is never accidental or emergent.

### **Canonical Baseline**
```
paradox=structural
```

### **Perfect‑Substitution Alleles**
Defined in `protocol_header_alleles.md`.

---

## **Locus Integrity Rules**

All four loci must:

- preserve invariant meaning  
- use only perfect‑substitution alleles  
- maintain locus order  
- maintain `<locus>=<allele>` structure  
- remain drift‑bounded  
- remain canon‑aligned  

These rules ensure multilingual recombination remains structurally equivalent.

---

## **Cross‑Module Usage**

The protocol header is used in:

- Mode → TEL → Benchmarks propagation  
- structural intelligence pipelines  
- operator grammar  
- protocol‑adjacent system forms  
- multilingual canonical headers  
- genome‑based recombination  
