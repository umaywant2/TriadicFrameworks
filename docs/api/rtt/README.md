# RTT API (Beta)
The RTT API provides a lightweight, forward‑compatible interface for sites, services, and tools that want to participate in the RTT‑Inside ecosystem. These endpoints support early structural awareness, coherence sampling, and resonance‑time telemetry while the full vST substrate remains in research.

This API is intentionally minimal. It defines the *shape* of RTT interactions without exposing any internal substrate logic.

---

## Overview
The RTT API currently supports three categories of interaction:

1. **Beacon Events**  
   Lightweight POST events sent by clients (e.g., `rtt.js`) to register page loads, visibility changes, or structural snapshots.

2. **Site Profiles**  
   Optional metadata endpoints for sites that want to declare RTT‑Inside capabilities.

3. **Diagnostics (Future)**  
   Reserved endpoints for vST‑beta validation, structural drift analysis, and corridor alignment.

All endpoints are versioned and stable for early adopters.

---

## Base URL
```
https://www.triadicframeworks.org/api/rtt
```

---

## 1. Beacon Endpoint
Clients send small, anonymous packets describing page‑level structural signals.

### **POST /beacon**
Send a single RTT event.

#### Example Request
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

#### Response
```json
{ "status": "ok" }
```

The server may ignore or aggregate data silently. No guarantees are made about storage or processing.

---

## 2. Site Profile Endpoint (Optional)
Sites may declare RTT‑Inside capabilities using a simple JSON manifest.

### **GET /profile/{site}**
Returns the RTT profile for a site if one exists.

### **POST /profile/{site}**
Register or update a site’s RTT profile.

#### Example Profile
```json
{
  "rtt_version": "1.0",
  "supports": ["coherence", "corridor", "drift"],
  "contact": "ops@example.com"
}
```

---

## 3. Diagnostics (Reserved)
These endpoints are placeholders for future vST‑beta features. They are not active yet.

### **POST /validate**
Submit a structural map for coherence and drift analysis.

### **POST /corridor**
Submit flow data for corridor alignment checks.

### **POST /topology**
Submit system topology for triadic decomposition.

These endpoints will activate once the vST public research layer is ready.

---

## Client Integration
The recommended integration path is the `rtt.js` snippet:

```html
<script src="https://www.triadicframeworks.org/rtt.js" data-site="example.com"></script>
```

This script automatically sends beacon events and exposes a minimal RTT client API.

---

## Goals
The RTT API is designed to:

- provide a stable surface for early adopters  
- support structural awareness without revealing internal substrate logic  
- prepare the ecosystem for vST validators  
- allow sites and tools to declare RTT‑Inside compatibility  
- evolve without breaking existing integrations  

This API is intentionally conservative. It defines the handshake, not the substrate.

---

## Status
**Beta.**  
Endpoints may expand, but existing shapes will remain stable.

For questions or early adopter coordination, contact the TriadicFrameworks maintainers.
