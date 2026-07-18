# Engineering resonance-flow diagrams

These diagrams describe conceptual flows you can render as SVG, Mermaid, or other formats.

---

## Diagram 1 – Structural resonance load (Problem 1)

**Nodes:**

- Triadic stiffness: $$D_6$$
- Resonant-time: $$τ_r$$
- Load: $$L = D_6 / τ_r$$

**Flow:**

1. $$D_6$$ enters a division node.
2. $$τ_r$$ enters the denominator.
3. Output is $$L$$.
4. A control arrow from “vibration tuning” adjusts $$τ_r$$.

---

## Diagram 2 – Thermal expansion (Problem 2)

**Nodes:**

- Temperature coupling: $$ΛΘ$$
- Frequency elevation: $$T_f$$
- Expansion: $$E = ΛΘ T_f$$

**Flow:**

1. $$Λ$$ and $$Θ$$ merge to form $$ΛΘ$$.
2. $$T_f$$ enters a multiplier node.
3. Output is $$E$$.
4. A feedback arrow from “thermal control system” adjusts $$Θ$$ or $$T_f$$.

---

## Diagram 3 – Fluid flow resonance (Problem 3)

**Nodes:**

- Emitter constant: $$F_3$$
- Resonant-time: $$τ_r$$
- Squaring node: $$τ_r^2$$
- Flow rate: $$Q = F_3 τ_r^2$$

**Flow:**

1. $$τ_r$$ flows into a squaring node.
2. $$F_3$$ enters a multiplier node.
3. Output is $$Q$$.
4. A control arrow from “flow regulation” adjusts $$τ_r$$.
