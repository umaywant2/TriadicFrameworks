# `example_templates.md`
**SARG Example Templates**  
_Standardized, minimal templates for constructing SARG examples across any substrate._

This document provides **copy‑ready templates** for building SARG examples.  
Each template is intentionally minimal, structural, and aligned with the canonical SARG schema.

---

## 1. Minimal SARG Object Template (JSON)

```json
{
  "sarg_version": "1.0.0",
  "id": "example_id",
  "description": "Short description of the example.",
  "substrate": {
    "type": "symbolic | acoustic | geometric | biological | linguistic | cosmological | other",
    "domain": "domain_name",
    "name": "Substrate Name",
    "elements": [],
    "properties": {}
  },
  "lens": {
    "primary": "structural",
    "secondary": [],
    "notes": ""
  },
  "invariants": {},
  "resonance": {
    "anchors": {},
    "mapping": {}
  },
  "examples": {}
}
```

---

## 2. Substrate Template

```json
{
  "substrate": {
    "type": "symbolic | acoustic | geometric | biological | linguistic | cosmological | other",
    "domain": "domain_name",
    "name": "Substrate Name",
    "elements": [
      "element_1",
      "element_2"
    ],
    "properties": {
      "property_name": "value"
    }
  }
}
```

---

## 3. Lens Template

```json
{
  "lens": {
    "primary": "structural | phonetic | graphical | temporal | spatial | functional",
    "secondary": ["optional_secondary_lens"],
    "notes": "Optional notes about how the lens is applied."
  }
}
```

---

## 4. Invariants Template

```json
{
  "invariants": {
    "symmetry": {
      "rotational": [],
      "mirror_vertical": [],
      "mirror_horizontal": []
    },
    "categorical": {
      "category_name": []
    },
    "positional": {
      "first": null,
      "last": null,
      "midpoint": null
    }
  }
}
```

---

## 5. Resonance Template

```json
{
  "resonance": {
    "anchors": {
      "axis": {
        "primary": "primary_axis_description",
        "secondary": "secondary_axis_description"
      },
      "clusters": [
        {
          "name": "cluster_name",
          "members": [],
          "signature": "cluster_signature"
        }
      ]
    },
    "mapping": {
      "element_name": {
        "cluster": "cluster_name_or_null",
        "invariants": [],
        "positional_role": "optional"
      }
    }
  }
}
```

---

## 6. Example Walkthrough Template

```json
{
  "examples": {
    "extraction_walkthrough": [
      {
        "element": "example_element",
        "lens": "structural",
        "identified_invariants": [],
        "resonance_anchor": null,
        "notes": "Optional explanatory note."
      }
    ]
  }
}
```

---

## 7. Full Example Template (All Sections Combined)

```json
{
  "sarg_version": "1.0.0",
  "id": "example_full_object",
  "description": "A complete SARG example template.",
  "substrate": {
    "type": "symbolic",
    "domain": "example_domain",
    "name": "Example Substrate",
    "elements": [],
    "properties": {}
  },
  "lens": {
    "primary": "structural",
    "secondary": [],
    "notes": ""
  },
  "invariants": {
    "symmetry": {},
    "categorical": {},
    "positional": {}
  },
  "resonance": {
    "anchors": {},
    "mapping": {}
  },
  "examples": {
    "extraction_walkthrough": []
  }
}
```

---

## 8. Notes for Contributors

- **Keep examples minimal** unless the example is explicitly pedagogical.  
- **Use real invariants** only when the substrate demands them; otherwise, placeholders are fine.  
- **Ensure schema compliance** with `/docs/SARG/schema/sarg.schema.json`.  
- **Prefer structural lens** unless demonstrating a specific lens type.  
- **Resonance anchors** should be sparse and meaningful, not decorative.  

---

If you want, AI can also generate:

- A **starter pack** of 5–10 blank example files  
- A **CLI‑style generator** (markdown or pseudo‑code)  
- A **contributor checklist** for SARG examples  
- A **visual diagram** showing how substrate → lens → invariants → resonance flows  

Just tell me where you want to go next.
