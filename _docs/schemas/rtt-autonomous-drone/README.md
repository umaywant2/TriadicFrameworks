# 🛸 RTT‑Autonomous‑Drone  
### **Domain Extensions for Aerial Autonomous Forms (RTT‑Inside)**

This module defines the **drone‑specific schema extensions** for the RTT‑Autonomous ecosystem.  
Where the **autonomous core** provides domain‑neutral structures (form descriptors, mission profiles, corridors, swarm state, morphology, energy, environmental interaction), this folder adds the **aerial robotics layer**.

These schemas describe the capabilities, constraints, and mission‑level behaviors of autonomous drones operating in airspace, including multirotors, fixed‑wing aircraft, and VTOL hybrids.

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

### **1. `drone_extension.schema.json`**  
Defines the drone‑specific identity and configuration fields that extend the core `autonomous_form_descriptor`.

Includes:

- frame type (quadcopter, hexacopter, fixed‑wing, VTOL)  
- propulsion type (electric, hybrid, fuel)  
- GPS capability (RTK, standard, none)  
- failsafe modes (RTL, hover, land)  

Use this schema when instantiating a drone as a specialized autonomous form.

---

### **2. `drone_flight_envelope.schema.json`**  
Describes the aerodynamic and performance limits of the drone.

Includes:

- max speed  
- climb/descent rates  
- wind resistance  
- stall speed (for fixed‑wing)  
- roll/pitch tilt limits  

This schema is essential for simulation, mission planning, and safety validation.

---

### **3. `drone_energy_and_battery.schema.json`**  
Defines the drone’s energy profile and thermal constraints.

Includes:

- battery capacity  
- battery health  
- average/peak power draw  
- thermal envelope  

This schema supports endurance prediction, mission feasibility checks, and energy‑aware autonomy.

---

### **4. `drone_mission_profile_extension.schema.json`**  
Adds drone‑specific mission parameters to the core `autonomous_mission_profile`.

Includes:

- altitude constraints  
- geofence zones  
- payload type + mass  
- landing behavior (precision, RTL, auto‑land)  

Use this schema to specialize mission plans for aerial operations.

---

## 🔗 Relationship to the Autonomous Core

This module extends the core schemas found in:

```
docs/schemas/rtt-autonomous/
```

Specifically:

- `autonomous_form_descriptor` → extended by `drone_extension`  
- `autonomous_mission_profile` → extended by `drone_mission_profile_extension`  
- `autonomous_morphology` → compatible with drone frame/actuator definitions  
- `autonomous_energy_profile` → complemented by drone‑specific battery schema  
- `autonomous_corridor_definition` → used for airspace corridors  
- `autonomous_swarm_state` → supports aerial swarms and formations  

The drone schemas never duplicate core fields; they only **extend** them.

---

## 🧩 Usage Pattern

A typical drone definition references:

1. **Core descriptor**  
2. **Drone extension**  
3. **Morphology**  
4. **Flight envelope**  
5. **Energy profile**  
6. **Mission profile + drone mission extension**  

This layered approach keeps the system modular, extensible, and consistent with the rest of the Triadic Frameworks schema ecosystem.

---

## 🌱 Future Extensions

This module is designed to grow with additional aerial robotics capabilities, such as:

- obstacle‑aware flight corridors  
- multi‑drone cooperative behaviors  
- sensor‑specific payload schemas (LiDAR, EO/IR, multispectral)  
- weather‑adaptive mission planning  
