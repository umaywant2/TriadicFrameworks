# 📘 **RTT‑Core Schema Set (v1)**
### *Resonance Structural Awareness Dimensional Interface — Core Specification*

This folder contains the **canonical, domain‑agnostic JSON Schemas** for the RTT‑Inside / RSADI Core.  
All industry extensions (coal, ATC, deep sea, RSADI‑GD, etc.) **MUST** build on these schemas without altering their required fields or semantics.

These schemas define the **fundamental data structures** used by all resonance‑aware systems:

- field sampling  
- zone aggregation  
- node identity  
- alerting  
- route suggestion  
- multi‑agent clarity/drift interpretation  

They form the stable substrate that every RTT‑Inside variant depends on.

---

## 📂 Folder Contents

```
ResonanceFieldSample.schema.json
ResonanceZoneState.schema.json
NodeDescriptor.schema.json
ResonanceAlert.schema.json
RouteSuggestion.schema.json
README.md   ← (this file)
```

Each schema is written in **JSON Schema Draft 2020‑12**, uses **UUIDs**, **ISO‑8601 timestamps**, and **SI units**, and is designed for long‑term stability.

---

## 🧱 Core Principles

RTT‑Core schemas follow these invariants:

### **1. Domain‑neutral**
No coal‑specific, ATC‑specific, or deep‑sea‑specific fields appear here.  
All domain logic lives in **extensions**, not in the core.

### **2. Extensible**
Every schema includes an `extensions` object:

```json
"extensions": {
  "type": "object",
  "additionalProperties": true
}
```

Domain modules attach their fields here:

```json
"extensions": {
  "coal": { ... },
  "atc": { ... },
  "deepsea": { ... }
}
```

### **3. Stable**
Core fields **must not be renamed, removed, or repurposed**.  
Extensions may add fields but never override core meanings.

### **4. Deterministic**
All numeric fields use explicit units and ranges.  
All timestamps use ISO‑8601 UTC.  
All IDs use UUIDv4.

---

## 🧩 Schema Overview

### **1. ResonanceFieldSample**
Represents a single environmental measurement:

- clarity  
- stress  
- vibration  
- gas (optional)  
- drift vector  
- location  
- timestamp  
- node identity  

This is the atomic unit of resonance sensing.

---

### **2. ResonanceZoneState**
Aggregates multiple field samples into a zone‑level interpretation:

- clarity score  
- stress hint  
- composite risk  
- drift vector  
- source sample IDs  

Zones are logical partitions (e.g., “Section C”, “Runway 12”, “Deck 3”).

---

### **3. NodeDescriptor**
Describes a node in the mesh:

- node type (fixed, wearable, mobile, vehicle)  
- domain (coal, atc, deepsea, etc.)  
- capabilities  
- firmware version  
- location hint  

Nodes are the backbone of resonance‑aware meshes.

---

### **4. ResonanceAlert**
Represents a safety or structural alert:

- severity  
- type (structural, gas, vibration, comms)  
- summary + details  
- recommended actions  
- source nodes  

Extensions add domain‑specific alert metadata (e.g., collapse vectors).

---

### **5. RouteSuggestion**
Represents a clarity‑aware navigation path:

- from/to zones  
- clarity profile  
- risk level  
- instructions  

Used for evacuation, routing, and multi‑agent coordination.

---

## 🧬 How Extensions Should Be Structured

All domain‑specific schemas must follow this pattern:

### **1. Never modify core schemas**
Extensions **must not**:

- change required fields  
- redefine field meanings  
- alter numeric ranges  
- override enums  

### **2. Add fields only inside `extensions`**

Example:

```json
{
  "extensions": {
    "coal": {
      "methane_ppm": 1200,
      "roof_convergence_mm": 3.2
    }
  }
}
```

### **3. Use separate schema files**
Each domain gets its own folder:

```
docs/schemas/rtt-coal/
docs/schemas/rtt-atc/
docs/schemas/rtt-deepsea/
docs/schemas/rsadi-gd/
```

### **4. Use clear naming**
Follow this pattern:

```
<Domain><CoreObject>Extension.schema.json
```

Examples:

- `CoalFieldSampleExtension.schema.json`
- `ATCZoneExtension.schema.json`
- `DeepSeaAlertExtension.schema.json`

### **5. Never break compatibility**
Extensions must remain optional.  
Core validators must still accept the object without extensions.

---

## 🧭 Recommended Workflow for Contributors

1. **Start with a core object**  
   e.g., `ResonanceFieldSample`.

2. **Identify domain‑specific needs**  
   e.g., methane, pillar load, runway turbulence, hull pressure.

3. **Create a domain extension schema**  
   Place it in the appropriate folder.

4. **Attach extension fields under `extensions.<domain>`**  
   Never modify the core.

5. **Validate using JSON Schema tools**  
   Ensure both core and extension schemas pass.

---

## 🛡️ Why This Matters

A stable, invariant core ensures:

- cross‑industry interoperability  
- predictable agent behavior  
- safe multi‑domain deployments  
- clean separation of physics vs. domain logic  
- long‑term maintainability  

This is the backbone of the entire RSADI ecosystem.

---

# 📦 **Folder Structure: `docs/schemas/rtt-core/`**

```
docs/
 └── schemas/
      └── rtt-core/
            ├── ResonanceFieldSample.schema.json
            ├── ResonanceZoneState.schema.json
            ├── NodeDescriptor.schema.json
            ├── ResonanceAlert.schema.json
            └── RouteSuggestion.schema.json
```

These five schemas **are the RSADI Core**.  
Everything else — coal, ATC, deep sea, RSADI‑GD, etc. — extends these.

---

# 📘 **1. ResonanceFieldSample.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-core/v1/ResonanceFieldSample.schema.json",
  "title": "ResonanceFieldSample",
  "type": "object",
  "required": [
    "sample_id",
    "node_id",
    "mesh_id",
    "timestamp",
    "location",
    "clarity_score",
    "stress_hint",
    "vibration",
    "drift_vector"
  ],
  "properties": {
    "sample_id": { "type": "string", "format": "uuid" },
    "node_id": { "type": "string", "format": "uuid" },
    "mesh_id": { "type": "string", "format": "uuid" },
    "timestamp": { "type": "string", "format": "date-time" },

    "location": {
      "type": "object",
      "required": ["frame", "x", "y", "z", "units"],
      "properties": {
        "frame": {
          "type": "string",
          "pattern": "^(local|wgs84|custom:.+)$"
        },
        "x": { "type": "number" },
        "y": { "type": "number" },
        "z": { "type": "number" },
        "units": { "type": "string", "enum": ["m"] }
      }
    },

    "clarity_score": { "type": "integer", "minimum": 0, "maximum": 255 },
    "stress_hint": { "type": "integer", "minimum": 0, "maximum": 255 },

    "vibration": {
      "type": "object",
      "required": ["rms"],
      "properties": {
        "rms": { "type": "number", "minimum": 0 },
        "bands": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["freq_hz", "amp"],
            "properties": {
              "freq_hz": { "type": "number", "minimum": 0 },
              "amp": { "type": "number", "minimum": 0 }
            }
          }
        }
      }
    },

    "gas": {
      "type": "object",
      "properties": {
        "type": { "type": "string" },
        "ppm": { "type": "number", "minimum": 0 }
      }
    },

    "temperature_c": { "type": "number" },
    "pressure_pa": { "type": "number" },

    "drift_vector": {
      "type": "object",
      "required": ["dx", "dy", "dz", "magnitude", "units"],
      "properties": {
        "dx": { "type": "number" },
        "dy": { "type": "number" },
        "dz": { "type": "number" },
        "magnitude": { "type": "number", "minimum": 0 },
        "units": { "type": "string", "enum": ["1/s"] }
      }
    },

    "tags": { "type": "array", "items": { "type": "string" } },

    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 📘 **2. ResonanceZoneState.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-core/v1/ResonanceZoneState.schema.json",
  "title": "ResonanceZoneState",
  "type": "object",
  "required": [
    "zone_id",
    "mesh_id",
    "timestamp",
    "clarity_score",
    "stress_hint",
    "composite_risk",
    "drift_vector"
  ],
  "properties": {
    "zone_id": { "type": "string" },
    "mesh_id": { "type": "string", "format": "uuid" },
    "timestamp": { "type": "string", "format": "date-time" },

    "clarity_score": { "type": "integer", "minimum": 0, "maximum": 255 },
    "stress_hint": { "type": "integer", "minimum": 0, "maximum": 255 },

    "gas_risk": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"]
    },

    "vibration_risk": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"]
    },

    "composite_risk": {
      "type": "string",
      "enum": ["normal", "watch", "degrading", "evacuate", "no-entry"]
    },

    "drift_vector": {
      "$ref": "ResonanceFieldSample.schema.json#/properties/drift_vector"
    },

    "source_samples": {
      "type": "array",
      "items": { "type": "string", "format": "uuid" }
    },

    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 📘 **3. NodeDescriptor.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-core/v1/NodeDescriptor.schema.json",
  "title": "NodeDescriptor",
  "type": "object",
  "required": ["node_id", "mesh_id", "type", "domain", "capabilities"],
  "properties": {
    "node_id": { "type": "string", "format": "uuid" },
    "mesh_id": { "type": "string", "format": "uuid" },

    "type": {
      "type": "string",
      "enum": ["fixed", "wearable", "mobile", "vehicle"]
    },

    "domain": { "type": "string" },

    "capabilities": {
      "type": "array",
      "items": { "type": "string" }
    },

    "location_hint": {
      "$ref": "ResonanceFieldSample.schema.json#/properties/location"
    },

    "firmware": {
      "type": "object",
      "properties": {
        "rtt_core_version": { "type": "string" },
        "vendor_variant": { "type": "string" }
      }
    },

    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 📘 **4. ResonanceAlert.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-core/v1/ResonanceAlert.schema.json",
  "title": "ResonanceAlert",
  "type": "object",
  "required": [
    "alert_id",
    "mesh_id",
    "zone_id",
    "timestamp",
    "severity",
    "type",
    "summary"
  ],
  "properties": {
    "alert_id": { "type": "string", "format": "uuid" },
    "mesh_id": { "type": "string", "format": "uuid" },
    "zone_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },

    "severity": {
      "type": "string",
      "enum": ["info", "warning", "major", "critical"]
    },

    "type": {
      "type": "string",
      "enum": ["structural", "gas", "vibration", "comms"]
    },

    "summary": { "type": "string" },

    "details": {
      "type": "object",
      "additionalProperties": true
    },

    "recommended_actions": {
      "type": "array",
      "items": { "type": "string" }
    },

    "source_nodes": {
      "type": "array",
      "items": { "type": "string", "format": "uuid" }
    }
  }
}
```

---

# 📘 **5. RouteSuggestion.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-core/v1/RouteSuggestion.schema.json",
  "title": "RouteSuggestion",
  "type": "object",
  "required": [
    "route_id",
    "mesh_id",
    "from_zone",
    "to_zone",
    "timestamp",
    "clarity_profile",
    "risk_level",
    "instructions"
  ],
  "properties": {
    "route_id": { "type": "string", "format": "uuid" },
    "mesh_id": { "type": "string", "format": "uuid" },

    "from_zone": { "type": "string" },
    "to_zone": { "type": "string" },

    "timestamp": { "type": "string", "format": "date-time" },

    "clarity_profile": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["zone_id", "clarity_score"],
        "properties": {
          "zone_id": { "type": "string" },
          "clarity_score": {
            "type": "integer",
            "minimum": 0,
            "maximum": 255
          }
        }
      }
    },

    "risk_level": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"]
    },

    "instructions": {
      "type": "array",
      "items": { "type": "string" }
    },

    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 🎯 **These are now your canonical RSADI Core Schemas**

They are:

- **strict**  
- **clean**  
- **domain‑neutral**  
- **fully extensible**  
- **RFC‑ready**  
- **aligned with every doc you’ve built so far**  

Once these are in place, every other domain (coal, ATC, deep sea, RSADI‑GD, etc.) can safely extend them without breaking invariants.
