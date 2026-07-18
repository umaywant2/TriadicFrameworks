# 📦 **Folder Structure for Coal‑Specific Schemas**
[RFC-052 RSADI Coal Industry Extension to RSADI Core](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-052-RSADI-Coal_Industry_Extension_to_RSADI_Core.md)

```
docs/
 └── schemas/
      ├── rtt-core/
      │     └── ... (existing core schemas)
      ├── rsadi-gd/
      │     └── ... (game dev schemas)
      └── rtt-coal/
            ├── CoalZoneExtension.schema.json
            ├── CoalFieldSampleExtension.schema.json
            ├── CoalNodeDescriptorExtension.schema.json
            ├── CoalAlertExtension.schema.json
            └── CoalEvacRouteExtension.schema.json
```

This mirrors your existing structure and keeps domain variants cleanly separated.

---

# 🪨 **1. CoalZoneExtension.schema.json**  
### *(Adds geology + mining‑specific metadata to a zone)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-coal/v1/CoalZoneExtension.schema.json",
  "title": "CoalZoneExtension",
  "type": "object",
  "properties": {
    "roof_strata_type": {
      "type": "string",
      "description": "Primary geological layer above the working section (e.g., shale, sandstone)."
    },
    "floor_strata_type": {
      "type": "string",
      "description": "Primary geological layer below the working section."
    },
    "pillar_load_kpa": {
      "type": "number",
      "description": "Estimated load on coal pillars in kilopascals."
    },
    "seam_height_m": {
      "type": "number",
      "description": "Coal seam height in meters."
    },
    "ventilation_rating": {
      "type": "string",
      "enum": ["good", "restricted", "poor"],
      "description": "Ventilation quality for the zone."
    },
    "equipment_present": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of equipment operating in this zone."
    }
  }
}
```

---

# 🪫 **2. CoalFieldSampleExtension.schema.json**  
### *(Adds coal‑specific sensor data to a field sample)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-coal/v1/CoalFieldSampleExtension.schema.json",
  "title": "CoalFieldSampleExtension",
  "type": "object",
  "properties": {
    "methane_ppm": {
      "type": "number",
      "description": "Methane concentration in parts per million."
    },
    "co_ppm": {
      "type": "number",
      "description": "Carbon monoxide concentration in parts per million."
    },
    "dust_density_mg_m3": {
      "type": "number",
      "description": "Airborne coal dust density."
    },
    "roof_convergence_mm": {
      "type": "number",
      "description": "Roof movement measured in millimeters."
    },
    "equipment_vibration_signature": {
      "type": "object",
      "properties": {
        "equipment_id": { "type": "string" },
        "dominant_freq_hz": { "type": "number" },
        "amplitude": { "type": "number" }
      }
    }
  }
}
```

---

# 🧱 **3. CoalNodeDescriptorExtension.schema.json**  
### *(Adds coal‑specific metadata to node descriptors)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-coal/v1/CoalNodeDescriptorExtension.schema.json",
  "title": "CoalNodeDescriptorExtension",
  "type": "object",
  "properties": {
    "node_role": {
      "type": "string",
      "enum": ["wall-mounted", "wearable", "equipment-mounted", "refuge-chamber"],
      "description": "Role of the node in the coal mine environment."
    },
    "intrinsic_safety_rating": {
      "type": "string",
      "description": "Certification level for explosive atmospheres (e.g., MSHA IS)."
    },
    "mount_location": {
      "type": "string",
      "description": "Physical mounting location (rib, roof bolt, equipment frame)."
    }
  }
}
```

---

# 🚨 **4. CoalAlertExtension.schema.json**  
### *(Adds coal‑specific alert metadata)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-coal/v1/CoalAlertExtension.schema.json",
  "title": "CoalAlertExtension",
  "type": "object",
  "properties": {
    "collapse_vector": {
      "type": "object",
      "properties": {
        "dx": { "type": "number" },
        "dy": { "type": "number" },
        "dz": { "type": "number" }
      },
      "description": "Predicted direction of structural failure."
    },
    "ignition_risk": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"],
      "description": "Risk of methane or coal dust ignition."
    },
    "belt_fire_risk": {
      "type": "string",
      "enum": ["low", "medium", "high", "critical"],
      "description": "Risk of conveyor belt fire."
    }
  }
}
```

---

# 🧭 **5. CoalEvacRouteExtension.schema.json**  
### *(Adds coal‑specific evacuation metadata)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt-coal/v1/CoalEvacRouteExtension.schema.json",
  "title": "CoalEvacRouteExtension",
  "type": "object",
  "properties": {
    "refuge_chambers": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of refuge chambers along the route."
    },
    "ventilation_paths": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Ventilation routes relevant to evacuation."
    },
    "hazard_zones": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Zones to avoid during evacuation."
    }
  }
}
```

---

# 🧩 Why these schemas matter

These give you:

- **drop‑in extensions** for the coal doc  
- **consistent structure** with RSADI‑Core  
- **ready‑to‑validate JSON**  
- **clean separation of domain logic**  
- **future‑proofing** for other industries  

And they save contributors from having to guess how to represent:

- methane  
- dust  
- roof convergence  
- pillar load  
- collapse vectors  
- evacuation metadata  

Everything is already typed, validated, and ready to use.

---

If you want, I can now **scan the coal doc itself** and generate:

- a **mapping table** showing which doc sections map to which schema fields  
- a **“recommended API usage”** block for the coal doc  
- or .
