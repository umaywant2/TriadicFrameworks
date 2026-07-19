## ⭐ 4. RESOURCE‑MAPPING SCHEMA (JSON)  
  
This schema powers the “ethical search” layer — clean, ad‑free, privacy‑safe.  

```
{
  "resource": {
    "name": "string",
    "type": "emergency | transitional | long_arc | legal | mental_health | foster_support | food | clothing | documents",
    "description": "string",
    "location": {
      "city": "string",
      "state": "string",
      "address": "string | null",
      "service_area": "string"
    },
    "contact": {
      "phone": "string | null",
      "website": "string | null",
      "hours": "string | null"
    },
    "eligibility": {
      "age": "string | null",
      "requirements": "string | null"
    },
    "safety": {
      "verified": "boolean",
      "notes": "string | null"
    },
    "stabilizers": [
      "dignity",
      "privacy",
      "clarity",
      "safety",
      "continuity",
      "compassion",
      "navigation"
    ]
  }
}
```

This schema is non‑extractive, non‑tracking, and non‑commercial.
