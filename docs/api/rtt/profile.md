# Site Profile Endpoint
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
