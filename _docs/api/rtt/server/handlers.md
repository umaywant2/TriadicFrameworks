# RTT API Handlers (Beta)

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
