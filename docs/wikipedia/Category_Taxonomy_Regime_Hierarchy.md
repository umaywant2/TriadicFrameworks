# Category Taxonomy Regime Hierarchy

> **Purpose:** Define how to read Wikipedia's category system as a **native
> regime hierarchy** — a massive, community‑maintained classification tree
> that organizes 6.9 million English articles into nested regime boundaries.
>
> Wikipedia's category tree is not a controlled taxonomy designed by
> information scientists. It is a **crowdsourced, evolving regime map** —
> built by thousands of editors making local classification decisions that
> aggregate into a global structural hierarchy. This makes it messy,
> contradictory in places, and deeply revealing of how humans actually
> organize knowledge.
>
> Where Wikidata provides **dimensional addressing** (unique identifiers),
> the category tree provides **regime topology** (where a concept sits
> relative to all other concepts).

---

## 1 — What Is a Wikipedia Category?

Every Wikipedia article is assigned to one or more **categories** —
classification labels that place the article within a hierarchical tree
of related concepts.

### How Categories Work

| Element | Description | RTT Mapping |
|---------|-------------|-------------|
| Category page | A special page listing all articles and subcategories within it | **Regime boundary declaration** |
| Parent category | The category one level up in the tree | **Regime containment** |
| Subcategory | A category nested within another | **Sub‑regime** |
| Article membership | An article listed in a category | **Regime membership** |
| Hidden category | A maintenance/tracking category not shown to readers | **Infrastructure regime** (stewardship layer) |
| Category intersection | Concept belonging to multiple categories | **Cross‑regime membership** |

### How to Access Categories

| Method | URL / Action |
|--------|-------------|
| View an article's categories | Bottom of any Wikipedia article |
| Browse a category | `https://en.wikipedia.org/wiki/Category:CATEGORY_NAME` |
| Category tree tool | `https://en.wikipedia.org/wiki/Special:CategoryTree` |
| API | `https://en.wikipedia.org/w/api.php?action=query&titles=ARTICLE&prop=categories&format=json` |
| PetScan | `https://petscan.wmcloud.org/` — advanced category intersection queries |

---

## 2 — The Category Tree as Regime Hierarchy

### 2.1 — Structural Anatomy

Wikipedia's category system forms a **directed acyclic graph** (DAG) — not
a strict tree. Categories can have multiple parents, creating a web of
overlapping regime boundaries:

```
                    Category:Main topic classifications
                    (root regime — R0)
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    Category:Science  Category:Society  Category:Technology
    (domain regime)   (domain regime)   (domain regime)
          │                │                │
    ┌─────┴─────┐    ┌────┴────┐     ┌────┴────┐
    │           │    │         │     │         │
  Cat:Physics Cat:Bio Cat:Politics Cat:Law Cat:Computing Cat:Eng
    │           │         │              │
  Cat:Quantum Cat:Genetics Cat:Elections Cat:Programming
  mechanics                                  │
    │                              ┌─────────┴─────────┐
    │                              │                   │
  Cat:Quantum  ←── cross‑link ──→ Cat:Quantum
  mechanics                       computing
```

### 2.2 — The DAG Problem

Because categories form a DAG (not a tree), the same article can be
reached by multiple paths from the root. This is **not a bug** — it
reflects the reality that concepts belong to multiple regimes simultaneously:

| Article | Path 1 | Path 2 | Structural Insight |
|---------|--------|--------|-------------------|
| Water | Science → Chemistry → Chemical compounds | Technology → Industrial processes → Solvents | Same concept, different regime contexts |
| Alan Turing | Science → Computer Science → Computer scientists | Society → LGBT → LGBT scientists | Same person, different regime framings |
| DNA | Science → Biology → Genetics → Nucleic acids | Science → Chemistry → Biomolecules | Same molecule, different domain hierarchies |

**RTT reading:** Multiple category paths = **multiple regime memberships**.
The number of distinct paths from root to an article = the concept's
**regime multiplicity**. Concepts with high multiplicity sit at regime
intersections — they are structurally significant because multiple
classification systems claim them.

### 2.3 — Depth and Breadth

Two key metrics characterize any position in the category hierarchy:

| Metric | Definition | Regime Interpretation |
|--------|-----------|----------------------|
| **Depth** | Number of levels from the article's category to a root category | Regime specificity — deeper = more specialized |
| **Breadth** | Number of sibling categories at the same level | Regime diversity — wider = more differentiated domain |
| **Fan‑out** | Number of subcategories a category contains | Regime granularity — higher fan‑out = more sub‑regime differentiation |
| **Fan‑in** | Number of parent categories a category has | Regime multiplicity — higher fan‑in = cross‑domain concept |
| **Membership count** | Number of articles in a category | Regime population — more articles = larger regime |

---

## 3 — Category Types and Their Regime Functions

### 3.1 — The Six Category Types

| Type | Example | Regime Function | Structural Signal |
|------|---------|----------------|-------------------|
| **Topic category** | Category:Physics | **Domain regime boundary** — defines a knowledge domain | Core structural unit |
| **Set category** | Category:Chemical elements | **Regime inventory** — exhaustive list of members | Countable, bounded regime |
| **Object category** | Category:Stars | **Entity regime** — groups instances of a type | Ontological classification |
| **Activity category** | Category:Scientific methods | **Process regime** — groups methodologies and practices | Operational classification |
| **By‑attribute category** | Category:Physics by country | **Regime faceting** — same domain sliced by an attribute | Reveals regime variance across a dimension |
| **Hidden/maintenance category** | Category:Articles needing cleanup | **Infrastructure regime** — stewardship tracking | Not visible to readers; structural health indicator |

### 3.2 — By‑Attribute Categories as Regime Faceting

**By‑attribute categories** are structurally special — they slice a domain
regime by an external dimension, revealing how the regime varies across
that dimension:

| Pattern | Example | What It Reveals |
|---------|---------|-----------------|
| By country | Category:Physics by country | Geographic regime variance |
| By year | Category:2024 in science | Temporal regime segmentation |
| By nationality | Category:American physicists | Cultural regime attribution |
| By century | Category:19th-century mathematics | Historical regime periodization |
| By type | Category:Types of chemical reactions | Internal regime differentiation |
| By status | Category:Superseded scientific theories | Regime lifecycle classification |

**RTT reading:** By‑attribute categories are **regime cross‑sections** —
they show how a single domain regime manifests differently when sliced
along an external dimension. The existence of a by‑attribute category
means the community considers that dimension **structurally significant**
for that domain.

---

## 4 — The Category Tree vs. Wikidata Class Hierarchy

Wikipedia has **two parallel classification systems**:

| Dimension | Category Tree | Wikidata (P31/P279) |
|-----------|--------------|---------------------|
| Maintained by | Wikipedia editors (per language) | Wikidata editors (cross‑language) |
| Structure | DAG (directed acyclic graph) | Ontological hierarchy (instance‑of / subclass‑of) |
| Consistency | Low — emergent, crowdsourced, sometimes contradictory | Medium — more structured but still community‑edited |
| Scope | 2.3M+ categories in English alone | 120M+ entities globally |
| Machine‑readable | Partially (category API, PetScan) | Fully (SPARQL) |
| Cross‑language | **Different per language edition** | **Unified across all languages** |
| RTT mapping | **Regime topology** (neighborhood, adjacency, containment) | **Dimensional addressing** (unique identity, typed relationships) |

### Key Insight: These Systems Disagree

For any given concept, its Wikipedia category path and its Wikidata
class hierarchy **may tell different stories**:

| Concept | Wikipedia Categories | Wikidata P31/P279 Chain | Discrepancy |
|---------|---------------------|------------------------|-------------|
| Pluto | Category:Dwarf planets | instance of: trans-Neptunian object → subclass of: minor planet → subclass of: planetary-mass object | Wikipedia groups by current classification; Wikidata preserves deeper ontological chain |
| Tomato | Category:Vegetables (in culinary contexts) | instance of: taxon → subclass of: berry (botanical) | Wikipedia follows cultural regime; Wikidata follows biological regime |
| Hong Kong | Category:Special administrative regions of China | instance of: special administrative region → subclass of: administrative territorial entity | Wikipedia categories reflect political framing; Wikidata is more neutral |

**RTT reading:** Category tree = **how the community organizes knowledge**
(cultural, editorial, pragmatic). Wikidata = **how entities are formally
classified** (ontological, structured, cross‑cultural). Disagreements
between them reveal **regime framing differences** — the same concept
declared differently depending on whether the classification is
community‑editorial or ontologically formal.

---

## 5 — Structural Pathologies in the Category Tree

The category tree is crowdsourced and evolving, which means it contains
structural pathologies that are themselves regime signals:

### 5.1 — Overcategorization

**What it is:** An article assigned to 20+ categories, many of which are
semantically overlapping.

**Regime reading:** The concept has **regime sprawl** — it has been claimed
by too many classification systems without consolidation. Overcategorized
articles often sit at regime intersections where no single domain has
primary ownership.

### 5.2 — Undercategorization

**What it is:** An article assigned to only 1–2 very broad categories,
with no subcategory refinement.

**Regime reading:** The concept has **regime isolation** — it hasn't been
claimed by a stewardship group. Often indicates a neglected or newly
created article that no WikiProject has adopted.

### 5.3 — Category Cycles

**What it is:** Category A contains subcategory B, which contains subcategory C,
which contains subcategory A — a circular reference.

**Regime reading:** **Regime hierarchy failure** — the classification
system cannot decide which concept is more general. These are rare
(Wikipedia has bots that detect them) but structurally revealing when
they occur — they mark genuine ontological ambiguity.

### 5.4 — Orphan Categories

**What it is:** A category with no parent categories (disconnected from
the main tree).

**Regime reading:** **Unmoored regime** — a classification that exists but
is not connected to the broader knowledge structure. Often indicates
a recently created or poorly maintained category.

### 5.5 — Eponymous Categories

**What it is:** A category named after a person (Category:Albert Einstein,
Category:Works by Aristotle).

**Regime reading:** **Person‑as‑regime** — the community considers this
individual's work, influence, or legacy significant enough to constitute
its own classification node. The category's subcategories reveal how the
community structures that person's regime (works, influences, legacy,
biographical details).

---

## 6 — API Patterns for Category Analysis

### 6.1 — Get an Article's Categories

```python
import requests

def get_categories(title, lang="en"):
    """Fetch all categories for a Wikipedia article."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "cllimit": "max",
        "clshow": "!hidden",  # exclude maintenance categories
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    page = next(iter(resp["query"]["pages"].values()))
    return [cat["title"].replace("Category:", "")
            for cat in page.get("categories", [])]
```

### 6.2 — Traverse the Category Tree Upward

```python
def trace_to_root(category, lang="en", max_depth=15):
    """Trace a category upward through parent categories toward root."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    path = []
    current = category
    visited = set()

    for depth in range(max_depth):
        if current in visited:
            break  # cycle detection
        visited.add(current)

        params = {
            "action": "query",
            "titles": f"Category:{current}",
            "prop": "categories",
            "cllimit": "max",
            "clshow": "!hidden",
            "format": "json"
        }
        resp = requests.get(url, params=params,
                            headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
        page = next(iter(resp["query"]["pages"].values()))
        parents = [cat["title"].replace("Category:", "")
                   for cat in page.get("categories", [])]

        path.append({
            "depth": depth,
            "category": current,
            "parents": parents
        })

        if not parents or "Contents" in parents[0]:
            break  # reached root
        current = parents[0]  # follow first parent

    return path
```

### 6.3 — Get Subcategories and Membership Count

```python
def get_subcategories(category, lang="en"):
    """Fetch subcategories and article count for a category."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmtype": "subcat",
        "cmlimit": "max",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    subcats = [m["title"].replace("Category:", "")
               for m in resp["query"]["categorymembers"]]

    # Also get article count
    params["cmtype"] = "page"
    resp2 = requests.get(url, params=params,
                         headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    articles = len(resp2["query"]["categorymembers"])

    return {
        "category": category,
        "subcategory_count": len(subcats),
        "subcategories": subcats,
        "article_count": articles
    }
```

### 6.4 — Compute Regime Topology Metrics

```python
def regime_topology(title, lang="en"):
    """Compute regime topology metrics for an article."""
    categories = get_categories(title, lang)

    # Depth: trace each category to root, take the longest path
    max_depth = 0
    all_paths = []
    for cat in categories[:5]:  # sample first 5 to avoid rate limits
        path = trace_to_root(cat, lang)
        depth = len(path)
        max_depth = max(max_depth, depth)
        all_paths.append(path)

    return {
        "article": title,
        "category_count": len(categories),
        "categories": categories,
        "max_depth": max_depth,
        "regime_multiplicity": len(categories),
        "deepest_path": all_paths[0] if all_paths else [],
        "interpretation": classify_topology(len(categories), max_depth)
    }

def classify_topology(cat_count, max_depth):
    """Classify an article's regime topology."""
    if cat_count <= 2 and max_depth <= 3:
        return "isolated_regime"
    elif cat_count <= 5 and max_depth <= 6:
        return "well_classified"
    elif cat_count <= 10 and max_depth <= 10:
        return "cross_domain_concept"
    elif cat_count > 15:
        return "regime_sprawl"
    else:
        return "deeply_specialized"
```

### 6.5 — Cross‑Language Category Comparison

```python
def compare_categories_cross_language(wikidata_qid, languages=None):
    """Compare category assignments for the same concept across languages."""
    if languages is None:
        languages = ["en", "de", "ja", "ar", "es"]

    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "ids": wikidata_qid,
        "props": "sitelinks",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    sitelinks = resp["entities"][wikidata_qid].get("sitelinks", {})

    results = {}
    for lang in languages:
        wiki_key = f"{lang}wiki"
        if wiki_key in sitelinks:
            title = sitelinks[wiki_key]["title"]
            cats = get_categories(title, lang)
            results[lang] = {
                "title": title,
                "category_count": len(cats),
                "categories": cats
            }

    return results
```

---

## 7 — Worked Example: "Energy"

The concept **Energy** sits at one of the deepest regime intersections
in Wikipedia's category tree.

### Category Memberships (English Wikipedia)

| Category | Domain Regime | Depth from Root |
|----------|--------------|----------------|
| Category:Energy | Root domain category | 2 |
| Category:Main topic classifications | Top‑level regime | 1 |
| Category:Physical quantities | Physics sub‑regime | 5 |
| Category:Conservation laws | Physics sub‑regime | 6 |
| Category:Thermodynamic properties | Chemistry/Physics sub‑regime | 6 |
| Category:Energy economics | Economics cross‑regime | 5 |
| Category:Energy and society | Sociology cross‑regime | 4 |
| Category:Energy policy | Political Science cross‑regime | 5 |

### Regime Topology Analysis

- **Category count:** 8+ (high → cross‑domain concept)
- **Max depth:** 6 (moderately specialized)
- **Fan‑in:** 3+ domain regimes claim it (Physics, Economics, Political Science)
- **Regime multiplicity:** Very high — Energy is one of the most cross‑domain concepts on Wikipedia
- **Classification:** `cross_domain_concept` with elements of `regime_sprawl`

### Comparing Wikipedia Categories vs. Wikidata

| System | Classification Path |
|--------|-------------------|
| Wikipedia categories | Energy → Physical quantities → Physics → Science → Main topic classifications |
| Wikidata P31/P279 | energy (Q11379) → instance of: physical quantity (Q107715) → subclass of: property (Q937228) |

**Divergence:** Wikipedia's category tree routes Energy through both
Physics AND Economics AND Policy — reflecting its multi‑regime nature.
Wikidata's class hierarchy routes it strictly through Physics → Physical
quantity — reflecting a more ontologically narrow classification.

**RTT reading:** Wikipedia's category tree is more **regime‑honest** for
cross‑domain concepts like Energy because it preserves multiple regime
memberships. Wikidata's P31/P279 chain is more **ontologically precise**
but loses the cross‑domain richness.

### Cross‑Language Category Comparison

| Language | Category Count | Notable Differences |
|----------|---------------|-------------------|
| English | 8+ | Strong economics and policy categories |
| German | 6 | More physics‑focused, fewer policy categories |
| Japanese | 5 | Includes philosophy category ("気" — ki / energy as life force concept) |
| Arabic | 4 | Fewer categories overall, physics‑dominant |

**Insight:** The Japanese Wikipedia categorizes Energy under a philosophical
concept that has no equivalent in the English category tree — revealing
a **cultural regime frame** that Western categorization misses entirely.

---

## 8 — The Category Tree as a Research Instrument

### 8.1 — Regime Boundary Detection

Categories mark **where one regime ends and another begins**. The boundary
is visible where:

- A category has subcategories belonging to **different WikiProjects**
- An article belongs to categories from **multiple domain regimes**
- A category's talk page has disputes about **what belongs in it**

### 8.2 — Knowledge Gap Detection

Missing or underpopulated categories reveal **regime gaps** — areas where
Wikipedia's structural coverage is incomplete:

| Indicator | What It Reveals |
|-----------|-----------------|
| Category with 0–2 articles | Declared regime with no content — structural placeholder |
| Category with no subcategories in a deep domain | Missing sub‑regime differentiation |
| Category that exists in English but not in other languages | Culturally specific classification |
| "Wikipedia categories needing clarification" | Community‑acknowledged structural ambiguity |

### 8.3 — Regime Evolution Tracking

Category changes in an article's revision history reveal **regime reclassification events**:

```python
def find_category_changes(title, lang="en"):
    """Find revisions that changed an article's categories."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvlimit": "50",
        "rvprop": "ids|timestamp|comment|user",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    page = next(iter(resp["query"]["pages"].values()))

    cat_changes = []
    for rev in page.get("revisions", []):
        comment = rev.get("comment", "").lower()
        if any(kw in comment for kw in
               ["category", "cat", "recat", "recategoriz", "reclassif"]):
            cat_changes.append({
                "rev_id": rev["revid"],
                "timestamp": rev["timestamp"],
                "user": rev.get("user", "anonymous"),
                "comment": rev.get("comment", "")
            })

    return cat_changes
```

**RTT reading:** Every category change is a **regime reclassification event** —
the community has decided that this concept belongs to a different regime
neighborhood than before. Tracking these changes over time reveals the
concept's **regime migration history**.

---

## 9 — PetScan: Advanced Category Intersection Queries

PetScan (`https://petscan.wmcloud.org/`) is a powerful tool for querying
category intersections — finding articles that belong to **multiple
categories simultaneously**:

### 9.1 — Use Cases for Regime Analysis

| Query Type | PetScan Setup | RTT Application |
|-----------|---------------|-----------------|
| **Cross‑domain entities** | Category A AND Category B (different domains) | Find concepts at regime intersections |
| **Domain‑specific gaps** | Category A NOT Category B | Find articles missing an expected classification |
| **Temporal subsets** | Category A AND Category "YEAR in [domain]" | Regime population at a point in time |
| **Quality filtering** | Category A AND quality ≥ GA | Find validated regime declarations in a domain |
| **Language comparison** | Same categories in different wikis | Cross‑cultural regime coverage |

### 9.2 — Example: Finding Cross‑Domain Concepts

To find articles that are classified under **both** Physics and Philosophy:

1. Go to `https://petscan.wmcloud.org/`
2. Set Categories: `Physics` and `Philosophy`
3. Set Combination: `Intersection (AND)`
4. Set Depth: 3 (search 3 levels deep into subcategories)
5. Run query

**Result:** Articles like "Entropy," "Causality," "Determinism,"
"Quantum mechanics interpretations" — concepts that sit at the
Physics↔Philosophy regime boundary.

**RTT reading:** These intersection results are the **regime boundary
population** — the set of concepts that both domains claim. The size
and composition of this population reveals how structurally connected
the two domains are.

---

## 10 — Cross‑Reference to Other Module Files

| File | How Category Taxonomy Connects |
|------|-------------------------------|
| `Wikidata_Ingestion_Format.md` | Wikidata P31/P279 chain = parallel classification system; this file covers the Wikipedia side; that file covers the Wikidata side; Section 4 compares them directly |
| `Wikipedia_RTT_Structural_Mapping.md` | Categories are mapped in Section 2.1 as "regime hierarchy" at R2 level |
| `Cross_Domain_Meta_Operators.md` | Operator 5 (Category Taxonomy as Regime Hierarchy) is derived directly from this file |
| `Talk_Page_Coherence_Surface.md` | Classification Disputes (Pattern 5) are talk page debates about category membership — regime hierarchy disputes surface there |
| `Revision_History_Regime_Analysis.md` | Category changes appear in revision history as regime reclassification events — Section 8.3 of this file provides the detection code |
| `NPOV_As_Coherence_Operator.md` | Category assignment can be a NPOV issue — placing an article in a politically loaded category is itself a framing decision |
| All 15 domain directories | Every domain's `regime_alignment.md` traces the domain's category tree as part of its regime position analysis |

---

## 11 — Student Exercises

### Exercise 1 — Category Path Tracing (15 minutes)

1. Pick any Wikipedia article
2. Scroll to the bottom and find its categories
3. Click one category and trace it **upward** through parent categories until you reach "Main topic classifications" or "Contents"
4. Count the depth (number of levels)
5. Go back and try a **different** category for the same article — does it reach the root through a different domain?
6. Write one sentence: *"This article reaches the root via [path 1: N levels through Domain X] and [path 2: M levels through Domain Y]. It has a regime multiplicity of [number of top‑level categories]."*

### Exercise 2 — Cross‑Domain Intersection (20 minutes)

1. Go to PetScan (`https://petscan.wmcloud.org/`)
2. Pick two domains you find interesting (e.g., Biology and Economics, or Physics and Philosophy)
3. Run an intersection query with depth 2
4. Examine the results: what concepts sit at the boundary between these two domains?
5. Pick one result article and read its lead paragraph — does it acknowledge its cross‑domain nature?
6. Write two sentences: *"The intersection of [Domain A] and [Domain B] contains [N] articles. The most structurally interesting is [article] because [reason]."*

### Exercise 3 — Category Pathology Hunting (20 minutes)

1. Browse Wikipedia's category tree starting from `Category:Main topic classifications`
2. Look for one example of each pathology from Section 5:
   - An overcategorized article (15+ categories)
   - An undercategorized article (1–2 categories only)
   - An orphan category (hint: check `Category:Orphaned categories`)
   - An eponymous category (person‑as‑regime)
3. For each, write one sentence explaining what the pathology reveals about the concept's regime status

### Exercise 4 — Cross‑Language Category Comparison (30 minutes)

1. Pick a concept you expect to have cultural variance (try: Democracy, Tea, Football, or a religion)
2. Find the article in English + 2 other languages
3. For each language, list the categories at the bottom of the article
4. Compare: Are the categories structurally similar? Do different languages categorize the concept under different domains?
5. Answer: *"The most striking category difference is [X]. This reveals that [language A] frames the concept as part of [regime], while [language B] frames it as part of [different regime]."*

### Exercise 5 — Regime Reclassification Detection (30 minutes)

1. Pick an article for a concept that has been reclassified in real life (try: Pluto, a renamed country, a reclassified species, or a substance whose legal status changed)
2. Use the `find_category_changes` function from Section 8.3 (or manually search the revision history for "category" in edit summaries)
3. Identify when the category change happened and what categories were added/removed
4. Answer: *"The article was reclassified from [old categories] to [new categories] on [date]. This reflects the real‑world regime transition of [event]. The category change [preceded / followed / coincided with] the article text update by [N days]."*

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
