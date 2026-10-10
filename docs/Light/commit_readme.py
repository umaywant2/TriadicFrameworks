#!/usr/bin/env python3
"""
TriadicFrameworks — Commit docs/Light/README.md
Run: python3 commit_readme.py
"""

import base64, json, urllib.request, urllib.error

TOKEN  = "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"
REPO   = "umaywant2/TriadicFrameworks"
BRANCH = "main"
PATH   = "docs/Light/README.md"

CONTENT = '''# Light
### TriadicFrameworks Canon · Capstone Field Module

> *"Light is not illumination. Light is the universe\'s most ancient carrier of field structure, gradient behavior, and metabolic potential."*

Light is the **capstone** of the TriadicFrameworks single-field sequence — the field that ties stellar physics to biospheric metabolism, gradient theory to organism scale, and substrate theory to artificial habitats.

This module is not about photons, brightness, or illumination.  
**Light is information** — the universe\'s original communication protocol.

---

## Sections

| # | File | What it establishes |
|---|---|---|
| — | [index.md](index.md) | Module hub · reading order · core definitions · forward linkage |
| 01 | [01_light_regime_epochs.md](01_light_regime_epochs.md) | The four spectral epochs that shaped life on Earth |
| 02 | [02_spectral_fingerprint_theory.md](02_spectral_fingerprint_theory.md) | The structural grammar of a light regime |
| 03 | [03_biospheric_scaling_law.md](03_biospheric_scaling_law.md) | Why light — not biology — determines organism size |
| 04 | [04_gradient_light_coupling.md](04_gradient_light_coupling.md) | The Gravity → Pressure → Light field triad |
| 05 | [05_light_substrate_engineering.md](05_light_substrate_engineering.md) | Building controlled spectral field environments |
| 06 | [06_stellar_interior_mapping.md](06_stellar_interior_mapping.md) | How stellar interiors generate spectral fingerprints |
| 07 | [07_artificial_light_regimes.md](07_artificial_light_regimes.md) | Programmable spectral environments (ALR-A, B, C) |
| 08 | [08_substrate_safety_protocols.md](08_substrate_safety_protocols.md) | Five-domain safety architecture for light substrates |
| 09 | [09_regime_transition_architecture.md](09_regime_transition_architecture.md) | Safe, gradient-aligned transitions between spectral regimes |
| 10 | [10_light_field_applications.md](10_light_field_applications.md) | Integration with the Unified Field, RTT, and future systems |
| — | [capture_the_light.md](capture_the_light.md) | Source capture file |

---

## The Core Chain

```
STELLAR INTERIOR
      │ generates
      ▼
SPECTRAL FINGERPRINT
      │ filtered through
      ▼
GRAVITY → PRESSURE → LIGHT
      │ received by
      ▼
METABOLISM → ECOSYSTEMS → EVOLUTION
```

---

## Canon Position

**Predecessor modules:** Gravity · Pressure · Arrival Substrate · The Inverted Star · Atmosphere · Regime Transition Arc  
**Successor module:** [`/docs/UnifiedField/`](../UnifiedField/index.md) — Light is Field 3 in the five-field stack  
**Forward linkage:** [`/docs/RTT/`](../RTT/index.md) *(forthcoming)*

---

*TriadicFrameworks Canon · Light Module · v1.0*
'''

encoded = base64.b64encode(CONTENT.encode("utf-8")).decode("utf-8")

payload = json.dumps({
    "message": "Add Light Module README.md",
    "content": encoded,
    "branch": BRANCH
}).encode("utf-8")

url = f"https://api.github.com/repos/{REPO}/contents/{PATH}"
req = urllib.request.Request(url, data=payload, method="PUT")
req.add_header("Authorization", f"token {TOKEN}")
req.add_header("Content-Type", "application/json")
req.add_header("Accept", "application/vnd.github+json")
req.add_header("User-Agent", "TriadicFrameworks-bot")

try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
        print("SUCCESS")
        print("Live at:", result["content"]["html_url"])
except urllib.error.HTTPError as e:
    print(f"ERROR {e.code}: {e.read().decode()}")
