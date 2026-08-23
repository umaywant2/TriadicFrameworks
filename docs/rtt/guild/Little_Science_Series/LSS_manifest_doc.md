# LSS manifest doc

> Generate a complete 144‑item JSON manifest for the Little Science Series, including all books (1–6), all scenes (1–6), all variants (A and B), and all asset types (STILL and ANIM). Each entry must include: filename, book number, book name, domain, scene number, scene name, variant, type, and the exact Imagine prompt text previously defined. The output must be a single JSON array with 144 objects, fully validated and ready for ingestion into the TriadicFrameworks repo.

I'll build the complete 144-item manifest now — generating all 6 books × 6 scenes × 2 variants × 2 types with proper filenames, metadata, and prompt text.

`LSS_manifest.json` is ready — **144 entries, fully validated, zero duplicate filenames.** Here's a quick structural breakdown:

---

### Manifest at a Glance

| Dimension | Values |
|---|---|
| **Books** | 1 Gravity · 2 Light · 3 Motion · 4 Time · 5 Matter · 6 Heat |
| **Domains** | `GRAV` · `LGHT` · `MOTN` · `TIME` · `MATTR` · `HEAT` |
| **Scenes per book** | 6 (S1–S6) |
| **Variants** | A · B |
| **Asset types** | `STILL` (`.png`) · `ANIM` (`.gif`) |
| **Items per book** | 24 (6 scenes × 2 variants × 2 types) |
| **Total** | **144** |

### Filename Convention
```
LSS_B{book#}_{domain}_S{scene#}_{type}_{variant}.{ext}

Example:  LSS_B1_GRAV_S1_STILL_A.png
          LSS_B6_HEAT_S6_ANIM_B.gif
```

### Fields per object
```json
{
  "filename":     "LSS_B2_LGHT_S3_ANIM_B.gif",
  "book_number":  2,
  "book_name":    "Light",
  "domain":       "LGHT",
  "scene_number": 3,
  "scene_name":   "Reflection",
  "variant":      "B",
  "type":         "ANIM",
  "prompt":       "Seamless loop of a concave mirror focusing multiple parallel rays..."
}
```
