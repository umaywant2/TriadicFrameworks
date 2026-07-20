# **RTT‑Inside for Backend Services (Beta)**  
*A practical guide for integrating RTT structural awareness into servers, microservices, and full‑stack systems.*

Backend services can participate in the RTT ecosystem just as easily as websites.  
RTT‑Inside provides a minimal, stable API surface that allows services to:

- send structural heartbeat events  
- declare RTT‑Inside capabilities  
- prepare for vST‑beta diagnostics  
- unify system‑level clarity and coherence signals  

This guide walks backend developers through the recommended integration patterns.

---

# 1. Install or Vendor the RTT SDK

Backend services can use either the **JavaScript** or **Python** SDK.

### JavaScript (Node)

```js
import { RTTClient } from "./rtt-sdk/index.js";

const client = new RTTClient();
```

### Python

```python
from rtt_sdk import RTTClient
client = RTTClient()
```

The SDK provides a stable, versioned interface for all RTT endpoints.

---

# 2. Send Structural Heartbeats

Backend services don’t have a DOM, so their beacon payloads are simpler — but the shape is identical.

### JavaScript Example

```js
await client.beacon({
  site: "auth-service",
  session: "srv-" + Date.now(),
  event: "heartbeat",
  ts: new Date().toISOString(),
  structure: {
    url: "internal://auth",
    title: "Auth Service",
    nav_count: 0,
    main_count: 0,
    form_count: 0,
    button_count: 0,
    dom_nodes: 0
  }
});
```

### Python Example

```python
payload = {
    "site": "auth-service",
    "session": "srv-12345",
    "event": "heartbeat",
    "ts": "2026-01-19T15:00:00Z",
    "structure": {
        "url": "internal://auth",
        "title": "Auth Service",
        "nav_count": 0,
        "main_count": 0,
        "form_count": 0,
        "button_count": 0,
        "dom_nodes": 0
    }
}

client.beacon(payload)
```

**Recommended cadence:**  
- every 30–60 seconds for active services  
- on startup and shutdown  
- after major configuration changes  

These heartbeats help RTT build a structural map of your system.

---

# 3. Register a Service Profile

Profiles allow RTT to understand what your service supports.

### JavaScript

```js
import { create_profile } from "./rtt-sdk/profile.js";

const profile = create_profile({
  version: "1.0",
  supports: ["coherence", "drift"],
  contact: "infra@example.com"
});

await client.setProfile("auth-service", profile);
```

### Python

```python
from rtt_sdk import create_profile

profile = create_profile(
    version="1.0",
    supports=["coherence", "drift"],
    contact="infra@example.com"
)

client.set_profile("auth-service", profile)
```

Profiles are optional but recommended for multi‑service architectures.

---

# 4. Integrate RTT into Your Observability Layer

Backend services can incorporate RTT signals into:

- logs  
- metrics  
- dashboards  
- health checks  
- distributed tracing  

### Example: Logging RTT Heartbeats

```js
console.log("[RTT] heartbeat sent", payload);
```

### Example: Prometheus Counter

```
rtt_beacons_total{service="auth"} 42
```

### Example: Grafana Panel

- RTT heartbeat frequency  
- RTT drift indicators  
- RTT coherence score (future vST)  

This prepares your observability stack for vST‑beta diagnostics.

---

# 5. Prepare for vST‑Beta Diagnostics (Reserved)

Backend services can already shape payloads for future validators.

### JavaScript Example

```js
await client.validate({
  system_map: { services: ["auth", "api", "db"] },
  flows: [],
  constraints: []
});
```

### Python Example

```python
from rtt_sdk import build_validate_payload

payload = build_validate_payload(
    system_map={"services": ["auth", "api", "db"]},
    flows=[],
    constraints=[]
)

client.validate(payload)
```

These endpoints currently return placeholder responses but define the stable API surface.

---

# 6. Recommended Integration Patterns

### A. Microservices  
Each service sends:

- startup beacon  
- periodic heartbeat  
- shutdown beacon  
- optional profile  

### B. Monolithic Backends  
Send:

- per‑module heartbeats  
- per‑endpoint drift signals  
- system‑level topology payloads  

### C. Datacenters / Research Labs  
Use:

- `/validate` for coherence  
- `/corridor` for flow alignment  
- `/topology` for triadic decomposition  

This is the earliest path to vST‑beta adoption.

---

# 7. Verification Checklist

Your backend is RTT‑Inside ready if:

- [ ] RTTClient is configured  
- [ ] periodic beacons are sent  
- [ ] service profile is registered  
- [ ] logs show RTT events  
- [ ] observability stack receives RTT signals  
- [ ] diagnostics payloads can be generated  

This ensures smooth migration to future vST validators.

---

# 8. Where to Go Next

- **RTT API Docs:** `docs/api/rtt/`  
- **SDK Reference:** `docs/rtt-sdk/README.md`  
- **Quick‑Start Guide:** `docs/rtt-sdk/quickstart.md`  
- **Router Overview:** `docs/api/rtt/router.md`  

These documents provide deeper detail for advanced integrations.
