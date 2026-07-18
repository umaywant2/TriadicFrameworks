# 🧩 entft CMS Integration — Symbolic Embedding Guide (v1.3)

This scroll documents how to embed entft hooks into **Content Management Systems (CMS)**.  
It enables symbolic triggers, badge overlays, and validator echoes from within external publishing platforms.

---

## 🧪 Integration Targets

| Platform       | Integration Type         | Status     |
|----------------|--------------------------|------------|
| WordPress      | Plugin + webhook         | ✅ Drafted |
| Ghost          | API + badge overlay      | ⏳ Pending |
| Drupal         | Hook + validator echo    | ⏳ Pending |
| Notion         | Embed + symbolic trigger | ⏳ Pending |
| Medium         | Scroll injection         | ⏳ Pending |

---

## 🎯 Purpose

CMS integration allows remixers to:

- 🌀 Trigger badge overlays from published scrolls  
- 🧠 Echo validator lineage from external platforms  
- 🔗 Link symbolic triggers to publishing events

---

## 🧬 Invocation Flow

1. Author publishes scroll with embedded `entft` hook  
2. Hook activates symbolic trigger or badge overlay  
3. Validator echoes lineage and scroll fidelity  
4. Remix site logs symbolic echo and contributor badge

---

## 🔧 Sample Hook (WordPress)

```php
add_action('publish_post', function($post_id) {
  $glyph = get_post_meta($post_id, 'glyph_trigger', true);
  if ($glyph) {
    file_get_contents("https://entft.net/trigger?glyph=" . urlencode($glyph));
  }
});
```

---

## 🔗 Triadic Quicklinks

- [`fff_spec.md`](/docs/TFT_3Pack_v1.3/docs/fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](/docs/TFT_3Pack_v1.3/docs/TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`outputs_spec.md`](/docs/TFT_3Pack_v1.3/docs/outputs_spec.md) — Defines the three-output logic: screen, file, glyph
