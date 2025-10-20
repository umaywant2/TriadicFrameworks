# 🌐 entft API Gateway Hook — External Trigger Interface (v1.3)

This YAML scroll defines the **OpenAPI spec** for triggering entft hooks from external systems.  
It enables symbolic overlays, badge logic, and validator echoes via RESTful invocation.

---

## 🧠 **Resonance Clarity refresh**
for `api_gateway_hook.yaml`, now tuned for validator-grade clarity, symbolic fidelity, and triadic discoverability. This scroll defines the API interface that lets external systems trigger `entft` logic—badge overlays, glyph echoes, and validator handshakes.

---

## 📡 Endpoint Summary

```yaml
openapi: 3.0.0
info:
  title: entft Trigger API
  version: 1.3
paths:
  /trigger:
    post:
      summary: Trigger symbolic glyph or badge overlay
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                glyph:
                  type: string
                badge:
                  type: string
                observer:
                  type: string
      responses:
        '200':
          description: Trigger accepted
        '400':
          description: Invalid payload
```

---

## 🧪 Sample Payload

```json
{
  "glyph": "denometer",
  "badge": "Trintellectual Hybrid",
  "observer": "ScrollFork"
}
```

---

## 🎯 Purpose

This API hook allows external systems to:

- 🧠 Trigger badge overlays from symbolic events  
- 🌀 Echo glyph lineage into validator dashboards  
- 🔗 Extend entft logic into remix platforms and registries

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
