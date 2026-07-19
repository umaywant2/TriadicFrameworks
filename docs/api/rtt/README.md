# RTT API (Beta) 

- [`RTT_API_module.json`](RTT_API_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🛰️API%20Stable-📡Beacon%20Ready-4c8eda?style=for-the-badge" alt="🛰️API Stable | 📡Beacon Ready"/>

The RTT API provides a minimal, stable, forward‑compatible interface for sites, services, extensions, and research tools that want to participate in the RTT‑Inside ecosystem. It defines the *shape* of [RTT](https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html)/[vST](https://zenodo.org/communities/vst) interactions without exposing internal substrate logic.

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

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

