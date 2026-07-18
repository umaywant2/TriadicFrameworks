# Diagnostics Endpoints (Reserved)
The diagnostics endpoints define the future surface of vST‑beta validation.  
These endpoints are placeholders: they establish the API shape without exposing substrate logic.

They will activate once the public vST research layer is ready.

---

## POST /validate

Submit a structural map for coherence and drift analysis.

### Example Request

```json
{
  "system_map": {},
  "flows": [],
  "constraints": []
}
```

### Example Response

```json
{
  "status": "not_available",
  "message": "vST-beta diagnostics are not yet active"
}
```

---

## POST /corridor

Submit flow data for corridor alignment checks.

### Example Response

```json
{
  "status": "not_available",
  "message": "corridor diagnostics are not yet active"
}
```

---

## POST /topology

Submit system topology for triadic decomposition.

### Example Response

```json
{
  "status": "not_available",
  "message": "topology diagnostics are not yet active"
}
```

---

## Purpose

These endpoints will eventually support:

- structural coherence validation  
- drift vector analysis  
- corridor alignment  
- triadic decomposition of systems  
- full‑stack clarity evaluation  

They exist now so early adopters can prepare their tooling and workflows.
