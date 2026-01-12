# 🏳️‍🌈 **RTTcodes — A QR‑Compatible Metadata Layer for Resonance‑Time Theory**
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

RTTcodes provide a universal, QR‑compatible way to identify, classify, and navigate artifacts across the TriadicFrameworks ecosystem. They act as **scannable resonance identifiers**, binding any artifact—digital or physical—to its canonical documentation, lineage, and onboarding guides.

RTTcodes are designed to work anywhere QR codes already operate in industry, science, and engineering, while adding a structured RTT‑native metadata layer.

---

## **Purpose**

RTTcodes enable:

- **Artifact binding**  
  Every folder, diagram, simulation, or manuscript section can carry its own RTTcode linking to its canonical representation.

- **Cross‑domain navigation**  
  Codes unify RTT, SET fields, substrate models, observer hierarchies, and future domains.

- **Onboarding clarity**  
  Scanning an RTTcode takes contributors directly to the correct documentation or operator guide.

- **Versioned lineage**  
  RTTcodes can encode version, domain, and resonance metadata, preserving the evolution of each artifact.

---

## **Design Principles**

RTTcodes are:

- **QR‑compatible**  
  Fully readable by standard QR scanners and industrial systems.

- **Metadata‑rich**  
  They encode structured RTT information in a compact JSON payload.

- **Domain‑aware**  
  Each code identifies its domain (e.g., `substrate`, `rtt`, `set`, `observer`).

- **Extensible**  
  The schema supports optional resonance triads, checksums, and future fields.

- **Visual and symbolic**  
  RTTcodes may include optional triadic overlays or domain color cues while remaining machine‑readable.

---

## **Schema Overview**

RTTcodes encode a structured payload. A typical example:

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

The full schema is defined in:

```
docs/rttcodes/schema/rttcode.schema.json
```

---

## **Repository Structure**

```
docs/
  rttcodes/
    README.md
    schema/
      rttcode.schema.json
      rttcode-payload-example.json
    generators/
      python/
        generate_rttcode.py
      js/
        generate_rttcode.js
    validators/
      validate_rttcode.py
    style/
      visual-guidelines.md
      color-domains.png
      rttcode-layout.svg
    examples/
      substrate/
      rtt/
      set/
```

Each folder contains reference implementations, style guides, and example RTTcodes for real TriadicFrameworks artifacts.

---

## **Usage**

RTTcodes can be embedded in:

- Markdown (`README.md`)
- LaTeX manuscripts
- SVG diagrams
- Simulation configs
- Physical prototypes
- Lab notebooks
- Educational materials

They serve as a universal pointer to the canonical source of truth.

---

## **Status**

This is the **initial scaffold** for the RTTcode system.  
Files will be added as the schema, generators, and validators are developed.

