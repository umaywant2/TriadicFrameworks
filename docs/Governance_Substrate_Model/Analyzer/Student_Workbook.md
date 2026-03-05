A complete **student workbook** for the GSM should feel like a guided journey: it teaches concepts in the order students naturally absorb them, gives them space to practice, and reinforces structural literacy through diagrams, examples, and reflection. What follows is a full, ready‑to‑paste workbook that pairs directly with your *student profile*, *teacher guide*, *simulation worksheets*, and the Analyzer architecture you’ve built.

---

# Governance Substrate Model  
## Student Workbook  
*A guided learning path for structural literacy*

This workbook helps learners build intuition for the GSM through structured lessons, diagrams, examples, and hands‑on exercises. It is designed for classroom use, workshops, and self‑guided study.

---

## 1. Orientation  
### What the GSM teaches  
The GSM helps you see governance as a **structural system**—not a set of opinions or policies. You learn to read structure the way a musician reads notation or a physicist reads a diagram.

### What you will learn  
- How to construct and interpret structural vectors  
- How invariants shape stability and tension  
- How physics forces create movement  
- How drift emerges and escalates  
- How basins define structural identity  
- How regime modes and phases describe behavior  
- How to read history, now, and future through the Observer  
- How to run and interpret simulations  

---

## 2. Your Student Profile  
Before starting, fill out your profile.

```yaml
student_profile:
  name: "<your_name>"
  date: "<today>"
  background:
    governance_experience: "<none|basic|intermediate|advanced>"
    analytical_experience: "<none|basic|intermediate|advanced>"
    modeling_experience: "<none|basic|intermediate|advanced>"
  foundational_understanding:
    structural_vectors: "<unfamiliar|emerging|competent|confident>"
    invariants: "<unfamiliar|emerging|competent|confident>"
    physics_forces: "<unfamiliar|emerging|competent|confident>"
    drift_categories: "<unfamiliar|emerging|competent|confident>"
    basins: "<unfamiliar|emerging|competent|confident>"
    regime_modes: "<unfamiliar|emerging|competent|confident>"
    phase_discipline: "<unfamiliar|emerging|competent|confident>"
    observer_lenses: "<unfamiliar|emerging|competent|confident>"
```

---

## 3. Lesson 1 — Structural Vectors  
### Concept  
The GSM uses five axes: **C, M, O, A, T**.  
A structural vector is:

```
[C, M, O, A, T]
```

### Diagram  
```
C — Centralization
M — Methods
O — Oversight
A — Access
T — Timing
```

### Guided Example  
Statement: *“Decision-making should be unified and fast.”*  
- Centralization ↑  
- Timing ↑  
- Oversight (implicit) → slight ↑  

Mapped vector (normalized):  
```
[0.78, 0.40, 0.55, 0.32, 0.72]
```

### Exercise  
Map these statements into vectors:  
1. “Participation should be broad and transparent.”  
2. “We need stricter review before acting.”  
3. “Teams should compete openly for solutions.”

Record your answers here:

```yaml
vector_exercises:
  - statement: ""
    vector: [C, M, O, A, T]
  - statement: ""
    vector: [C, M, O, A, T]
  - statement: ""
    vector: [C, M, O, A, T]
```

---

## 4. Lesson 2 — Invariants  
### Concept  
Invariants are structural rules that must remain coherent. They can be:  
- **aligned**  
- **in tension**  
- **violated**

### Diagram  
```
Aligned → stable  
Tension → strain  
Violated → breakdown risk
```

### Guided Example  
Vector: `[0.82, 0.40, 0.33, 0.28, 0.71]`  
- C high, O low → C↔O tension  
- O low, T high → O↔T tension  

### Exercise  
Identify aligned, tension, and violated invariants for three vectors of your choice.

---

## 5. Lesson 3 — Physics Forces  
### Concept  
Cross‑axis physics creates movement:  
- **C↔O**  
- **M↔A**  
- **O↔T**

### Diagram  
```
C ↔ O   (authority vs oversight)
M ↔ A   (methods vs access)
O ↔ T   (oversight vs timing)
```

### Exercise  
For each pair, describe a real‑world example of imbalance.

---

## 6. Lesson 4 — Drift  
### Concept  
Drift is structural movement.  
Categories:  
- micro  
- meso  
- macro  
- regime_shift

### Guided Example  
Delta: `[0.12, 0.08, 0.15, 0.04, 0.10]` → magnitude ≈ meso.

### Exercise  
Compute drift magnitude for three deltas.

---

## 7. Lesson 5 — Basins  
### Concept  
Basins represent structural identities:  
- CPL  
- CPF  
- CTR  
- PCL  
- HCL

### Diagram  
A simple 2D projection of basin regions.

### Exercise  
Given three vectors, identify nearest basin and boundary proximity.

---

## 8. Lesson 6 — Regime Modes  
### Concept  
Modes describe operational behavior:  
stable → tension → drift → compensatory → transition → reconstruction

### Exercise  
Given a structural state, classify its regime mode.

---

## 9. Lesson 7 — Phase Discipline  
### Concept  
Phases enforce structural coherence:  
stable_phase → tension_phase → drift_phase → transition_phase → reconstruction_phase

### Exercise  
Given a sequence of states, identify phase transitions and structural debt.

---

## 10. Lesson 8 — Observer Lenses  
### Concept  
The Observer tracks:  
- **history**  
- **now**  
- **future**

### Exercise  
Record a history of three states and write a narrative for each.

---

## 11. Lesson 9 — Simulation Steps  
Use the worksheet template to run a 3–5 step simulation.

### Exercise  
Fill out:

```yaml
simulation_run:
  steps:
    - step_1: {...}
    - step_2: {...}
    - step_3: {...}
```

---

## 12. Lesson 10 — Scenario Exploration  
Choose a scenario:  
- stable basin  
- rising tension  
- drift escalation  
- basin transition  
- regime shift  
- absorptive recovery  
- fragmentation  
- counterfactual

### Exercise  
Run the scenario and write a structural narrative.

---

## 13. Reflection  
### What you learned  
Write 3–5 insights about structural movement.

### What you want to explore next  
Add 1–2 questions or goals.

---

## 14. Instructor Feedback  
Space for comments, guidance, and next steps.

---

# Complete **multi‑file student kit** 

Works best when each file has a single, clear purpose, and together they form a coherent learning arc: *orientation → concepts → practice → simulation → reflection*. What follows is a full kit you can drop directly into your `/Governance_Substrate_Model/Analyzer/` directory. Each file is self‑contained, printable, and cross‑linked.

Organized the kit into **eight files**, each with diagrams (ASCII‑safe), filled examples, and worksheets.

---

# 1. `workbook_overview.md`  
*A map of the entire learning journey*

## Purpose  
Gives students a clear path through the GSM curriculum and how each file fits together.

## Contents  
- What the GSM teaches  
- How to use the student kit  
- Recommended order  
- Time estimates  
- Cross‑links to all other files  

## Diagram — GSM Learning Arc  
```
Vectors → Invariants → Physics → Drift → Basins → Modes → Phases → Observer → Simulation
```

---

# 2. `lesson_structural_vectors.md`  
*Concepts, diagrams, examples, and exercises*

## Diagram — The Five Axes  
```
C — Centralization
M — Methods
O — Oversight
A — Access
T — Timing
```

## Filled Example  
Statement: “Decision-making should be unified and fast.”  
Mapped vector:  
```
[0.78, 0.40, 0.55, 0.32, 0.72]
```

## Exercises  
- Map 5 statements  
- Identify implicit structural claims  
- Normalize raw values  

---

# 3. `lesson_invariants_and_physics.md`  
*How stability, tension, and forces shape structure*

## Diagram — Invariant States  
```
Aligned → stable
Tension → strain
Violated → breakdown risk
```

## Diagram — Physics Forces  
```
C ↔ O   (authority vs oversight)
M ↔ A   (methods vs access)
O ↔ T   (oversight vs timing)
```

## Filled Example  
Vector: `[0.82, 0.40, 0.33, 0.28, 0.71]`  
- C↔O tension  
- O↔T tension  

## Exercises  
- Evaluate invariants for 3 vectors  
- Identify physics forces in 3 scenarios  

---

# 4. `lesson_drift_and_basins.md`  
*Movement, magnitude, categories, and topology*

## Diagram — Drift Categories  
```
micro < meso < macro < regime_shift
```

## Drift Example  
Delta: `[0.12, 0.08, 0.15, 0.04, 0.10]` → meso

## Diagram — Basin Map (ASCII)  
```
   CPF      CTR      CPL
     \       |       /
      \      |      /
       PCL---+---HCL
```

## Exercises  
- Compute drift magnitude  
- Classify drift category  
- Identify nearest basin  

---

# 5. `lesson_modes_and_phases.md`  
*Operational behavior and structural sequencing*

## Diagram — Regime Modes  
```
stable → tension → drift → compensatory → transition → reconstruction
```

## Diagram — Phase Discipline  
```
stable_phase → tension_phase → drift_phase → transition_phase → reconstruction_phase
```

## Filled Example  
Given a state with:  
- tension_score = 5  
- drift_category = micro  
→ regime mode = tension

## Exercises  
- Classify 5 regime modes  
- Identify phase transitions in a sequence  

---

# 6. `observer_practice.md`  
*History, now, future lenses with examples*

## Diagram — Triadic Observer  
```
History ← Now → Future
```

## Filled Example  
History record:  
```
vector: [0.45, 0.52, 0.47, 0.50, 0.48]
mode: stable
```

Future projection:  
```
vector: [0.52, 0.55, 0.50, 0.48, 0.53]
likelihood: 0.62
```

## Exercises  
- Create 3 history records  
- Write narratives for each lens  
- Compare two futures  

---

# 7. `simulation_workbook.md`  
*A full simulation practice file with filled examples*

## Step‑by‑Step Example (filled)  
### Step 1  
```
input_vector: [0.60, 0.50, 0.55, 0.40, 0.45]
drift: micro
tension_score: 2
mode: stable
```

### Step 2  
```
input_vector: [0.68, 0.52, 0.48, 0.38, 0.52]
drift: meso
tension_score: 4
mode: tension
```

### Step 3  
```
boundary_proximity: 0.72
mode: transition
```

## Blank Worksheets  
- 5‑step simulation template  
- Transition checkpoints  
- Narrative summary  

---

# 8. `student_profile_and_reflection.md`  
*Profile, goals, logs, and reflection*

## Profile (from earlier)  
Students fill out background, skills, and goals.

## Practice Log  
```
- exercise_id: V1
  type: vector
  notes: "C↔O tension was easier to see than M↔A."
```

## Reflection Prompts  
- What patterns did you notice?  
- Where did drift escalate?  
- How did basin topology influence movement?  

---

# How these files work together  
- **Lessons** teach concepts.  
- **Diagrams** build intuition.  
- **Filled examples** show correct reasoning.  
- **Worksheets** give practice.  
- **Profile + reflection** track growth.  
- **Simulation workbook** ties everything together.  

This kit becomes a complete, printable, classroom‑ready package.
