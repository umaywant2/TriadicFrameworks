# Alignment Analyzer  
*A structural interpretation engine for governance systems within the GSM*

The Alignment Analyzer evaluates governance systems, statements, and historical profiles by mapping them into the five‑axis structural vector, checking them against GSM invariants, applying cross‑axis physics, and determining basin alignment and drift tendencies. It is the core reasoning module that transforms raw descriptions into structural insight.

---

## Purpose of the Analyzer

The Analyzer determines:

- the structural vector of a system  
- its alignment with GSM invariants  
- its coherence across axes  
- its nearest equilibrium basin  
- its drift direction and magnitude  
- its likely transition pathways  

This allows students, developers, and researchers to interpret governance systems using a unified structural language.

---

## Input Types

The Analyzer accepts several forms of input:

- **Natural‑language descriptions** of governance systems or reforms  
- **Structural vectors** (`[C, M, O, A, T]`)  
- **Historical profiles** (single or multi‑snapshot)  
- **Reform proposals**  
- **Simulation scenarios**  

All inputs are normalized into a structural vector before analysis.

---

## Core Components

### Structural Vectorizer
Converts natural‑language descriptions into the five‑axis vector:

- **C** — Centralization  
- **M** — Method  
- **O** — Oversight  
- **A** — Access  
- **T** — Timing  

Mapping rules are defined in `statement_mapping_rules.yaml`.

### Invariant Checker
Evaluates the vector against GSM invariants:

- behavioral invariants  
- awareness layers  
- absorptive structures  
- regime‑mode constraints  
- phase‑discipline rules  

Logic defined in `invariant_check_rules.yaml`.

### Cross‑Axis Physics Engine
Applies structural forces that shape drift:

- centralization ↔ oversight  
- method ↔ access  
- oversight ↔ timing  
- method ↔ centralization  
- access ↔ oversight  

Physics rules defined in `governance_physics.yaml`.

### Basin Classifier
Determines the nearest equilibrium basin:

- CPL — Competitive–Plurality  
- CPF — Competitive–Preferential  
- CTR — Competitive–Two‑Round  
- PCL — Proportional–Coalition  
- HCL — Hierarchical–Centralized  

Basin definitions in `equilibrium_basins.yaml`.

### Drift Detector
Computes:

- drift vector  
- drift magnitude  
- active forces  
- structural tension  
- basin approach or departure  

Logic defined in `drift_detection.yaml`.

### Transition Pathway Engine
Uses the transition graph to determine:

- lowest‑cost basin transitions  
- intermediate states  
- structural coherence of transitions  

Defined in `transition_graph.yaml`.

---

## Analyzer Pipeline

The Analyzer follows a consistent pipeline:

1. **Normalize input**  
2. **Vectorize**  
3. **Check invariants**  
4. **Apply physics**  
5. **Classify basin**  
6. **Compute drift**  
7. **Evaluate transitions**  
8. **Generate narrative output**

Pipeline defined in `analyzer_pipeline.yaml`.

---

## Outputs

The Analyzer produces:

- normalized structural vector  
- invariant alignment report  
- coherence score  
- drift vector and active forces  
- nearest basin  
- transition pathway  
- structural narrative  

These outputs feed into the Transition Simulator, dashboards, and teaching tools.

---

## Integration with GSM

The Analyzer depends on:

- **governance_manifold.yaml**  
- **governance_physics.yaml**  
- **equilibrium_basins.yaml**  
- **transition_graph.yaml**  
- **absorptive_structures.yaml**  
- **behavioral_invariants.yaml**  
- **awareness_layers.yaml**  

It is the interpretive layer that connects the substrate to applications.

---

## Example Use Cases

- mapping a historical system into the manifold  
- evaluating the coherence of a reform proposal  
- detecting drift between two eras  
- comparing two governance systems structurally  
- generating student‑friendly narratives  
- feeding vectors into the transition simulator  

---

## Developer Notes

- All logic must remain **non‑ideological** and **structure‑first**.  
- Changes to invariants, physics, or basins require updates across dependent modules.  
- Mapping rules should be transparent and explainable.  
- Narrative output should be readable by students and educators.  
