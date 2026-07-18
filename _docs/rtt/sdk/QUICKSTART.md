# **RTT‑Inside Quick‑Start Guide (Beta)**  
*A fast path for developers integrating RTT structural awareness into their sites or services.*

RTT‑Inside provides a lightweight, forward‑compatible way for websites, applications, and backend services to participate in the RTT ecosystem. These integrations support early structural awareness, coherence sampling, and future vST‑beta features.

This guide walks you through the fastest way to get RTT‑Inside running.

---

# 1. Add the RTT JavaScript Snippet (Web Integration)

The simplest way to enable RTT‑Inside on a website is to include the `rtt.js` client.

```html
<script src="https://www.triadicframeworks.org/rtt.js" data-site="example.com"></script>
```

This automatically:

- sends page‑load and visibility beacons  
- collects lightweight structural snapshots  
- registers the site with RTT  
- exposes a global `RTT` object for optional manual use  

### Optional: Manual Beacon

```js
RTT.ping("user_action");
```

### Optional: Inspect Structure

```js
console.log(RTT.getStructureSnapshot());
```

---

# 2. Declare RTT‑Inside Support (Optional but Recommended)

Add RTT metadata to your site to signal RTT‑Inside compatibility.

### Option A — HTML `<meta>` tags

```html
<meta name="rtt:coherence" content="declared">
<meta name="rtt:version" content="1.0">
```

### Option B — `/rtt.json` manifest

Create a file at the root of your site:

```
/rtt.json
```

```json
{
  "rtt_version": "1.0",
  "supports": ["coherence", "drift"],
  "contact": "ops@example.com"
}
```

This allows RTT tools and validators to recognize your site.

---

# 3. Use the RTT SDK (JavaScript or Python)

The SDK provides a clean, stable interface for interacting with the RTT API.

---

## JavaScript Example

```js
import { RTTClient } from "./rtt-sdk/index.js";

const client = new RTTClient();

await client.beacon({
  site: "example.com",
  event: "page_load",
  ts: new Date().toISOString()
});
```

---

## Python Example

```python
from rtt_sdk import RTTClient, build_beacon_payload, create_session_id

client = RTTClient()

payload = build_beacon_payload(
    site="example.com",
    session=create_session_id(),
    event="page_load"
)

resp = client.beacon(payload)
print(resp)
```

---

# 4. Register a Site Profile (Optional)

Profiles allow RTT to understand your site’s capabilities.

### JavaScript

```js
import { create_profile } from "./rtt-sdk/profile.js";

const profile = create_profile({
  version: "1.0",
  supports: ["coherence"],
  contact: "ops@example.com"
});

await client.setProfile("example.com", profile);
```

### Python

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

# 5. Prepare for vST‑Beta Diagnostics (Reserved)

These endpoints are placeholders but stable:

- `/validate`  
- `/corridor`  
- `/topology`  

You can already shape your payloads using the SDK.

### Example (Python)

```python
from rtt_sdk import build_validate_payload

payload = build_validate_payload(
    system_map={"services": ["auth", "api", "db"]},
    flows=[],
    constraints=[]
)

client.validate(payload)
```

---

# 6. Verify Integration

Once RTT‑Inside is active, you can:

- check your server logs for beacon events  
- inspect RTT API responses  
- confirm your profile is registered  
- use the SDK to send manual test events  

Everything is safe, minimal, and forward‑compatible.

---

# 7. Where to Go Next

- **RTT API Docs:** `docs/api/rtt/`  
- **SDK Reference:** `docs/rtt-sdk/README.md`  
- **Router Overview:** `docs/api/rtt/router.md`  

These documents provide deeper detail for advanced integrations.
