# ⚡ **tft‑3pack Quick‑Start Guide**  
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### *Chaining Primitives into Higher‑Order Triadic Patterns*

The **3‑Pack** is the smallest complete unit of RTT‑aligned action:

1. **Primitive 1** — Begin  
2. **Primitive 2** — Transform  
3. **Primitive 3** — Close  

But the real power of the 3‑Pack emerges when you **chain** these primitives into *higher‑order triadic patterns*.  
This guide shows you how to do that using the 3PAK Shell.

---

# 🔹 1. Basic 3‑Pack Cycle

The simplest triadic action:

```bash
primitive1.sh
primitive2.sh
primitive3.sh
```

This produces a clean:

- beginning  
- middle transformation  
- closure  

This is the “heartbeat” of the system.

---

# 🔸 2. Nested Triadic Pattern  
### *(Triad inside a triad)*

Useful when a transformation itself requires a full triadic arc.

```
Outer Cycle:
  P1 → P2 → P3

Inner Cycle (nested inside P2):
  P1 → P2 → P3
```

Shell example:

```bash
primitive1.sh          # Begin outer cycle
primitive2.sh          # Transform outer cycle

  primitive1.sh        # Begin nested cycle
  primitive2.sh        # Transform nested cycle
  primitive3.sh        # Close nested cycle

primitive3.sh          # Close outer cycle
```

This creates a **triadic pulse inside a triadic wave**.

---

# 🔺 3. Sequential Triadic Pattern  
### *(Triads in a row)*

Useful for workflows that require multiple complete cycles.

```bash
# Cycle 1
primitive1.sh
primitive2.sh
primitive3.sh

# Cycle 2
primitive1.sh
primitive2.sh
primitive3.sh
```

This produces a **triadic chain**, each cycle building on the last.

---

# 🔻 4. Expanded Triadic Pattern  
### *(3 × 3 pattern)*

This is a higher‑order structure:  
each primitive becomes a *mini‑triad*.

```
P1 → (P1 P2 P3)
P2 → (P1 P2 P3)
P3 → (P1 P2 P3)
```

Shell example:

```bash
# P1 expanded
primitive1.sh
primitive2.sh
primitive3.sh

# P2 expanded
primitive1.sh
primitive2.sh
primitive3.sh

# P3 expanded
primitive1.sh
primitive2.sh
primitive3.sh
```

This creates a **9‑step resonance arc**.

---

# 🔼 5. Resonant Triadic Spiral  
### *(Each cycle increases in scope)*

This is a triadic pattern that **grows**:

```
Cycle 1: P1 → P2 → P3
Cycle 2: (P1 P2) → (P2 P3) → (P3 P1)
Cycle 3: Full triadic expansion
```

Shell example:

```bash
# Cycle 1
primitive1.sh
primitive2.sh
primitive3.sh

# Cycle 2
primitive1.sh
primitive2.sh
primitive2.sh
primitive3.sh
primitive3.sh
primitive1.sh

# Cycle 3 (full expansion)
primitive1.sh
primitive2.sh
primitive3.sh
primitive1.sh
primitive2.sh
primitive3.sh
primitive1.sh
primitive2.sh
primitive3.sh
```

This produces a **spiraling resonance pattern** — ideal for complex workflows.

---

# 🧭 6. Using 3‑Pack Patterns with WRSADC

Because the 3‑Pack integrates cleanly with WRSADC:

- each primitive call becomes a lineage event  
- each cycle becomes a boundary‑safe action  
- each pattern becomes a structural‑awareness arc  

This means you can wrap any WRSADC dispatch inside a triadic pattern:

```bash
primitive1.sh
python mymodule.py --phase=transform
primitive2.sh
python mymodule.py --phase=finalize
primitive3.sh
```

---

# 🧙 Mythmatical Architect’s Note

Triads are not steps — they are **gestures**.  
When you chain them, you create **rhythms**.  
When you nest them, you create **structures**.  
When you spiral them, you create **growth**.

The 3‑Pack is the smallest breath of RTT.  
These patterns are its songs.
