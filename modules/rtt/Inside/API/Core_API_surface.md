### 3. Core API surface (HTTP/JSON example)

We can later mirror this as gRPC, MQTT topics, etc.—but HTTP/JSON is a clean RFC baseline.

#### 3.1. Field samples

- `POST /api/rtt/core/v1/field-samples`  
  Ingest a `ResonanceFieldSample`.

- `GET /api/rtt/core/v1/field-samples?zone_id=…&since=…`  
  Query samples for analysis / replay.

#### 3.2. Zone state

- `GET /api/rtt/core/v1/zones/{zone_id}/state`  
  Returns `ResonanceZoneState`.

- `GET /api/rtt/core/v1/zones?mesh_id=…`  
  List all zones and their current state.

#### 3.3. Nodes

- `POST /api/rtt/core/v1/nodes/register`  
  Register or update a `NodeDescriptor`.

- `GET /api/rtt/core/v1/nodes/{node_id}`  
  Get node info.

- `GET /api/rtt/core/v1/nodes?mesh_id=…&zone_id=…`  
  List nodes in a mesh/zone.

#### 3.4. Alerts

- `GET /api/rtt/core/v1/alerts?mesh_id=…&since=…`  
  Fetch `ResonanceAlert` objects.

- (Optional) `POST /api/rtt/core/v1/alerts`  
  For systems that generate alerts externally but want to register them centrally.

#### 3.5. Routes / clarity gradients

- `POST /api/rtt/core/v1/routes/suggest`  

  **Request:**

  ```json
  {
    "mesh_id": "uuid",
    "from_zone": "urn:rtt:zone:coal:blue_hollow:section_c",
    "to_zone": "urn:rtt:zone:coal:blue_hollow:primary_exit",
    "constraints": {
      "max_risk": "high",
      "avoid_zones": ["urn:rtt:zone:coal:blue_hollow:panel_3"]
    }
  }
  ```

  **Response:** `RouteSuggestion`.

---

### 4. Agent‑facing API (for open‑source AI agents)

This is the bit that matters for your “vendor agent + RTT‑Inside” vision.

#### 4.1. Local agent bindings (conceptual)

Expose a **local SDK** (language‑agnostic spec, then bindings):

- `rtt.get_clarity(zone_id: string | null) -> int`
- `rtt.get_drift_vector(zone_id: string | null) -> DriftVector`
- `rtt.subscribe(event_type: string, callback)`
  - `event_type` examples: `"clarity_drop"`, `"resonance_spike"`, `"zone_status_change"`
- `rtt.get_zone_state(zone_id: string) -> ResonanceZoneState`
- `rtt.get_route(from_zone: string, to_zone: string, constraints: RouteConstraints) -> RouteSuggestion`

Agents don’t see raw sensor noise—they see **structured resonance state**.

---

### 5. Standards alignment (the “no weird snowflake” rule)

- **Time:** ISO‑8601 UTC (`YYYY-MM-DDThh:mm:ssZ`)  
- **IDs:** UUIDv4 for entities, URNs/OIDs for zones and domains  
- **Units:** SI only (`m`, `Pa`, `°C`, `Hz`, `1/s`, `ppm`)  
- **Encodings:** JSON for RFC baseline; Protobuf/CBOR allowed as alternative encodings with identical schemas  
- **Error model:** HTTP status codes + JSON error object with `code`, `message`, `details`  

---

### 6. How we extend this per domain (next step)

Once this **core** is locked, each domain gets an extension spec:

- `rtt.coal.v1`  
- `rtt.atc.v1`  
- `rtt.deepsea.v1`  
- `rtt.space.v1`  
- `rtt.gpr.v1`  
- etc.

Each extension:

- reuses `ResonanceFieldSample`, `ZoneState`, `NodeDescriptor`, `Alert`, `RouteSuggestion`  
- adds **domain‑specific fields** via `details` / `extensions` blocks or separate resources  
- never breaks core invariants

Example: `ResonanceFieldSample.extensions.coal` could add:

```json
"extensions": {
  "coal": {
    "roof_strata_type": "shale",
    "pillar_load_kpa": 320.0
  }
}
```

---

### 7. RFC‑ready framing

You’re basically ready to write:

- **Title:** “RTT‑Inside Core API: A Resonance Structural Awareness Dimensional Interface”  
- **Sections:**
  1. Terminology and concepts (clarity, drift, resonance, zone, mesh, node)  
  2. Data model (the JSON schemas above)  
  3. Transport bindings (HTTP/JSON baseline)  
  4. Agent bindings (local SDK expectations)  
  5. Security and safety considerations (auth, integrity, misuse)  
  6. Domain extension model  

You’ve already got the narrative and the use‑cases in your docs; this API is the spine that ties them together.
