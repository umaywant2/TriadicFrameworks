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
