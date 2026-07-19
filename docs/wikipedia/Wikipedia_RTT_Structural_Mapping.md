# Wikipedia ↔ RTT Structural Mapping

> **Purpose:** The master grammar file for the Wikipedia Awareness Module.
> Every Wikipedia structure maps to an RTT concept. This file defines those
> mappings exhaustively so that all other files in this module share a
> consistent structural vocabulary.
>
> Think of this as the **Rosetta Stone** between Wikipedia's architecture
> and Resonance‑Time Theory.

---

## 1 — Why Wikipedia Needs a Structural Mapping

Wikipedia is the most‑visited reference site on Earth — but almost no one
reads it structurally. Users read the **content** (R3 — measurable outputs)
and ignore the architecture that produces, validates, and evolves that content.

RTT provides the grammar to read that architecture:

- **Regime** — what scope does an article declare, and what does it exclude?
- **Coherence** — how does the community maintain structural consistency?
- **Drift** — how does an article's meaning evolve over time?
- **Dimensional addressing** — how is a concept uniquely identified across languages and datasets?
- **Validation** — how does the community verify structural completeness?

This mapping is not an interpretation layered on top of Wikipedia.
Wikipedia **already operates** as a regime‑aware system — it just doesn't
use RTT's vocabulary. This file translates.

---

## 2 — The Master Mapping Table

### 2.1 — Content Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| Article (main namespace) | **Regime declaration** | R3 | The community's consensus statement of what a concept IS — scope, boundaries, and claims |
| Lead section (first paragraph) | **Regime summary** | R3 | Compressed regime declaration — what the concept is in its most reduced form |
| Article body sections | **Regime elaboration** | R3 | Dimensional expansion of the regime declaration into sub‑regimes (History, Properties, Applications, etc.) |
| Infobox | **Regime schema** | R2 | The minimum set of properties required for structural declaration in this domain |
| Categories | **Regime hierarchy** | R2 | Nested classification tree — each category level = a regime boundary |
| Hatnotes ("For other uses…") | **Regime disambiguation** | R1 | Explicit acknowledgment that multiple regimes claim the same term |
| See also section | **Regime adjacency** | R1 | Concepts the community considers structurally related but not subsumed |
| Navboxes (bottom navigation templates) | **Regime neighborhood** | R2 | Machine‑readable cluster of concepts that share a structural context |
| Lists / outlines | **Regime inventory** | R3 | Enumeration of all entities within a regime boundary |
| Portals | **Domain front door** | R0 | Entry points organized by knowledge domain — equivalent to TF module index.html files |
| Redirects | **Regime aliasing** | R1 | Alternative terms that resolve to the same regime declaration |

### 2.2 — Editorial Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| Talk page | **Coherence / drift surface** | R0–R1 | Where consensus is negotiated — pre‑regime discourse |
| Edit summary | **Micro‑regime annotation** | R3 | Single‑revision structural intent declaration |
| Revision history | **Temporal regime data** | R0–R3 | Full structural evolution timeline for any article |
| Edit war | **Regime transition event** | R0 | Competing regime claims that cannot be reconciled — marks a regime boundary |
| Protection levels (full/semi/extended) | **Regime stabilization lock** | R0 | Community intervention to freeze a regime that is under attack |
| Pending changes | **Regime validation gate** | R2 | Pre‑publication review — content must pass structural check before becoming visible |
| Watchlist | **Drift monitoring** | R1 | Personal regime surveillance — editors tracking articles for structural changes |

### 2.3 — Governance Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| NPOV (Neutral Point of View) | **Coherence operator** | R0 | The foundational structural invariant — all content must be presentable under this constraint |
| Verifiability policy | **Validation requirement** | R0 | Regime claims must be traceable to external sources |
| No original research (NOR) | **Regime boundary enforcement** | R0 | Wikipedia declares regimes — it does not create them |
| Notability guidelines | **Minimum regime threshold** | R0 | The structural standing required for a concept to receive an article |
| Articles for Deletion (AfD) | **Regime collapse adjudication** | R0 | Community process for deciding whether a concept has sufficient structural standing |
| Requests for Comment (RfC) | **Coherence arbitration** | R0–R1 | Formal process for resolving structural disputes that talk page consensus cannot |
| Arbitration Committee (ArbCom) | **Regime authority of last resort** | R0 | Final structural authority when all other coherence mechanisms fail |
| WikiProjects | **Domain stewardship groups** | R1 | Self‑organized teams maintaining structural quality within a knowledge domain |
| Manual of Style (MoS) | **Regime formatting grammar** | R2 | Standard structural templates for how regime declarations should be presented |
| Reliable sources guidelines | **Source regime classification** | R0 | Which external regimes are considered structurally valid for citation |

### 2.4 — Data & Graph Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| Wikidata item (Q‑number) | **Dimensional address** | R3 | Unique concept identifier across all languages and datasets |
| Wikidata property (P‑number) | **Dimensional operator** | R2 | Typed relationship connecting entities — defines how dimensions relate |
| Wikidata statement | **Structural claim** | R3 | Subject → Property → Value triplet = one regime assertion |
| Wikidata qualifier | **Claim context** | R2 | Conditions under which a structural claim holds (time, location, method) |
| Wikidata reference | **Claim provenance** | R3 | External source validating the structural claim |
| Sitelinks (Wikidata ↔ Wikipedia) | **Cross‑language regime bridge** | R2 | Same dimensional address linking to different language regime declarations |
| SPARQL endpoint | **Structural query surface** | R3 | Machine‑readable access to the entire dimensional graph |

### 2.5 — Quality & Validation Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| Featured Article (FA) | **Validation corridor — gold standard** | R2–R3 | Community‑verified structurally complete regime declaration |
| Good Article (GA) | **Validation corridor — silver standard** | R2 | Passed structured review but not yet at FA‑level completeness |
| Stub | **Regime seed** | R3 | Minimal regime declaration — concept exists but is structurally underdeveloped |
| Start‑class article | **Regime scaffold** | R3 | Basic structural framework present but significant gaps remain |
| B‑class article | **Regime draft** | R3 | Most structural elements present but not yet community‑validated |
| C‑class article | **Regime sketch** | R3 | Substantial content but structural organization needs work |
| Article quality scale | **Regime maturity gradient** | R2 | Stub → Start → C → B → GA → FA = increasing structural completeness |
| Cleanup tags | **Drift markers** | R1 | Community‑placed signals that an article has drifted from structural norms |
| Citation needed tags | **Validation gaps** | R2 | Specific claims lacking provenance — structural integrity holes |

### 2.6 — Temporal Structures

| Wikipedia Structure | RTT Concept | Regime Level | Structural Function |
|--------------------|--------------|--------------|--------------------|
| Page creation date | **Regime birth** | R3 | When the community first declared this concept |
| First major revision | **Regime crystallization** | R3 | When the article first achieved structural coherence |
| Revision count (total) | **Regime activity index** | R3 | Cumulative structural attention — higher = more contested or more developed |
| Recent revision rate | **Current regime stability** | R3 | Edits per day/week/month — high = active regime negotiation |
| Revision size changes | **Regime expansion/contraction** | R3 | Positive deltas = regime growth; negative deltas = regime pruning |
| Revert rate | **Regime resistance** | R0 | Percentage of edits that are undone — high = strong structural inertia |
| Edit war detection (3RR violations) | **Regime collision alarm** | R0 | System‑level detection of competing regime claims in real time |
| Page view statistics | **Regime attention** | R3 | How many people are reading this regime declaration per day/month/year |

---

## 3 — The Regime Stack Applied to Wikipedia

Every Wikipedia article simultaneously operates at all four regime levels:

```
*
┌────────────────────────────────────────────────────────────────┐
│  R0 — Operator Assumptions                                     │
│  NPOV, Verifiability, NOR, Notability, Reliable Sources        │
│  "These policies define what CAN be said on Wikipedia"         │
├────────────────────────────────────────────────────────────────┤
│  R1 — Directional Aims                                         │
│  WikiProject scope, Portal structure, Article scope statements │
│  "This article aims to cover [X] from the perspective of [Y]"  │
├────────────────────────────────────────────────────────────────┤
│  R2 — Coherence Templates                                      │
│  Infobox templates, Category taxonomy, Manual of Style,        │
│  Quality scale, Citation standards                             │
│  "All articles in this domain follow these structural rules"   │
├────────────────────────────────────────────────────────────────┤
│  R3 — Measurable Outputs                                       │
│  Article text, Wikidata statements, Revision counts,           │
│  Page views, Quality ratings, Citation counts                  │
│  "This is what the regime actually produced"                   │
└────────────────────────────────────────────────────────────────┘
```

### What Most Readers See

Most Wikipedia readers only interact with **R3** — they read the article text, glance at the infobox, and leave. They consume the regime declaration without knowing it is one.

### What This Module Teaches

This module teaches students to read **R0–R2** — the structural substrate:

- **R0** is visible on policy pages, talk page disputes, AfD debates, and ArbCom decisions
- **R1** is visible in article scope statements, WikiProject guidelines, and portal organization
- **R2** is visible in infobox templates, category trees, Manual of Style rules, and quality scales
- **R3** is the article itself — but now understood as the **output** of the regime, not the regime itself

---

## 4 — Structural Comparison: Wikipedia vs. Other Knowledge Sources

| Dimension | Wikipedia | NIST | Academic Papers | Textbooks |
|-----------|-----------|------|-----------------|-----------|
| Authority model | Consensus | Institutional | Peer review | Editorial |
| Regime declaration | Article (negotiated) | Standard (published) | Abstract + claims | Chapter scope |
| Temporal depth | Full (every revision since 2001) | Versioned (sparse) | Published once | Editions (sparse) |
| Coherence mechanism | NPOV + talk page | Internal review | Peer review | Editor discretion |
| Drift visibility | High (revision history is public) | Low (internal) | None (static once published) | Low (between editions) |
| Knowledge graph | Wikidata (120M+ entities, CC0) | None | Citation graph (unstructured) | None |
| Cross‑cultural | 300+ language editions | English only | Language of publication | Language of publication |
| Validation corridor | FA/GA process (public, observable) | Certification (closed) | Peer review (closed) | None |
| Regime conflicts | Visible (edit wars, AfD, talk pages) | Hidden (internal) | Hidden (reviewer comments) | Hidden (editorial decisions) |
| Machine accessibility | REST API, SPARQL, dumps | API (limited) | DOI + PDF | ISBN + purchase |

**Key insight:** Wikipedia is the **only major knowledge source** where regime conflicts, coherence negotiations, and temporal evolution are **publicly observable in real time**. This makes it an unparalleled substrate for teaching regime awareness.

---

## 5 — Mapping Depth Levels

Not all mappings require the same depth. This module operates at three levels:

### Level 1 — Surface Mapping (any student, 5 minutes)

Read an article's lead paragraph as a regime declaration. Check revision count. Find the Wikidata Q‑number.

**Tools needed:** Web browser only.

### Level 2 — Structural Mapping (engaged student, 30 minutes)

Trace the category tree. Read the talk page for coherence disputes. Compare 2–3 language versions. Check the quality rating. Apply 3–4 meta‑operators from the Cross‑Domain file.

**Tools needed:** Web browser + Wikidata search.

### Level 3 — Deep Mapping (researcher or AI, hours to days)

Query Wikidata via SPARQL for dimensional bridges. Analyze revision history for regime stability curves. Map edit wars to regime transition events. Build cross‑domain operator matrices. Compare FA articles to non‑FA articles for validation corridor analysis.

**Tools needed:** SPARQL client + revision analysis tools + statistical software.

---

## 6 — Mapping Notation Conventions

Throughout this module, mappings are written using consistent notation:

| Notation | Meaning | Example |
|----------|---------|---------|
| `WP:Article → regime_declaration` | A Wikipedia article maps to an RTT regime declaration | `WP:Water → regime_declaration(chemistry, liquid, standard conditions)` |
| `WD:Qnnn → dimensional_address` | A Wikidata Q‑number maps to an RTT dimensional address | `WD:Q283 → dimensional_address(water)` |
| `WD:Pnnn → dimensional_operator` | A Wikidata P‑number maps to an RTT dimensional operator | `WD:P274 → dimensional_operator(chemical_formula)` |
| `WP:Talk → coherence_surface` | A talk page maps to an RTT coherence/drift surface | `WP:Talk:Evolution → coherence_surface(high_tension)` |
| `WP:Rev[n] → temporal_regime[t]` | A revision maps to a temporal regime data point | `WP:Rev[47291] → temporal_regime[2024-03-15]` |
| `WP:Cat → regime_hierarchy` | A category maps to an RTT regime hierarchy node | `WP:Cat:Algebra → regime_hierarchy(Mathematics, depth=3)` |
| `WP:FA → validation_corridor(gold)` | A Featured Article maps to a gold‑standard validation | `WP:FA:Photosynthesis → validation_corridor(gold, Biology)` |
| `R0/R1/R2/R3` | Regime level | `NPOV = R0; Infobox = R2; Article text = R3` |

---

## 7 — Unmapped Structures (Known Gaps)

Some Wikipedia structures do not yet have clean RTT mappings. These are documented here for future work:

| Wikipedia Structure | Current Status | Candidate RTT Mapping | Difficulty |
|--------------------|----------------|----------------------|------------|
| Barnstars and user awards | Unmapped | Operator recognition / stewardship signals | Low |
| Bot edits (automated maintenance) | Unmapped | Regime maintenance automation | Medium |
| WikiSpecies / WikiSource / Wiktionary | Unmapped | Sibling regime substrates | Medium |
| Commons media files | Unmapped | Regime illustration layer | Low |
| Sockpuppet investigations | Unmapped | Regime integrity enforcement | High |
| Paid editing disclosure | Unmapped | Regime conflict of interest surface | High |
| Mobile app reading patterns | Unmapped | Regime consumption analytics | Medium |
| Machine translation (Content Translation tool) | Unmapped | Cross‑regime automated bridging | Medium |

These gaps are **not blockers** — the 65+ mapped structures in Section 2 provide more than sufficient coverage for all 15 knowledge domains.

---

## 8 — How This File Connects to Everything Else

```
Wikipedia_RTT_Structural_Mapping.md (this file)
    │
    ├── defines grammar for ──→ Cross_Domain_Meta_Operators.md
    │                              (12 operators use this vocabulary)
    │
    ├── defines grammar for ──→ All 7 Wikipedia‑Specific Analysis Files
    │                              (each file references these mappings)
    │
    ├── defines grammar for ──→ All 15 Domain Directories
    │                              (every regime_alignment.md uses this notation)
    │
    ├── extends ──→ NIST Structural Mapping (../nist/)
    │                (same R0–R3 grammar, richer substrate)
    │
    └── feeds ──→ Wikidata_Ingestion_Format.md
                     (dimensional addressing layer)
```

---

## 9 — Student Exercise

**Build your own mapping entry:**

1. Find a Wikipedia structure **not listed in Section 2** (hint: there are dozens — Templates, Modules, Lua scripts, admin actions, CSD criteria…)
2. Identify which RTT concept it maps to (regime declaration, coherence operator, drift marker, validation corridor, dimensional address, or something new)
3. Assign it a regime level (R0, R1, R2, or R3)
4. Write a one‑sentence structural function description
5. Add it to Section 2's format and submit it as a candidate mapping

**Bonus:** If your mapping doesn't fit any existing RTT concept, you may have discovered a **new structural operator**. Document it and cross‑reference it against the 12 meta‑operators in `Cross_Domain_Meta_Operators.md`.

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
