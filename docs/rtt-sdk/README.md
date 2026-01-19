# RTT SDK (Beta)

The RTT SDK provides a minimal, stable, and forward‑compatible interface for interacting with the RTT API. It supports early RTT‑Inside integrations across browsers, services, and research environments while the full vST substrate remains in development.

This SDK defines the **shape** of RTT interactions without exposing internal substrate logic. It is safe for early adopters and suitable for experimentation, prototyping, and structural‑awareness tooling.

---

## Features

- Send RTT beacon events  
- Create and validate RTT site profiles  
- Prepare vST‑beta diagnostics payloads  
- Unified client for all RTT API endpoints  
- Identical API surface across JavaScript and Python  
- Stable versioning (`0.1.0`) for long‑term compatibility  

---

## Directory Structure

```
docs/rtt-sdk/
├── beacon.js
├── beacon.py
├── client.js
├── client.py
├── diagnostics.js
├── diagnostics.py
├── index.js
├── profile.js
├── profile.py
└── __init__.py
```

Each file provides a minimal, well‑defined interface for its domain:

- **beacon** — session IDs, structural snapshots, beacon payloads  
- **profile** — RTT‑Inside profile creation and validation  
- **diagnostics** — vST‑beta payload builders (placeholders)  
- **client** — unified RTT API client (JS + Python)  
- **index / \_\_init\_\_** — clean package exports  

---

# JavaScript Usage

## Install (local copy)

Place the SDK folder in your project and import:

```js
import { RTTClient } from "./rtt-sdk/index.js";

const client = new RTTClient();

await client.beacon({
  site: "example.com",
  event: "page_load",
  ts: new Date().toISOString()
});
```

## Build a Beacon Payload

```js
import { build_beacon_payload, create_session_id } from "./rtt-sdk/beacon.js";

const payload = build_beacon_payload({
  site: "example.com",
  session: create_session_id(),
  event: "manual_ping"
});
```

## Manage Profiles

```js
import { create_profile } from "./rtt-sdk/profile.js";

const profile = create_profile({
  version: "1.0",
  supports: ["coherence"],
  contact: "ops@example.com"
});

await client.setProfile("example.com", profile);
```

---

# Python Usage

## Import

```python
from rtt_sdk import RTTClient, build_beacon_payload, create_session_id
```

## Send a Beacon

```python
client = RTTClient()

payload = build_beacon_payload(
    site="example.com",
    session=create_session_id(),
    event="page_load"
)

resp = client.beacon(payload)
print(resp)
```

## Create a Profile

```python
from rtt_sdk import create_profile

profile = create_profile(
    version="1.0",
    supports=["coherence"],
    contact="ops@example.com"
)

client.set_profile("example.com", profile)
```

---

# Diagnostics (Reserved)

The following methods exist for future vST‑beta validators:

- `validate(payload)`  
- `corridor(payload)`  
- `topology(payload)`  

These endpoints currently return placeholder responses but define the stable API surface for future structural analysis.

---

# API Reference

Full RTT API documentation is available in:

```
docs/api/rtt/
```

Key files:

- **README.md** — overview of the RTT API  
- **beacon.md** — beacon endpoint  
- **profile.md** — RTT‑Inside site profiles  
- **diagnostics.md** — vST‑beta endpoint shapes  
- **router.md** — endpoint wiring and routing philosophy  

---

# Versioning

The SDK follows semantic versioning:

- **0.1.x** — early adopters, stable shapes, no substrate logic  
- **0.2.x** — vST‑beta integration  
- **1.x.x** — full validator support  

---

# Status

**Beta.**  
The SDK is stable for integration and experimentation.  
Internal substrate logic will activate as vST research becomes public.
