# **client.md — Interacting with the RTT API Router**

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
