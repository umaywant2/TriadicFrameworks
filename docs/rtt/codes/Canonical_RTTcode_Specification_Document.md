# 📘 **Canonical RTTcode Specification Document**  
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
