# Simulation Scenarios  
*A catalog of structural scenarios for the GSM Simulation Engine*

Simulation scenarios define **starting conditions**, **structural constraints**, and **exploration goals** for running simulations in the Governance Substrate Model (GSM). They allow analysts, students, and contributors to explore how systems evolve under different tensions, drift pressures, basin positions, and awareness configurations.

Scenarios are not predictions—they are structured explorations of the possibility space.

---

## Scenario structure

Each scenario includes:

- **scenario_id** — unique identifier  
- **title** — human‑readable name  
- **description** — purpose and context  
- **initial_vector** — starting [C, M, O, A, T]  
- **initial_conditions** — invariants, drift, physics, awareness, absorptive strength  
- **constraints** — fixed or variable parameters  
- **goals** — what the scenario is meant to explore  
- **expected_patterns** — typical structural behaviors  
- **termination_conditions** — when the simulation stops  

This structure ensures consistency across teaching, analysis, and research.

---

## Core scenario types

### 1. Stable Basin Scenario  
Explores how a system behaves when starting deep inside a basin with low tension.

- **Purpose** — demonstrate stability, micro‑drift, and compensatory physics  
- **Initial vector** — near basin centroid  
- **Expected patterns** — low drift, high coherence, stable regime mode  
- **Termination** — fixed number of steps or stability plateau  

---

### 2. Rising Tension Scenario  
Models invariant strain and cross‑axis imbalance.

- **Purpose** — show how tension accumulates and triggers drift  
- **Initial vector** — near basin edge with rising tension  
- **Expected patterns** — tension → drift → compensatory mode  
- **Termination** — drift category reaches *meso*  

---

### 3. Drift Escalation Scenario  
Focuses on directional movement driven by physics forces.

- **Purpose** — illustrate drift amplification and directional consistency  
- **Initial vector** — moderate imbalance across C↔O or M↔A  
- **Expected patterns** — meso drift, possible transition approach  
- **Termination** — boundary proximity > 0.7  

---

### 4. Basin Transition Scenario  
Simulates crossing from one basin to another.

- **Purpose** — teach basin topology and transition thresholds  
- **Initial vector** — near boundary with high drift pressure  
- **Expected patterns** — drift → transition → reconstruction  
- **Termination** — new basin stability_score > 0.5  

---

### 5. Regime‑Shift Scenario  
Models rare, high‑energy structural reconfiguration.

- **Purpose** — demonstrate regime‑shift detection and nonlinear movement  
- **Initial vector** — high tension, macro drift, weak absorptive strength  
- **Expected patterns** — destabilization → basin crossing → re‑anchoring  
- **Termination** — regime_shift_detected == true  

---

### 6. Absorptive Recovery Scenario  
Explores how systems stabilize after tension or drift.

- **Purpose** — show absorptive dampening and return to stability  
- **Initial vector** — moderate tension, strong absorptive structures  
- **Expected patterns** — drift dampening → tension reduction → stable mode  
- **Termination** — coherence_score > 70  

---

### 7. Fragmentation Scenario  
Models structural breakdown and loss of coherence.

- **Purpose** — illustrate invariant violations and physics destabilization  
- **Initial vector** — multiple invariant violations, low oversight/timing coherence  
- **Expected patterns** — fragmentation → reconstruction or collapse  
- **Termination** — reconstruction_phase_entered  

---

### 8. Counterfactual Scenario  
Allows analysts to explore “what if” structural histories.

- **Purpose** — compare alternate structural paths  
- **Initial vector** — user‑defined  
- **Constraints** — fixed or variable depending on the counterfactual  
- **Termination** — user‑defined  

---

## Scenario definition template

```yaml
scenario:
  scenario_id: "<unique_id>"
  title: "<scenario_name>"
  description: "<purpose_and_context>"
  initial_vector:
    C: <number>
    M: <number>
    O: <number>
    A: <number>
    T: <number>
  initial_conditions:
    invariants:
      aligned: [...]
      tension: [...]
      violated: [...]
    drift:
      vector: [...]
      magnitude: <number>
      category: "<micro|meso|macro|regime_shift>"
    physics_forces:
      - axis_pair: "<C↔O | M↔A | O↔T>"
        magnitude: <number>
        direction: "<positive|negative>"
    awareness_layers:
      structural: <0–10>
      procedural: <0–10>
      historical: <0–10>
      anticipatory: <0–10>
      relational: <0–10>
    absorptive_strength: <0–1>
    regime_mode: "<mode>"
    phase_state: "<phase>"
  constraints:
    fixed_parameters: [...]
    variable_parameters: [...]
  goals:
    - "<goal_1>"
    - "<goal_2>"
  expected_patterns:
    - "<pattern_1>"
    - "<pattern_2>"
  termination_conditions:
    - "<condition_1>"
    - "<condition_2>"
```

---

## How scenarios integrate with the Analyzer

Scenarios plug directly into:

- **Simulation Engine** — stepwise structural evolution  
- **Projection Rules** — drift and basin trajectory forecasting  
- **Regime Modes** — operational behavior classification  
- **Phase Discipline** — phase‑honest transitions  
- **Observer Layer** — history/now/future interpretation  
- **Dashboards** — scenario visualization  

This ensures every scenario is structurally coherent and analytically meaningful.
