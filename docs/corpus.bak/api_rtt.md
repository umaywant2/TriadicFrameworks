api_rtt 
# Beacon Endpoint
The beacon endpoint provides the simplest RTT‑Inside integration path.  
Clients such as `rtt.js` send lightweight, anonymous structural signals that help establish early coherence, drift, and clarity patterns across participating sites.

This endpoint is intentionally minimal. It defines the handshake, not the substrate.

---

## POST /beacon

Send a single RTT event.

### Request Body

```json
{
  "site": "example.com",
  "session": "rtt-abc123",
  "event": "page_load",
  "ts": "2026-01-19T14:22:00Z",
  "structure": {
    "url": "https://example.com",
    "title": "Home",
    "nav_count": 1,
    "main_count": 1,
    "form_count": 0,
    "button_count": 3,
    "dom_nodes": 142
  }
}
```

### Response

```json
{ "status": "ok" }
```

The server may aggregate, discard, or analyze the payload silently.  
No guarantees are made about storage or processing.

---

## Purpose

Beacon events allow RTT to:

- observe structural patterns across sites  
- detect drift or coherence changes  
- prepare for future vST validators  
- support RTT‑Inside browser extensions and tools  

This endpoint is safe, low‑friction, and suitable for all early adopters.
# **client.md — Interacting with the RTT API Router**

This document describes how clients, services, and tools can interact with the RTT API.  
It provides examples for:

- command‑line usage (`curl`)  
- browser‑side JavaScript  
- Node/server‑to‑server integrations  

All examples target the canonical RTT API surface:

```
/api/rtt/beacon
/api/rtt/profile/{site}
/api/rtt/validate
/api/rtt/corridor
/api/rtt/topology
```

The diagnostics endpoints are placeholders but included for completeness.

---

# 1. Using `curl`

## Send a Beacon Event

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/beacon \
  -H "Content-Type: application/json" \
  -d '{
        "site": "example.com",
        "session": "rtt-abc123",
        "event": "page_load",
        "ts": "2026-01-19T14:22:00Z",
        "structure": {
          "url": "https://example.com",
          "title": "Home",
          "nav_count": 1,
          "main_count": 1,
          "form_count": 0,
          "button_count": 3,
          "dom_nodes": 142
        }
      }'
```

---

## Get a Site Profile

```bash
curl https://www.triadicframeworks.org/api/rtt/profile/example.com
```

---

## Set a Site Profile

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/profile/example.com \
  -H "Content-Type: application/json" \
  -d '{
        "rtt_version": "1.0",
        "supports": ["coherence"],
        "contact": "ops@example.com"
      }'
```

---

## Call a Diagnostics Endpoint (Reserved)

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/validate \
  -H "Content-Type: application/json" \
  -d '{"system_map": {}, "flows": [], "constraints": []}'
```

---

# 2. JavaScript (Browser)

## Sending a Beacon Event Manually

```js
fetch("https://www.triadicframeworks.org/api/rtt/beacon", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    site: "example.com",
    session: "rtt-" + Math.random().toString(36).slice(2),
    event: "manual_ping",
    ts: new Date().toISOString(),
    structure: {
      url: window.location.href,
      title: document.title,
      nav_count: document.querySelectorAll("nav").length,
      dom_nodes: document.getElementsByTagName("*").length
    }
  })
});
```

---

## Using the `rtt.js` Global API

If the site includes:

```html
<script src="https://www.triadicframeworks.org/rtt.js" data-site="example.com"></script>
```

Then:

```js
// Send a manual ping
RTT.ping("user_action");

// Get a structural snapshot
const snapshot = RTT.getStructureSnapshot();
console.log(snapshot);
```

---

# 3. JavaScript (Node / Server‑to‑Server)

## Sending a Beacon Event

```js
import fetch from "node-fetch";

async function sendBeacon() {
  const payload = {
    site: "backend-service",
    session: "srv-" + Date.now(),
    event: "heartbeat",
    ts: new Date().toISOString(),
    structure: {
      url: "internal://service",
      title: "Service Node",
      dom_nodes: 0
    }
  };

  await fetch("https://www.triadicframeworks.org/api/rtt/beacon", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
}

sendBeacon();
```

---

## Setting a Profile from a Backend

```js
import fetch from "node-fetch";

await fetch("https://www.triadicframeworks.org/api/rtt/profile/myservice", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    rtt_version: "1.0",
    supports: ["coherence", "drift"],
    contact: "infra@example.com"
  })
});
```

---

## Calling Diagnostics (Future‑Ready)

```js
import fetch from "node-fetch";

const response = await fetch("https://www.triadicframeworks.org/api/rtt/validate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    system_map: { services: ["auth", "api", "db"] },
    flows: [],
    constraints: []
  })
});

const result = await response.json();
console.log(result);
```

---

# 4. Integration Patterns

## A. Browser Extensions  
Extensions can:

- listen for navigation events  
- collect structural snapshots  
- send periodic beacons  
- annotate pages with RTT clarity indicators  

They use the same `/beacon` endpoint.

---

## B. Web Services  
Services can:

- declare RTT‑Inside support via `/profile/{site}`  
- send periodic structural heartbeats  
- prepare for vST‑beta diagnostics  

---

## C. Datacenters / Research Labs  
These clients will eventually use:

- `/validate` for coherence  
- `/corridor` for flow alignment  
- `/topology` for triadic decomposition  

The API surface is stable even if the internals are not yet active.

---

# 5. Summary

This document provides:

- `curl` examples  
- browser JavaScript examples  
- Node/server‑to‑server examples  
- integration patterns for extensions, services, and datacenters  

The RTT API is intentionally minimal and stable, allowing early adopters to integrate now while the vST substrate continues to evolve.
# Diagnostics Endpoints (Reserved)
The diagnostics endpoints define the future surface of vST‑beta validation.  
These endpoints are placeholders: they establish the API shape without exposing substrate logic.

They will activate once the public vST research layer is ready.

---

## POST /validate

Submit a structural map for coherence and drift analysis.

### Example Request

```json
{
  "system_map": {},
  "flows": [],
  "constraints": []
}
```

### Example Response

```json
{
  "status": "not_available",
  "message": "vST-beta diagnostics are not yet active"
}
```

---

## POST /corridor

Submit flow data for corridor alignment checks.

### Example Response

```json
{
  "status": "not_available",
  "message": "corridor diagnostics are not yet active"
}
```

---

## POST /topology

Submit system topology for triadic decomposition.

### Example Response

```json
{
  "status": "not_available",
  "message": "topology diagnostics are not yet active"
}
```

---

## Purpose

These endpoints will eventually support:

- structural coherence validation  
- drift vector analysis  
- corridor alignment  
- triadic decomposition of systems  
- full‑stack clarity evaluation  

They exist now so early adopters can prepare their tooling and workflows.
# Site Profile Endpoint
The profile endpoint allows sites and services to declare RTT‑Inside capabilities.  
Profiles are optional but recommended for platforms that want deeper structural alignment or future vST‑beta features.

A profile is a simple JSON manifest describing what the site supports.

---

## GET /profile/{site}

Retrieve the RTT profile for a site.

### Example Response

```json
{
  "site": "example.com",
  "profile": {
    "rtt_version": "1.0",
    "supports": ["coherence", "corridor", "drift"],
    "contact": "ops@example.com"
  }
}
```

If no profile exists, `profile` will be `null`.

---

## POST /profile/{site}

Register or update a site’s RTT profile.

### Example Request

```json
{
  "rtt_version": "1.0",
  "supports": ["coherence"],
  "contact": "admin@example.com"
}
```

### Response

```json
{ "status": "ok" }
```

---

## Purpose

Profiles allow RTT to:

- recognize RTT‑Inside participants  
- enable optional features (coherence, drift, corridor)  
- support future vST validators  
- provide site‑specific diagnostics or insights  

Profiles are stable, human‑readable, and versioned for long‑term compatibility.
# RTT API (Beta)

The RTT API provides a minimal, stable, forward‑compatible interface for sites, services, extensions, and research tools that want to participate in the RTT‑Inside ecosystem. It defines the *shape* of [RTT](https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html)/[vST](https://zenodo.org/communities/vst) interactions without exposing internal substrate logic.

This API supports early structural awareness, coherence sampling, and future vST‑beta diagnostics.

---

## Endpoint Families

1. **Beacon** — lightweight structural signals  
2. **Profile** — RTT‑Inside site declarations  
3. **Diagnostics** — reserved vST‑beta endpoints  

All endpoints are version‑stable and safe for early adopters.

---

## Base URL

```
https://www.triadicframeworks.org/api/rtt
```

---

## Beacon Endpoint

### POST `/beacon`

Send a single RTT event.

Example:

```json
{
  "site": "example.com",
  "session": "rtt-abc123",
  "event": "page_load",
  "ts": "2026-01-19T14:22:00Z",
  "structure": {
    "url": "https://example.com",
    "title": "Home",
    "nav_count": 1,
    "main_count": 1,
    "form_count": 0,
    "button_count": 3,
    "dom_nodes": 142
  }
}
```

Response:

```json
{ "status": "ok" }
```

---

## Profile Endpoint

### GET `/profile/{site}`  
Retrieve a site’s RTT profile.

### POST `/profile/{site}`  
Register or update a site’s RTT profile.

Example:

```json
{
  "rtt_version": "1.0",
  "supports": ["coherence", "drift"],
  "contact": "ops@example.com"
}
```

---

## Diagnostics Endpoints (Reserved)

These endpoints define the future vST‑beta validator surface.

- POST `/validate`
- POST `/corridor`
- POST `/topology`

All currently return placeholder responses.

---

## Router Overview

```
/api/rtt
│
├── POST /beacon
│
├── GET  /profile/{site}
└── POST /profile/{site}
│
├── POST /validate      (reserved)
├── POST /corridor      (reserved)
└── POST /topology      (reserved)
```

---

## Status

**Beta.**  
Endpoint shapes are stable; handler behavior may evolve as the RTT ecosystem grows.

# RTT API Router (Beta)
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
```json

```
```json

```
```json

```
```javascript
// beacon_handler.js — minimal RTT beacon handler (beta)

export async function handleBeacon(req, res) {
  try {
    const payload = await req.json();

    // TODO: aggregate, store, or ignore payload
    // This handler defines the shape, not the substrate logic.

    res.json({ status: "ok" });
  } catch (err) {
    res.status(400).json({ error: "invalid_request" });
  }
}
```
```javascript
// diagnostics_handler.js — vST-beta diagnostics placeholders

export async function validate(req, res) {
  res.json({
    status: "not_available",
    message: "vST-beta validation is not yet active"
  });
}

export async function corridor(req, res) {
  res.json({
    status: "not_available",
    message: "corridor diagnostics are not yet active"
  });
}

export async function topology(req, res) {
  res.json({
    status: "not_available",
    message: "topology diagnostics are not yet active"
  });
}
```
# RTT API Handlers (Beta)

This document describes the server-side handler modules used by the RTT API router.  
Handlers are intentionally minimal and do not implement substrate logic.  
They define the *shape* of RTT interactions for early adopters.

---

## Beacon Handler

**File:** `beacon_handler.js`  
**Endpoint:** `POST /beacon`  
Accepts lightweight RTT events from clients such as `rtt.js`, browser extensions, or backend services.

---

## Profile Handler

**File:** `profile_handler.js`  
**Endpoints:**  
- `GET /profile/{site}`  
- `POST /profile/{site}`  

Stores or retrieves RTT‑Inside site profiles.

---

## Diagnostics Handler (Reserved)

**File:** `diagnostics_handler.js`  
**Endpoints:**  
- `POST /validate`  
- `POST /corridor`  
- `POST /topology`  

These endpoints define the future vST‑beta validator surface.  
All currently return placeholder responses.

---

## Routing Philosophy

Handlers are:

- decoupled  
- stable  
- minimal  
- forward‑compatible  

They provide a predictable API surface while the vST substrate evolves.
```javascript
// profile_handler.js — minimal RTT profile handler (beta)

const profiles = new Map();

export async function getProfile(req, res, site) {
  const profile = profiles.get(site) || null;
  res.json({ site, profile });
}

export async function setProfile(req, res, site) {
  try {
    const profile = await req.json();
    profiles.set(site, profile);
    res.json({ status: "ok" });
  } catch (err) {
    res.status(400).json({ error: "invalid_profile" });
  }
}
```
```javascript
// router.js — RTT API router (beta)
// Wires all RTT endpoint families into a single routing surface.

import { handleBeacon } from "./beacon_handler.js";
import { getProfile, setProfile } from "./profile_handler.js";
import {
  validate,
  corridor,
  topology
} from "./diagnostics_handler.js";

export function registerRTTRoutes(app) {
  // Beacon events
  app.post("/api/rtt/beacon", handleBeacon);

  // Site profiles
  app.get("/api/rtt/profile/:site", (req, res, site) =>
    getProfile(req, res, site)
  );

  app.post("/api/rtt/profile/:site", (req, res, site) =>
    setProfile(req, res, site)
  );

  // Diagnostics (reserved)
  app.post("/api/rtt/validate", validate);
  app.post("/api/rtt/corridor", corridor);
  app.post("/api/rtt/topology", topology);
}
```
```javascript
// server.js — minimal RTT API server (beta)
// This file wires the RTT router into a tiny HTTP server.
// It is intentionally lightweight and suitable for local testing.

import http from "http";
import { registerRTTRoutes } from "./router.js";

// Simple Express‑style micro‑framework
function createApp() {
  const routes = [];

  function addRoute(method, path, handler) {
    routes.push({ method, path, handler });
  }

  const app = {
    get: (path, handler) => addRoute("GET", path, handler),
    post: (path, handler) => addRoute("POST", path, handler),
    routes
  };

  app.listen = function (port, cb) {
    const server = http.createServer(async (req, res) => {
      const match = routes.find(r =>
        r.method === req.method &&
        matchPath(r.path, req.url)
      );

      if (!match) {
        res.writeHead(404, { "Content-Type": "application/json" });
        return res.end(JSON.stringify({ error: "not_found" }));
      }

      const params = extractParams(match.path, req.url);

      // Minimal request wrapper
      const reqWrapper = {
        method: req.method,
        url: req.url,
        json: () =>
          new Promise((resolve, reject) => {
            let body = "";
            req.on("data", chunk => (body += chunk));
            req.on("end", () => {
              try {
                resolve(JSON.parse(body || "{}"));
              } catch (e) {
                reject(e);
              }
            });
          })
      };

      // Minimal response wrapper
      const resWrapper = {
        status: code => {
          res.statusCode = code;
          return resWrapper;
        },
        json: obj => {
          res.writeHead(res.statusCode || 200, {
            "Content-Type": "application/json"
          });
          res.end(JSON.stringify(obj));
        }
      };

      match.handler(reqWrapper, resWrapper, ...params);
    });

    server.listen(port, cb);
  };

  return app;
}

// Path matching helpers
function matchPath(routePath, url) {
  const routeParts = routePath.split("/");
  const urlParts = url.split("?")[0].split("/");

  if (routeParts.length !== urlParts.length) return false;

  return routeParts.every((part, i) =>
    part.startsWith(":") || part === urlParts[i]
  );
}

function extractParams(routePath, url) {
  const routeParts = routePath.split("/");
  const urlParts = url.split("?")[0].split("/");

  return routeParts
    .map((part, i) => (part.startsWith(":") ? urlParts[i] : null))
    .filter(Boolean);
}

// Create and start the server
const app = createApp();
registerRTTRoutes(app);

app.listen(3000, () => {
  console.log("RTT API server running on http://localhost:3000");
});
```
