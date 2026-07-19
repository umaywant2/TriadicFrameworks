## 📦 **RTT Client SDK (Outline)**  

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

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

*JavaScript + Python editions*

The SDK provides a stable, versioned interface for interacting with the RTT API:

- sending beacon events  
- managing site profiles  
- preparing for vST‑beta diagnostics  
- enabling RTT‑Inside integrations  

The SDK does **not** expose substrate logic.  
It defines the *contract*, not the implementation.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

# 🟦 **JavaScript SDK Outline**  
*(Node + Browser compatible)*

```
rtt-sdk/
├── package.json
├── src/
│   ├── index.js
│   ├── client.js
│   ├── beacon.js
│   ├── profile.js
│   └── diagnostics.js
└── README.md
```

## `src/index.js`

```js
import { RTTClient } from "./client.js";

export default {
  RTTClient
};
```

---

## `src/client.js`

```js
export class RTTClient {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || "https://www.triadicframeworks.org/api/rtt";
    this.version = "0.1.0";
  }

  async beacon(payload) {
    const res = await fetch(`${this.baseUrl}/beacon`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async getProfile(site) {
    const res = await fetch(`${this.baseUrl}/profile/${site}`);
    return res.json();
  }

  async setProfile(site, profile) {
    const res = await fetch(`${this.baseUrl}/profile/${site}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile)
    });
    return res.json();
  }

  // Diagnostics (reserved)
  async validate(payload) {
    const res = await fetch(`${this.baseUrl}/validate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async corridor(payload) {
    const res = await fetch(`${this.baseUrl}/corridor`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async topology(payload) {
    const res = await fetch(`${this.baseUrl}/topology`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }
}
```

---

## Example Usage

```js
import RTT from "rtt-sdk";

const client = new RTT.RTTClient();

await client.beacon({
  site: "example.com",
  event: "page_load",
  ts: new Date().toISOString()
});
```

---

# 🐍 **Python SDK Outline**

```
rtt_sdk/
├── __init__.py
├── client.py
├── beacon.py
├── profile.py
└── diagnostics.py
```

---

## `client.py`

```python
import requests
import json

class RTTClient:
    def __init__(self, base_url="https://www.triadicframeworks.org/api/rtt"):
        self.base_url = base_url
        self.version = "0.1.0"

    def beacon(self, payload):
        r = requests.post(f"{self.base_url}/beacon", json=payload)
        return r.json()

    def get_profile(self, site):
        r = requests.get(f"{self.base_url}/profile/{site}")
        return r.json()

    def set_profile(self, site, profile):
        r = requests.post(f"{self.base_url}/profile/{site}", json=profile)
        return r.json()

    # Diagnostics (reserved)
    def validate(self, payload):
        r = requests.post(f"{self.base_url}/validate", json=payload)
        return r.json()

    def corridor(self, payload):
        r = requests.post(f"{self.base_url}/corridor", json=payload)
        return r.json()

    def topology(self, payload):
        r = requests.post(f"{self.base_url}/topology", json=payload)
        return r.json()
```

---

## Example Usage

```python
from rtt_sdk.client import RTTClient

client = RTTClient()

resp = client.beacon({
    "site": "example.com",
    "event": "page_load",
    "ts": "2026-01-19T14:22:00Z"
})

print(resp)
```

---

# 🎯 Design Principles

Both SDKs follow the same structural rules:

- **Stable versioning** (`0.1.0` for early adopters)  
- **Minimal surface** (beacon, profile, diagnostics)  
- **No substrate exposure**  
- **Forward‑compatible with vST**  
- **Drop‑in simplicity**  

This is the exact shape you want for a future ecosystem:  
clear, predictable, and ready for expansion.
