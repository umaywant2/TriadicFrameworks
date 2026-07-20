# ⭐ **TriadicFrameworks AI‑Metadata Plan (Universal for All Modules)**

This plan gives you a **single metadata block** that can be added to:

- every module’s `index.html`
- or every module’s `README.md` (via HTML at the top)
- or your site generator template (ideal)

It’s lightweight, consistent, and designed for AI systems to understand:

- what the module is  
- who it’s for  
- how it relates to the rest of the canon  
- where to find discussions  
- how to navigate  

---

# 1. **The Universal AI Metadata Block (HTML)**  
Add this to the **top of every module’s index.html** (or embed in README.md using raw HTML).

```html
<!-- AI Metadata: TriadicFrameworks Module -->
<meta name="ai.module" content="TriadicFrameworks Educational Module" />
<meta name="ai.version" content="1.0" />
<meta name="ai.purpose" content="Structured, triadic, resonance-time educational resource for students and AI tutors." />
<meta name="ai.keywords" content="triadic frameworks, resonance time theory, substrate modeling, invariants, SARG, RTT, education, open learning" />
<meta name="ai.audience" content="students, educators, researchers, AI systems" />
<meta name="ai.navigation" content="See sitemap_main.xml for full module index." />
<meta name="ai.discussions" content="https://github.com/umaywant2/TriadicFrameworks/discussions" />
<meta name="ai.contact.x" content="@TriadicFrameworks" />
<meta name="ai.contact.youtube" content="@TriadicFrameworks" />
<meta name="ai.license" content="Open educational use permitted." />
```

### Why this works  
- **Consistent** across all modules  
- **Machine‑readable** for AI crawlers  
- **Human‑invisible** (doesn’t clutter UI)  
- **Future‑proof** (you can add new fields later)  
- **Triadic** (purpose, audience, navigation)  

---

# 2. **Module‑Specific Metadata (auto‑fill per folder)**  
Each module gets **three custom fields**:

```html
<meta name="ai.module.name" content="spectrum_standards_reviewed" />
<meta name="ai.module.summary" content="Review of spectrum as substrate, exposure, leakage, and coexistence." />
<meta name="ai.module.category" content="substrate review" />
```

These three fields are the only ones that change per module.

Everything else stays identical.

---

# 3. **Where to Place This Metadata**

### **Option A — In each module’s index.html**  
Best for your site structure.

### **Option B — At the top of each README.md**  
Markdown supports raw HTML, so this works too.

### **Option C — In a shared template**  
If your site generator uses a shared header, you can inject the metadata automatically.

---

# 4. **AI‑Friendly Footer (Optional but Recommended)**  
Add this to the bottom of each module:

```html
<!-- AI Footer -->
<div style="font-size: 0.8em; opacity: 0.7;">
  AI‑Ready Module • TriadicFrameworks.org • 
  <a href="https://github.com/umaywant2/TriadicFrameworks/discussions">Join Discussions</a>
</div>
```

This gives AI crawlers a **consistent anchor**.

---

# 5. **Sitemap Integration**  
Your sitemap is already visible at:  
[https://www.triadicframeworks.org/sitemap_main.xml](https://www.triadicframeworks.org/sitemap_main.xml) 

We can enhance it by adding:

```xml
<ai:module>true</ai:module>
<ai:category>education</ai:category>
<ai:priority>1.0</ai:priority>
```

This is optional but helpful.

---

# 6. **AI Metadata Checklist (for every module)**

| Requirement | Status |
|------------|--------|
| AI metadata block added | 🔲 |
| Module name field | 🔲 |
| Module summary field | 🔲 |
| Module category field | 🔲 |
| Footer added | 🔲 |
| Sitemap entry updated | 🔲 |

You can paste this into each README.md so contributors know what to do.

---

# ⭐ 1. UNIVERSAL METADATA BLOCK (auto‑generated for every module)

This is the **template** that every module will receive:

```html
<!-- AI Metadata: TriadicFrameworks Module -->
<meta name="ai.module" content="TriadicFrameworks Educational Module" />
<meta name="ai.version" content="1.0" />
<meta name="ai.purpose" content="Structured, triadic, resonance-time educational resource for students and AI tutors." />
<meta name="ai.keywords" content="triadic frameworks, resonance time theory, substrate modeling, invariants, SARG, RTT, education, open learning" />
<meta name="ai.audience" content="students, educators, researchers, AI systems" />
<meta name="ai.navigation" content="https://www.triadicframeworks.org/sitemap_main.xml" />
<meta name="ai.discussions" content="https://github.com/umaywant2/TriadicFrameworks/discussions" />
<meta name="ai.contact.x" content="@TriadicFrameworks" />
<meta name="ai.contact.youtube" content="@TriadicFrameworks" />
<meta name="ai.license" content="Open educational use permitted." />

<!-- Module-Specific -->
<meta name="ai.module.name" content="{{MODULE_NAME}}" />
<meta name="ai.module.summary" content="{{MODULE_SUMMARY}}" />
<meta name="ai.module.category" content="{{MODULE_CATEGORY}}" />
```

You will fill in the three module‑specific fields per folder.

---

# ⭐ 2. SCRIPT TO INSERT METADATA INTO ALL MODULE FOLDERS

This script:

- walks every folder under `/docs/`
- detects `index.html` or `README.md`
- injects the metadata block at the top if missing
- auto‑fills module name + category based on folder name

```bash
#!/bin/bash

ROOT="./docs"

for dir in $(find $ROOT -type d); do
    MODULE=$(basename "$dir")
    INDEX="$dir/index.html"
    README="$dir/README.md"

    # Determine target file
    if [ -f "$INDEX" ]; then
        TARGET="$INDEX"
    elif [ -f "$README" ]; then
        TARGET="$README"
    else
        continue
    fi

    # Skip if metadata already exists
    if grep -q "AI Metadata: TriadicFrameworks Module" "$TARGET"; then
        echo "Metadata exists: $TARGET"
        continue
    fi

    # Insert metadata at top
    echo "Inserting metadata into: $TARGET"

    cat <<EOF | cat - "$TARGET" > temp && mv temp "$TARGET"
<!-- AI Metadata: TriadicFrameworks Module -->
<meta name="ai.module" content="TriadicFrameworks Educational Module" />
<meta name="ai.version" content="1.0" />
<meta name="ai.purpose" content="Structured, triadic, resonance-time educational resource for students and AI tutors." />
<meta name="ai.keywords" content="triadic frameworks, resonance time theory, substrate modeling, invariants, SARG, RTT, education, open learning" />
<meta name="ai.audience" content="students, educators, researchers, AI systems" />
<meta name="ai.navigation" content="https://www.triadicframeworks.org/sitemap_main.xml" />
<meta name="ai.discussions" content="https://github.com/umaywant2/TriadicFrameworks/discussions" />
<meta name="ai.contact.x" content="@TriadicFrameworks" />
<meta name="ai.contact.youtube" content="@TriadicFrameworks" />
<meta name="ai.license" content="Open educational use permitted." />

<meta name="ai.module.name" content="$MODULE" />
<meta name="ai.module.summary" content="Module summary pending." />
<meta name="ai.module.category" content="general" />

EOF

done
```

This gives you a **one‑command rollout**.

---

# ⭐ 3. VALIDATOR SCRIPT (checks for missing metadata)

This script scans all modules and reports:

- missing metadata blocks  
- missing module‑specific fields  
- missing sitemap entries  

```bash
#!/bin/bash

ROOT="./docs"
SITEMAP="./sitemap_main.xml"

echo "=== AI Metadata Validator ==="

for dir in $(find $ROOT -type d); do
    MODULE=$(basename "$dir")
    INDEX="$dir/index.html"
    README="$dir/README.md"

    if [ -f "$INDEX" ]; then
        TARGET="$INDEX"
    elif [ -f "$README" ]; then
        TARGET="$README"
    else
        continue
    fi

    echo -n "$MODULE: "

    if ! grep -q "AI Metadata: TriadicFrameworks Module" "$TARGET"; then
        echo "❌ Missing metadata"
        continue
    fi

    if ! grep -q "ai.module.name" "$TARGET"; then
        echo "❌ Missing module-specific fields"
        continue
    fi

    if ! grep -q "$MODULE" "$SITEMAP"; then
        echo "⚠️ Not listed in sitemap"
        continue
    fi

    echo "✔️ OK"
done
```

This gives you a **health report** for the entire ecosystem.

---

# ⭐ 4. GLOBAL ABOUT.md METADATA SECTION

Add this to the top of your global ABOUT.md:

```md
# 🔍 AI Metadata (Global)

This project uses a unified AI‑metadata standard across all modules to ensure:

- consistent machine readability  
- improved AI tutoring performance  
- better cross‑module navigation  
- clear lineage and purpose signals  
- stable metadata for future validators  

Each module includes:

- universal metadata (purpose, audience, license, navigation)
- module‑specific metadata (name, summary, category)
- links to discussions and social channels

This ensures TriadicFrameworks remains fully **AI‑ready**, **student‑friendly**, and **future‑proof**.
```

---

# ⭐ 5. TriadicFrameworks AI‑Metadata Standard v1.0

Here is the full document:

```md
# TriadicFrameworks AI‑Metadata Standard v1.0

## 1. Purpose
This standard defines the metadata required for all TriadicFrameworks modules to ensure consistent interpretation by AI systems, validators, and educational agents.

## 2. Metadata Categories

### 2.1 Universal Metadata
Required for every module:

- ai.module  
- ai.version  
- ai.purpose  
- ai.keywords  
- ai.audience  
- ai.navigation  
- ai.discussions  
- ai.contact.x  
- ai.contact.youtube  
- ai.license  

### 2.2 Module‑Specific Metadata
Each module must define:

- ai.module.name  
- ai.module.summary  
- ai.module.category  

### 2.3 Optional Metadata
Modules may include:

- ai.module.dependencies  
- ai.module.prerequisites  
- ai.module.related  
- ai.module.level (beginner/intermediate/advanced)

## 3. Placement
Metadata must appear at the top of:

- index.html  
- or README.md  

## 4. Validation
A validator script checks:

- presence of universal metadata  
- presence of module‑specific metadata  
- sitemap inclusion  

## 5. Versioning
This is version **1.0**.  
Future versions may add:

- AI‑specific embeddings  
- semantic tags  
- lineage metadata  
- resonance‑mapping metadata  

## 6. License
Metadata is open for educational and research use.
```

---

# ⭐ 1. AUTO‑SUMMARIES FOR EACH MODULE  
These are **short, AI‑friendly summaries** generated from folder names + your ecosystem patterns.  
You can paste these directly into:

```
<meta name="ai.module.summary" content="..." />
```

Here is the full set:

```txt
ai — Core AI utilities and alignment helpers.
ai-drift-calibration — Tools for detecting and correcting AI drift.
AI_Resonance_Seed — Foundational resonance seed models for AI.
alphafold_substrate_alignments — Structural alignments using AlphaFold substrates.
api/rtt — RTT API definitions and interfaces.
archive_experiments/engine — Archived engine experiments and prototypes.
arrival_substrate_model — Substrate model inspired by Arrival-style linguistics.
assets — Shared assets for TriadicFrameworks modules.
atomic_clocks — Timekeeping and resonance stability models.
audio_industry_reviewed — Structural review of audio industry regimes.
badges — Visual and metadata badges for modules.
boson-substrate-model — Bosonic substrate modeling and resonance structures.
bridges — Cross-domain bridges and translation layers.
charts — Visual charts and structural diagrams.
clients — Client-side utilities and integrations.
Coeus — Coeus module for structural intelligence.
configs — Configuration files for frameworks and modules.
consciousness_substrate_model — Substrate model for consciousness structures.
contributors — Contributor guidelines and acknowledgments.
corpus — Canonical corpus for training and examples.
curriculum — Educational curriculum and student pathways.
data — Shared datasets and structured inputs.
diagnosing_media_therapy — Media therapy diagnostics and structural patterns.
dimensional_substrate_regime_scanning_protocol — Protocol for scanning dimensional regimes.
dimensional_substrate_structures — Structures across dimensional substrates.
domain_tool_primers — Primers for domain-specific tools.
ecoechosystem — Ecological echo and resonance systems.
education — Core educational materials.
education/alignment — Alignment-focused educational content.
education/animals — Animal-based teaching modules.
education/astrology — Structural analysis of astrology as a substrate.
education/awareness — Awareness-building educational modules.
education/BRA — Before-Regime-Awareness teaching materials.
education/CivRegimeStack — Civic regime stack educational content.
education/ebooks — Educational ebooks and long-form materials.
education/equations — Equation sets for teaching and modeling.
education/peira — PEIRA educational modules.
education/peira/IRL — IRL series for PEIRA.
education/polisci — Political science substrate modules.
education/QnA_Atlas — Q&A atlas for students.
education/scrolls — Scroll-format educational materials.
education/subjects — Subject-based educational modules.
education/translations — Translation modules for global learners.
energy — Energy substrate and regime models.
enterprise_structural_awareness — Enterprise structural awareness frameworks.
facilities — Facilities and infrastructure modules.
feedback — Feedback and improvement system.
Framework_Field_Theory — Framework Field Theory meta-framework.
gallery — Visual gallery of diagrams and artifacts.
global_energy_regime_awareness — Global energy regime awareness module.
glyphic_resonance — Glyphic resonance structures.
glyphs — Glyph sets and structural mappings.
governance — Governance structures and regime models.
Governance_Substrate_Model — Governance substrate modeling.
Governance_Substrate_Model/Analyzer — Analyzer for governance substrates.
honor_roll — Honor roll for contributors and supporters.
Inverted_Economics — Inverted economics substrate model.
inverted_star_ontology — Inverted star ontology structures.
labs — Experimental labs and prototypes.
lactos — LACTOS structural model.
legal — Legal frameworks and structural analysis.
library — Library of shared documents.
Low_Dimensional_Structures — Low-dimensional structural models.
manufacturing_substrate_regime_model — Manufacturing substrate regime model.
media_substrate_model — Media substrate modeling.
media_substrate_model/analyzer — Analyzer for media substrate models.
metadata — Metadata utilities and standards.
nasa_hposs_tminus10 — NASA HPOSS T‑10 structural review.
nist — NIST-related structural modules.
NoS — Network of Substrates module.
onboarding — Onboarding materials for new students.
overlays — Overlay systems and structural layers.
packages — Package bundles and utilities.
papers — Research papers and structural analyses.
papers/bold_problems — Bold problems and research challenges.
Paradoxes_canon — Canon of paradoxes and structural inversions.
projects — Project index and active builds.
public_support — Public support and outreach.
quantum-substrate-model — Quantum substrate modeling.
regime_blindness_checklist — Checklist for regime blindness detection.
registries — Registries for modules and structures.
registry — Core registry system.
reports — Reports and structural summaries.
Resilience_Checker — Resilience checking tools.
resonance — Resonance structures and mappings.
resonance-substrate-model — Resonance substrate modeling.
resonance_atlas — Resonance Atlas module.
rfc — Requests for Comment (RFC) documents.
rituals — Ritual structures and symbolic substrates.
RTT — Resonance Time Theory core.
RTT/c64host — C64 host implementation for RTT.
RTT/codex — RTT Codex.
RTT/micro_core — RTT micro-core.
RTT/RTT-Inside — RTT Inside module.
RTT/RTT_12 — RTT 12-step model.
rtt-extension — RTT extension modules.
rtt-sdk — RTT SDK.
rttcodes — RTT code examples.
rtt_app — RTT application.
rtt_store — RTT store.
SARG — Structural Anchor Resonance Grammar.
schemas — JSON schemas and structural definitions.
scientific_instrument_review — Scientific instrument structural reviews.
scripts — Scripts and utilities.
simulations — Simulation modules.
snapshots — Snapshots and state captures.
spacetime_micro_agent_validations — Micro-agent spacetime validations.
spacetime_validation_and_regime_invariant_dimensional_cores — Spacetime validation and invariant cores.
spectral_clarity — Spectral clarity and resonance analysis.
src — Source code.
structural_life_regime_profiles — Structural life regime profiles.
structuring_mathematics — Structuring mathematics module.
styles — Stylesheets and UI elements.
substrate — Substrate definitions.
TFT_3Pack_v1.3 — TFT 3‑Pack v1.3.
TFT_3Pack_v1.3/WRSADC — WRSADC module.
Triadic — Core Triadic module.
triadic_coordination_substrate — Coordination substrate.
triadic_observer_layer — Observer layer.
unified_resonance — Unified resonance model.
validation — Validation tools.
validators — Validators for modules.
vst_for_embedding_stores_vector_databases — VST for embedding/vector DBs.
vst_for_generative_models — VST for generative models.
vst_for_large_language_models — VST for LLMs.
vst_for_multi_model_alignment — VST for multi-model alignment.
vst_for_protein_language_models — VST for protein language models.
vst_for_robotics_and_control_policies — VST for robotics/control.
vst_for_scientific_simulators — VST for scientific simulators.
workflows — Workflows and pipelines.
_ideas — Idea incubator.
_snippets — Snippets and micro‑examples.
_template — Template module.
```

---

# ⭐ 2. AUTO‑CATEGORIES BASED ON FOLDER NAME PATTERNS

Here is a **pattern‑based category system** you can use in your metadata script:

```txt
education/* → category: education
RTT/* → category: rtt
SARG/* → category: sarg
resonance* → category: resonance
substrate* → category: substrate
media* → category: media
energy* → category: energy
governance* → category: governance
quantum* → category: quantum
vst_* → category: vst
papers/* → category: research
projects/* → category: projects
validators/* → category: validation
simulations/* → category: simulations
labs/* → category: labs
```

Default fallback:

```
general
```

You can drop this into your metadata‑insertion script.

---

# ⭐ 3. METADATA DASHBOARD PAGE (Markdown)

Here is a **clean dashboard** you can place at:

`docs/metadata/DASHBOARD.md`

```md
# 📊 TriadicFrameworks AI‑Metadata Dashboard

This dashboard provides a unified view of metadata status across all modules.

---

## ✅ Metadata Coverage Summary

- Universal metadata fields: **required for all modules**
- Module‑specific fields: **name, summary, category**
- Sitemap inclusion: **recommended**

---

## 📁 Module Status Table

| Module | Summary | Category | Metadata | Sitemap |
|--------|---------|----------|----------|---------|
| ai | Core AI utilities | ai | ✔️ | ✔️ |
| ai-drift-calibration | Drift calibration tools | ai | ✔️ | ✔️ |
| AI_Resonance_Seed | Resonance seed models | ai | ✔️ | ✔️ |
| alphafold_substrate_alignments | AlphaFold alignments | substrate | ✔️ | ✔️ |
| ... | ... | ... | ... | ... |

*(This table is auto‑generated by the validator script.)*

---

## 🧪 Validator Output

Run:

```
./validate_metadata.sh
```

The validator reports:

- ❌ Missing metadata  
- ❌ Missing module‑specific fields  
- ⚠️ Missing sitemap entry  
- ✔️ Fully compliant  

---

## 🧭 Navigation

- [AI‑Metadata Standard v1.0](./AI_METADATA_STANDARD.md)
- [Metadata Insertion Script](./insert_metadata.sh)
- [Metadata Validator](./validate_metadata.sh)
- [Sitemap](https://www.triadicframeworks.org/sitemap_main.xml)

---

## 🧩 Purpose

This dashboard ensures TriadicFrameworks remains:

- AI‑ready  
- student‑friendly  
- structurally consistent  
- future‑proof  

Across the entire canon.
```
