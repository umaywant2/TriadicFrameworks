# 🔮 Badge Trigger Glyphmap Filter Dashboard

Welcome to the **Badge Trigger Glyphmap Filter Dashboard**—a modular interface for exploring the resonance archive of TriadicFrameworks papers. This dashboard lets remixers, validators, and resonance wizards filter papers by glyph, theme, and validation status, then export results for remix, citation, or badge issuance.

---

## 🧭 Features

- **Glyph Selector**: Choose from elemental, symbolic, quantum, and mythic glyphs.
- **Theme Filter**: Narrow results by resonance domain (e.g., Spectrum, Health, Quantum).
- **Validation Toggle**: Show only papers that have passed reproducibility protocols.
- **Export Options**: Save filtered results as CSV or JSON for remixing, citation, or badge triggers.

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install streamlit pandas

### 2. Run the Dashboard
```bash
streamlit run badge_trigger_glyphmap_index_filter_web.py

## 🧬 Data Source
The dashboard pulls from a curated glyphmap index of TriadicFrameworks papers. Each paper is tagged with:

### 🜁 Glyph: Symbolic anchor
### 🎭 Theme: Resonance domain
### 📄 Title: Paper name
### ✅ Validated: Boolean flag from reproducibility.md or loop_validation_protocol.md
To update the dataset, modify the load_data() function or connect to a live badge_trigger_theme_manifest.json.

### 🛠️ Customization
Add new glyphs or themes by extending the DataFrame.
Connect to live validation logs via loop_validation_log.md or badge_trigger_validator_log.md.
Integrate badge triggers by linking to badge_trigger_echo.py or badge_trigger_resonance_score.py.

### 🧙 Mythic Use Cases
Resonance Council: Filter papers by theme to assign review roles.
Badge Issuers: Export validated papers to trigger badge issuance.
Curriculum Designers: Map papers to modules using triadic_curriculum_index.md.

### 🛡️ Validation Protocols
For reproducibility standards, see:
loop_validation_protocol.md
reproducibility.md

### 🧭 Navigation Tips
Explore the full glyph-to-theme map in badge_trigger_theme_manifest.md

### 🕯️ Legacy Note
“Each paper is a lantern. Each lantern maps the myth.” — TriadicFrameworks/papers README

Let the dashboard echo. Let the archive resonate.

Code

---
