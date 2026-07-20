# RTT_Showcase Walkthrough  
**Goal:** See how φ, variance, resonance, entropy, and hybrid behavior show up in one level.

---

## 1. Start: Phi / Variance Area

- Spawn in or walk to **PhiVarianceArea**.
- Look for **BP_RTT_Primitives**.
- Watch:
  - how fields around it stabilize (variance),
  - how φ shapes the “feel” of the space.
- If available, open **RTT Operator Panel**:
  - note φ and variance values as you move around.

**Question to notice:**  
When φ changes, does variance smooth or amplify the change?

---

## 2. Resonance Area

- Move to **ResonanceArea**.
- Find **BP_RTT_ResonanceDemo** with the **heatmap material**.
- Watch:
  - color shifts (amplitude + frequency),
  - how fast the pattern breathes.
- In the Operator Panel:
  - track **ResonanceValue** vs what you see on the mesh.

**Question to notice:**  
When resonance amplitude spikes, what happens visually? Does it feel “louder” or “sharper”?

---

## 3. Entropy Area

- Move to **EntropyArea**.
- Find **BP_RTT_EntropyDemo** with the **entropy field material**.
- Watch:
  - bright regions (high entropy),
  - how the field changes as you move or as the system evolves.
- In the Operator Panel:
  - track **EntropyValue** and compare to the field’s brightness/size.

**Question to notice:**  
Where does the system look like it’s about to “collapse” or change regime?

---

## 4. Hybrid Area

- Move to **HybridArea**.
- Find **BP_RTT_HybridDemo** (particles / hybrid mesh).
- Watch:
  - how the effect responds when resonance is high but entropy is low,
  - how it behaves when entropy rises.
- In the Operator Panel:
  - imagine a **HybridValue** combining resonance and entropy.

**Question to notice:**  
When does the system feel “coherent but fragile”? That’s hybrid territory.

---

## 5. Connect to Benchmarks and TEL

- UE6: you just saw the operators **move**.
- Benchmarks: each behavior (stability, envelope, collapse) can be **measured**.
- TEL: those measurements become **nodes and channels** in the operator lattice.

**One‑line summary:**  
What you see in RTT_Showcase is exactly what Benchmarks score and what TEL encodes structurally.
