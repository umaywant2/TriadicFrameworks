# Wikidata Ingestion Format

> **Purpose:** Define how TriadicFrameworks ingests, queries, and structurally
> interprets Wikidata — the world's largest open knowledge graph (120M+ entities,
> CC0 license). Wikidata is Wikipedia's **dimensional addressing layer** — the
> machine‑readable substrate beneath every human‑readable article.
>
> This file provides SPARQL templates, ingestion patterns, and RTT mappings
> so that students, researchers, and AIs can query Wikidata with structural
> awareness.

---

## 1 — What Is Wikidata?

Wikidata is a **free, collaborative, multilingual knowledge graph** maintained
by the Wikimedia Foundation. It stores structured data as entity–property–value
triplets that can be queried via SPARQL.

### Key Facts

| Dimension | Value |
|-----------|-------|
| Entities | 120M+ items (Q‑numbers) |
| Properties | 12,000+ relationship types (P‑numbers) |
| Statements | 2B+ structural claims |
| Languages | Labels in 400+ languages |
| License | CC0 — public domain (no attribution required) |
| Query endpoint | `https://query.wikidata.org/` |
| Entity lookup | `https://www.wikidata.org/wiki/Qnnn` |
| Property lookup | `https://www.wikidata.org/wiki/Property:Pnnn` |

### Why CC0 Matters

Wikidata's CC0 license means **no copyright restrictions on reuse**. Unlike
Wikipedia article text (CC BY‑SA 4.0, which requires attribution and share‑alike),
Wikidata statements can be freely ingested, transformed, and republished
without any license obligations. This makes Wikidata the **ideal ingestion
substrate** for automated RTT analysis.

---

## 2 — RTT Structural Mapping

### 2.1 — The Core Triplet

Every Wikidata statement follows the pattern:

```
Subject (Q‑number) → Property (P‑number) → Value (Q‑number, string, or quantity)
```

In RTT terms:

```
Dimensional Address → Dimensional Operator → Structural Claim
```

**Example:**

```
Q283 (Water) → P274 (chemical formula) → "H₂O"

RTT reading:
  dimensional_address(Water)
    → dimensional_operator(chemical_formula)
      → structural_claim("H₂O")
```

### 2.2 — Full Mapping Table

| Wikidata Element | RTT Concept | Function |
|-----------------|-------------|----------|
| Item (Q‑number) | **Dimensional address** | Unique coordinate for a concept across all languages and datasets |
| Property (P‑number) | **Dimensional operator** | Typed relationship that connects dimensional addresses |
| Statement | **Structural claim** | One regime assertion: "this entity has this property with this value" |
| Qualifier | **Claim context** | Conditions under which the claim holds (time range, location, method, applies‑to) |
| Reference | **Claim provenance** | External source validating the structural claim |
| Rank (preferred/normal/deprecated) | **Claim confidence** | Structural standing of the claim — preferred = regime consensus; deprecated = superseded regime |
| Sitelink | **Cross‑language regime bridge** | Same dimensional address linking to regime declarations in different language Wikipedias |
| Label | **Regime name** | Human‑readable name for the dimensional address in a specific language |
| Description | **Regime summary** | One‑sentence regime declaration in a specific language |
| Aliases | **Regime aliases** | Alternative names that resolve to the same dimensional address |

### 2.3 — Qualifiers as Regime Context

Qualifiers are what make Wikidata structurally rich — they add **context** to
claims, turning flat assertions into regime‑aware statements:

| Qualifier Property | RTT Function | Example |
|-------------------|--------------|---------|
| P580 (start time) | **Regime birth** | "Germany (Q183) → capital (P36) → Berlin (Q64), start time: 1990" |
| P582 (end time) | **Regime expiry** | "Germany (Q183) → capital (P36) → Bonn (Q586), end time: 1990" |
| P585 (point in time) | **Regime snapshot** | "World population (Q11188) → population (P1082) → 8B, point in time: 2023" |
| P1013 (criterion used) | **Regime method** | "Mount Everest (Q513) → elevation (P2044) → 8848.86m, criterion: EGM2008 geoid" |
| P459 (determination method) | **Measurement regime** | How the value was obtained — structural provenance |
| P518 (applies to part) | **Sub‑regime scope** | The claim applies to a specific sub‑component, not the whole entity |
| P1480 (sourcing circumstances) | **Claim reliability** | "circa," "presumably," "possibly" — structural confidence markers |

---

## 3 — SPARQL Query Templates

All queries run at `https://query.wikidata.org/`

### 3.1 — Basic: Get All Properties for an Entity

**Use case:** What does the knowledge graph say about a concept?

```sparql
# All statements for a given entity
# Replace Q283 with any Q-number
SELECT ?property ?propertyLabel ?value ?valueLabel
WHERE {
  wd:Q283 ?claim ?statement .
  ?statement ?ps ?value .
  ?property wikibase:claim ?claim .
  ?property wikibase:statementProperty ?ps .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?propertyLabel
```

**RTT reading:** This returns the **full regime declaration** for a concept —
every structural claim the knowledge graph makes about it.

---

### 3.2 — Cross‑Domain Bridging: Find All Domains a Concept Touches

**Use case:** How many knowledge domains does this concept connect to?

```sparql
# Count cross-domain P-number bridges for an entity
# Replace Q283 with any Q-number
SELECT ?property ?propertyLabel
       (COUNT(DISTINCT ?value) AS ?connections)
WHERE {
  wd:Q283 ?claim ?statement .
  ?statement ?ps ?value .
  ?property wikibase:claim ?claim .
  ?property wikibase:statementProperty ?ps .
  FILTER(ISIRI(?value))
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
GROUP BY ?property ?propertyLabel
ORDER BY DESC(?connections)
```

**RTT reading:** Each P‑number that points to an entity in a different domain
= a **dimensional bridge**. The count of cross‑domain bridges = the concept's
**structural connectivity score**.

---

### 3.3 — Temporal Regime Analysis: Track Property Changes Over Time

**Use case:** How has a concept's regime evolved?

```sparql
# Temporal regime evolution for a property
# Example: Population of France over time
SELECT ?population ?pointInTime
WHERE {
  wd:Q142 p:P1082 ?statement .
  ?statement ps:P1082 ?population .
  ?statement pq:P585 ?pointInTime .
}
ORDER BY ?pointInTime
```

**RTT reading:** Each row = a **temporal regime snapshot**. The series reveals
the regime's evolution curve — growth, stability, decline, or oscillation.

---

### 3.4 — Regime Hierarchy: Traverse the Class Tree

**Use case:** Where does a concept sit in the regime hierarchy?

```sparql
# Class hierarchy (upward traversal) for an entity
# Replace Q283 with any Q-number
SELECT ?class ?classLabel ?depth
WHERE {
  wd:Q283 wdt:P31/wdt:P279* ?class .
  {
    SELECT ?class (COUNT(?mid) AS ?depth)
    WHERE {
      wd:Q283 wdt:P31/wdt:P279* ?mid .
      ?mid wdt:P279* ?class .
    }
    GROUP BY ?class
  }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
ORDER BY ?depth
```

**RTT reading:** This traces the concept's position in the **regime hierarchy** —
from specific instance up through increasingly general regime classifications.
Depth = regime granularity. Breadth at each level = regime diversity.

---

### 3.5 — Cross‑Language Regime Comparison: Sitelink Coverage

**Use case:** How many languages declare this concept?

```sparql
# Count Wikipedia sitelinks (language versions) for an entity
SELECT ?sitelink
WHERE {
  ?sitelink schema:about wd:Q283 .
  ?sitelink schema:isPartOf/wikibase:wikiGroup "wikipedia" .
}
```

**RTT reading:** Each sitelink = a **regime declaration in a different cultural
context**. High sitelink count = universally recognized concept. Low count =
culturally specific or specialized regime. Comparing article lengths across
sitelinks reveals **cultural regime variance** — same concept, different
structural emphasis.

---

### 3.6 — Validation Corridor: Find Featured Articles by Domain

**Use case:** What are the structurally validated reference points in a domain?

```sparql
# Find items with Featured Article sitelinks in English Wikipedia
# Filter by domain using instance-of (P31) or subclass-of (P279)
SELECT ?item ?itemLabel ?article
WHERE {
  ?article schema:about ?item .
  ?article schema:isPartOf <https://en.wikipedia.org/> .
  ?article wikibase:badge wd:Q17437796 .
  ?item wdt:P31/wdt:P279* wd:Q11344 .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
LIMIT 50
```

**RTT reading:** Featured Articles = **validation corridor gold standard**.
These are the concepts whose regime declarations have been community‑verified
as structurally complete. They serve as reference templates for the domain.

---

### 3.7 — Regime Collision: Find Disambiguation Entities

**Use case:** Which concepts have competing regime claims on the same term?

```sparql
# Find disambiguation items — concepts where multiple regimes
# claim the same term
SELECT ?item ?itemLabel ?article
WHERE {
  ?item wdt:P31 wd:Q4167410 .
  ?article schema:about ?item .
  ?article schema:isPartOf <https://en.wikipedia.org/> .
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
  }
}
LIMIT 100
```

**RTT reading:** Every disambiguation entity = a **regime collision point** —
two or more structural regimes claiming the same term. The list of disambiguated
meanings reveals the competing regime declarations.

---

## 4 — Ingestion Patterns

### 4.1 — Single Entity Deep Profile

**Purpose:** Build a complete RTT structural profile for one concept.

**Steps:**

1. **Resolve the Q‑number** — search `https://www.wikidata.org/w/api.php?action=wbsearchentities&search=TERM&language=en&format=json`
2. **Pull all statements** — use Query 3.1
3. **Count dimensional bridges** — use Query 3.2
4. **Trace the regime hierarchy** — use Query 3.4
5. **Check sitelink coverage** — use Query 3.5
6. **Check for Featured Article badge** — use Query 3.6

**Output format:**

```json
{
  "entity": "Q283",
  "label": "Water",
  "regime_declaration": "chemical compound, binary compound, oxide",
  "dimensional_bridges": 47,
  "regime_hierarchy_depth": 8,
  "sitelink_count": 298,
  "featured_article": true,
  "top_properties": [
    "P274 (chemical formula): H₂O",
    "P31 (instance of): chemical compound",
    "P361 (part of): hydrosphere",
    "P2054 (density): 997 kg/m³",
    "P2101 (melting point): 0°C"
  ],
  "cross_domain_connections": [
    "Chemistry (compound properties)",
    "Physics (thermodynamic constants)",
    "Biology (biological role)",
    "Earth Sciences (hydrosphere)",
    "Engineering (industrial solvent)",
    "Medicine (essential nutrient)"
  ]
}
```

### 4.2 — Domain Sweep

**Purpose:** Map all Wikidata entities within a knowledge domain.

**Steps:**

1. Identify the domain's root class (e.g., Physics → Q413 "physics")
2. Query all instances and subclasses:
   ```sparql
   SELECT ?item ?itemLabel
   WHERE {
     ?item wdt:P31/wdt:P279* wd:Q413 .
     SERVICE wikibase:label {
       bd:serviceParam wikibase:language "en" .
     }
   }
   LIMIT 1000
   ```
3. For each entity, count cross‑domain P‑number bridges
4. Rank by structural connectivity
5. The top‑ranked entities = the domain's **most structurally connected concepts**

### 4.3 — Temporal Regime Tracking

**Purpose:** Monitor how a concept's regime evolves over time.

**Steps:**

1. Select a property with temporal qualifiers (P580/P582/P585)
2. Use Query 3.3 to extract the time series
3. Plot the series: stable plateaus = crystallized regime; sharp transitions = regime shifts
4. Cross‑reference with Wikipedia revision history for the same period — do article edits correlate with Wikidata property changes?

### 4.4 — Cross‑Language Regime Divergence

**Purpose:** Compare how the same concept is structurally declared across cultures.

**Steps:**

1. Use Query 3.5 to get all sitelinks
2. For the top 5 largest language editions, compare:
   - Article length (word count)
   - Section structure (headings)
   - Lead paragraph (regime declaration)
   - Categories assigned
3. Divergences = **cultural regime variance** — same dimensional address, different structural emphasis

---

## 5 — Property Families for RTT Analysis

Not all 12,000+ P‑numbers are equally useful for RTT analysis. These **property families** provide the highest structural signal:

### 5.1 — Classification Properties (Regime Identity)

| Property | Name | RTT Function |
|----------|------|-------------|
| P31 | instance of | **Regime declaration** — "this entity IS a [class]" |
| P279 | subclass of | **Regime hierarchy** — "this class is WITHIN [parent class]" |
| P361 | part of | **Regime containment** — "this entity is PART OF [whole]" |
| P527 | has part(s) | **Regime composition** — "this entity CONTAINS [parts]" |
| P460 | said to be the same as | **Regime aliasing** — cross‑ontology identity claim |
| P1889 | different from | **Regime boundary** — "do not confuse with [other entity]" |

### 5.2 — Relationship Properties (Dimensional Bridges)

| Property | Name | RTT Function |
|----------|------|-------------|
| P737 | influenced by | **Regime lineage** — structural ancestry |
| P1542 | has effect | **Regime causation** — what this entity produces |
| P1269 | facet of | **Regime perspective** — this entity is one view of a broader concept |
| P2283 | uses | **Regime dependency** — structural requirements |
| P366 | has use | **Regime application** — what this entity enables |

### 5.3 — Temporal Properties (Regime Dynamics)

| Property | Name | RTT Function |
|----------|------|-------------|
| P571 | inception | **Regime birth** — when the concept first existed |
| P576 | dissolved/abolished | **Regime death** — when the concept ceased to exist |
| P580 | start time | **Regime activation** — when a claim became true |
| P582 | end time | **Regime expiry** — when a claim stopped being true |
| P585 | point in time | **Regime snapshot** — claim valid at a specific moment |
| P1319 | earliest date | **Regime lower bound** — structural uncertainty floor |
| P1326 | latest date | **Regime upper bound** — structural uncertainty ceiling |

### 5.4 — Quantitative Properties (Regime Metrics)

| Property | Name | RTT Function |
|----------|------|-------------|
| P1082 | population | **Regime scale** (demographic) |
| P2044 | elevation above sea level | **Regime position** (geographic) |
| P2054 | density | **Regime density** (physical) |
| P2067 | mass | **Regime mass** (physical) |
| P2101 | melting point | **Regime phase boundary** (thermodynamic) |
| P2102 | boiling point | **Regime phase boundary** (thermodynamic) |
| P2196 | students count | **Regime scale** (educational) |
| P4010 | GDP per capita | **Regime scale** (economic) |

---

## 6 — Rate Limits and Ethical Use

### Wikidata Query Service Limits

| Limit | Value |
|-------|-------|
| Query timeout | 60 seconds |
| Results per query | 500,000 rows max |
| Concurrent connections | 5 per IP |
| User‑Agent required | Yes — identify your tool/project |

### Ethical Guidelines

1. **Respect rate limits** — do not flood the endpoint with parallel queries
2. **Set a User‑Agent header** — identify yourself: `User-Agent: TriadicFrameworks/1.0 (https://www.triadicframeworks.org/; contact@triadicframeworks.org)`
3. **Cache results** — don't re‑query the same data repeatedly
4. **Use database dumps for bulk analysis** — the query endpoint is for interactive and moderate‑scale use
5. **Contribute back** — if you discover missing data or errors, edit Wikidata directly (it's open for anyone to edit)

---

## 7 — Relationship to Other Module Files

| File | Connection |
|------|-----------|
| `Wikipedia_RTT_Structural_Mapping.md` | Defines the RTT vocabulary this file uses (Q = dimensional address, P = dimensional operator) |
| `Cross_Domain_Meta_Operators.md` | Operator 4 (Wikidata Dimensional Bridging) depends directly on Query 3.2 from this file |
| `Category_Taxonomy_Regime_Hierarchy.md` | Wikipedia categories and Wikidata class hierarchy (P31/P279) are parallel regime classification systems — this file covers the Wikidata side |
| `Revision_History_Regime_Analysis.md` | Wikidata items have their own revision history — combine with Wikipedia article revision history for complete temporal coverage |
| `Edit_War_Regime_Transition_Detection.md` | Wikidata edit wars (P31 disputes, label conflicts) are structurally equivalent to Wikipedia edit wars |
| All 15 domain directories | Every domain's `regime_alignment.md` references Wikidata entities for its core concepts |
| `../resonance_atlas/nist_ingestion_format.md` | Sibling — NIST ingestion format covers a single institutional source; this file covers a crowdsourced knowledge graph |

---

## 8 — Student Exercises

### Exercise 1 — Entity Profile (15 minutes)

1. Pick any concept you know well
2. Find its Wikidata Q‑number at `https://www.wikidata.org/`
3. List its top 10 properties (P‑numbers)
4. Classify each property into one of the 4 property families from Section 5
5. Write a 1‑sentence regime declaration based on the P31 (instance of) value

### Exercise 2 — Dimensional Bridging (30 minutes)

1. Pick a concept with high cross‑domain connectivity (try: Energy Q11379, Information Q11028, Evolution Q1063, or Network Q1900326)
2. Run Query 3.2 to count its dimensional bridges
3. List the top 5 P‑numbers by connection count
4. For each, identify which knowledge domain the bridge connects to
5. Draw a simple diagram: your concept in the center, domains around the edges, P‑numbers as labeled connections

### Exercise 3 — Cross‑Language Regime Variance (30 minutes)

1. Pick a concept you expect to have cultural variance (try: Democracy Q7174, Marriage Q8445, or Freedom Q124490)
2. Run Query 3.5 to count its sitelinks
3. Open the Wikipedia article in English + 2 other languages (use Google Translate if needed)
4. Compare: article length, section headings, lead paragraph framing
5. Write a 2‑sentence summary: *"The English Wikipedia declares [concept] as [X]. The [other language] Wikipedia declares it as [Y]. The structural difference reveals [Z]."*

### Exercise 4 — Temporal Regime Tracking (45 minutes)

1. Pick a concept with temporal data (try: any country's population, a city's mayor, or a company's CEO)
2. Run Query 3.3 to extract the time series
3. Identify: stable plateaus, sharp transitions, gradual trends
4. Cross‑reference with the Wikipedia article's revision history for the same period
5. Answer: *"Do Wikidata property changes and Wikipedia article edits correlate? If so, which leads — the data change or the narrative change?"*

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
