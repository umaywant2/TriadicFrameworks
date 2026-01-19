# RTT API Router (Beta)
This document describes how the RTT API endpoints are wired together into a single routing surface.  
It is framework‑agnostic and focuses on the structural flow of requests through the RTT API.

The router defines three endpoint families:

1. **Beacon** — lightweight structural signals  
2. **Profile** — RTT‑Inside site declarations  
3. **Diagnostics** — reserved vST‑beta endpoints  

Each family maps to a dedicated handler module.

---

## Router Overview

```
/api/rtt
│
├── POST /beacon          → beacon_handler.handleBeacon
│
├── GET  /profile/{site}  → profile_handler.getProfile
└── POST /profile/{site}  → profile_handler.setProfile

# Reserved (inactive)
├── POST /validate        → diagnostics_handler.validate
├── POST /corridor        → diagnostics_handler.corridor
└── POST /topology        → diagnostics_handler.topology
```

All endpoints are version‑stable and safe for early adopters.

---

## Example Router (Pseudo‑Code)

```js
import { handleBeacon } from "./server/beacon_handler.js";
import { getProfile, setProfile } from "./server/profile_handler.js";
import {
  validate,
  corridor,
  topology
} from "./server/diagnostics_handler.js";

export function registerRTTRoutes(app) {
  // Beacon events
  app.post("/api/rtt/beacon", handleBeacon);

  // Site profiles
  app.get("/api/rtt/profile/:site", (req, res) =>
    getProfile(req, res, req.params.site)
  );
  app.post("/api/rtt/profile/:site", (req, res) =>
    setProfile(req, res, req.params.site)
  );

  // Diagnostics (reserved)
  app.post("/api/rtt/validate", validate);
  app.post("/api/rtt/corridor", corridor);
  app.post("/api/rtt/topology", topology);
}
```

This example uses a generic `app` object (Express‑style), but the structure applies to any server framework.

---

## Routing Philosophy

The RTT router is designed to:

- keep endpoint families cleanly separated  
- avoid coupling between handlers  
- maintain stable URLs for early adopters  
- allow future vST validators to slot in without breaking changes  
- keep the API surface minimal and predictable  

The router defines the *shape* of the RTT API, not the substrate logic behind it.

---

## Future Extensions

The router may eventually include:

- `/events` for SSE/WebSocket structural streams  
- `/corridors` for RTT corridor introspection  
- `/vst/*` for full validator surfaces  
- `/metrics` for RTT‑Inside observability  

These will be added without altering existing endpoints.

---

## Status

**Beta.**  
Routing is stable, but handler behavior may evolve as the RTT ecosystem grows.
