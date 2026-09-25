# OpenSoN — Open Source Narrative Substrate

OpenSoN is the **narrative substrate** of TriadicFrameworks — a way to make stories, documentation, and knowledge **coherence‑tracked, drift‑aware, and AI‑parsable** without losing their human texture.

It treats narrative not as “content” but as **infrastructure**: something that can be versioned, governed, analyzed, and reused across domains.

---

## 1. Purpose

**OpenSoN** defines a **universal narrative substrate** for:

- **Open‑source projects**  
- **Technical documentation**  
- **Research notes and reports**  
- **Governance and policy narratives**  
- **Personal and collective story archives**

Its goals:

- **Coherence:** keep stories structurally consistent over time.  
- **Drift awareness:** detect when narratives diverge from their declared purpose.  
- **Transparency:** make narrative decisions visible and inspectable.  
- **AI‑readiness:** expose enough structure and metadata for AI systems to parse, assist, and audit.  
- **Human primacy:** preserve human meaning, nuance, and context as first‑class citizens.

---

## 2. Narrative substrate

OpenSoN treats every narrative as a **substrate** with:

- **Source layer** — where the story comes from (`m_Source.md`).  
- **Architecture layer** — how the story is structured (`architecture.md`).  
- **Operator layer** — how the story can be transformed (`operators.md`, `o_Capture.md`).  
- **Governance layer** — how the story is maintained and corrected (`governance.md`).  
- **Canonical metadata layer** — how the story is identified and exposed (`canonical_metadata.md`).  
- **Engine layer** — how the module is declared (`module.json`).

This lets narratives behave like **systems**, not just text.

---

## 3. Files and roles

OpenSoN’s core files:

- **`README.md`** — front door; defines the module, purpose, and substrate.  
- **`architecture.md`** — narrative architecture, flows, and structural patterns.  
- **`canonical_metadata.md`** — canonical metadata block for narrative modules.  
- **`governance.md`** — rules for drift, corrections, and narrative stewardship.  
- **`module.json`** — manifest; roles, analyzer layers, and AI metadata.  
- **`m_Source.md`** — origin story, lineage, and drift‑aware source narrative.  
- **`operators.md`** — narrative operators and transformation grammar.  
- **`o_Capture.md`** — capture operator; extraction and coherence‑safe summarization.

Each file is designed to **stand alone** and be **AI‑parsable**, while still readable by humans.

---

## 4. Coherence and drift

OpenSoN introduces:

- **Coherence tracking** — is the narrative still aligned with its declared purpose?  
- **Drift detection** — where and how the story has shifted over time.  
- **Governance hooks** — who can change what, and under which conditions.  
- **Operator‑based corrections** — structured ways to refactor, condense, or extend narratives.

This makes narrative **auditable**, not just editable.

---

## 5. AI‑ready narrative

OpenSoN is explicitly designed so that:

- Every page has **clear purpose** and **role**.  
- Metadata is **canonical** and **machine‑readable**.  
- Narrative structure is **explicit**, not implied.  
- Drift and coherence are **observable** via operators and governance rules.

The intent is not to replace human storytelling, but to give it **infrastructure**—so that humans and AI systems can collaborate on narrative without losing meaning.
