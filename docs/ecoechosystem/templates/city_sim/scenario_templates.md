# **City Scenario Templates**  
### *Reusable narrative and execution scaffolds for city‑scale simulation scenarios*

Scenarios are **structured stories** told through the simulation loop.  
They define *what happens*, *when it happens*, and *what pressures are applied* — without hard‑coding outcomes.

Scenario templates allow cities to be:
- compared across runs  
- stress‑tested under identical conditions  
- explored across alternate futures  
- used for training, policy testing, or research  

Scenarios turn the city from a model into a **laboratory**.

---

## **Purpose**
Scenario templates exist to:

- standardize how scenarios are defined and executed  
- separate narrative intent from simulation mechanics  
- enable replay, comparison, and branching futures  
- support crisis, growth, collapse, and recovery modeling  
- provide AI‑legible scenario structure  

Scenarios are **inputs**, not scripts.

---

## **Scenario as Substrate Expression**

Each scenario operates through the shared substrate:

- **Structure (S)** — which systems are stressed or altered  
- **Activation (E)** — how intensity is injected or dampened  
- **Relational Time (R)** — when events occur and how long effects persist  

Scenarios shape *conditions*, not *decisions*.

---

# **Canonical Scenario Template Structure**

Every scenario should follow this structure.

---

## **Scenario Identity**

**Scenario Name:**  
**Scenario Type:** growth / crisis / collapse / recovery / mixed  
**Primary Stress Domain(s):** infrastructure, population, economy, governance, information, inequality  
**Time Horizon:** short / medium / long  
**Replayable:** yes / no  

---

## **Narrative Intent**
Describe the high‑level story the scenario explores.

Examples:
- rapid growth under infrastructure strain  
- misinformation‑driven unrest  
- resource scarcity and governance response  
- inequality‑driven fragmentation  
- coordinated recovery after collapse  

This section is **human‑readable**, not executable.

---

## **Initial Conditions**
Define the starting state of the city.

Include:
- baseline regimes for each subsystem  
- resource stock levels  
- population activation state  
- governance legitimacy  
- inequality distribution  

Initial conditions anchor the scenario.

---

## **Trigger Events**
Define discrete events injected into the simulation.

Examples:
- infrastructure failure  
- economic shock  
- environmental event  
- policy change  
- information disruption  

Each trigger specifies:
- affected subsystem(s)  
- magnitude  
- timing  

---

## **Ongoing Pressures**
Define sustained forces applied over time.

Examples:
- prolonged resource scarcity  
- sustained misinformation  
- chronic underinvestment  
- demographic shift  

Ongoing pressures shape **trajectory**, not spikes.

---

## **Intervention Windows**
Define when interventions are allowed or expected.

Examples:
- early governance response window  
- late emergency intervention  
- recovery investment phase  

Intervention timing is often **more important than strength**.

---

## **Success & Failure Conditions**
Define scenario evaluation criteria.

Examples:
- stabilization achieved  
- collapse triggered  
- inequality reduced  
- legitimacy restored  

Outcomes are **observed**, not forced.

---

## **Metrics & Observables**
Specify what is tracked.

Examples:
- population stress index  
- economic volatility  
- infrastructure failure rate  
- trust and legitimacy  
- inequality persistence  

Metrics enable **comparison across runs**.

---

## **Branching Conditions (Optional)**
Define conditions that alter scenario flow.

Examples:
- if unrest exceeds threshold → emergency governance  
- if trust recovers → accelerated recovery  

Branching enables **non‑linear futures**.

---

## **Termination Conditions**
Define when the scenario ends.

Examples:
- time horizon reached  
- irreversible collapse  
- stable recovery achieved  

Termination is a **state**, not a timer.

---

# **Canonical Scenario Archetypes**

Common reusable scenario families include:

- Growth Under Strain  
- Infrastructure Shock  
- Resource Scarcity Crisis  
- Misinformation Cascade  
- Inequality Fracture  
- Governance Failure  
- Coordinated Recovery  

Each archetype can be parameterized.

---

# **Scenario Execution Flow**

Scenarios execute by:
1. Initializing city state  
2. Injecting triggers and pressures  
3. Running the city simulation loop  
4. Applying interventions when allowed  
5. Observing outcomes and metrics  

Scenarios **do not override** the simulation loop.

---

# **Integration Notes**

Scenario templates:
- sit above the city simulation loop  
- remain domain‑agnostic  
- enable comparison and learning  
- support AI‑driven exploration  

They are the **interface between intent and dynamics**.

---

# **Status**
Canonical city‑scale scenario template framework.  
Designed for extension by domain‑specific or narrative layers.
