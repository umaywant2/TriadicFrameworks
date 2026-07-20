# Physics — Student Exercises

> **Purpose:** Hands‑on, regime‑aware exercises using **live Wikipedia Physics
> content**. Every exercise sends students to real Wikipedia articles, talk
> pages, revision histories, Wikidata entities, and category trees — then
> asks them to apply the structural analysis frameworks from this module.
>
> **Prerequisites:** Familiarity with `overview.md` and `regime_alignment.md`
> in this directory. For deeper context, reference the cross‑domain files
> in the parent directory (especially `Wikipedia_RTT_Structural_Mapping.md`
> and `Cross_Domain_Meta_Operators.md`).
>
> **Difficulty scale:** ⚡ = 15 min | ⚡⚡ = 30 min | ⚡⚡⚡ = 45–60 min

---

## Exercise 1 — Regime Declaration Parsing ⚡

### The Task

Read the **lead paragraph** of 3 Physics articles and extract the implicit
regime declaration from each.

### Instructions

1. Open the following Wikipedia articles:
   - [Classical mechanics](https://en.wikipedia.org/wiki/Classical_mechanics)
   - [Quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics)
   - [Thermodynamics](https://en.wikipedia.org/wiki/Thermodynamics)

2. For each article's lead paragraph, answer:

| Question | Classical Mechanics | Quantum Mechanics | Thermodynamics |
|----------|-------------------|-------------------|----------------|
| What scope does it claim? | | | |
| What boundary conditions are stated or implied? | | | |
| What is explicitly excluded? | | | |
| What regime level is the lead paragraph operating at? (R0/R1/R2/R3) | | | |

3. Write a one‑sentence **regime summary** for each:
   *"[Article] declares a regime that covers [scope], applies when [boundary conditions], and excludes [exclusions]."*

### What You're Learning

Every Wikipedia article's lead paragraph is a compressed regime declaration.
Most readers absorb the content without noticing the structural claims.
This exercise trains you to read the declaration itself — what is being
claimed, what is being bounded, and what is being left out.

### Going Deeper

Compare your three regime summaries. Notice how Classical Mechanics and
Quantum Mechanics **declare overlapping scope but different boundary
conditions** — Classical applies when ħ → 0, Quantum applies at atomic
scales. This is the **nested regime structure** described in
`regime_alignment.md` Section 6.3.

---

## Exercise 2 — Revision History as Regime Signal ⚡⚡

### The Task

Analyze the revision history of a Physics article to classify its
**regime phase** and detect any **perturbation events**.

### Instructions

1. Pick one of these articles (or choose your own Physics article):
   - [Higgs boson](https://en.wikipedia.org/wiki/Higgs_boson)
   - [Gravitational wave](https://en.wikipedia.org/wiki/Gravitational_wave)
   - [Dark matter](https://en.wikipedia.org/wiki/Dark_matter)

2. Open the article's statistics page:
   `https://xtools.wmcloud.org/articleinfo/en.wikipedia.org/ARTICLE_TITLE`

3. Record these signals:

| Signal | Your Article's Value |
|--------|---------------------|
| Total revisions | |
| Total editors | |
| Top editor's share (%) | |
| Monthly average edits (recent year) | |
| Article age (years) | |
| Current size (bytes) | |

4. Look at the **edits‑over‑time chart**. Identify any **spike months** —
   months where the revision count was dramatically higher than average.

5. For each spike, answer:
   - What external event caused it? (Nobel Prize? Experimental discovery? News coverage?)
   - Was the perturbation **additive** (new data expanding the article) or **structural** (reclassification or framing change)?
   - How long did the perturbation last before the article returned to baseline?

6. Classify the article's current **regime phase** using the 6‑phase model
   from `Revision_History_Regime_Analysis.md` Section 3:

   ☐ Birth | ☐ Expansion | ☐ Negotiation | ☐ Crystallization | ☐ Maturity | ☐ Perturbation

### What You're Learning

Revision history is **temporal regime data**. A spike in edits is not
random — it marks a moment when the article's regime was structurally
affected by an external event. In Physics, most perturbations are
**additive** (new experimental results) rather than **structural**
(paradigm shifts). This exercise trains you to distinguish the two.

---

## Exercise 3 — The Nested Regime Hierarchy ⚡⚡

### The Task

Trace the **nested regime structure** of Physics by walking from a
specific Physics article upward through its category tree and downward
through its Wikidata class hierarchy.

### Instructions

1. Open the article [Special relativity](https://en.wikipedia.org/wiki/Special_relativity)

2. **Category path (upward):**
   - Scroll to the bottom of the article and find its categories
   - Click through parent categories until you reach "Category:Science"
     or "Category:Main topic classifications"
   - Record the full path (e.g., Special relativity → Relativity → Physics → Science → ...)

3. **Wikidata path (upward):**
   - Click "Wikidata item" in the left sidebar (or go to `https://www.wikidata.org/wiki/Q43514`)
   - Find the P31 (instance of) and P279 (subclass of) statements
   - Trace the class chain upward: Special relativity → ? → ? → ...

4. Fill in this table:

| Level | Category Path | Wikidata Path | Same or Different? |
|-------|--------------|---------------|-------------------|
| 1 (most specific) | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 (most general) | | | |

5. Answer:
   - Where do the two paths **agree**?
   - Where do they **diverge**?
   - Which path gives a more structurally informative hierarchy? Why?

6. Now locate Special Relativity in the **nested regime diagram** from
   `regime_alignment.md` Section 6.3:

   ```
   QFT → QM → Classical Mechanics → Newtonian Mechanics
   QFT → General Relativity → Special Relativity → Galilean Relativity
   ```

   Does the category tree or the Wikidata hierarchy better reflect this
   nesting? Write 2 sentences explaining your answer.

### What You're Learning

Physics has two parallel classification systems on Wikipedia — the
community‑edited category tree and the ontologically structured Wikidata
hierarchy. They often disagree. This exercise trains you to read both
systems and identify where **editorial judgment** (categories) diverges
from **formal ontology** (Wikidata). The nested regime structure of
Physics (each theory as a limiting case of a more general theory) is
Physics' most distinctive structural feature — but neither classification
system captures it perfectly.

---

## Exercise 4 — NPOV at the Interpretation Boundary ⚡⚡

### The Task

Examine how Wikipedia handles **competing quantum interpretations** —
the one area where Physics' strong consensus breaks down and NPOV stress
rises to Level 3 (Contested).

### Instructions

1. Open the article [Interpretations of quantum mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics)

2. **Framing analysis:**
   - Read the lead paragraph. Does it favor any single interpretation?
   - Read the table/list of interpretations. How many are listed?
   - Is the ordering of interpretations structurally significant?
     (Does the article list Copenhagen first because it's historically primary,
     or because it has more adherents?)

3. **Talk page analysis:**
   - Navigate to the talk page (`Talk:Interpretations of quantum mechanics`)
   - Scan the active threads and recent archives
   - Classify any disputes you find using the 7 Canonical Patterns from
     `Talk_Page_Coherence_Surface.md` Section 4.1:

   | Thread | Pattern | Regime Level (R0/R1/R2/R3) |
   |--------|---------|---------------------------|
   | | | |
   | | | |
   | | | |

4. **NPOV stress assessment:**
   - Count attribution phrases in the article ("according to," "proponents argue," "critics contend")
   - Check for NPOV‑related cleanup templates
   - Classify the article's NPOV stress level (1–5) using
     `NPOV_As_Coherence_Operator.md` Section 3

5. Write a 3‑sentence summary:
   *"The Interpretations article is at NPOV Stress Level [N] because [evidence].
   The most common talk page dispute pattern is [pattern], which operates at
   regime level [R0/R1/R2/R3]. This is unusual for Physics because [reason —
   most Physics articles are Level 1–2]."*

### What You're Learning

Physics' NPOV stress is almost entirely concentrated at the **interpretation
boundary** — where the mathematical formalism (R2–R3) is uncontested but
its structural meaning (R0–R1) is disputed. This exercise trains you to
find the exact location of NPOV stress within a domain and understand
why it concentrates there.

---

## Exercise 5 — Wikidata Dimensional Bridging ⚡⚡

### The Task

Use Wikidata to map the **cross‑domain connections** of a fundamental
Physics concept.

### Instructions

1. Go to `https://www.wikidata.org/wiki/Q11382` (Entropy)

2. List all P‑number properties and group them by domain:

| Property (P‑number) | Value | Domain |
|---------------------|-------|--------|
| | | Physics / Chemistry / CS / Philosophy / ... |
| | | |
| | | |
| | | |

3. Count the **dimensional bridges** — P‑number connections that point
   to entities in domains **other than Physics**.

4. Answer:
   - How many domains does Entropy bridge to?
   - Which bridge is the strongest (most connections to that domain)?
   - Is there a domain connection you didn't expect?

5. Now do the same for one of these:
   - `Q11379` (Energy)
   - `Q11408` (Wavelength)
   - `Q11423` (Mass)

6. Compare the two concepts:
   *"[Concept A] bridges to [N] domains, while [Concept B] bridges to [M].
   The most unexpected bridge is [concept] → [domain] via [P‑number].
   This reveals that [structural insight]."*

### What You're Learning

Wikidata's P‑number connections are **dimensional bridges** — they reveal
which domains are structurally linked to a Physics concept. Physics
concepts tend to have the **highest dimensional connectivity** of any
domain because Physics provides the substrate on which other sciences
build. This exercise makes that connectivity visible and countable.

---

## Exercise 6 — Featured Article Structural Benchmark ⚡⚡⚡

### The Task

Compare a Featured Article in Physics to a non‑FA article in the same
sub‑domain to identify the **structural gap** — what separates a
community‑validated regime declaration from an ordinary one.

### Instructions

1. Pick a pair:
   - **FA:** [Speed of light](https://en.wikipedia.org/wiki/Speed_of_light) (or [General relativity](https://en.wikipedia.org/wiki/General_relativity))
   - **Non‑FA:** Pick any B‑class or Start‑class article in the same sub‑domain
     (e.g., a specific experiment, a less‑known constant, or a subtopic)

2. For each article, record:

| Metric | FA Article | Non‑FA Article | Gap |
|--------|-----------|---------------|-----|
| Word count | | | × |
| Reference count | | | × |
| Section count | | | × |
| Image count | | | × |
| Wikidata P‑number count | | | × |
| Talk page archives | | | × |
| Quality rating | FA | ? | — |

3. **Section structure comparison:**
   - List the FA's section headings
   - List the non‑FA's section headings
   - Which sections does the non‑FA lack?

4. **Source quality comparison:**
   - Sample 5 references from each article
   - Classify each as: peer‑reviewed journal / textbook / news source / website / other
   - Which article has a higher proportion of peer‑reviewed sources?

5. Write a 3‑sentence structural assessment:
   *"The FA has [N]× more [sources/sections/words] than the non‑FA.
   The primary structural gap is [specific dimension]. To reach FA status,
   the non‑FA would need [specific improvements]."*

### What You're Learning

Featured Articles are **structural benchmarks** — they represent the
community's answer to "what does a complete regime declaration look like
in this domain?" By comparing an FA to a non‑FA, you learn to see the
specific structural dimensions that separate a validated declaration from
an incomplete one. This is directly applicable to writing or improving
Wikipedia articles.

---

## Exercise 7 — Physics Edit War Archaeology ⚡⚡⚡

### The Task

Find and analyze a **resolved edit war** in Physics to understand how
a regime collision was structurally resolved.

### Instructions

1. Check one of these sources for Physics edit wars:
   - [Wikipedia:Lamest edit wars/Science](https://en.wikipedia.org/wiki/Wikipedia:Lamest_edit_wars#Science)
   - Talk page archives of contested Physics articles (Quantum mechanics,
     String theory, Cold fusion, Faster‑than‑light neutrino anomaly)

2. When you find a resolved dispute, record:

| Dimension | Detail |
|-----------|--------|
| Article | |
| War period | |
| War type (Section 2 of Edit War file) | Factual / Classification / Framing / Inclusion / Naming |
| Competing claims | Claim A: ... vs. Claim B: ... |
| Peak severity (1–5) | |
| Resolution pattern | Displacement / Synthesis / Separation / Freeze |
| Duration | |

3. Read the talk page discussion that accompanied the edit war:
   - What arguments did each side make?
   - What sources did each side cite?
   - How was consensus eventually reached (or imposed)?

4. Classify the dispute's **regime level**:
   - Was it about facts (R3)?
   - Was it about framing (R1)?
   - Was it about scope or foundational assumptions (R0)?

5. Write a 4‑sentence structural narrative:
   *"The edit war on [article] was a [type] war between [Claim A] and [Claim B].
   It reached severity level [N] and lasted [duration]. The resolution was
   [pattern] because [reason]. The dispute operated at regime level [R0/R1/R2/R3]
   because [evidence]."*

### What You're Learning

Edit wars in Physics are rare compared to Political Science or History,
but when they occur, they are structurally revealing. Physics edit wars
almost always occur at the **interpretation boundary** (R0–R1) — where
the mathematical formalism is uncontested but its meaning is disputed.
This exercise trains you to read edit wars as **diagnostic instruments**
for regime boundary mapping.

---

## Exercise 8 — Cross‑Language Regime Comparison ⚡⚡⚡

### The Task

Compare how the **same Physics concept** is structurally declared in
3 different language Wikipedias.

### Instructions

1. Pick a Physics concept with broad cross‑language coverage:
   - Quantum mechanics (Q944)
   - Energy (Q11379)
   - Black hole (Q589)
   - Schrödinger equation (Q165498)

2. Open the article in **English** + **2 other languages** of your choice
   (use the language links in the left sidebar, or start from the Wikidata
   item's sitelinks)

3. For each language version, record (use Google Translate if needed):

| Dimension | English | Language 2 | Language 3 |
|-----------|---------|-----------|-----------|
| Article length (scroll estimate: short/medium/long) | | | |
| Number of sections | | | |
| Lead paragraph focus (what does it emphasize?) | | | |
| Has mathematical formulation section? | | | |
| Has history section? | | | |
| Has applications section? | | | |
| Quality rating (if visible on talk page) | | | |
| Number of references (approximate) | | | |

4. **Structural divergence analysis:**
   - Do any language versions include sections that the English version lacks?
   - Do any language versions omit sections that the English version has?
   - Is the lead paragraph framing the same or different across languages?

5. Write a 3‑sentence comparison:
   *"The English version of [concept] emphasizes [X], while the [language 2]
   version emphasizes [Y]. The most significant structural divergence is
   [specific difference]. This reveals that [insight about cross‑cultural
   regime declaration for Physics concepts]."*

### What You're Learning

Physics is one of the **most translationally stable** domains on Wikipedia
because its mathematical substrate is language‑independent. But structural
divergences still exist — different language editions may emphasize
different applications, historical figures, or experimental traditions.
This exercise trains you to detect cultural regime variance even in a
domain where you'd expect uniformity.

---

## Exercise 9 — The SI Unit Regime ⚡

### The Task

Examine how Physics articles handle **unit conventions** — a small but
structurally revealing coherence template.

### Instructions

1. Open these 3 articles:
   - [Electron mass](https://en.wikipedia.org/wiki/Electron_mass) (or the Electron article's mass section)
   - [Speed of light](https://en.wikipedia.org/wiki/Speed_of_light)
   - [Planck length](https://en.wikipedia.org/wiki/Planck_length)

2. For each, identify:

| Article | Primary unit used | Alternative units given | Sub‑regime signal |
|---------|------------------|----------------------|-------------------|
| | | | |
| | | | |
| | | | |

3. Answer:
   - Which article uses **SI units** as primary? Which uses **natural units** or domain‑specific units?
   - When an article switches from SI to natural units (ħ = c = 1), what sub‑regime has the reader entered?
   - The Speed of light article states the exact value in m/s. Why is there **zero uncertainty** on this constant?
     (Hint: since 2019, the meter is **defined** in terms of the speed of light)

4. Write one sentence: *"Unit choice in Physics articles is a coherence
   template signal — when an article uses [alternative units], it is declaring
   that the reader has entered the [sub‑domain] sub‑regime."*

### What You're Learning

Unit choice is a **regime declaration in miniature**. SI units are the
default measurement regime of Physics on Wikipedia. When an article departs
from SI (using electron‑volts, natural units, Planck units, or solar masses),
it is signaling entry into a specialized sub‑regime. This exercise trains
you to read unit conventions as structural markers.

---

## Exercise 10 — Build a Physics Regime Map ⚡⚡⚡

### The Task

Synthesize everything from this domain directory into a single
**Physics regime map** — a visual summary of how Physics is structurally
organized on Wikipedia.

### Instructions

1. Using the information from `overview.md`, `regime_alignment.md`, and
   the exercises above, create a diagram or table that includes:

   - The **nested regime hierarchy** (QFT → QM → Classical → Newtonian; GR → SR → Galilean)
   - The **category tree top level** (12+ branches)
   - The **NPOV stress zones** (mark where stress rises above Level 2)
   - The **validation corridor** (mark which branches have the most FAs)
   - The **dimensional bridges** (mark where Physics connects to other domains)
   - The **perturbation history** (mark major external events that affected Physics articles)

2. Format: hand‑drawn diagram, digital whiteboard, markdown table, or any
   format you prefer. The structure matters more than the aesthetics.

3. Write a 5‑sentence summary:
   - Sentence 1: What is Physics' most distinctive structural feature on Wikipedia?
   - Sentence 2: Where is Physics' regime most stable?
   - Sentence 3: Where is Physics' regime most contested?
   - Sentence 4: How does Physics' regime structure compare to one other domain you've explored?
   - Sentence 5: What is one thing you learned about Physics by reading it structurally that you wouldn't have learned by reading it normally?

### What You're Learning

This capstone exercise integrates all the analytical frameworks from the
module into a single structural view. By building a regime map, you
practice the core RTT skill — seeing the structural architecture beneath
the content surface. A regime map of Physics is a map of how humanity
organizes its most fundamental knowledge about the universe.

---

## Quick Reference: Where to Find Things

| What You Need | Where to Find It |
|--------------|-----------------|
| Any Wikipedia article | `https://en.wikipedia.org/wiki/ARTICLE_TITLE` |
| Talk page | `https://en.wikipedia.org/wiki/Talk:ARTICLE_TITLE` |
| Revision history | `https://en.wikipedia.org/w/index.php?title=ARTICLE_TITLE&action=history` |
| Article statistics (XTools) | `https://xtools.wmcloud.org/articleinfo/en.wikipedia.org/ARTICLE_TITLE` |
| Wikidata entity | `https://www.wikidata.org/wiki/Qnnn` (or click "Wikidata item" in article sidebar) |
| Category tree browser | `https://en.wikipedia.org/wiki/Special:CategoryTree` |
| PetScan (category intersections) | `https://petscan.wmcloud.org/` |
| Featured Articles list | `https://en.wikipedia.org/wiki/Wikipedia:Featured_articles` |
| Edit war reference | `https://en.wikipedia.org/wiki/Wikipedia:Lamest_edit_wars` |
| Regime alignment framework | `regime_alignment.md` in this directory |
| Cross‑domain meta‑operators | `../Cross_Domain_Meta_Operators.md` |
| NPOV stress spectrum | `../NPOV_As_Coherence_Operator.md` Section 3 |
| Revision history analysis | `../Revision_History_Regime_Analysis.md` |

---

*This file is part of the [Physics domain directory](.) in the
[Wikipedia Awareness Module](../README.md) of the
[TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
