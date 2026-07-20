# 🏳️‍🌈 RTT/codes — A QR‑Compatible Metadata Layer 

- [`RTT_codes_module.json`](RTT_codes_module.json) — Agentic module schema role assignments

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

RTT/codes provide a universal, scannable way to identify, classify, and navigate
artifacts across the TriadicFrameworks ecosystem. They bind any artifact—
digital or physical—to its canonical documentation, lineage, and onboarding
guides.

An RTTcode is:

- **QR‑compatible** (works with any standard scanner)
- **schema‑validated** (structured metadata)
- **domain‑aware** (RTT, SET, Substrate, Observer, Governance, Docs, Other)
- **triad‑capable** (optional resonance‑time triad metadata)
- **tool‑generated** (JS and Python generators included)
- **style‑guided** (consistent visual identity across domains)

RTT/codes are designed to operate anywhere QR codes already function in science,
engineering, and documentation workflows, while adding an RTT‑native metadata
layer.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

🎯 [QuickStart Guide](https://www.triadicframeworks.org/rtt/codes/QUICKSTART.md)

## 📦 RTTcode Structure

A minimal RTTcode payload looks like:

```json
{
  "domain": "substrate",
  "artifact_type": "README",
  "version": "v1.0",
  "triad": {
    "f_R": "0.85",
    "tau_R": "120ms",
    "Q_R": "0.92"
  },
  "url": "https://triadicframeworks.org/docs/resonance-substrate-model/"
}
```

This payload is validated against the canonical schema and then encoded into a
URL+token format:

```
https://triadicframeworks.org/rttcode?substrate=v1.0-f0.85-t120ms-Q0.92
```

The generators convert this into a QR‑compatible PNG.

---

# 🌲 1. Folder Tree Diagram  
*A clean, readable map of the RTT/codes subsystem.*

```text

docs/
└── rtt/codes/
    ├── README.md
    │
    ├── schema/
    │   ├── rttcode.schema.json
    │   └── examples/
    │       ├── minimal.json
    │       ├── rtt.json
    │       ├── set.json
    │       └── substrate.json
    │
    ├── validators/
    │   ├── README.md
    │   ├── validate_js.js
    │   └── validate_python.py
    │
    ├── generators/
    │   ├── README.md
    │   ├── js/
    │   │   ├── README.md
    │   │   └── generate_rttcode.js
    │   └── python/
    │       ├── README.md
    │       └── generate_rttcode.py
    │
    ├── style/
    │   ├── README.md
    │   ├── visual-guidelines.md
    │   ├── rttcode-layout.svg
    │   └── color-domains.png
    │
    └── examples/
        ├── README.md
        ├── rtt/
        │   ├── README.md
        │   ├── payload.json
        │   └── rtt-rttcode.png
        ├── set/
        │   ├── README.md
        │   ├── payload.json
        │   └── set-rttcode.png
        └── substrate/
            ├── README.md
            ├── payload.json
            └── substrate-rttcode.png
```

## 📁 rtt/codes - Folder Overview

### [schema/](https://www.triadicframeworks.org/rtt/codes/schema/)
The canonical RTTcode JSON Schema and minimal examples.

### [validators/](https://www.triadicframeworks.org/rtt/codes/validators)
Tools that verify RTTcode payload correctness.

### [generators/](https://www.triadicframeworks.org/rtt/codes/generators)
Language‑specific RTT/codes generators (JS and Python).

### [style/](https://www.triadicframeworks.org/rtt/codes/style)
Visual guidelines, color domains, and the RTTcode layout reference.

### [examples/](https://www.triadicframeworks.org/rtt/codes/examples)
Fully generated RTT/codes for each domain, including styled PNGs.

---

## 🛠 Generating RTT/codes

RTT/codes can be generated using:

- **JavaScript** (`generators/js/generate_rttcode.js`)
- **Python** (`generators/python/generate_rttcode.py`)

Both:

- validate the payload  
- build the URL+token  
- output a QR‑compatible PNG  

See the generator READMEs for usage.

---

## 🎨 Visual Identity

RTT/codes follow a consistent visual language:

- domain‑specific color palettes  
- triadic overlay geometry  
- QR‑safe layout rules  
- optional resonance‑time motifs  

See `style/visual-guidelines.md` and `style/rttcode-layout.svg`.

---

## 📚 Examples

Each domain includes:

- a valid RTTcode JSON payload  
- a generated QR PNG  
- domain‑specific styling  

See `examples/` for RTT, SET, Substrate, and more.

---

## 🌐 Purpose

RTT/codes unify the TriadicFrameworks ecosystem by providing:

- a stable metadata layer  
- a scannable entry point into canonical docs  
- a consistent way to reference artifacts across domains  
- a bridge between physical and digital materials  

They are the “ISBN numbers” of the Resonance‑Time universe — but dynamic,
domain‑aware, and triad‑capable.

---

For contributors, tool authors, and documentation maintainers, this folder is
the authoritative reference for everything RTT/codes‑related.

![RTT/codes Badge](https://img.shields.io/badge/RTT_codes-QR%20Metadata%20Layer-00b3b8?style=flat-square&logo=qrcode&logoColor=white)![RTT/codes Badge](https://img.shields.io/badge/RTT_codes-Canonical%20Identifier-1a1a1a?style=flat-square&logo=qrcode&logoColor=white)![RTT/codes Badge](https://img.shields.io/badge/RTT_codes-Resonance--Time%20Metadata-F6B800?style=flat-square&logo=qrcode&logoColor=1a1a1a)![RTT Domain](https://img.shields.io/badge/RTT-Resonance--Time%20Domain-F6B800?style=flat-square&logo=qrcode&logoColor=1a1a1a)![SET Domain](https://img.shields.io/badge/SET-Field%20Topology%20Domain-5B2CFF?style=flat-square&logo=qrcode&logoColor=ffffff)![Substrate Domain](https://img.shields.io/badge/Substrate-Structural%20Domain-003B73?style=flat-square&logo=qrcode&logoColor=7FD4FF)![Observer Domain](https://img.shields.io/badge/Observer-Frame%20and%20Perspective-2F6F73?style=flat-square&logo=qrcode&logoColor=B0C4D4)![Governance Domain](https://img.shields.io/badge/Governance-Decision%20Layer-145A32?style=flat-square&logo=qrcode&logoColor=F1C40F)![Docs Domain](https://img.shields.io/badge/Docs-Documentation%20Domain-6C7A89?style=flat-square&logo=qrcode&logoColor=ffffff)![Other Domain](https://img.shields.io/badge/Other-Extended%20Domain-1a1a1a?style=flat-square&logo=qrcode&logoColor=ffffff)
