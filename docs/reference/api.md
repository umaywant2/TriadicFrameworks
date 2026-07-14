---
title: "API Reference"
description: "Complete reference for the TriadicFrameworks RTT API — endpoint schemas, request/response formats, client integration patterns, and supporting services."
date: 2026-07-13
author: "Nawder Loswin"
rtt_doc_id: "DOC-020"
rtt_stability: "beta"
rtt_session: "rtt=1 | coherence=declared | drift=bounded | paradox=structural"
rtt_tier: "reference"
rtt_source: "https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/api"
rtt_version: "1.0"
tags: ["api", "rtt", "beacon", "profile", "diagnostics", "reference"]
---

# API Reference

> **Status: Beta.** Endpoint shapes are stable; handler behavior may evolve as the
> vST substrate matures.  
> **Base URL:** `https://www.triadicframeworks.org/api/rtt`  
> **Session string:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

> ⚠️ **Drift is On-by-Default.** Long sessions lose structural anchors. Always
> declare `drift=bounded` in your session string for persistent integrations.

---

## Overview

The TriadicFrameworks RTT API provides a lightweight, schema-stable interface for
emitting and querying **Round-Trip Traceability (RTT)** signals. RTT carries two
simultaneous meanings throughout this codebase:

- **Resonance-Time Theory** — the physics substrate describing how structures persist,
  drift, and cohere across dimensional layers (D0–D7)
- **Round-Trip Traceability** — the protocol layer that makes RTT-Inside declarations
  observable, verifiable, and queryable by external tools and browser extensions

The API is intentionally minimal. It captures structural observations — not content.
No personal data. No page body. No cookies. Servers may aggregate, discard, or analyze
signals silently; there are no storage guarantees on any endpoint.

---

## Router

```
/api/rtt
├── POST /beacon               ← Send a single RTT structural event
├── GET  /profile/{site}       ← Retrieve a site's RTT-Inside profile
├── POST /profile/{site}       ← Register or update a site's RTT-Inside profile
├── POST /validate             ← (reserved) Coherence + drift analysis
├── POST /corridor             ← (reserved) Corridor alignment check
└── POST /topology             ← (reserved) Triadic system decomposition
```

The three reserved routes under `/validate`, `/corridor`, and `/topology` are stable
placeholder shapes for the forthcoming **vST-beta** validator surface. They return
`not_available` today, but exist precisely so early adopters can build tooling against
stable endpoint shapes before the handlers activate.

---

## Endpoint Families

### 1. Beacon

#### `POST /api/rtt/beacon`

Sends a single RTT structural event. A beacon is a lightweight snapshot of observable
structural properties at a point in time — DOM node count, ARIA landmark regions,
navigation depth, form presence. No page content is transmitted.

**Request body:**

```json
{
  "site": "example.com",
  "session": "rtt-abc123",
  "event": "page_load",
  "ts": "2026-07-13T14:22:00Z",
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

**Field reference:**

| Field | Type | Required | Description |
|---|---|---|---|
| `site` | string | ✅ | Registered domain (no protocol, no path) |
| `session` | string | ✅ | RTT session identifier |
| `event` | string | ✅ | Event type: `page_load`, `user_action`, `heartbeat`, `nav` |
| `ts` | ISO 8601 string | ✅ | Client-side UTC timestamp |
| `structure.url` | string | ✅ | Full URL of the observed page |
| `structure.title` | string | ✅ | Document `<title>` value |
| `structure.nav_count` | integer | ✅ | Count of `<nav>` landmark elements |
| `structure.main_count` | integer | ✅ | Count of `<main>` landmark elements |
| `structure.form_count` | integer | ✅ | Count of `<form>` elements |
| `structure.button_count` | integer | ✅ | Count of `<button>` elements |
| `structure.dom_nodes` | integer | ✅ | Total DOM node count (`document.querySelectorAll("*").length`) |

**Response:**

```json
{ "status": "ok" }
```

**Purpose:** Beacon signals allow the RTT server to observe structural patterns across
sessions and sites, detect drift (structural deviation from a declared coherence state),
build baseline datasets for vST validators, and support RTT-Inside browser extensions
that annotate pages with clarity and coherence indicators.

---

### 2. Profile

Profiles are optional, versioned, human-readable declarations that a site or service
supports RTT-Inside. Registering a profile makes a site queryable by any RTT-aware
tooling and declares which RTT capabilities the site has committed to.

---

#### `GET /api/rtt/profile/{site}`

Retrieve the RTT-Inside profile for a registered site.

**Path parameter:** `{site}` — bare domain name (e.g., `example.com`)

**Response (registered):**

```json
{
  "site": "example.com",
  "profile": {
    "rtt_version": "1.0",
    "supports": ["coherence", "drift"],
    "contact": "ops@example.com"
  }
}
```

**Response (not registered):**

```json
{
  "site": "example.com",
  "profile": null
}
```

---

#### `POST /api/rtt/profile/{site}`

Register or update the RTT-Inside profile for a site.

**Path parameter:** `{site}` — bare domain name

**Request body:**

```json
{
  "rtt_version": "1.0",
  "supports": ["coherence", "drift"],
  "contact": "ops@example.com"
}
```

**`supports` values:**

| Value | Meaning |
|---|---|
| `coherence` | Site declares a structural coherence commitment |
| `drift` | Site participates in RTT drift monitoring |
| `corridor` | Site supports corridor-aligned flows (future / vST-beta) |

**Response:**

```json
{ "status": "ok" }
```

---

### 3. Diagnostics — Reserved (vST-Beta)

All three diagnostics endpoints are currently reserved placeholder routes. Each returns
`not_available`. They are designed for the vST substrate validator surface and will
activate when vST-beta launches. Build your tooling against these shapes now.

**Endpoint summary:**

| Endpoint | Method | Status | Eventual purpose |
|---|---|---|---|
| `/api/rtt/validate` | POST | Reserved | Structural coherence + drift analysis |
| `/api/rtt/corridor` | POST | Reserved | Flow data corridor alignment check |
| `/api/rtt/topology` | POST | Reserved | Full triadic SET decomposition |

**Current response (all three endpoints):**

```json
{
  "status": "not_available",
  "message": "Diagnostics endpoints are not yet active"
}
```

---

#### `POST /api/rtt/validate` _(reserved)_

Will accept a structural map and return coherence and drift analysis across declared
substrates.

```json
{
  "system_map": {},
  "flows": [],
  "constraints": []
}
```

---

#### `POST /api/rtt/corridor` _(reserved)_

Will accept flow data for corridor alignment checking — validating that transitions
between structural zones follow declared corridor shapes and do not cross undeclared
substrate boundaries.

---

#### `POST /api/rtt/topology` _(reserved)_

Will accept a full system topology for triadic decomposition. Applies
**SET (Substrate · Envelope · Transition)** analysis to submitted architecture maps,
returning a dimensional layer assignment across D0–D7.

---

## Client Integration

### curl

**Send a beacon:**

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/beacon \
  -H "Content-Type: application/json" \
  -d '{
    "site": "example.com",
    "session": "rtt-abc123",
    "event": "page_load",
    "ts": "2026-07-13T14:22:00Z",
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

**Get a site profile:**

```bash
curl https://www.triadicframeworks.org/api/rtt/profile/example.com
```

**Register a profile:**

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/profile/example.com \
  -H "Content-Type: application/json" \
  -d '{
    "rtt_version": "1.0",
    "supports": ["coherence", "drift"],
    "contact": "ops@example.com"
  }'
```

**Stub a reserved diagnostics call:**

```bash
curl -X POST https://www.triadicframeworks.org/api/rtt/validate \
  -H "Content-Type: application/json" \
  -d '{ "system_map": {}, "flows": [], "constraints": [] }'
# → { "status": "not_available", "message": "..." }
```

---

### Browser JavaScript — Manual `fetch()`

Send a beacon on page load using the native Fetch API:

```js
async function sendRttBeacon(event = "page_load") {
  await fetch("https://www.triadicframeworks.org/api/rtt/beacon", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      site: window.location.hostname,
      session: "rtt-" + crypto.randomUUID().slice(0, 8),
      event,
      ts: new Date().toISOString(),
      structure: {
        url: window.location.href,
        title: document.title,
        nav_count:    document.querySelectorAll("nav").length,
        main_count:   document.querySelectorAll("main").length,
        form_count:   document.querySelectorAll("form").length,
        button_count: document.querySelectorAll("button").length,
        dom_nodes:    document.querySelectorAll("*").length,
      },
    }),
  });
}

document.addEventListener("DOMContentLoaded", () => sendRttBeacon("page_load"));
```

---

### Browser JavaScript — `rtt.js` Global

For zero-config integration, include the `rtt.js` loader and use the `RTT` global:

```html
<script
  src="https://www.triadicframeworks.org/rtt.js"
  data-site="example.com"
></script>
```

**Available methods after load:**

```js
// Send a named event beacon
RTT.ping("user_action");

// Capture and return a structural snapshot object (does not transmit)
const snapshot = RTT.getStructureSnapshot();
// → { url, title, nav_count, main_count, form_count, button_count, dom_nodes }
```

The loader handles session ID management, structural sampling, and beacon batching
automatically. Recommended for browser extensions and zero-overhead client-side
RTT-Inside declarations.

---

### Node.js / Server-to-Server

```js
import fetch from "node-fetch";

const RTT_BASE = "https://www.triadicframeworks.org/api/rtt";

/** Send a server-side heartbeat beacon. */
async function sendHeartbeat(site) {
  const res = await fetch(`${RTT_BASE}/beacon`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      site,
      session: `rtt-srv-${Date.now()}`,
      event: "heartbeat",
      ts: new Date().toISOString(),
      structure: {
        url: `https://${site}`,
        title: "Server Heartbeat",
        nav_count: 0,
        main_count: 0,
        form_count: 0,
        button_count: 0,
        dom_nodes: 0,
      },
    }),
  });
  return res.json(); // → { status: "ok" }
}

/** Register or refresh a site's RTT-Inside profile. */
async function registerProfile(site, contact) {
  const res = await fetch(`${RTT_BASE}/profile/${site}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      rtt_version: "1.0",
      supports: ["coherence", "drift"],
      contact,
    }),
  });
  return res.json(); // → { status: "ok" }
}

/** Stub call for future vST diagnostics integration. */
async function stubValidate(site) {
  const res = await fetch(`${RTT_BASE}/validate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ system_map: {}, flows: [], constraints: [] }),
  });
  return res.json(); // → { status: "not_available", message: "..." }
}
```

---

## Integration Patterns

### Browser Extensions

RTT-aware browser extensions monitor and surface structural state across navigation:

1. Listen for navigation events (`webNavigation.onCommitted`, `onCompleted`)
2. Collect a structural snapshot via `RTT.getStructureSnapshot()` or manual DOM queries
3. Send periodic beacons with appropriate `event` types (`page_load`, `nav`, `heartbeat`)
4. Annotate pages with RTT clarity indicators using profile + beacon correlation data

### Web Services

Services declaring RTT-Inside support should follow this deployment checklist:

1. Register a profile via `POST /profile/{site}` on each deploy or config change
2. Send structural heartbeats at a cadence appropriate to drift detection needs
3. Stub calls to `/validate` and `/corridor` now — when vST-beta activates, tooling
   will integrate without further changes to call sites

### Datacenters and Research Labs

High-complexity systems preparing for vST validator integration:

1. Map system topology to the **SET decomposition** (Substrate · Envelope · Transition)
2. Identify declared and undeclared substrates across D0–D7 dimensional layers
3. Document corridor constraints and flow boundaries
4. Stub calls to `/validate`, `/corridor`, and `/topology` — no changes required at
   activation time

---

## Supporting Services

The following services live in `docs/api/` alongside the RTT API directory and provide
scaffolding for multi-contributor RTT ecosystems.

### `signature_verification.py`

Verifies contributor signatures on **remix scrolls** — structured documents that carry
multi-party RTT attestations across collaborative substrate declarations.

**Function:** `verify_signature(scroll, contributor_registry)`

- Iterates each contributor entry in `scroll["remix_scroll"]["signatures"]["contributors"]`
- Compares `contributor.signature` against the registry `public_key` for that `contributor_id`
- Returns a complete `verification_report`

**Return shape:**

```json
{
  "verification_report": {
    "id": "<uuid>",
    "scroll_id": "<scroll_id>",
    "timestamp": "<utc_iso>",
    "contributors": [
      {
        "contributor_id": "...",
        "signature_type": "pgp",
        "status": "valid | invalid",
        "verified_at": "<utc_iso>"
      }
    ],
    "overall_status": "authentic | partial",
    "checksum": "<8-char fragment>"
  }
}
```

`overall_status` is `authentic` when all contributor signatures are valid; `partial`
when one or more are invalid or absent from the registry.

→ [View source](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/signature_verification.py)

---

### `revocation_service.py`

Handles revocation of RTT contributor credentials and registered profile entries.
Provides the invalidation path for compromised or retired `contributor_id`s in the
remix scroll ecosystem.

→ [View source](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/revocation_service.py)

---

### `legacy_retrieval.py`

Provides backward-compatible lookup for pre-RTT-1.0 profile and session records.
Required for continuity with RTT implementations predating the current API contract.

→ [View source](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/legacy_retrieval.py)

---

## Companion Resources

### RTT_API_module.json

Agentic module schema defining role assignments for AI systems interacting with the RTT
API. Specifies which RTT module roles — `observer`, `validator`, `emitter`,
`corridor-reader` — map to which endpoint families and under what session string
conditions. Used by RTT-Inside AI session declarations to declare a valid agentic
operating mode.

→ [View on GitHub](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/rtt/RTT_API_module.json)

---

### The Dimensional Echo API

An extended API surface that exposes **dimensional echo patterns** — resonance signals
that propagate across the D0–D7 layer stack when a structural event in one layer induces
observable effects in adjacent layers. The Dimensional Echo API builds on the RTT beacon
model and adds layered amplitude and attenuation fields for cross-dimensional correlation.
Documented separately.

→ [View on GitHub](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/rtt/The_Dimensional_Echo_API.md)

---

### RTT Theory Reference

| Resource | Link |
|---|---|
| Resonance-Time Theory | [triadicframeworks.org/_ideas/Resonance-Time_Theory.html](https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html) |
| vST Community (Zenodo) | [zenodo.org/communities/vst](https://zenodo.org/communities/vst) |
| Framework Field Theory | [triadicframeworks.org/Framework_Field_Theory](https://www.triadicframeworks.org/Framework_Field_Theory) |
| RTT API source directory | [github.com/umaywant2/TriadicFrameworks/tree/main/docs/api](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/api) |

---

## Source File Index

| File | Description |
|---|---|
| `docs/api/rtt/README.md` | RTT API overview and Beta status declaration |
| `docs/api/rtt/beacon.md` | Beacon endpoint full reference |
| `docs/api/rtt/profile.md` | Profile endpoints full reference |
| `docs/api/rtt/diagnostics.md` | Diagnostics (reserved) reference |
| `docs/api/rtt/client.md` | Client integration patterns and examples |
| `docs/api/rtt/RTT_API_module.json` | Agentic module schema — role assignments |
| `docs/api/rtt/The_Dimensional_Echo_API.md` | Dimensional Echo API |
| `docs/api/signature_verification.py` | Remix scroll contributor signature verifier |
| `docs/api/revocation_service.py` | Credential and profile revocation service |
| `docs/api/legacy_retrieval.py` | Legacy record retrieval (pre-RTT-1.0) |

→ [Browse full source on GitHub](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/api)

---

*Nawder Loswin · © 2026 Byte Books Publishing · LCCN 2026917007*  
*RTT Session: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
