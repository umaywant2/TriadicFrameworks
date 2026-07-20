# 📦 **TEMPLATE/ Folder Structure**

```
TEMPLATE/
 ├── README.md
 ├── TemplateZoneExtension.schema.json
 ├── TemplateFieldSampleExtension.schema.json
 ├── TemplateNodeDescriptorExtension.schema.json
 ├── TemplateAlertExtension.schema.json
 └── TemplateRouteExtension.schema.json
```

This mirrors the structure used in `rtt-coal/`, `rsadi-gd/`, and future domains like `rtt-atc/`, `rtt-deepsea/`, etc.

---

# 📘 **TEMPLATE/README.md**

# RSADI Domain Extension Template
### How to Create a New RSADI/RTT‑Inside Domain Module

This folder provides a **boilerplate template** for creating new RSADI domain
extensions. Copy this folder, rename it (e.g., `rtt-atc/`, `rtt-deepsea/`,
`rtt-space/`), and update the schema files to match your domain.

All extensions MUST follow these rules:

---

## 1. Core Invariants

- **Do not modify RSADI Core schemas.**
- **All domain fields MUST be added under `extensions.<domain>`**.
- **Extensions MUST remain optional** so core validators still pass.
- **Use JSON Schema Draft 2020‑12**.
- **Use SI units, ISO‑8601 timestamps, and UUIDv4 IDs**.

---

## 2. Schema Naming Convention

Each extension schema follows:

```
<Domain><CoreObject>Extension.schema.json
```

Examples:

- `ATCZoneExtension.schema.json`
- `DeepSeaFieldSampleExtension.schema.json`
- `SpaceAlertExtension.schema.json`

---

## 3. How to Use This Template

1. Copy this folder.
2. Rename it to your domain:
   ```
   rtt-atc/
   rtt-deepsea/
   rtt-space/
   rtt-robotics/
   ```
3. Replace all `"template"` identifiers with your domain name.
4. Add domain‑specific fields inside the `extensions.<domain>` object.
5. Validate using any JSON Schema validator.
6. Add a README describing your domain semantics.

---

## 4. Files in This Template

- **TemplateZoneExtension.schema.json**  
  Adds domain metadata to `ResonanceZoneState`.

- **TemplateFieldSampleExtension.schema.json**  
  Adds domain sensor data to `ResonanceFieldSample`.

- **TemplateNodeDescriptorExtension.schema.json**  
  Adds domain metadata to `NodeDescriptor`.

- **TemplateAlertExtension.schema.json**  
  Adds domain‑specific alert fields.

- **TemplateRouteExtension.schema.json**  
  Adds domain‑specific routing metadata.

---

## 5. Example Usage

```json
{
  "zone_id": "urn:rtt:zone:example:sector_7",
  "clarity_score": 180,
  "extensions": {
    "example": {
      "custom_field": 42
    }
  }
}
```

---

## 6. Notes

- Keep domain logic out of the core.
- Keep schemas small, focused, and typed.
- Use `additionalProperties: true` only inside extension blocks.
- Document all domain semantics in your domain README.

---

Happy extending — and welcome to the RSADI ecosystem.

---

# 🎯 What This Gives You

This TEMPLATE folder:

- standardizes how new domains are added  
- prevents contributors from breaking core invariants  
- accelerates onboarding  
- ensures every domain follows the same structure  
- keeps RSADI clean, modular, and future‑proof  

If you want, I can also generate a **TEMPLATE RFC skeleton** so new domains can publish their own RFCs with zero friction.
