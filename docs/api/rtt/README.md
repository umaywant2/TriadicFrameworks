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

