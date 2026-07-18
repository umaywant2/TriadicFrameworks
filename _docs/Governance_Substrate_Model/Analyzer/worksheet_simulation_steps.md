# Worksheet: Simulation Steps  
*A guided exercise for running step‑by‑step GSM simulations*

This worksheet helps students practice evaluating structural states, computing drift, interpreting physics forces, classifying regime modes, and determining transitions. It is designed for classroom use, workshops, and self‑guided learning.

---

## 1. Starting structural state

Record the initial vector and metadata.

```yaml
initial_state:
  vector: [C, M, O, A, T]
  invariants:
    aligned: [...]
    tension: [...]
    violated: [...]
    tension_score: <number>
  drift:
    vector: [0, 0, 0, 0, 0]
    magnitude: 0
    category: micro
  physics_forces: [...]
  basin:
    nearest_basin: <CPL|CPF|CTR|PCL|HCL>
    basin_distance: <number>
    boundary_proximity: <number>
    stability_score: <number>
  regime_mode: <mode>
  phase_state: <phase>
  absorptive_strength: <0–1>
  notes: "<context>"
```

---

## 2. Step evaluation template

Use this template for each simulation step.

### Step N

```yaml
step_N:
  input_vector: [C, M, O, A, T]

  # 1. Invariant evaluation
  invariants:
    aligned: [...]
    tension: [...]
    violated: [...]
    tension_score: <number>

  # 2. Physics forces
  physics_forces:
    - axis_pair: "<C↔O | M↔A | O↔T>"
      magnitude: <number>
      direction: "<positive|negative>"

  # 3. Drift computation
  drift:
    vector: [dC, dM, dO, dA, dT]
    magnitude: <number>
    category: "<micro|meso|macro|regime_shift>"

  # 4. Updated structural vector
  updated_vector: [C', M', O', A', T']

  # 5. Basin classification
  basin:
    nearest_basin: <CPL|CPF|CTR|PCL|HCL>
    basin_distance: <number>
    boundary_proximity: <number>
    stability_score: <number>

  # 6. Regime mode
  regime_mode: "<mode>"

  # 7. Phase state
  phase_state: "<phase>"

  # 8. Events
  events:
    - type: "<alignment|tension|drift|transition|regime_shift|reconstruction>"
      summary: "<short description>"

  # 9. Narrative
  narrative:
    summary: "<short interpretation>"
    highlights:
      - "<key insight>"
      - "<key insight>"
```

---

## 3. Step‑by‑step practice sequence

Students repeat the template for each step.

### Step 1  
Evaluate invariants → physics → drift → basin → mode → phase → events → narrative.

### Step 2  
Use the updated vector from Step 1 as the new input.

### Step 3  
Continue until a transition, reconstruction, or stabilization occurs.

---

## 4. Transition checkpoints

At each step, check for:

- **tension rise** (tension_score > 3)  
- **drift escalation** (meso → macro → regime_shift)  
- **boundary proximity** (> 0.7)  
- **absorptive failure** (< 0.3)  
- **invariant violations** (≥ 2)  
- **regime mode changes**  
- **phase transitions**  

These checkpoints help determine whether the system is stabilizing, escalating, or transitioning.

---

## 5. End‑of‑simulation summary

After completing all steps, fill out:

```yaml
simulation_summary:
  total_steps: <number>
  final_vector: [C, M, O, A, T]
  final_basin: <CPL|CPF|CTR|PCL|HCL>
  final_regime_mode: <mode>
  final_phase_state: <phase>
  cumulative_drift: <number>
  invariant_violations: <number>
  transitions_detected: <number>
  regime_shifts_detected: <number>
  narrative:
    - "<summary insight>"
    - "<summary insight>"
```

---

## 6. Reflection prompts

- What forces drove the system’s movement?  
- Where did tension accumulate?  
- How did drift evolve across steps?  
- Did the system approach or cross a basin boundary?  
- Which regime modes appeared, and why?  
- Was the transition phase‑honest?  
- What structural narrative emerges from the sequence?

These prompts help students build structural intuition.
