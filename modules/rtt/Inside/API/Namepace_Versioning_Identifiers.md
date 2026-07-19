### 1. Namespace, versioning, and identifiers

**Namespace (logical):**

- `rtt.core.v1` — resonance structural awareness dimensional core

**Identifier strategy:**

- **Node IDs:** UUIDv4  
- **Mesh IDs:** UUIDv4  
- **Zone IDs:** URN‑style, e.g. `urn:rtt:zone:coal:blue_hollow:section_c`  
- **OIDs (if you want strict ASN.1 style):**  
  - Root: `1.3.6.1.4.1.<your-enterprise>.rtt`  
  - Core: `1.3.6.1.4.1.<your-enterprise>.rtt.core`  
  - Domains later: `.coal`, `.atc`, `.deepsea`, etc.

**Versioning:**

- Semantic: `v1.0.0` for the first stable core  
- API path example: `/api/rtt/core/v1/...`  

---

### 2. Core data model (common across all domains)

#### 2.1. `ResonanceFieldSample`

```json
{
  "sample_id": "uuid",
  "node_id": "uuid",
  "mesh_id": "uuid",
  "timestamp": "2026-01-08T17:21:00Z",
  "location": {
    "frame": "local",          // "local" | "wgs84" | "custom:<urn>"
    "x": 12.3,
    "y": 4.5,
    "z": -650.0,
    "units": "m"
  },
  "clarity_score": 182,        // 0–255
  "stress_hint": 143,          // 0–255
  "vibration": {
    "rms": 0.72,
    "bands": [
      { "freq_hz": 10, "amp": 0.12 },
      { "freq_hz": 60, "amp": 0.44 }
    ]
  },
  "gas": {
    "type": "CH4",
    "ppm": 1200.0
  },
  "temperature_c": 28.4,
  "pressure_pa": 101325.0,
  "drift_vector": {
    "dx": -0.3,
    "dy": 0.1,
    "dz": 0.0,
    "magnitude": 0.32,
    "units": "1/s"
  },
  "tags": [
    "zone:urn:rtt:zone:coal:blue_hollow:section_c",
    "domain:coal"
  ]
}
```

---

#### 2.2. `ResonanceZoneState`

```json
{
  "zone_id": "urn:rtt:zone:coal:blue_hollow:section_c",
  "mesh_id": "uuid",
  "timestamp": "2026-01-08T17:21:00Z",
  "clarity_score": 164,
  "stress_hint": 151,
  "gas_risk": "medium",        // "low" | "medium" | "high" | "critical"
  "vibration_risk": "high",
  "composite_risk": "degrading",
  "drift_vector": {
    "dx": -0.2,
    "dy": 0.0,
    "dz": 0.1,
    "magnitude": 0.22,
    "units": "1/s"
  },
  "status": "evacuate",        // "normal" | "watch" | "evacuate" | "no-entry"
  "source_samples": ["uuid", "uuid"]
}
```

---

#### 2.3. `NodeDescriptor`

```json
{
  "node_id": "uuid",
  "mesh_id": "uuid",
  "type": "fixed",             // "fixed" | "wearable" | "mobile" | "vehicle"
  "domain": "coal",            // or "atc", "deepsea", etc.
  "capabilities": [
    "sense:vibration",
    "sense:gas",
    "sense:pressure",
    "comm:subghz",
    "comm:ble"
  ],
  "location_hint": {
    "zone_id": "urn:rtt:zone:coal:blue_hollow:section_c",
    "x": 10.0,
    "y": 5.0,
    "z": -650.0,
    "units": "m"
  },
  "firmware": {
    "rtt_core_version": "1.0.0",
    "vendor_variant": "acme.coal.v1.2.3"
  }
}
```

---

#### 2.4. `ResonanceAlert`

```json
{
  "alert_id": "uuid",
  "mesh_id": "uuid",
  "zone_id": "urn:rtt:zone:coal:blue_hollow:section_c",
  "timestamp": "2026-01-08T17:21:05Z",
  "severity": "critical",      // "info" | "warning" | "major" | "critical"
  "type": "structural",        // "structural" | "gas" | "vibration" | "comms"
  "summary": "Roof stress + high vibration coupling",
  "details": {
    "clarity_before": 172,
    "clarity_after": 118,
    "stress_hint": 201,
    "gas_ppm": 1300.0
  },
  "recommended_actions": [
    "evacuate_zone",
    "reduce_vibration_sources",
    "increase_ventilation"
  ],
  "source_nodes": ["uuid", "uuid"]
}
```

---

#### 2.5. `RouteSuggestion` (for evacuation / navigation)

```json
{
  "route_id": "uuid",
  "mesh_id": "uuid",
  "from_zone": "urn:rtt:zone:coal:blue_hollow:section_c",
  "to_zone": "urn:rtt:zone:coal:blue_hollow:primary_exit",
  "timestamp": "2026-01-08T17:21:10Z",
  "clarity_profile": [
    { "zone_id": "…:section_c", "clarity_score": 118 },
    { "zone_id": "…:crosscut_4", "clarity_score": 164 },
    { "zone_id": "…:main_entry", "clarity_score": 201 }
  ],
  "risk_level": "medium",
  "instructions": [
    "move_east_40m",
    "turn_north_at_crosscut_4",
    "follow_main_entry_to_primary_exit"
  ]
}
```
