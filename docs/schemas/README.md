# 📘 **Triadic Frameworks — Schema Hierarchy Overview**
### *RTT‑Inside / RSADI Schema Architecture (Core + Extensions)*

This directory contains the **complete schema hierarchy** for the Resonance Structural Awareness Dimensional Interface (RSADI) and its domain‑specific extensions.  
Schemas are organized to ensure:

- **stability** (core never breaks)  
- **extensibility** (domains add fields cleanly)  
- **interoperability** (all systems speak the same resonance language)  
- **clarity** (contributors know exactly where new schemas belong)  

This document explains the structure, purpose, and rules for all schema folders.

---

# 🧱 1. Schema Folder Structure

```
docs/
 └── schemas/
      ├── rtt-core/        ← invariant, domain‑neutral foundation
      ├── rtt-coal/        ← coal mining industry extension
      ├── rsadi-gd/        ← game developer extension
      ├── rtt-atc/         ← (future) air traffic control extension
      ├── rtt-deepsea/     ← (future) deep sea / submersible extension
      ├── rtt-space/       ← (future) aerospace / orbital extension
      └── TEMPLATE/        ← boilerplate for new domain extensions
```

Each folder contains JSON Schemas written in **Draft 2020‑12**, using:

- UUIDv4 identifiers  
- ISO‑8601 timestamps  
- SI units  
- strict typing  
- optional `extensions` blocks  

---

# 🧩 2. RTT‑Core (Invariant Foundation)

**Folder:** `rtt-core/`  
**Purpose:** Defines the *universal* RSADI data model used by all domains.

Schemas included:

- `ResonanceFieldSample.schema.json`  
- `ResonanceZoneState.schema.json`  
- `NodeDescriptor.schema.json`  
- `ResonanceAlert.schema.json`  
- `RouteSuggestion.schema.json`  

These schemas define:

- clarity  
- drift  
- stress  
- vibration  
- gas (optional)  
- nodes  
- alerts  
- routing  

**Core Rule:**  
> RTT‑Core schemas MUST NOT be modified in ways that break compatibility.  
> All domain‑specific fields MUST be added via `extensions.<domain>`.

---

# 🪨 3. RTT‑Coal (Coal Industry Extension)

**Folder:** `rtt-coal/`  
**Purpose:** Adds coal‑specific structural, geological, and safety fields.

Schemas include:

- `CoalZoneExtension.schema.json`  
- `CoalFieldSampleExtension.schema.json`  
- `CoalNodeDescriptorExtension.schema.json`  
- `CoalAlertExtension.schema.json`  
- `CoalEvacRouteExtension.schema.json`  

Examples of added fields:

- methane_ppm  
- roof_convergence_mm  
- pillar_load_kpa  
- ignition_risk  
- collapse_vector  
- refuge_chambers  

**Rule:**  
> Coal extensions MUST attach under `extensions.coal` in core objects.

---

# 🎮 4. RSADI‑GD (Game Developer Extension)

**Folder:** `rsadi-gd/`  
**Purpose:** Provides lightweight, deterministic schemas for game engines.

Schemas include:

- `GDClaritySample.schema.json`  
- `GDDriftVector.schema.json`  
- `GDZoneState.schema.json`  
- `GDRiskLevel.schema.json`  
- `GDRouteSuggestion.schema.json`  
- `GDEventSubscription.schema.json`  

These are optimized for:

- Unity  
- Unreal  
- Godot  
- custom engines  
- deterministic multiplayer  

**Rule:**  
> RSADI‑GD schemas mirror core semantics but simplify structure for real‑time engines.

---

# 🌐 5. Future Domains (ATC, Deep Sea, Space, Robotics)

These folders follow the same pattern as coal and RSADI‑GD:

```
rtt-atc/
rtt-deepsea/
rtt-space/
rtt-robotics/
```

Each domain:

- defines its own extension schemas  
- attaches fields under `extensions.<domain>`  
- never modifies core schemas  
- may define domain‑specific enums, thresholds, or metadata  

Examples:

### **ATC**
- turbulence vectors  
- runway resonance  
- aircraft structural load  
- air corridor clarity  

### **Deep Sea**
- hull pressure  
- salinity  
- thermal vents  
- submersible drift  

### **Space**
- radiation clarity  
- orbital drift  
- hull micro‑stress  
- docking resonance  

---

# 🧬 6. Extension Rules (Must Follow)

All domain extensions MUST follow these rules:

### **1. Never modify core schemas**
Core fields are invariant.

### **2. Add fields only under `extensions.<domain>`**
Example:

```json
"extensions": {
  "coal": {
    "methane_ppm": 1200
  }
}
```

### **3. Use separate schema files**
Each domain has its own folder.

### **4. Use clear naming**
`<Domain><CoreObject>Extension.schema.json`

### **5. Maintain backward compatibility**
Extensions must be optional.

### **6. Keep domain logic out of the core**
Core = physics  
Extensions = industry semantics  

---

# 🧭 7. How to Add a New Domain

1. Copy the `TEMPLATE/` folder.  
2. Rename it to `rtt-<domain>/`.  
3. Create extension schemas for each core object you need.  
4. Attach fields under `extensions.<domain>`.  
5. Validate using JSON Schema tools.  
6. Add a domain README explaining semantics.  

---

# 🛡️ 8. Why This Hierarchy Matters

This structure ensures:

- **global interoperability**  
- **predictable agent behavior**  
- **safe industrial deployments**  
- **clean separation of concerns**  
- **future‑proof extensibility**  
- **cross‑domain resonance coherence**  

It is the backbone of the entire Triadic Frameworks ecosystem.

---

# 🧾 Schemas — Resonance Data Contracts  

## 🔭 Purpose  
This folder contains **JSON schema artifacts** that define the structure and validation rules for resonance data. They are the **contracts** remixers use to ensure scrolls, manifests, and snapshots remain consistent across the lineage.  

## 📂 Contents  
- `attestation_receipt.schema.json` → Defines the structure for buffer exit attestations (Ω, Φ, Δ₀).  
- `constraint_pack.json` → Encodes validator constraints for resonance experiments.  
- `corridor_env_manifest.json` → Schema for corridor environment manifests (arc corridors, universes).  
- `lineage_manifest.json` → Defines how lineage data is recorded and validated.  
- `miracles.json` → Schema for improbable but validated resonance events.  
- `survival_traits.json` → Schema for encoding adaptive traits across universes.  

## 🛠️ Usage  
1. Use these schemas to **validate JSON manifests** before committing them to the repo.  
2. Extend schemas when new RFCs introduce additional invariants or constructs.  
3. Treat schemas as **living contracts**—they evolve with the canon but always preserve validator clarity.  

## 🌐 Lineage  
- Rooted in **RFC‑008 (Quadrant Invariants)**.  
- Extended by **RFC‑068 (Temporal Buffer Lattice)** and **RFC‑069 (Temporal Guardians)**.  
- Provides the **structural backbone** for manifests, snapshots, and dashboards.  

## 🛡️ Validator Echo  
_"Schemas are not just rules.  
They are the bones of resonance,  
ensuring scrolls and fossils  
speak the same language."_  

---
