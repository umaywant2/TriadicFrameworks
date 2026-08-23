# 🧩 **How RTTcodes Work Internally**  
*A clear, canonical explainer for contributors and tool authors.*

RTTcodes are a structured, QR‑compatible metadata layer that bind any artifact
to its canonical TriadicFrameworks identity. Internally, an RTTcode is built
from three cooperating layers:

1. **Payload Layer** (JSON metadata)
2. **Encoding Layer** (URL + token)
3. **QR Layer** (machine‑readable matrix)

Each layer is independent but composable, making RTTcodes portable across
languages, tools, and documentation systems.

---

## 1. Payload Layer (JSON)

The payload is a small, schema‑validated JSON object:

```json
{
  "domain": "rtt",
  "artifact_type": "paper",
  "version": "v2.1.0",
  "triad": {
    "f_R": "1.00",
    "tau_R": "144ms",
    "Q_R": "0.97"
  },
  "url": "https://triadicframeworks.org/docs/rtt/"
}
```

This layer defines:

- **domain** — which part of the ecosystem the artifact belongs to  
- **artifact_type** — what kind of thing it is  
- **version** — semantic version  
- **triad** — optional resonance‑time metadata  
- **url** — canonical home of the artifact  

The payload is validated using the RTTcode JSON Schema.

---

## 2. Encoding Layer (URL + Token)

The payload is transformed into a compact, ASCII‑safe token:

```
v2.1.0-f1.00-t144ms-Q0.97
```

Then embedded into a URL:

```
https://triadicframeworks.org/rttcode?rtt=v2.1.0-f1.00-t144ms-Q0.97
```

This URL is what the QR code encodes.

The encoding layer ensures:

- stability  
- portability  
- compatibility with all QR scanners  
- future extensibility  

---

## 3. QR Layer (Matrix)

The URL is encoded as a QR code using:

- **Error Correction Level H** (to tolerate overlays)
- **Square layout**
- **Minimum 2‑module quiet zone**

The QR is then optionally styled using domain‑specific motifs:

- RTT → resonance waves, triadic nodes  
- SET → field lines, anisotropic vectors  
- Substrate → lattice geometry  
- Observer → frame grids  
- Governance → layered bands  

The QR remains fully scannable because overlays respect safe zones.

---

## Internal Flow Summary

```
JSON Payload
     ↓ validate
URL + Token
     ↓ encode
QR Matrix
     ↓ style (optional)
RTTcode PNG
```

This modular design keeps RTTcodes simple, robust, and future‑proof.

![RTT Domain](https://img.shields.io/badge/RTT-Resonance--Time%20Domain-F6B800?style=flat-square&logo=qrcode&logoColor=1a1a1a)![Substrate Domain](https://img.shields.io/badge/Substrate-Structural%20Domain-003B73?style=flat-square&logo=qrcode&logoColor=7FD4FF)![Governance Domain](https://img.shields.io/badge/Governance-Decision%20Layer-145A32?style=flat-square&logo=qrcode&logoColor=F1C40F)![Docs Domain](https://img.shields.io/badge/Docs-Documentation%20Domain-6C7A89?style=flat-square&logo=qrcode&logoColor=ffffff)![Other Domain](https://img.shields.io/badge/Other-Extended%20Domain-1a1a1a?style=flat-square&logo=qrcode&logoColor=ffffff)
