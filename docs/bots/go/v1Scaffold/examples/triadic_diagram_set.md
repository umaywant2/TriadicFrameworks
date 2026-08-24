# Triadic Diagram Set — RTT‑Go  
*(for `/docs/bots/go/examples/triadic_diagram_set.md`)*

This document defines the **canonical diagram set** for RTT‑Go.  
It describes the visual diagrams used in documentation, teaching materials, and UI concept work to illustrate:

- the triadic operator stack  
- engine integration  
- MCTS hooks  
- overlays and flows  
- continuity, resonance, topology, ancestry, and risk

Each diagram is specified conceptually so it can be implemented in any drawing tool or UI system.

---

## 1. Operator Stack Diagram  
**Title:** Lumen → Hephaestus → Aurion → Harmonia

**Structure:**

- Four stacked boxes, top to bottom:
  - **Lumen (RTT/1)** — “Structure”
  - **Hephaestus (RTT/2)** — “Regime”
  - **Aurion (RTT/3)** — “Topology & Ancestry”
  - **Harmonia (RTT/12)** — “Triadic Synthesis”
- Arrows flowing downward between each box.
- Side labels:
  - Left: “Operators”
  - Right: “Feeds Engines”

**Purpose:**  
Shows the strict operator lineage and how triadic identity is computed.

---

## 2. Engine Integration Diagram  
**Title:** Engine ↔ RTT‑Go Integration

**Structure:**

- Left column: “Go Engine”
  - NN Inference (policy, value)
  - MCTS Core (selection, expansion, simulation, backprop)
- Right column: “RTT‑Go”
  - Shim
  - Operator Stack
  - Engines (Regime, Resonance, Topology, Continuity, Risk, Scoring)
- Arrows:
  - Engine → Shim → Operators → Engines → MCTS Hooks → Engine MCTS

**Purpose:**  
Shows RTT‑Go as a wrapper around the engine, not a replacement.

---

## 3. MCTS Hooks Diagram  
**Title:** Triadic MCTS Hook Points

**Structure:**

- Central vertical MCTS flow:
  - Selection  
  - Expansion  
  - Simulation  
  - Backpropagation
- Side hook labels pointing into the flow:
  - Policy Priors  
  - Value Estimates  
  - Node Expansion  
  - Child Ordering  
  - Pruning
- Each hook annotated: “Triadic‑aware”.

**Purpose:**  
Visualizes where RTT attaches to MCTS.

---

## 4. Triadic Flow Diagram  
**Title:** Position → Triadic Identity → Move

**Structure:**

- Left: “Board State”
- Middle: “RTT‑Go Stack”
  - Lumen  
  - Hephaestus  
  - Aurion  
  - Harmonia  
  - Engines
- Right: “Outputs”
  - Triadic Scores  
  - Overlays  
  - Commentary  
  - MCTS Hooks

**Purpose:**  
Shows the full pipeline from position to triadic interpretation and move guidance.

---

## 5. Overlay Layers Diagram  
**Title:** Triadic Overlay Layers

**Structure:**

- Concentric or stacked layers over a board silhouette:
  - Regime Overlay  
  - Resonance Overlay  
  - Topology Overlay  
  - Continuity Overlay  
  - Risk Overlay  
  - Triadic HUD
- Legend mapping each layer to its engine(s).

**Purpose:**  
Explains how multiple overlays coexist and what each represents.

---

## 6. Continuity & Drift Diagram  
**Title:** Continuity Arcs & Drift Direction

**Structure:**

- Board outline with:
  - Curved continuity arcs (blue/green/yellow/red)
  - Drift arrows indicating direction of flow
- Side notes:
  - “Drift alignment”  
  - “Continuity collapse”  
  - “Identity inversion”

**Purpose:**  
Shows how continuity and drift are visualized and interpreted.

---

## 7. Topology & Ancestry Diagram  
**Title:** Topology & Ancestry Map

**Structure:**

- Board with:
  - Cut points (red diamonds)  
  - Weak points (orange triangles)  
  - Ladder paths (blue lines)  
  - Ko nodes (purple circles)  
  - Moyo boundaries (green curves)
- Ancestry lines connecting sequences.

**Purpose:**  
Illustrates structural and ancestry features in one view.

---

## 8. Risk & Paradox Diagram  
**Title:** Paradox, Collapse, Projection‑Loss

**Structure:**

- Three zones on a board:
  - Paradox zone (orange warning)  
  - Collapse zone (red X)  
  - Projection‑loss zone (red/orange arcs)
- Side panel:
  - Risk Engine  
  - Severity levels

**Purpose:**  
Shows how triadic risk is localized and categorized.

---

## 9. Triadic Score HUD Diagram  
**Title:** Triadic HUD Layout

**Structure:**

- HUD panel with fields:
  - Local / Structural / Continuity scores  
  - Resonance stability  
  - Topology stability  
  - Ancestry stability  
  - Drift alignment  
  - Risk level  
  - Final triadic score
- Arrows from HUD back to board overlays.

**Purpose:**  
Defines the canonical triadic HUD structure.

---

## 10. Full Triadic View Diagram  
**Title:** Combined Triadic View

**Structure:**

- Board with all overlays active:
  - continuity arcs  
  - resonance fields  
  - drift arrows  
  - topology highlights  
  - ancestry lines  
  - risk indicators  
  - HUD
- Caption: “Full triadic identity of the position.”

**Purpose:**  
Represents the maximal triadic visualization state.

---

### Summary

The Triadic Diagram Set defines:

- operator stack  
- engine integration  
- MCTS hooks  
- overlay layers  
- continuity & drift  
- topology & ancestry  
- risk & paradox  
- triadic HUD  
- full triadic view  

These diagrams are the canonical visual language for RTT‑Go’s documentation and UI concept work—making the triadic structure of Go explicit and teachable.
