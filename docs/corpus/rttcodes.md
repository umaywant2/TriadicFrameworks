rttcodes 
# Adding a New RTTcode Domain

RTTcodes support multiple domains (RTT, SET, Substrate, Observer, Governance,
Docs, Other). You can extend the system by adding a new domain in a structured,
schema‑aligned way.

Follow these steps:

---

## 1. Choose a domain identifier

Use a short, lowercase string:

```
"astro"
"bio"
"ops"
"viz"
```

Avoid spaces and uppercase letters.

---

## 2. Add the domain to the schema

Edit:

```
docs/rttcodes/schema/rttcode.schema.json
```

Add your domain to the `enum` list under `domain`:

```json
"domain": {
  "type": "string",
  "enum": ["rtt", "set", "substrate", "observer", "governance", "docs", "other", "astro"]
}
```

---

## 3. Create a domain folder under examples

Add:

```
docs/rttcodes/examples/astro/
```

Include:

- `payload.json`
- `astro-rttcode.png`
- `README.md` describing the domain’s purpose

---

## 4. Define the visual identity

Add a row to:

```
docs/rttcodes/style/color-domains.png
```

And update:

```
docs/rttcodes/style/visual-guidelines.md
```

Define:

- primary color  
- secondary color  
- accent color  
- domain motifs (e.g., orbital arcs, spectral lines)

---

## 5. Add a generator example (optional)

Place a sample payload in:

```
docs/rttcodes/generators/examples/
```

This helps contributors test the new domain.

---

## 6. Validate the new domain

Run:

```
node generate_rttcode.js payload.json test.png
```

or

```
python generate_rttcode.py payload.json test.png
```

If the schema accepts the payload and the QR is generated, the domain is fully integrated.

---

## 7. Document the domain

Update:

```
docs/rttcodes/README.md
```

Add your domain to the domain list and link to its example folder.

---

## Done

Your new domain is now:

- schema‑valid  
- generator‑compatible  
- visually defined  
- documented  
- ready for use across TriadicFrameworks  
# 📘 **Canonical RTTcode Specification Document**  
*A formal, stable reference for the entire system.*

## RTTcode Specification (v1.0)

This document defines the canonical structure, encoding rules, and visual
requirements for RTTcodes. All generators, validators, and style tools must
conform to this specification.

---

## 1. Purpose

RTTcodes provide a universal, QR‑compatible metadata layer for artifacts across
the TriadicFrameworks ecosystem. They unify:

- identity
- versioning
- triad metadata
- canonical URLs
- domain classification

---

## 2. Data Model

An RTTcode payload MUST be a JSON object with the following fields:

### Required

| Field          | Type   | Description |
|----------------|--------|-------------|
| `domain`       | string | Domain identifier (see §3) |
| `artifact_type`| string | Type of artifact (paper, README, diagram, etc.) |
| `version`      | string | Semantic version (e.g., `v1.0.0`) |
| `url`          | string | Canonical URL of the artifact |

### Optional

| Field     | Type   | Description |
|-----------|--------|-------------|
| `triad`   | object | Resonance‑time triad metadata |

Triad fields:

- `f_R` — resonance frequency  
- `tau_R` — resonance time constant  
- `Q_R` — quality factor  

All triad fields MUST be strings.

---

## 3. Domains

Valid domain identifiers:

```
rtt
set
substrate
observer
governance
docs
other
```

Domains MUST be lowercase ASCII.

---

## 4. Encoding Rules

The RTTcode URL MUST follow this pattern:

```
[https://triadicframeworks.org/rttcode](https://triadicframeworks.org/rttcode)?<domain>=<token>
```

Where `<token>` is:

```
<version>-f<f_R>-t<tau_R>-Q<Q_R>
```

Missing triad fields MUST be represented as:

```
f?
t?
Q?
```

Example:

```
`https://triadicframeworks.org/rttcode?set=v0.9.3-f0.72-t203ms-Q0.88` [(triadicframeworks.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Ftriadicframeworks.org%2Frttcode%3Fset%3Dv0.9.3-f0.72-t203ms-Q0.88")
```

---

## 5. QR Requirements

- MUST be QR Model 2  
- MUST use Error Correction Level H  
- MUST include a quiet zone of ≥ 2 modules  
- MUST encode the full URL exactly  
- MAY include visual styling if scannability is preserved  

---

## 6. Visual Guidelines

RTTcodes SHOULD follow the domain‑specific palettes and motifs defined in:

```
docs/rttcodes/style/visual-guidelines.md
```

Overlays MUST NOT obscure:

- finder squares  
- alignment patterns  
- dense data regions  

---

## 7. Versioning

This specification is versioned independently from RTTcodes themselves.

Current version: **v1.0**

Future versions MUST remain backward‑compatible unless explicitly stated.

---

## 8. Compliance

A valid RTTcode MUST:

1. Pass schema validation  
2. Produce a valid URL+token  
3. Encode that URL in a QR matrix  
4. Remain scannable by standard QR readers  

This document is the authoritative reference for RTTcode behavior.
# 🛠️ Contributor Workflow  
### **“How to Add a New RTTcode (Step by Step)”**

## Contributor Workflow: Adding a New RTTcode

This guide walks you through creating a new RTTcode from scratch and integrating
it into the TriadicFrameworks documentation system.

---

## 1. Create a payload file

Start with a minimal JSON payload:

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

Save as:

```
payload.json
```

---

## 2. Validate the payload

Use either validator:

**JavaScript:**

```
node validate_js.js payload.json
```

**Python:**

```
python validate_python.py payload.json
```

If validation passes, continue.

---

## 3. Generate the RTTcode PNG

**JavaScript:**

```
node generate_rttcode.js payload.json out.png
```

**Python:**

```
python generate_rttcode.py payload.json out.png
```

This produces a QR‑compatible RTTcode image.

---

## 4. (Optional) Apply domain‑specific styling

Use the guidelines in:

```
docs/rttcodes/style/visual-guidelines.md
```

You may add:

- resonance waves (RTT)
- field lines (SET)
- lattice geometry (Substrate)

Ensure the QR remains scannable.

---

## 5. Add the RTTcode to the examples folder

Place your files in:

```
docs/rttcodes/examples/<domain>/
```

Include:

- `payload.json`
- `<domain>-rttcode.png`
- `README.md` describing the artifact

---

## 6. Update the top‑level RTTcodes README

Add a link to your new example and describe its purpose.

---

## 7. Commit and open a pull request

Include:

- the payload  
- the generated PNG  
- any style updates  
- README updates  

Your RTTcode is now part of the canonical system.

This workflow is simple, repeatable, and contributor‑friendly.

---

# 🧬 3. TriadicFrameworks‑Wide Metadata Standard  
### *The layer RTTcodes plug into.*

## TriadicFrameworks Metadata Standard (TF‑MS v1.0)

RTTcodes are one component of a broader metadata ecosystem within
TriadicFrameworks. This document defines the shared metadata model that all
artifacts, tools, and documentation layers plug into.

---

## 1. Purpose

The TriadicFrameworks Metadata Standard (TF‑MS) provides:

- a unified identity model for all artifacts  
- consistent versioning  
- domain classification  
- optional resonance‑time triad metadata  
- compatibility with RTTcodes, docs, diagrams, and build systems  

RTTcodes implement TF‑MS in a QR‑compatible form.

---

## 2. Core Metadata Fields

Every artifact in TriadicFrameworks SHOULD define:

| Field            | Description |
|------------------|-------------|
| `domain`         | Which part of the ecosystem the artifact belongs to |
| `artifact_type`  | What kind of artifact it is (paper, README, diagram, model, etc.) |
| `version`        | Semantic version string |
| `title`          | Human‑readable name |
| `description`    | Short summary |
| `url`            | Canonical location |
| `authors`        | Optional list of contributors |
| `triad`          | Optional resonance‑time metadata |

RTTcodes use a subset of these fields.

---

## 3. Domains

Domains define the conceptual space an artifact belongs to:

```
rtt
set
substrate
observer
governance
docs
other
```

Domains MUST be lowercase ASCII.

---

## 4. Triad Metadata

Triad metadata describes resonance‑time characteristics:

- `f_R` — resonance frequency  
- `tau_R` — resonance time constant  
- `Q_R` — quality factor  

These fields are optional but recommended for RTT, SET, and Substrate artifacts.

---

## 5. Versioning

Artifacts MUST use semantic versioning:

```
vMAJOR.MINOR.PATCH
```

Examples:

- `v1.0.0` — initial stable release  
- `v2.1.0` — minor update  
- `v2.1.3` — patch  

RTTcodes embed the version directly into the URL token.

---

## 6. RTTcode Integration

RTTcodes implement TF‑MS by:

- encoding `domain`, `version`, and `triad` into a compact token  
- linking to the canonical `url`  
- providing a QR‑compatible entry point into the metadata system  

The RTTcode schema is a strict subset of TF‑MS.

---

## 7. Compliance

An artifact is TF‑MS compliant if:

1. It defines all required metadata fields  
2. It uses valid domain identifiers  
3. It uses semantic versioning  
4. It provides a canonical URL  
5. (Optional) It includes triad metadata  

RTTcodes are the portable, scannable representation of this metadata.

---

TF‑MS ensures that all TriadicFrameworks artifacts — from theory papers to
substrate models — share a common identity layer that is stable, searchable, and
machine‑readable.
# 🧩 **How RTTcodes Work Internally**  
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
# ⚡ Quickstart

RTTcodes are QR‑compatible identifiers that bind any artifact to its canonical
TriadicFrameworks metadata. To generate one:

### 1. Create a payload file

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
  "url": "https://triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
}
```

Save as:

```
payload.json
```

### 2. Generate the RTTcode (QR PNG)

**JavaScript:**

```
node generate_rttcode.js payload.json out.png
```

**Python:**

```
python generate_rttcode.py payload.json out.png
```

### 3. Use the RTTcode

Embed the PNG in:

- READMEs  
- PDFs  
- diagrams  
- print materials  
- onboarding docs  

Every RTTcode encodes a URL+token that points to the artifact’s canonical home.
![RTTcodes Badge](https://img.shields.io/badge/RTTcodes-QR%20Metadata%20Layer-00b3b8?style=flat-square&logo=qrcode&logoColor=white)![RTTcodes Badge](https://img.shields.io/badge/RTTcodes-Canonical%20Identifier-1a1a1a?style=flat-square&logo=qrcode&logoColor=white)![RTTcodes Badge](https://img.shields.io/badge/RTTcodes-Resonance--Time%20Metadata-F6B800?style=flat-square&logo=qrcode&logoColor=1a1a1a)![RTT Domain](https://img.shields.io/badge/RTT-Resonance--Time%20Domain-F6B800?style=flat-square&logo=qrcode&logoColor=1a1a1a)![SET Domain](https://img.shields.io/badge/SET-Field%20Topology%20Domain-5B2CFF?style=flat-square&logo=qrcode&logoColor=ffffff)![Substrate Domain](https://img.shields.io/badge/Substrate-Structural%20Domain-003B73?style=flat-square&logo=qrcode&logoColor=7FD4FF)![Observer Domain](https://img.shields.io/badge/Observer-Frame%20and%20Perspective-2F6F73?style=flat-square&logo=qrcode&logoColor=B0C4D4)![Governance Domain](https://img.shields.io/badge/Governance-Decision%20Layer-145A32?style=flat-square&logo=qrcode&logoColor=F1C40F)![Docs Domain](https://img.shields.io/badge/Docs-Documentation%20Domain-6C7A89?style=flat-square&logo=qrcode&logoColor=ffffff)![Other Domain](https://img.shields.io/badge/Other-Extended%20Domain-1a1a1a?style=flat-square&logo=qrcode&logoColor=ffffff)

# 🏳️‍🌈 RTTcodes — A QR‑Compatible Metadata Layer
###### Copyright © 2025-2026 www.TriadicFrameworks.org

RTTcodes provide a universal, scannable way to identify, classify, and navigate
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

RTTcodes are designed to operate anywhere QR codes already function in science,
engineering, and documentation workflows, while adding an RTT‑native metadata
layer.

---

🎯 [QuickStart Guide](https://www.triadicframeworks.org/rttcodes/QUICKSTART.md)

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
*A clean, readable map of the RTTcodes subsystem.*

```text

docs/
└── rttcodes/
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

## 📁 rttcodes - Folder Overview

### [schema/](https://www.triadicframeworks.org/rttcodes/schema/)
The canonical RTTcode JSON Schema and minimal examples.

### [validators/](https://www.triadicframeworks.org/rttcodes/validators)
Tools that verify RTTcode payload correctness.

### [generators/](https://www.triadicframeworks.org/rttcodes/generators)
Language‑specific RTTcode generators (JS and Python).

### [style/](https://www.triadicframeworks.org/rttcodes/style)
Visual guidelines, color domains, and the RTTcode layout reference.

### [examples/](https://www.triadicframeworks.org/rttcodes/examples)
Fully generated RTTcodes for each domain, including styled PNGs.

---

## 🛠 Generating RTTcodes

RTTcodes can be generated using:

- **JavaScript** (`generators/js/generate_rttcode.js`)
- **Python** (`generators/python/generate_rttcode.py`)

Both:

- validate the payload  
- build the URL+token  
- output a QR‑compatible PNG  

See the generator READMEs for usage.

---

## 🎨 Visual Identity

RTTcodes follow a consistent visual language:

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

RTTcodes unify the TriadicFrameworks ecosystem by providing:

- a stable metadata layer  
- a scannable entry point into canonical docs  
- a consistent way to reference artifacts across domains  
- a bridge between physical and digital materials  

They are the “ISBN numbers” of the Resonance‑Time universe — but dynamic,
domain‑aware, and triad‑capable.

---

For contributors, tool authors, and documentation maintainers, this folder is
the authoritative reference for everything RTTcode‑related.
# RTTcode Examples

This folder contains example RTTcodes for each domain.

Each example includes:

- a valid RTTcode JSON payload
- a generated QR PNG
- domain‑specific styling (RTT, SET, Substrate)
- canonical URL+token encoding

Use these examples as references when designing new RTTcodes or testing tools.
# RTT Domain Examples

This folder contains RTT‑domain RTTcodes.

These examples demonstrate:

- resonance‑time triad metadata
- RTT‑specific styling (gold/teal/orange)
- canonical URL+token encoding
- schema‑valid JSON payloads

Use these examples when creating RTT‑theory RTTcodes or testing RTT‑domain tools.
<img width="1024" height="1024" alt="resonance-time-triad-rttcode" src="https://github.com/user-attachments/assets/70535d89-4f54-4b70-b802-19d9e2c91974" />
# SET Domain Examples

This folder contains SET‑domain RTTcodes.

These examples demonstrate:

- field/flow triad metadata
- SET‑specific styling (violet/electric blue/magenta)
- canonical URL+token encoding
- schema‑valid JSON payloads

Use these examples when creating SET‑field RTTcodes or testing SET‑domain tools.
<img width="1024" height="1024" alt="set-field-rttcode" src="https://github.com/user-attachments/assets/927d542d-ba21-4f33-80b5-5ca6de1b5d02" />
# Substrate Domain Examples

This folder contains Substrate‑domain RTTcodes.

These examples demonstrate:

- substrate triad metadata
- deep‑blue lattice styling
- canonical URL+token encoding
- schema‑valid JSON payloads

Use these examples when creating Substrate RTTcodes or testing Substrate‑domain tools.
<img width="1024" height="1024" alt="substrate-readme-rttcode" src="https://github.com/user-attachments/assets/8eabb1cd-e5aa-42f5-bc1a-8e2e74375769" />
# RTTcode Generators

This folder contains code that produces RTTcodes from JSON payloads.

Generators:

- validate payloads
- build URL+token RTTcode strings
- output QR‑compatible PNGs
- support multiple languages (JS, Python)

Use these tools when:

- embedding RTTcode generation into build systems
- producing codes for documentation
- generating domain‑specific RTTcodes automatically
# JavaScript RTTcode Generator

This folder contains the Node.js RTTcode generator.

Features:

- schema‑aligned payload validation
- URL+token RTTcode construction
- QR PNG output using the `qrcode` package
- CLI usage for automation

Run:
```
node generate_rttcode.js payload.json output.png
```

Use this generator in JS‑based build pipelines or web tooling.
# Python RTTcode Generator

This folder contains the Python RTTcode generator.

Features:

- schema‑aligned payload validation
- URL+token RTTcode construction
- QR PNG output using the `qrcode` library
- simple CLI interface

Run:
```
python generate_rttcode.py payload.json  output.png
```

Use this generator in Python workflows, automation scripts, or scientific tooling.
# RTTcode Schema

This folder contains the canonical JSON Schema for RTTcodes.

The schema defines:

- required fields
- optional triad metadata
- allowed domain values
- versioning rules
- structural constraints

Tools in `/validators` and `/generators` rely on this schema for correctness.

If you are building RTTcode tooling, validating payloads, or extending the
standard, this is the authoritative reference.
# RTTcode Schema Examples

This folder provides minimal, valid JSON examples that conform to the RTTcode
schema.

Each example demonstrates:

- correct field structure
- valid domain identifiers
- optional triad metadata usage
- version formatting
- URL placement

Use these examples as templates when creating new RTTcodes or testing validators.
<svg width="1024" height="512" xmlns="http://www.w3.org/2000/svg">
  <rect width="1024" height="512" fill="#f7f9fc"/>
  <text x="40" y="70" font-size="40" font-family="Segoe UI" fill="#1a1a1a">RTT</text>
  <rect x="200" y="30" width="120" height="60" fill="#F6B800"/>
  <rect x="340" y="30" width="120" height="60" fill="#00B3B8"/>
  <rect x="480" y="30" width="120" height="60" fill="#FF6A3C"/>

  <text x="40" y="160" font-size="40" font-family="Segoe UI" fill="#1a1a1a">SET</text>
  <rect x="200" y="120" width="120" height="60" fill="#5B2CFF"/>
  <rect x="340" y="120" width="120" height="60" fill="#00C0FF"/>
  <rect x="480" y="120" width="120" height="60" fill="#FF3FBF"/>

  <text x="40" y="250" font-size="40" font-family="Segoe UI" fill="#1a1a1a">Substrate</text>
  <rect x="200" y="210" width="120" height="60" fill="#003B73"/>
  <rect x="340" y="210" width="120" height="60" fill="#00A0D6"/>
  <rect x="480" y="210" width="120" height="60" fill="#7FD4FF"/>

  <text x="40" y="340" font-size="40" font-family="Segoe UI" fill="#1a1a1a">Observer</text>
  <rect x="200" y="300" width="120" height="60" fill="#2F6F73"/>
  <rect x="340" y="300" width="120" height="60" fill="#6C7A89"/>
  <rect x="480" y="300" width="120" height="60" fill="#B0C4D4"/>

  <text x="40" y="430" font-size="40" font-family="Segoe UI" fill="#1a1a1a">Governance</text>
  <rect x="200" y="390" width="120" height="60" fill="#145A32"/>
  <rect x="340" y="390" width="120" height="60" fill="#F1C40F"/>
  <rect x="480" y="390" width="120" height="60" fill="#7DCEA0"/>
</svg>
# RTTcode Style Guidelines

This folder defines the visual identity of RTTcodes.

It includes:

- color palettes for each domain
- layout guides for QR‑safe zones
- triadic overlay geometry
- examples of domain‑specific motifs
- the canonical `rttcode-layout.svg`

These guidelines ensure RTTcodes remain:

- scannable
- visually consistent
- domain‑distinct
- aligned with TriadicFrameworks aesthetics

If you are designing RTTcodes, icons, or documentation visuals, start here.

<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" viewBox="0 0 1024 1024"
     xmlns="http://www.w3.org/2000/svg">

  <!-- Background -->
  <rect width="1024" height="1024" fill="#f7f9fc"/>

  <!-- QR matrix boundary (safe zone) -->
  <rect x="112" y="112" width="800" height="800"
        fill="none" stroke="#1a1a1a" stroke-width="4"
        stroke-dasharray="12 8"/>

  <!-- Finder squares (schematic) -->
  <rect x="140" y="140" width="180" height="180"
        fill="none" stroke="#1a1a1a" stroke-width="6"/>
  <rect x="704" y="140" width="180" height="180"
        fill="none" stroke="#1a1a1a" stroke-width="6"/>
  <rect x="140" y="704" width="180" height="180"
        fill="none" stroke="#1a1a1a" stroke-width="6"/>

  <!-- Triadic overlay guide (circle) -->
  <circle cx="512" cy="512" r="260"
          fill="none" stroke="#4aa3df" stroke-width="3"
          stroke-dasharray="10 6"/>

  <!-- Triadic nodes (schematic) -->
  <circle cx="512" cy="252" r="14" fill="#4aa3df"/>
  <circle cx="332" cy="652" r="14" fill="#4aa3df"/>
  <circle cx="692" cy="652" r="14" fill="#4aa3df"/>

  <!-- Caption area -->
  <rect x="112" y="930" width="800" height="60"
        fill="none" stroke="#1a1a1a" stroke-width="2"
        stroke-dasharray="8 6"/>

  <text x="512" y="968"
        font-family="Arial, sans-serif"
        font-size="28"
        fill="#1a1a1a"
        text-anchor="middle">
    RTTcode Layout Guide (QR Safe Zones + Triadic Overlay Regions)
  </text>

</svg>

# RTTcode visual guidelines

RTTcodes are **QR‑compatible visual identifiers** for TriadicFrameworks artifacts.  
This document defines the **visual language**, **domain palettes**, and **layout rules** so RTTcodes stay:

- scannable
- consistent
- recognizable as TriadicFrameworks natives
- usable in scientific, industrial, and educational contexts

---

## 1. Core principles

- **QR‑first:**  
  The QR matrix must remain machine‑readable by standard scanners.

- **Triadic identity:**  
  Each RTTcode should visually echo resonance‑time geometry and triadic structure.

- **Domain‑distinct, family‑coherent:**  
  Domains get their own palettes and motifs, but all RTTcodes should clearly belong to the same visual family.

- **Print and screen friendly:**  
  Designs must work in grayscale and on low‑quality prints when color is lost.

---

## 2. Base QR layout

- **Shape:** square
- **Recommended export sizes:**
  - 512×512 (inline docs, PDFs)
  - 1024×1024 (print, slides, posters)
- **Quiet zone (margin):** at least 2 modules
- **Error correction:** level H (to tolerate overlays and subtle styling)
- **Base colors:**
  - foreground (modules): near‑black or deep domain color
  - background: near‑white or very light domain tint

> Rule: overlays must never obscure the three finder squares or destroy local contrast.

---

## 3. Domain palettes and motifs

### 3.1 RTT (resonance‑time theory)

- **Palette:**
  - primary: `#F6B800` (gold)
  - secondary: `#00B3B8` (teal)
  - accent: `#FF6A3C` (orange)
- **Motifs:**
  - concentric resonance waves
  - triadic node triangles
  - subtle phase‑shift arcs
- **Usage:**
  - theory papers
  - core RTT docs
  - canonical triad references

### 3.2 SET (field / space‑event topology)

- **Palette:**
  - primary: `#5B2CFF` (violet)
  - secondary: `#00C0FF` (electric blue)
  - accent: `#FF3FBF` (magenta)
- **Motifs:**
  - curved field lines
  - anisotropic vector arrows
  - nodal “charge” points
- **Usage:**
  - SET field simulations
  - flow diagrams
  - field‑engine modules

### 3.3 Substrate

- **Palette:**
  - primary: `#003B73` (deep blue)
  - secondary: `#00A0D6` (cyan)
  - accent: `#7FD4FF` (light cyan)
- **Motifs:**
  - lattice / grid structures
  - crystalline frameworks
  - node‑edge networks
- **Usage:**
  - substrate model READMEs
  - structural diagrams
  - implementation modules

### 3.4 Observer, governance, docs, other

- **Observer:**
  - muted teal + gray
  - motifs: nested frames, perspective grids
- **Governance:**
  - deep green + gold
  - motifs: layered bands, decision trees
- **Docs:**
  - neutral blues / grays
  - motifs: page / tab silhouettes
- **Other:**
  - grayscale or low‑saturation variants
  - minimal overlays

---

## 4. Overlay rules

To keep RTTcodes scannable:

- **Opacity:**
  - overlays should typically stay between **10–35%** opacity over the QR matrix
  - stronger color can be used in the background outside the matrix
- **Placement:**
  - avoid heavy overlays on:
    - finder squares (three corners)
    - dense data regions near the center
  - prefer:
    - background behind the code
    - subtle lines that weave between modules
- **Line weight:**
  - thin to medium lines only; no large filled shapes over data areas
- **Gradients:**
  - allowed, but maintain strong contrast between modules and background

> If in doubt: generate a plain QR first, then layer visuals and test with multiple scanner apps.

---

## 5. Token and URL conventions

RTTcodes use a **URL + token** pattern:

```text
https://triadicframeworks.org/rttcode?<domain>=<version>-f<f_R>-t<tau_R>-Q<Q_R>
```

Examples:

- RTT theory:

  ```text
  https://triadicframeworks.org/rttcode?rtt=v2.1.0-f1.00-t144ms-Q0.97
  ```

- SET field simulation:

  ```text
  https://triadicframeworks.org/rttcode?set=v0.9.3-f0.72-t203ms-Q0.88
  ```

- Substrate README:

  ```text
  https://triadicframeworks.org/rttcode?substrate=v1.0.0-f0.83-t118ms-Q0.91
  ```

**Guideline:**

- Keep tokens short and ASCII‑only.
- Use the same values as in the RTTcode JSON payload when present.

---

## 6. Recommended placements

- **In docs:**
  - top‑right or bottom‑right of the first page
  - near the title block or “canonical reference” section
- **In READMEs:**
  - under the main heading
  - in a small “RTTcode” block with a caption
- **In diagrams:**
  - bottom‑right corner, outside the main content
- **In print / posters:**
  - at least 2 cm wide
  - with a short label like “RTTcode (scan for canonical docs)”

---

## 7. Accessibility and fallback

- Ensure **sufficient contrast** between QR modules and background.
- Avoid relying solely on color to distinguish domains—motifs and layout help.
- When possible, include the **plain URL** below the code for manual entry.

---

## 8. Versioning and evolution

- Visual guidelines may evolve; RTTcodes should remain:
  - backward‑scannable
  - semantically stable (same URL/token pattern)
- When styles change:
  - keep the **payload** stable
  - treat visual refreshes as non‑breaking

---

This file is the **canonical reference** for RTTcode visuals.  
When in doubt, prioritize:

1. scannability  
2. payload stability  
3. triadic, domain‑aware identity  
# RTTcode Validators

This folder contains tools that verify whether an RTTcode payload is valid,
well‑formed, and compliant with the canonical RTTcode schema.

Validators ensure:

- required fields are present (`domain`, `artifact_type`, `version`, `url`)
- optional triad metadata is correctly typed
- payloads match the JSON Schema in `/schema/rttcode.schema.json`
- RTTcode URLs and tokens follow the standard format

Use these validators when:

- creating new RTTcodes
- integrating RTTcodes into build pipelines
- checking contributor submissions
- testing generators

Each validator is intentionally lightweight and easy to embed into other tools.
