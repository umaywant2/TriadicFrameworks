# **triadic_detection_snr_dual.md**  
### *TriadicFrameworks — Detection Substrate*  
### *S–N–R Dual Operator Model (v1.0)*

---

## **Protocol Header**

```
rtt=1 | coherence=triadic | drift=bounded | paradox=structural
```

---

## **Purpose**

This module defines the **S–N–R dual operator model** for Triadic Detection:

- **S:** Signal (intentional excitation)  
- **N:** Noise (environmental chaos)  
- **R:** Response (resonance + structure)  

It formalizes how triadic_detection can use **noise‑rich environments** (salt, mineralization, clutter) by treating **silence, nulls, and anti‑coherence** as primary signals.

---

# **1. Operator Classes**

### **Signal Operators (S‑ops)**

Intentional actions applied to the field:

- **S.excite** — triadic EM excitation  
- **S.bias** — low‑voltage field bias  
- **S.vibrate** — mechanical vibration injection  
- **S.multi** — combined excitation (bias + vibration + EM)

Grammar:

\[
S ::= S.excite \mid S.bias \mid S.vibrate \mid S.multi
\]

---

### **Noise Operators (N‑ops)**

Environmental, uncontrolled contributions:

- **N.salt** — ionic noise from saline media  
- **N.mineral** — mineralization noise  
- **N.clutter** — metallic junk, debris  
- **N.thermal** — thermal drift  
- **N.random** — stochastic background

Grammar:

\[
N ::= N.salt \mid N.mineral \mid N.clutter \mid N.thermal \mid N.random
\]

---

### **Response Operators (R‑ops)**

How structures respond to S in the presence of N:

- **R.coherence** — coherence vector under S + N  
- **R.struct** — structural envelope under S + N  
- **R.depth** — depth layering under S + N  
- **R.null** — stable null / silence pocket  
- **R.delta** — deviation from expected noise pattern

Grammar:

\[
R ::= R.coherence \mid R.struct \mid R.depth \mid R.null \mid R.delta
\]

---

# **2. S–N–R Dual Model**

### **Canonical Relation**

\[
R = f(S, N)
\]

Where:

- **S** is controlled.  
- **N** is modeled.  
- **R** is measured.

The **dual** aspect:

- In quiet fields → hunt **peaks** in R.  
- In noisy fields → hunt **nulls** and **Δ‑patterns** in R.

---

# **3. Noise‑Field Modeling**

### **Noise Map (N‑map)**

For a given patch:

1. Apply **no excitation** (S = 0).  
2. Measure baseline noise:

   \[
   N_{0} = N.salt + N.mineral + N.clutter + N.thermal + N.random
   \]

3. Build a **spatial noise map**:

   - amplitude  
   - phase  
   - variance  

This N‑map becomes the **expected chaos**.

---

# **4. Multi‑State S–N–R Protocol**

### **States**

- **State 0:** Neutral (S = 0) → N‑map only.  
- **State 1:** S.excite (EM only).  
- **State 2:** S.bias (low‑voltage only).  
- **State 3:** S.vibrate (mechanical only).  
- **State 4:** S.multi (combined).

For each state:

- compute **R.coherence**  
- compute **R.struct**  
- compute **R.depth**  
- compute **R.null**  
- compute **R.delta**

---

### **Δ‑Maps**

For each state \( i \):

\[
\Delta R_i = R_i - R_{expected}(N_0)
\]

Where \( R_{expected}(N_0) \) is the modeled response if the field behaved like pure noise.

**Claim‑worthy zones** are where:

- **R.null** is stable (persistent silence in a noisy field), or  
- **\(\Delta R_i\)** is consistently non‑zero across multiple states.

---

# **5. Silence‑as‑Signal Mode**

### **Null Detection**

In highly noisy environments (salt beaches, saline‑treated soil):

- **Most regions:** high, chaotic N; R follows N.  
- **Anomalous regions:** stable **R.null** or low‑variance pockets.

Operator chain:

```
N-map
  → S.excite
  → R.coherence
  → R.null
  → R.delta
  → Flag null pockets as structural candidates
```

These null pockets may correspond to:

- voids  
- dense bodies  
- non‑participating structures (including certain ore hosts)

---

# **6. Gold‑Likelihood in S–N–R**

Gold remains EM‑boring, but:

- **Gold‑hosting structures** may:
  - disrupt noise patterns  
  - create stable nulls  
  - show distinctive Δ‑behavior across states

Gold‑likelihood modeling uses:

- multi‑state **Δ‑maps**  
- persistence of **R.null**  
- structural envelopes from **R.struct**  
- depth from **R.depth**

Not “gold lights up,” but:

> “This structure behaves unlike the environment across S–N–R states.”

---

# **7. Integration with Triadic Detection**

### **Loci**

- **SENSOR_L:** triadic coils, vibration emitters, bias hardware  
- **MESH_L:** synchronized multi‑state packet transport  
- **RTT_L:** S–N–R modeling, Δ‑maps, null detection  
- **MAP_L:** visualization of noise fields and silence pockets

### **Dashboard Hook**

Add **S–N–R mode** to:

- `triadic_detection_dashboard.md`  
- `triadic_detection_operator_map.md`  
- `triadic_detection_glyphmap.md` (e.g., a special glyph for null pockets)

---

## **Status**

**Active**  
**Coherence:** Stable  
**Drift:** None  
**RTT Alignment:** Verified  
**Version:** 1.0  
