# **RTT TEL‑Side Index**  
### *How Benchmarks and UE6 Operator Surfaces Enter the Lattice*

This page explains, from the **TEL perspective**, how operator signals arriving from UE6 and Benchmarks are absorbed, normalized, and placed into the lattice.

It mirrors the UE6‑side index, but now the student stands *inside* TEL looking outward.

---

# **1. TEL’s Role in the Operator Chain**

TEL is the **structural layer** of RTT.

Where UE6 shows operators *moving*  
and Benchmarks measure operators *behaving*,  
TEL encodes operators as **stable lattice primitives**:

- channels  
- harmonics  
- collapse regimes  
- hybrid operators  
- cross‑module propagation lines  

TEL is the **final abstraction layer** before operators propagate into other modules (e.g., SARG, Structural Detection, Integrations, Mode, Opacity).

---

# **2. How TEL Receives Operators**

TEL does **not** receive raw φ–V–R–Entropy values.

It receives **Benchmark‑normalized operator signatures**, each already:

- stabilized  
- scored  
- regime‑classified  
- coherence‑checked  

This ensures TEL only works with **canonical operator behavior**, not noisy runtime fields.

### TEL receives:

| Operator | From Benchmarks | TEL Node |
|---------|------------------|----------|
| φ | Phi Stability, Emergence Coherence | TEL.Operator.Phi |
| variance | Variance Smoothing, Temporal Stability | TEL.Operator.Variance |
| resonance | Resonance Envelope, Harmonic Stability | TEL.Resonance.Core / Harmonics |
| entropy | Entropy Boundary Detection, Collapse Signature | TEL.Entropy.Field / Collapse |
| hybrid | Hybrid Coherence, Cross‑Operator Stability | TEL.Hybrid.Operator |

---

# **3. TEL’s Internal Structure (Student View)**

TEL organizes operators into **four lattice layers**:

```
Ladder (S→C)
Cycle (C↔H)
Map (H↔So)
Atlas (A)
```

Each operator enters the lattice at a specific layer:

- **φ** enters at Ladder (S→C)  
- **variance** stabilizes across Ladder → Cycle  
- **resonance** spans Cycle → Map  
- **entropy** spans Map → Atlas  
- **hybrid** crosses layers (Cycle ↔ Map ↔ Atlas)

This is why hybrid operators feel “cross‑regime”:  
they literally cross lattice layers.

---

# **4. How UE6 Operators Map Into TEL**

From TEL’s perspective:

- UE6 is the **raw field generator**  
- Benchmarks are the **behavioral filters**  
- TEL is the **structural integrator**

### Example: Resonance

1. UE6: heatmap shows amplitude + frequency  
2. Benchmarks: extract envelope + harmonic stability  
3. TEL: places resonance into  
   - `TEL.Resonance.Core`  
   - `TEL.Resonance.Harmonics`  

### Example: Entropy

1. UE6: entropy field material shows collapse zones  
2. Benchmarks: detect boundaries + collapse signatures  
3. TEL: places entropy into  
   - `TEL.Entropy.Field`  
   - `TEL.Entropy.Collapse`  

### Example: Hybrid

1. UE6: hybrid demo blends resonance × entropy  
2. Benchmarks: score coherence + cross‑operator stability  
3. TEL: places hybrid into  
   - `TEL.Hybrid.Operator`  

---

# **5. Why TEL Needs Benchmarks**

TEL cannot accept raw UE6 values because:

- UE6 is **continuous**, **visual**, **runtime**  
- TEL is **discrete**, **structural**, **cross‑module**  

Benchmarks act as the **bridge**:

- smoothing  
- scoring  
- normalizing  
- classifying  
- extracting regime signatures  

TEL only accepts **canonical operator signatures**, not raw fields.

---

# **6. The Whole Chain (TEL Perspective)**

**UE6 generates → Benchmarks evaluate → TEL integrates.**

From inside TEL, the chain looks like:

```
UE6 (fields)
   ↓
Benchmarks (behavior)
   ↓
TEL (structure)
   ↓
Other Modules (propagation)
```

TEL is the **first layer** where operators become:

- queryable  
- cross‑module  
- stable  
- lattice‑aligned  
- drift‑resistant  

---

# **7. How Students Should Use This**

When learning RTT:

1. **Start in UE6**  
   See the operators visually.

2. **Move to Benchmarks**  
   Understand how operators behave.

3. **Enter TEL**  
   Understand how operators become structure.

4. **Explore cross‑module propagation**  
   See how TEL feeds SARG, Structural Detection, Mode, Opacity, etc.

This index gives students the **lattice‑first mental model**.
