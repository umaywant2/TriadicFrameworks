# 🛠️ Contributor Workflow  
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
