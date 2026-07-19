# Simulation Engine  
*A structural simulation framework for the Governance Substrate Model (GSM)*

The simulation engine models stepwise structural movement across the GSM manifold. It integrates drift dynamics, cross‑axis physics, invariant tension, absorptive capacity, basin topology, regime modes, and phase discipline to generate plausible structural trajectories. It is not predictive; it explores the structural possibility space.

---

### Core purpose of the simulation engine

The engine enables:

- stepwise structural evolution  
- basin approach, departure, and crossing  
- drift amplification and dampening  
- regime‑mode transitions  
- phase‑honest structural sequences  
- scenario exploration for teaching and analysis  

It provides the backbone for interactive dashboards, Observer timelines, and structural scenario tools.

---

## Simulation inputs

The engine requires:

- **initial structural vector** `[C, M, O, A, T]`  
- **invariant status** and tension score  
- **physics forces** across axis pairs  
- **drift vector** and category  
- **basin classification** and boundary proximity  
- **awareness layers**  
- **absorptive strength**  
- **regime mode** and **phase state**  
- **projection rules** (optional)  

These inputs define the system’s starting structural conditions.

---

## Step engine

Each simulation step consists of:

1. **Evaluate invariants**  
   - classify aligned, tension, violated  
   - compute tension score  

2. **Apply physics forces**  
   - compute compensatory movement  
   - detect destabilizing forces  

3. **Compute drift**  
   - update drift vector  
   - classify drift category  
   - apply drift amplification or dampening  

4. **Update structural vector**  
   - apply drift and compensatory deltas  
   - clamp to manifold boundaries  

5. **Recompute basin position**  
   - nearest basin  
   - basin distance  
   - boundary proximity  
   - stability score  

6. **Evaluate regime mode**  
   - stable, tension, drift, compensatory, transition, absorptive, fragmentation, reconstruction  

7. **Evaluate phase discipline**  
   - stable phase  
   - tension phase  
   - drift phase  
   - transition phase  
   - reconstruction phase  

8. **Generate step event**  
   - alignment, tension, drift, transition, or regime‑shift event  

9. **Record step in simulation log**  

Each step produces a new structural state.

---

## Drift engine integration

The simulation engine uses the drift engine to:

- compute drift magnitude  
- classify drift category  
- detect directional consistency  
- identify regime‑shift drift  
- evaluate absorptive dampening  

Drift determines whether the system stabilizes, moves, or transitions.

---

## Physics engine integration

Cross‑axis physics governs:

- compensatory movement  
- tension accumulation  
- drift amplification  
- destabilization thresholds  

Physics forces determine whether drift is corrected or amplified.

---

## Basin engine integration

The basin engine provides:

- nearest basin  
- basin distance  
- stability gradients  
- boundary proximity  
- transition thresholds  

Basin topology determines whether the system stabilizes or transitions.

---

## Regime‑mode integration

Regime modes interpret operational behavior:

- **stable** — aligned, low drift  
- **tension** — rising strain  
- **drift** — directional movement  
- **compensatory** — physics correction  
- **transition** — basin crossing  
- **absorptive** — buffering  
- **fragmentation** — structural breakdown  
- **reconstruction** — re‑anchoring  

Modes provide behavioral context for each step.

---

## Phase discipline integration

Phase discipline ensures phase‑honest transitions:

- stable → tension → drift → transition → reconstruction  
- no skipping phases unless drift is regime‑shift  
- structural debt accumulates if exit conditions are ignored  

Phases provide structural coherence across steps.

---

## Projection integration

The simulation engine can optionally use projection rules to:

- extend drift vectors  
- estimate basin trajectories  
- compute transition likelihood  
- forecast absorptive strength  
- project regime‑mode sequences  

Projections guide scenario exploration.

---

## Simulation outputs

Each simulation run produces:

- **stepwise structural states**  
- **drift sequences**  
- **basin trajectories**  
- **regime‑mode sequences**  
- **phase sequences**  
- **transition events**  
- **regime‑shift events**  
- **narrative summaries**  

These outputs feed the Observer and dashboards.

---

## Simulation log schema

Each step is recorded as:

```yaml
step:
  step_id: <number>
  vector: [C, M, O, A, T]
  drift:
    vector: [dC, dM, dO, dA, dT]
    magnitude: <number>
    category: <micro|meso|macro|regime_shift>
  physics_forces:
    - axis_pair: <C↔O | M↔A | O↔T>
      magnitude: <number>
      direction: <positive|negative>
  invariants:
    aligned: [...]
    tension: [...]
    violated: [...]
    tension_score: <number>
  basin:
    nearest: <CPL|CPF|CTR|PCL|HCL>
    distance: <number>
    boundary_proximity: <number>
    stability_score: <number>
  regime_mode: <mode>
  phase_state: <phase>
  absorptive_strength: <number>
  events: [...]
```

---

## Simulation modes

The engine supports:

- **deterministic mode** — fixed rules, no randomness  
- **stochastic mode** — controlled variation in drift and physics  
- **scenario mode** — user‑defined interventions  
- **counterfactual mode** — alternate structural histories  

These modes support teaching, analysis, and exploration.

---

## Narrative engine integration

The simulation engine generates:

- structural narratives  
- drift narratives  
- basin narratives  
- transition narratives  
- regime‑shift narratives  

Narratives make simulations interpretable for humans.
