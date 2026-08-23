# 📘 **RTT‑Inside Core API — Formal JSON Schemas (v0.1)**  
### *Draft 2020‑12 compliant, domain‑agnostic, RFC‑ready*

---

# 1. **ResonanceFieldSample.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt/core/v1/ResonanceFieldSample.schema.json",
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
    "sample_id": {
      "type": "string",
      "format": "uuid"
    },
    "node_id": {
      "type": "string",
      "format": "uuid"
    },
    "mesh_id": {
      "type": "string",
      "format": "uuid"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "location": {
      "type": "object",
      "required": ["frame", "x", "y", "z", "units"],
      "properties": {
        "frame": {
          "type": "string",
          "enum": ["local", "wgs84"],
          "pattern": "^(local|wgs84|custom:.+)$"
        },
        "x": { "type": "number" },
        "y": { "type": "number" },
        "z": { "type": "number" },
        "units": { "type": "string", "enum": ["m"] }
      }
    },
    "clarity_score": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "stress_hint": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
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
    "tags": {
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

# 2. **ResonanceZoneState.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt/core/v1/ResonanceZoneState.schema.json",
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

# 3. **NodeDescriptor.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt/core/v1/NodeDescriptor.schema.json",
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

# 4. **ResonanceAlert.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt/core/v1/ResonanceAlert.schema.json",
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

# 5. **RouteSuggestion.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rtt/core/v1/RouteSuggestion.schema.json",
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

# 🌐 These schemas are now RFC‑ready

They’re:

- **strict**  
- **extensible**  
- **domain‑agnostic**  
- **standards‑aligned**  
- **ready for per‑domain extension modules**  

- [RFC-049 A Resonance Structural Awareness Dimensional Interface](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-049-A_Resonance_Structural_Awareness_Dimensional_Interface.md)
