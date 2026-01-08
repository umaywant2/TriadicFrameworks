### 📘 RFC‑052: RSADI‑Coal — Industry Extension to RSADI Core  
*A Resonance Structural Awareness Dimensional Interface for Underground Coal Mines*

```text
Internet‑Draft                                             Triadic Frameworks
Intended status: Standards Track                               January 2026
Expires: TBD

          RFC‑052: RSADI‑Coal — Coal Industry Extension
                    draft-rsadi-coal-00
```

---

## Abstract

This document defines **RSADI‑Coal**, a coal‑industry‑specific extension to the **Resonance Structural Awareness Dimensional Interface (RSADI)**.  
RSADI‑Coal specifies additional data fields, behaviors, and safety semantics required to apply RSADI in underground coal mining environments, including:

- methane and CO sensing  
- roof and floor strata characterization  
- pillar load and roof convergence  
- equipment vibration signatures  
- collapse vectors and ignition risk  
- resonance‑aware evacuation routing  

RSADI‑Coal builds on the RSADI Core data model and transport bindings without altering core invariants.

---

## Status of This Memo

Standard Internet‑Draft boilerplate (work in progress, subject to change, not yet a standard).

---

## Table of Contents

1. Introduction  
2. Terminology  
3. Relationship to RSADI Core  
4. Coal‑Specific Data Extensions  
5. RSADI‑Coal Message Semantics  
6. Evacuation and Clarity Gradient Semantics  
7. Node Roles and Mesh Behavior in Coal Mines  
8. Security Considerations  
9. Safety Considerations  
10. Privacy Considerations  
11. IANA Considerations  
12. References  
13. Acknowledgments  

---

## 1. Introduction

Explains:

- why underground coal mines are a natural RSADI domain  
- how resonance, clarity, drift, and structural stress map to coal mining hazards  
- the need for standardized coal‑specific extensions so vendors, operators, and regulators can interoperate safely  

States that RSADI‑Coal is **normative** for any RSADI deployment in coal mines.

---

## 2. Terminology

Defines coal‑specific terms:

- **Seam**  
- **Pillar**  
- **Roof Strata / Floor Strata**  
- **Convergence**  
- **Refuge Chamber**  
- **Belt Entry**  
- **Return / Intake Airway**  
- **Ignition Risk**  
- **Collapse Vector**  

Also references RSADI Core terms (clarity, drift, zone, node, mesh).

---

## 3. Relationship to RSADI Core

Clarifies:

- RSADI‑Coal **extends** RSADI Core objects via `extensions.coal` blocks  
- RSADI‑Coal does **not** change core field meanings or ranges  
- RSADI‑Coal is compatible with all RSADI Core transports (HTTP/JSON, MQTT, etc.)  

References the core schemas and shows how coal schemas plug in.

---

## 4. Coal‑Specific Data Extensions

Normatively binds the previously defined schemas:

- `CoalZoneExtension`  
- `CoalFieldSampleExtension`  
- `CoalNodeDescriptorExtension`  
- `CoalAlertExtension`  
- `CoalEvacRouteExtension`  

Each subsection:

- names the JSON Schema  
- describes when it **MUST** / **SHOULD** be used  
- explains field semantics (e.g., `methane_ppm`, `roof_convergence_mm`, `pillar_load_kpa`)  

Example:

> RSADI‑Coal deployments **MUST** populate `extensions.coal.methane_ppm` on any field sample taken in gassy seams.

---

## 5. RSADI‑Coal Message Semantics

Defines how coal extensions affect interpretation:

- how `methane_ppm` and `co_ppm` influence **composite risk**  
- how `roof_convergence_mm` and `pillar_load_kpa` influence **stress_hint**  
- how `equipment_vibration_signature` interacts with resonance coupling detection  
- how `collapse_vector` is computed and propagated in alerts  

Specifies thresholds and recommended mappings (informative, not prescriptive).

---

## 6. Evacuation and Clarity Gradient Semantics

Defines:

- how clarity gradients are computed in coal mines (gas + stress + ventilation + dust)  
- how `CoalEvacRouteExtension` annotates routes with refuge chambers, hazard zones, and ventilation paths  
- how wall‑mounted and wearable nodes should interpret **evacuate**, **no‑entry**, and **refuge** states  

Normative statements for:

- route suggestion behavior under rapidly degrading clarity  
- fallback to refuge when all routes exceed risk thresholds  

---

## 7. Node Roles and Mesh Behavior in Coal Mines

Defines coal‑specific node roles:

- `wall-mounted`  
- `wearable`  
- `equipment-mounted`  
- `refuge-chamber`  

Specifies:

- expected capabilities per role (sensing, comms, power)  
- mesh behavior in partial collapse scenarios  
- minimum behavior for **intrinsically safe** nodes  

---

## 8. Security Considerations

Covers:

- integrity of safety‑critical data (alerts, routes, gas readings)  
- mesh poisoning and spoofed nodes  
- authentication and authorization for control room systems  
- secure firmware update requirements for coal nodes  

---

## 9. Safety Considerations

Focuses on:

- avoiding over‑reliance on RSADI‑Coal (must complement, not replace, existing safety systems)  
- fail‑safe behavior on data loss or mesh partition  
- conservative defaults when clarity or gas data is missing  
- human‑factors considerations for miners using wearable nodes  

---

## 10. Privacy Considerations

Discusses:

- handling of miner location and movement data  
- retention of historical exposure and evacuation traces  
- anonymization for analytics vs. incident investigation  

---

## 11. IANA Considerations

If needed:

- registers an RSADI‑Coal media type (e.g., `application/rsadi-coal+json`)  
- registers a URN namespace for coal zones (e.g., `urn:rtt:zone:coal:...`)  

---

## 12. References

- Normative: RSADI Core RFC, JSON Schema, HTTP, UUID, ISO‑8601  
- Informative: Coal safety standards, MSHA guidance, TriadicFrameworks coal doc  

---

## 13. Acknowledgments

Credits contributors, miners, engineers, and reviewers.
