# 🧩 **SimConnect Adapter (Simulation‑Only)**

This document describes how **Resonance Time Theory (RTT)** can be prototyped safely inside a flight simulator environment such as **Microsoft Flight Simulator (MSFS)** using **SimConnect**.

This adapter is a *sandbox interface* — a way to listen to telemetry, compute coherence, detect drift, and generate advisories **without touching real aircraft systems**.

---

# 🎯 **Purpose**

The SimConnect Adapter allows RTT to:

- listen to aircraft telemetry  
- compute multi‑domain coherence  
- detect drift early  
- classify structural patterns  
- generate advisory messages  
- log events for later analysis  

This is a **prototype‑only** environment.  
It is not intended for real‑world flight operations.

---

# 🧭 **1. Architecture Overview**

RTT in simulation uses three layers:

### **1. Telemetry Listener (SimConnect Input Layer)**  
Collects raw data from the simulator:
- aircraft body signals  
- environmental forcing  
- pilot/automation intent  

### **2. Coherence Engine (RTT Logic Layer)**  
Applies RTT’s structural model:
- domain alignment  
- drift detection  
- timing windows  
- forcing thresholds  
- reintegration cues  

### **3. Advisory Output (Sim‑Safe Feedback Layer)**  
Outputs:
- coherence score  
- drift classification  
- advisory messages  
- event logs  

This keeps the simulation loop clean and modular.

---

# 📡 **2. Data Channels**

Below are the recommended SimConnect variables for each RTT domain.

## **2.1 Aircraft Body Domain**
- `PLANE PITCH DEGREES`  
- `PLANE BANK DEGREES`  
- `PLANE HEADING DEGREES TRUE`  
- `VERTICAL SPEED`  
- `AIRSPEED INDICATED`  
- `G FORCE`  
- `ROTATION VELOCITY BODY X/Y/Z`  
- `ENGINE TORQUE`  
- `ENGINE THRUST`  

These signals describe how the airplane “feels.”

---

## **2.2 Environmental Domain**
- `AMBIENT WIND VELOCITY`  
- `AMBIENT WIND DIRECTION`  
- `AMBIENT TEMPERATURE`  
- `AMBIENT PRESSURE`  
- `TURBULENCE ACTIVE`  
- `ICING LEVEL`  

These signals describe what the sky is doing.

---

## **2.3 Pilot/Automation Domain**
- `AUTOPILOT MASTER`  
- `AUTOPILOT MODE`  
- `AUTOPILOT PITCH HOLD`  
- `AUTOPILOT HEADING LOCK`  
- `YOKE POSITION`  
- `RUDDER POSITION`  
- `THROTTLE POSITION`  

These signals describe what the human or computer is trying to do.

---

# 🔍 **3. Coherence Computation**

The adapter computes a **coherence score** using RTT’s three‑domain model:

- **Body–Environment alignment**  
- **Body–Intent alignment**  
- **Environment–Intent alignment**  
- **Timing window health**  
- **Forcing thresholds**  
- **Resonance patterns**  

The output is a single coherence value (0–100) plus domain‑level sub‑scores.

This score is not a safety rating — it is a **clarity indicator**.

---

# 🌀 **4. Drift Classification**

The adapter classifies drift into:

- **Soft Drift** — small mismatches  
- **Hard Drift** — growing mismatches  
- **Cross‑Domain Drift** — domains disagree  
- **Intent Mismatch** — pilot vs. automation  
- **Regime Boundary Violation** — sudden mode change  

Each drift event is logged with:
- timestamp  
- domain signals  
- drift type  
- coherence score  
- advisory text  

---

# 🔔 **5. Advisory Output**

Advisories are simulation‑safe messages such as:

- “Sky forcing rising — adjust workload.”  
- “Intent mismatch detected — clarify control authority.”  
- “Asymmetric forcing — verify engine performance.”  
- “Sensor disagreement — cross‑check airspeed.”  

These appear in:
- console output  
- on‑screen debug text  
- log files  

No control inputs are modified.  
No automation is overridden.  
This is strictly observational.

---

# 🧪 **6. Logging and Analysis**

The adapter logs:
- coherence score stream  
- drift events  
- domain signals  
- reintegration cues  

These logs can be used to:
- replay scenarios  
- tune thresholds  
- visualize drift  
- test new RTT logic  

This is where the real learning happens.

---

# 🛑 **7. Safety and Scope**

This module is:
- **simulation‑only**  
- **non‑certified**  
- **non‑interfering**  
- **for research and education**  

It must **never** be used in real aircraft or real‑world flight operations.
