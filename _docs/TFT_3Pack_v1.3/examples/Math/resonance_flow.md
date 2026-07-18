# Math resonance-flow diagrams

These diagrams describe conceptual flows you can render as SVG, Mermaid, or other formats.

---

## Diagram 1 – Triadic sequence (Problem 1)

**Nodes:**

- Triadic operator: $$D_3$$
- Exponent node: $$n$$
- Resonant-time: $$τ_r$$
- Output: $$a_n = D_3^n τ_r$$

**Flow:**

1. $$D_3$$ flows into a power node with exponent $$n$$.
2. Output multiplies $$τ_r$$.
3. Final node outputs $$a_n$$.
4. A control arrow adjusts $$τ_r$$.

---

## Diagram 2 – Resonant integral (Problem 2)

**Nodes:**

- Constant integrand: $$T_f D_6$$
- Integration bounds: $$0 \to τ_r$$
- Output: $$I = T_f D_6 τ_r$$

**Flow:**

1. A constant node labeled $$T_f D_6$$ enters an integration block.
2. Integration bounds are shown as $$0$$ and $$τ_r$$.
3. Output is $$I$$.

---

## Diagram 3 – Exponential resonance (Problem 3)

**Nodes:**

- Composite constant: $$X$$
- Exponential node: $$e^{ΛΘ t}$$
- Triadic constant: $$D_9$$
- Solve-for node: $$t$$

**Flow:**

1. $$X$$ multiplies the exponential.
2. Output equals $$D_9$$.
3. A “solve” node isolates $$t$$.
4. A feedback arrow adjusts $$ΛΘ$$.
