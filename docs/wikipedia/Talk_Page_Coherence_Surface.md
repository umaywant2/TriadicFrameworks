# Talk Page Coherence Surface

> **Purpose:** Define how to read Wikipedia talk pages as **coherence and drift
> surfaces** — the pre‑regime discourse layer where structural consensus is
> negotiated, challenged, and sometimes destroyed before it ever reaches
> the article itself.
>
> Talk pages are Wikipedia's **most underread structural asset**. Most readers
> never visit them. Most students don't know they exist. Yet talk pages are
> where the real regime work happens — where editors argue about what a concept
> IS, what scope the article should have, what sources count, and whose framing
> should prevail.
>
> No other major knowledge source exposes this layer publicly.

---

## 1 — What Is a Talk Page?

Every Wikipedia article has a paired **talk page** (also called a discussion page)
where editors discuss the article's content, structure, and quality.

### How to Access Talk Pages

| Method | URL Pattern |
|--------|------------|
| Web UI | `https://en.wikipedia.org/wiki/Talk:ARTICLE_TITLE` |
| From any article | Click the "Talk" tab at the top of any article |
| API | `https://en.wikipedia.org/w/api.php?action=parse&page=Talk:ARTICLE_TITLE&format=json` |
| Archives | `https://en.wikipedia.org/wiki/Talk:ARTICLE_TITLE/Archive_1` (and /Archive_2, /Archive_3, etc.) |

### Talk Page Anatomy

A typical talk page contains:

| Element | Purpose | RTT Mapping |
|---------|---------|-------------|
| Banner templates (WikiProject, quality ratings) | Article classification by stewardship groups | **Regime stewardship declaration** |
| Active discussion threads | Current structural debates | **Live coherence surface** |
| Resolved/archived threads | Historical structural debates | **Regime archaeology** |
| RfC (Request for Comment) notices | Formal dispute resolution | **Coherence arbitration** |
| Edit war notices / protection logs | Conflict markers | **Drift alerts** |
| To‑do lists | Structural gaps acknowledged by stewards | **Regime development roadmap** |
| FAQ sections | Pre‑answered recurring disputes | **Crystallized coherence positions** |

---

## 2 — Talk Pages as Coherence Surfaces

### 2.1 — The Coherence Model

In RTT, **coherence** is the degree to which a regime's internal claims
are structurally consistent. A Wikipedia article's coherence is not determined
by its text alone — it is determined by the **consensus process** visible
on its talk page.

```
Article text (R3) ← produced by → Talk page consensus (R0–R1)
                                         │
                     ┌───────────────────┼───────────────────┐
                     │                   │                   │
              Factual disputes     Framing disputes     Scope disputes
              (surface — R3)       (structural — R1)    (regime — R0)
                     │                   │                   │
              "This date is        "This article         "Should this
               wrong"              frames X as Y          concept even
                                   — it should            have an article?"
                                   frame it as Z"
```

### 2.2 — The Three Dispute Layers

Not all talk page disputes are equal. They operate at different regime levels:

| Dispute Layer | Regime Level | What's Contested | Coherence Impact | Example |
|--------------|-------------|------------------|-----------------|---------|
| **Factual** | R3 | Specific claims, dates, numbers, citations | Low — easily resolved with better sources | "The population figure is outdated — here's the 2024 census" |
| **Framing** | R1–R2 | How the article presents information, section structure, emphasis, tone | Medium — requires negotiation about perspective | "This article presents X primarily from a Western perspective — it needs global balance" |
| **Scope** | R0 | What the article should cover, whether it should exist, how it relates to other articles | High — fundamental regime negotiation | "This article should be merged with [other article]" or "This topic doesn't meet notability guidelines" |

**Key insight:** Most talk page threads are **factual disputes** (R3). These
are structurally shallow — they don't challenge the regime, just correct
its outputs. The rare **scope disputes** (R0) are where regimes are born,
merged, split, or killed. Learning to distinguish these layers is the core
skill this file teaches.

---

## 3 — Reading Talk Pages Structurally

### 3.1 — The Coherence Gradient

Every talk page can be scored on a **coherence gradient** based on the
nature and volume of its active disputes:

| Gradient Level | Indicator | What It Means |
|---------------|-----------|---------------|
| **High coherence** | Few active threads, mostly factual corrections, FAQ section exists | Regime is crystallized — community agrees on what the article IS |
| **Moderate coherence** | Active threads on framing or emphasis, periodic RfCs, steady but managed activity | Regime is stable but actively maintained — consensus requires ongoing negotiation |
| **Low coherence** | Multiple competing framing proposals, edit war notices, protection banners, unresolved RfCs | Regime is contested — no stable consensus on what the article should be |
| **Incoherent** | Talk page dominated by scope disputes, AfD notices, merge proposals, fundamental disagreements about the article's right to exist | Regime is in crisis — structural identity under challenge |

### 3.2 — Signal Extraction Checklist

When reading any talk page, extract these signals:

| # | Signal | Where to Find It | What It Reveals |
|---|--------|-------------------|-----------------|
| 1 | **WikiProject banners** | Top of talk page | Which stewardship groups claim this article — multiple WikiProjects = cross‑domain concept |
| 2 | **Quality rating** | WikiProject banner | Current regime maturity assessment (Stub/Start/C/B/GA/FA) |
| 3 | **Importance rating** | WikiProject banner | How central this concept is to its domain's regime |
| 4 | **Active thread count** | Scan the page | Current coherence workload — more threads = more active negotiation |
| 5 | **Thread age** | Check dates on threads | Old unresolved threads = chronic coherence failures |
| 6 | **Archive count** | Check for /Archive links | Total historical coherence volume — many archives = much past negotiation |
| 7 | **RfC notices** | Tagged threads | Formal coherence arbitration in progress |
| 8 | **Edit war banners** | Top of talk page | Active or recent regime conflicts |
| 9 | **Protection notices** | Top of talk page | Regime has been locked due to instability |
| 10 | **FAQ section** | Top of talk page or separate subpage | Recurring disputes that have been formally resolved — crystallized coherence positions |
| 11 | **To‑do list** | Talk page body | Acknowledged structural gaps — the regime's own development roadmap |
| 12 | **Mediation/ArbCom links** | Talk page threads | Disputes that escalated beyond community consensus — regime authority invoked |

---

## 4 — Discourse Patterns

### 4.1 — The Seven Canonical Talk Page Patterns

Through structural analysis of thousands of Wikipedia talk pages, seven
recurring discourse patterns emerge:

#### Pattern 1: Source War

**What it looks like:** Editors repeatedly add and remove citations,
arguing about which sources are "reliable" for a given claim.

**RTT reading:** This is a **regime provenance dispute** — editors disagree
about which external regimes are structurally valid for citation. The
dispute reveals the article's **source regime boundary** — the line between
accepted and rejected external authority.

**Coherence impact:** Medium. Usually resolved by appeal to Wikipedia's
Reliable Sources guidelines (WP:RS).

---

#### Pattern 2: Framing Contest

**What it looks like:** Editors argue about the article's lead paragraph,
section ordering, or emphasis. "This article gives undue weight to X" or
"The introduction frames this topic incorrectly."

**RTT reading:** This is a **regime declaration dispute** — editors agree
on the facts but disagree on how to **structurally present** them. The
lead paragraph is the article's regime summary, and competing framings
represent competing regime declarations.

**Coherence impact:** High. Framing contests can persist for years because
they involve structural perspective, not factual accuracy.

---

#### Pattern 3: Scope Creep Debate

**What it looks like:** Some editors want to expand the article's coverage;
others want to narrow it. "This article is trying to cover too much" vs.
"This important aspect is missing."

**RTT reading:** This is a **regime boundary negotiation** — the community
is actively deciding where this concept's regime ends and adjacent regimes
begin. Proposals to split an article into sub‑articles = regime differentiation.
Proposals to merge articles = regime consolidation.

**Coherence impact:** High. Scope decisions define the regime itself.

---

#### Pattern 4: Neutrality Challenge

**What it looks like:** An editor or group argues that the article violates
NPOV — it presents one viewpoint too favorably or suppresses legitimate
alternative viewpoints.

**RTT reading:** This is a **coherence operator violation** — the article's
structural invariant (NPOV) is being challenged. See `NPOV_As_Coherence_Operator.md`
for the full framework.

**Coherence impact:** Very high. NPOV challenges question the article's
fundamental structural integrity.

---

#### Pattern 5: Classification Dispute

**What it looks like:** Editors argue about how to categorize the article's
subject. "Is X a type of Y or a type of Z?" or "Should this be classified
as A or B?"

**RTT reading:** This is a **regime hierarchy dispute** — the concept's
position in the classification tree is contested. These disputes often
map directly to real‑world taxonomic or definitional controversies.
See `Category_Taxonomy_Regime_Hierarchy.md`.

**Coherence impact:** Medium to high. Classification determines which
regime neighborhood the article belongs to.

---

#### Pattern 6: Notability Challenge

**What it looks like:** An editor questions whether the article's subject
meets Wikipedia's notability requirements. May include AfD nominations.

**RTT reading:** This is a **regime existence challenge** — the most
fundamental coherence dispute possible. The community is deciding whether
this concept has sufficient structural standing to maintain a regime
declaration on Wikipedia.

**Coherence impact:** Maximum. This challenges the regime's right to exist.

---

#### Pattern 7: Consensus Crystallization

**What it looks like:** A long‑running dispute reaches resolution. Editors
agree on a final version. The resolved thread may be moved to an FAQ or
archive. The article stabilizes.

**RTT reading:** This is **coherence achieved** — the structural negotiation
has produced a stable consensus. The crystallized position becomes part of
the article's structural foundation. Future editors who raise the same
dispute are pointed to the archived resolution.

**Coherence impact:** Positive — coherence increases. The resolved dispute
becomes a structural precedent.

---

### 4.2 — Pattern Distribution by Domain

| Pattern | Sciences | Humanities | Applied | Most Common In |
|---------|----------|------------|---------|---------------|
| Source War | ●●● | ●● | ●● | Medicine, Psychology |
| Framing Contest | ●● | ●●● | ●● | History, Political Science, Philosophy |
| Scope Creep | ●● | ●● | ●●● | Computer Science, Engineering |
| Neutrality Challenge | ● | ●●● | ●● | Political Science, History, Economics |
| Classification Dispute | ●●● | ●● | ●● | Biology, Linguistics, Chemistry |
| Notability Challenge | ● | ●● | ●●● | Computer Science (tech companies, software) |
| Consensus Crystallization | ●●● | ●● | ●●● | Physics, Mathematics, Astronomy |

**Key:** ●●● = very common | ●● = common | ● = occasional

---

## 5 — Temporal Dynamics of Talk Pages

### 5.1 — Talk Page Lifecycle

Talk pages follow a lifecycle that mirrors the article's regime phases
(from `Revision_History_Regime_Analysis.md`):

| Article Phase | Talk Page Activity | Coherence State |
|--------------|-------------------|-----------------|
| **Birth** | Empty or single welcome message | No coherence surface yet |
| **Expansion** | First substantive threads appear — usually factual corrections | Coherence emerging |
| **Negotiation** | Multiple active threads, framing contests, possible RfCs | Coherence contested |
| **Crystallization** | Disputes resolving, FAQ forming, archives growing | Coherence stabilizing |
| **Maturity** | Low activity, mostly factual updates, FAQ handles recurring questions | Coherence crystallized |
| **Perturbation** | Sudden thread explosion, new editors arriving, old disputes reopened | Coherence disrupted |

### 5.2 — The Talk‑Article Lag

Talk page activity often **leads** article changes:

```
Talk page dispute begins → Discussion escalates → Consensus forms → Article updated
       t=0                     t+days/weeks         t+weeks/months     t+final
```

This lag means that **talk pages are a leading indicator** of regime change.
An article that looks stable today may have active talk page disputes that
will produce structural changes next month.

**Research application:** Monitor talk pages to **predict** article regime
transitions before they happen.

### 5.3 — Archive Depth as Coherence History

The number of talk page archives reveals the **total coherence workload**
the article has required:

| Archive Count | Interpretation |
|--------------|---------------|
| 0 | Low‑attention article — minimal coherence negotiation |
| 1–5 | Normal article lifecycle — moderate historical negotiation |
| 5–20 | High‑attention article — significant past disputes |
| 20–50 | Perpetually contested — the article is a coherence battleground |
| 50+ | Among the most contested articles on Wikipedia (e.g., Israel, United States, Jesus) |

---

## 6 — API Patterns for Talk Page Analysis

### 6.1 — Fetch Talk Page Content

```python
import requests

def get_talk_page(title, lang="en"):
    """Fetch the current talk page content for an article."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": f"Talk:{title}",
        "prop": "wikitext|sections",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    return resp.get("parse", {})
```

### 6.2 — Count Archives

```python
def count_archives(title, lang="en"):
    """Count the number of talk page archives for an article."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "allpages",
        "apprefix": f"Talk:{title}/Archive",
        "apnamespace": 0,
        "aplimit": "max",
        "format": "json"
    }
    # Note: archives are in Talk namespace (1), adjust query
    params["apnamespace"] = 1
    params["apprefix"] = f"{title}/Archive"

    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    pages = resp.get("query", {}).get("allpages", [])
    return len(pages)
```

### 6.3 — Extract Thread Structure

```python
import re

def extract_threads(wikitext):
    """Extract discussion thread headers and nesting depth from talk page wikitext."""
    threads = []
    for line in wikitext.split("\n"):
        # Thread headers use == Level 2 == format
        match = re.match(r'^(={2,})\s*(.+?)\s*\1\s*$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            threads.append({
                "level": level,
                "title": title,
                "depth": level - 2  # == is depth 0, === is depth 1
            })
    return threads
```

### 6.4 — Coherence Signal Extraction

```python
def extract_coherence_signals(wikitext):
    """Scan talk page wikitext for key coherence signal markers."""
    signals = {
        "rfc_notices": len(re.findall(r'\{\{rfc', wikitext, re.IGNORECASE)),
        "npov_mentions": len(re.findall(r'NPOV|neutral|bias|POV', wikitext, re.IGNORECASE)),
        "merge_proposals": len(re.findall(r'merge|split|consolidat', wikitext, re.IGNORECASE)),
        "notability_challenges": len(re.findall(r'notab|AfD|delet', wikitext, re.IGNORECASE)),
        "source_disputes": len(re.findall(r'reliable source|WP:RS|citation|source', wikitext, re.IGNORECASE)),
        "edit_war_mentions": len(re.findall(r'edit war|3RR|revert war|warring', wikitext, re.IGNORECASE)),
        "consensus_declarations": len(re.findall(r'consensus|agreed|resolved|closed', wikitext, re.IGNORECASE)),
        "wikiproject_banners": len(re.findall(r'\{\{WikiProject', wikitext, re.IGNORECASE)),
        "faq_present": bool(re.search(r'\{\{FAQ', wikitext, re.IGNORECASE)),
        "todo_present": bool(re.search(r'\{\{To do', wikitext, re.IGNORECASE))
    }
    return signals
```

### 6.5 — Classify Coherence Gradient

```python
def classify_coherence(signals, archive_count):
    """Classify talk page coherence level based on extracted signals."""
    stress_score = (
        signals["rfc_notices"] * 5 +
        signals["npov_mentions"] * 3 +
        signals["merge_proposals"] * 4 +
        signals["notability_challenges"] * 5 +
        signals["edit_war_mentions"] * 4 -
        signals["consensus_declarations"] * 2 -
        (5 if signals["faq_present"] else 0)
    )

    if stress_score < 5:
        return "high_coherence"
    elif stress_score < 15:
        return "moderate_coherence"
    elif stress_score < 30:
        return "low_coherence"
    else:
        return "incoherent"
```

---

## 7 — Worked Example: "Evolution"

The Wikipedia article on **Evolution** has one of the richest talk pages
in the encyclopedia — 60+ archives spanning 20+ years of coherence negotiation.

### The Core Dispute Layers

| Layer | What's Contested | Duration | Resolution |
|-------|-----------------|----------|------------|
| **Factual (R3)** | Specific evolutionary mechanisms, dates, examples | Ongoing, low intensity | Resolved through citation updates |
| **Framing (R1)** | How much weight to give "controversy" with creationism | Intense 2004–2012 | Consensus: evolution is the scientific consensus; creationism belongs in separate article |
| **Scope (R0)** | Whether the article should address the "evolution vs. creationism debate" at all | Periodic, high intensity | Crystallized position: the article covers the scientific theory; the sociopolitical debate has its own article |

### The FAQ as Crystallized Coherence

The Evolution talk page has a prominent **FAQ section** — a set of pre‑answered
questions that address the most common recurring disputes. This FAQ is
**crystallized coherence** — it represents formal consensus positions that
the community has explicitly decided:

- *"Why doesn't this article present creationism as an alternative?"* →
  Crystallized answer referencing NPOV, scientific consensus, and WP:UNDUE
- *"Why does the lead say evolution is a 'fact'?"* →
  Crystallized answer distinguishing between evolution as observed
  phenomenon and evolutionary theory as explanatory framework
- *"Why are specific criticisms of evolution not included?"* →
  Crystallized answer referencing WP:FRINGE and WP:WEIGHT

### RTT Reading

The Evolution talk page demonstrates:

1. **Coherence surfaces are layered** — factual, framing, and scope disputes
   coexist but operate at different regime levels
2. **FAQ sections are regime precedent** — crystallized coherence positions
   that reduce future dispute cost
3. **Archive depth correlates with regime significance** — 60+ archives
   means this concept sits at a major regime intersection (science vs. religion)
4. **Scope crystallization is the highest‑value coherence event** — once
   the community decided that the evolution article covers science and
   the creationism article covers the debate, the regime boundary was set

---

## 8 — Cross‑Reference to Other Module Files

| File | How Talk Pages Connect |
|------|----------------------|
| `Revision_History_Regime_Analysis.md` | Talk page disputes are a **leading indicator** of revision spikes — disputes surface on Talk before erupting in article edits |
| `Edit_War_Regime_Transition_Detection.md` | Edit wars are the **failure mode** of talk page consensus — when Talk cannot resolve a dispute, it manifests as edit warring in the article |
| `NPOV_As_Coherence_Operator.md` | NPOV disputes are the most structurally significant talk page pattern — Pattern 4 in this file maps directly to the NPOV file |
| `Featured_Article_Validation_Corridor.md` | FA reviewers examine talk page health as part of quality assessment — articles with chronic unresolved disputes rarely pass FA review |
| `Category_Taxonomy_Regime_Hierarchy.md` | Classification Disputes (Pattern 5) often play out on talk pages before manifesting as category changes |
| `Cross_Domain_Meta_Operators.md` | Operator 3 (Talk Page Coherence Gradient) is derived directly from Section 3 of this file |
| `Wikipedia_RTT_Structural_Mapping.md` | This file implements the editorial structures mapped in Section 2.2 of the master mapping |

---

## 9 — Advanced Patterns

### 9.1 — Cross‑Language Talk Page Comparison

The **same article's talk page** in different languages reveals cultural
coherence dynamics:

- **English Talk:Evolution** — 60+ archives dominated by science/religion framing disputes
- **German Diskussion:Evolution** — far fewer archives, minimal religion‑related disputes
- **Arabic نقاش:تطور** — different dispute landscape, different framing tensions

**Method:** Compare archive counts, FAQ content, and dominant discourse
patterns across 3+ language editions. Divergences reveal which **coherence
disputes are culturally universal** vs. **culturally specific**.

### 9.2 — WikiProject Banner Analysis

The WikiProject banners at the top of a talk page reveal which **stewardship
groups** claim the article:

| Banner Count | Interpretation |
|-------------|---------------|
| 1 | Single‑domain concept — clear regime ownership |
| 2–3 | Cross‑domain concept — shared stewardship |
| 4–6 | Highly cross‑domain — may create jurisdictional disputes |
| 7+ | Structural crossroads — the concept sits at the intersection of many regimes |

**Example:** The article "Water" has WikiProject banners for Chemistry,
Physics, Environment, Geology, and more — reflecting its position as a
cross‑domain structural node.

### 9.3 — Consensus Detection Heuristics

How to identify when a talk page thread has reached consensus:

| Indicator | Confidence |
|-----------|-----------|
| Thread marked `{{resolved}}` or `{{closed}}` | **High** — explicit community marker |
| No new replies for 30+ days after substantive discussion | **Moderate** — implied consensus through silence |
| Admin or experienced editor posts summary conclusion | **Moderate** — community authority signal |
| Thread moved to FAQ | **High** — promoted to crystallized position |
| Thread archived with no resolution marker | **Low** — may be abandoned rather than resolved |
| Thread has `{{stale}}` tag | **Low** — community acknowledged discussion died without resolution |

### 9.4 — Talk Page Health Score

A composite metric combining multiple signals:

```python
def talk_page_health(signals, archive_count, article_age_years):
    """
    Compute a talk page health score (0-100).
    Higher = more coherent, better maintained.
    """
    # Positive indicators
    faq_bonus = 15 if signals["faq_present"] else 0
    todo_bonus = 5 if signals["todo_present"] else 0
    consensus_score = min(signals["consensus_declarations"] * 3, 20)
    wikiproject_score = min(signals["wikiproject_banners"] * 5, 15)

    # Negative indicators
    conflict_penalty = min((
        signals["rfc_notices"] * 5 +
        signals["npov_mentions"] * 2 +
        signals["edit_war_mentions"] * 4 +
        signals["notability_challenges"] * 5
    ), 40)

    # Archive ratio (archives per year — moderate is healthy)
    archive_ratio = archive_count / max(article_age_years, 1)
    archive_score = 10 if 0.5 < archive_ratio < 3 else 5

    health = 50 + faq_bonus + todo_bonus + consensus_score + wikiproject_score + archive_score - conflict_penalty
    return max(0, min(100, health))
```

---

## 10 — Student Exercises

### Exercise 1 — Coherence Gradient Assessment (20 minutes)

1. Pick any Wikipedia article you've read before
2. Navigate to its talk page (click the "Talk" tab)
3. Apply the Signal Extraction Checklist from Section 3.2
4. Classify the talk page's coherence gradient (High / Moderate / Low / Incoherent)
5. Write one sentence: *"This article's coherence is [level] because [evidence]."*

### Exercise 2 — Discourse Pattern Identification (30 minutes)

1. Pick an article you expect to have an active talk page (try: a controversial topic, a current event, or a broad scientific concept)
2. Read the 3 most recent talk page threads
3. Classify each thread as one of the 7 Canonical Patterns from Section 4.1
4. For each, identify: What regime level is contested? (R0/R1/R2/R3)
5. Which pattern is most common on this talk page? What does that tell you about the article's regime?

### Exercise 3 — FAQ as Crystallized Coherence (20 minutes)

1. Find an article with a talk page FAQ (try: Evolution, Climate change, Homeopathy, or any article with `{{FAQ}}` on its talk page)
2. Read 3 FAQ entries
3. For each, identify: What was the original dispute? What regime level was it? How was it resolved?
4. Write one sentence: *"This FAQ entry crystallized the position that [X], resolving a [factual/framing/scope] dispute about [Y]."*

### Exercise 4 — Talk‑Article Lag Detection (45 minutes)

1. Pick an article that was recently updated (check the revision history for recent substantial edits)
2. Check the talk page for related discussion threads
3. Find the thread that preceded the article change
4. Measure the lag: how many days/weeks between the talk page discussion and the article update?
5. Answer: *"The talk page discussion began on [date]. The article was updated on [date]. The lag was [N days]. The discussion [did/did not] directly cause the change."*

### Exercise 5 — Cross‑Language Coherence Comparison (30 minutes)

1. Pick a concept with cultural sensitivity (try: Democracy, Colonialism, Marriage, or a historical conflict)
2. Check the talk page archive count in English + 2 other languages
3. Compare: Which language has the most archives? Which has active disputes? Are the disputes about the same issues?
4. Write two sentences: *"The [language] talk page focuses on [dispute type], while the [other language] talk page focuses on [different dispute type]. This reveals that [insight about cultural regime variance]."*

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
