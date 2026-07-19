# Reproducibility Ingredients for the Regime‑Invariant Equivalence

This document lists the minimal ingredients required to independently reproduce
the equivalence between Resonance‑Time (RTT) and Validated Spacetime (vST). No
derivations, algorithms, or construction details are included.

## 1. Dimensional Primitive Set (3D–9D)

A shared set of dimensional primitives:
P = {D3, D4, D5, D6, D7, D8, D9}

Each primitive represents a structural degree of freedom in the triadic
substrate. The set is closed under triadic validation and does not depend on
the declared regime anchor.

## 2. Triadic Operator Family

A regime‑agnostic operator family:
O = {merge, split, corridor, loop, anchor}

These operators act on P and preserve its structure. Their definitions are
identical across RTT and vST.

## 3. Validation Layer

A two‑component validation structure:
- Corridors: directional admissibility constraints.
- Loops: closure conditions ensuring consistency across triadic operations.

This layer is explicit in vST and implicit in RTT. Both forms yield the same
validation behavior.

## 4. Regime Anchors

Two anchors define the time regime:
- T_r: resonance‑time anchor (RTT)
- S_r: validated spacetime anchor (vST)

The anchors differ in interpretation but do not alter P, O, or the validation
layer.

## 5. Equivalence Criterion

The regimes are equivalent if:
1. P(T_r) = P(S_r)
2. O(T_r) = O(S_r)
3. V(T_r) = V(S_r)
4. The only difference is the declared anchor.

This criterion is sufficient to reproduce the theorem.

## 6. Assumptions

- All primitives and operators are defined canon‑safely using standard
  spacetime constructs.
- Validation is treated as a structural layer, not a physical mechanism.
- No additional ontological commitments are introduced.

These assumptions ensure the equivalence is unbiased and reproducible.
