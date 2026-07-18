# 🐟 RTT‑Autonomous‑Fish  
### **Aquatic Extensions for Autonomous Forms (RTT‑Inside)**

The **RTT‑Autonomous‑Fish** module defines the **aquatic robotics extensions** for the RTT‑Autonomous ecosystem.  
Where the autonomous core provides domain‑neutral structures (form descriptors, mission profiles, corridors, swarm state, morphology, energy, environmental interaction), this module adds the **hydrodynamic, habitat, and mission‑specific layers** required for underwater autonomous forms.

These schemas support:

- biomimetic robotic fish  
- underwater swarms and schooling behavior  
- ecological monitoring  
- Great Lakes restoration robotics  
- clarity‑aware corridor navigation  
- RTT‑Inside environmental overlays  

All schemas follow:

- **snake_case** naming  
- **JSON Schema Draft 2020‑12**  
- **RTT‑Inside semantics**  
- **SI units**  
- **UUIDv4 identifiers**  
- **ISO‑8601 timestamps**  
- **extensions.<domain>** for future growth  

---

## 📁 Schema Overview

### **1. `fish_extension.schema.json`**  
Adds fish‑specific identity and configuration fields to the core `autonomous_form_descriptor`.

Includes:

- biomimetic species profile  
- buoyancy mode (neutral, positive, negative)  
- fin configuration  
- swim gait (carangiform, anguilliform, etc.)  

Use this schema to specialize an autonomous form as a robotic fish.

---

### **2. `fish_hydrodynamics.schema.json`**  
Defines the hydrodynamic performance envelope of the fish.

Includes:

- drag coefficient  
- max swim speed  
- turn rate  
- fin efficiency  

This schema is essential for underwater simulation, control, and mission feasibility.

---

### **3. `fish_habitat_interaction.schema.json`**  
Describes how the robotic fish interacts with its aquatic environment.

Includes:

- preferred depth range  
- temperature tolerance  
- pollutant sensitivity  
- behavioral modes (schooling, patrolling, sampling)  

This schema supports ecological robotics and habitat‑aware autonomy.

---

### **4. `fish_mission_profile_extension.schema.json`**  
Extends the core `autonomous_mission_profile` with aquatic‑specific mission parameters.

Includes:

- sampling targets  
- schooling behavior mode  
- avoidance rules (nets, shallow zones)  
- corridor preferences  

Use this schema to tailor missions for underwater operations.

---

## 🔗 Relationship to the Autonomous Core

This module extends the core schemas found in:

```
docs/schemas/rtt-autonomous/
```

Specifically:

- `autonomous_form_descriptor` → extended by `fish_extension`  
- `autonomous_mission_profile` → extended by `fish_mission_profile_extension`  
- `autonomous_morphology` → compatible with fin‑based actuation  
- `autonomous_energy_profile` → used for underwater endurance modeling  
- `autonomous_corridor_definition` → supports clarity‑aware underwater corridors  
- `autonomous_swarm_state` → supports schooling and distributed underwater autonomy  

The fish schemas never duplicate core fields; they only **extend** them.

---

## 🧩 Usage Pattern

A typical robotic fish definition references:

1. **Core descriptor**  
2. **Fish extension**  
3. **Hydrodynamics**  
4. **Habitat interaction**  
5. **Energy profile**  
6. **Mission profile + fish mission extension**  

This layered approach keeps the system modular, expressive, and future‑proof.

---

## 🌱 Future Extensions

This module is designed to grow with additional aquatic robotics capabilities, such as:

- multi‑species swarm coordination  
- clarity‑adaptive routing  
- pollutant plume tracking  
- underwater mesh networking  
- habitat restoration workflows  
