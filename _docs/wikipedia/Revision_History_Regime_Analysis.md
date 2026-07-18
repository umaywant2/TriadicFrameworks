# Revision History Regime Analysis

> **Purpose:** Define how to read Wikipedia's revision history as **temporal
> regime data** — the structural evolution of knowledge over time. No other
> major knowledge source exposes this surface publicly. Every Wikipedia article
> carries a complete, timestamped, author‑attributed record of every structural
> change since its creation — often spanning 20+ years.
>
> This file teaches students, researchers, and AIs to extract regime stability
> signals, identify regime transitions, and build temporal regime profiles
> from raw revision data.

---

## 1 — What Is a Revision History?

Every Wikipedia article stores a **complete, immutable log** of every edit
ever made to it. Each revision record contains:

| Field | Content | RTT Mapping |
|-------|---------|-------------|
| Revision ID | Unique integer | Regime event identifier |
| Timestamp | UTC datetime | Regime event time coordinate |
| User | Editor username or IP | Regime agent |
| Size (bytes) | Article size after this edit | Regime mass at time t |
| Size delta (bytes) | Change from previous revision | Regime growth/contraction signal |
| Edit summary | Editor's description of the change | Micro‑regime annotation |
| Tags | System‑applied labels (reverted, mobile edit, visual edit, etc.) | Regime event classification |
| Parent revision | Previous revision ID | Temporal chain link |

### How to Access Revision History

| Method | URL Pattern | Best For |
|--------|------------|----------|
| Web UI | `https://en.wikipedia.org/w/index.php?title=ARTICLE&action=history` | Manual inspection |
| API (recent) | `https://en.wikipedia.org/w/api.php?action=query&titles=ARTICLE&prop=revisions&rvlimit=500&rvprop=ids|timestamp|user|size|comment|tags&format=json` | Programmatic access (up to 500 revisions per call) |
| API (full) | Same as above with `rvcontinue` pagination | Complete history extraction |
| XTools | `https://xtools.wmcloud.org/articleinfo/en.wikipedia.org/ARTICLE` | Pre‑computed statistics and visualizations |
| Quarry SQL | `https://quarry.wmcloud.org/` with `revision` table queries | Bulk analysis across many articles |

---

## 2 — The Five Regime Signals in Revision History

### Signal 1: Revision Count — Regime Activity Index

The **total number of revisions** is the simplest and most powerful regime signal.

| Revision Count | Regime Interpretation | Examples |
|---------------|----------------------|----------|
| < 100 | **Quiet regime** — low structural attention, possibly stable or neglected | Obscure mathematical theorems, minor geographic features |
| 100–1,000 | **Active regime** — regular maintenance, moderate community attention | Most science articles, mid‑sized cities |
| 1,000–10,000 | **Contested or high‑interest regime** — significant editorial attention | Major historical events, prominent public figures, scientific controversies |
| > 10,000 | **Perpetually contested regime** — the article is a structural battleground | United States, Jesus, Muhammad, Israel, Climate change, Donald Trump |

**Key insight:** Revision count does not measure **quality** — it measures
**structural attention**. A 50,000‑revision article is not 500× better than
a 100‑revision article. It is 500× more **structurally contested**.

---

### Signal 2: Revision Rate — Current Regime Stability

The **number of revisions per unit time** (day/week/month) reveals whether
the regime is currently stable, active, or in crisis.

| Rate Pattern | Regime Interpretation |
|-------------|---------------------|
| Flat near zero | **Crystallized regime** — consensus achieved, minimal maintenance |
| Low and steady | **Stable regime** — ongoing minor updates, no structural disputes |
| Periodic spikes | **Cyclically contested** — regime destabilizes around recurring events (elections, anniversaries, seasons) |
| Sudden spike from baseline | **Regime perturbation** — external event triggered structural attention (news event, scientific discovery, controversy) |
| Sustained high rate | **Regime in active negotiation** — no consensus, continuous structural competition |

#### How to Compute Revision Rate

```python
# Using the MediaWiki API
# Fetch revisions with timestamps, then compute rate

import requests
from collections import Counter
from datetime import datetime

url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "titles": "Climate_change",
    "prop": "revisions",
    "rvlimit": "500",
    "rvprop": "timestamp",
    "format": "json"
}

response = requests.get(url, params=params).json()
pages = response["query"]["pages"]
page = next(iter(pages.values()))

# Count revisions per month
months = Counter()
for rev in page["revisions"]:
    ts = datetime.fromisoformat(rev["timestamp"].replace("Z", "+00:00"))
    months[f"{ts.year}-{ts.month:02d}"] += 1

# Print monthly revision rate
for month in sorted(months):
    print(f"{month}: {months[month]} revisions")
```

---

### Signal 3: Size Delta Patterns — Regime Growth and Contraction

Each revision records the article's size in bytes. The **delta** (change)
between consecutive revisions reveals structural dynamics:

| Delta Pattern | Regime Interpretation |
|--------------|---------------------|
| Consistent positive deltas | **Regime expansion** — community adding knowledge, building scope |
| Large positive spike | **Major regime event** — significant new content added (new section, new data, major update) |
| Consistent negative deltas | **Regime pruning** — community removing content, tightening scope |
| Large negative spike | **Regime contraction event** — major content removal (vandalism revert, consensus deletion, split to sub‑article) |
| Oscillating deltas | **Regime instability** — content being added and removed repeatedly (possible edit war) |
| Flat (near‑zero deltas) | **Crystallized regime** — only minor formatting or typo fixes |

#### Size Delta as Regime Evolution Curve

When plotted over time, cumulative article size creates a **regime evolution
curve**:

```
Size (bytes)
    │
    │                          ╭───── Regime maturity plateau
    │                    ╭────╯
    │               ╭───╯
    │          ╭───╯        ← Rapid regime expansion
    │     ╭───╯
    │╭───╯
    │╯  ← Regime birth
    └────────────────────────────────→ Time

Typical "healthy" article: sigmoid growth curve
  - Regime birth → rapid expansion → gradual stabilization → plateau
```

**Deviations from this curve are structurally significant:**

- **Sudden drops** = content removal events (investigate: vandalism? consensus? article split?)
- **Late‑stage spikes** = regime perturbation (investigate: external event? new discovery?)
- **Sawtooth pattern** = edit war (investigate: talk page for competing claims)
- **No plateau** = regime never crystallized (investigate: ongoing structural disputes)

---

### Signal 4: Revert Rate — Regime Resistance

A **revert** is an edit that undoes a previous edit, restoring the article
to an earlier state. The revert rate measures how strongly the existing regime
**resists change**.

| Revert Rate | Regime Interpretation |
|------------|---------------------|
| < 5% | **Open regime** — community welcomes new contributions |
| 5–15% | **Guarded regime** — moderate quality control, some gatekeeping |
| 15–30% | **Defended regime** — strong editorial consensus, new contributions frequently challenged |
| > 30% | **Fortress regime** — heavily protected, approaching or under active edit restriction |

#### Revert Detection

Reverts can be identified by:

1. **Exact size match** — revision returns article to exact byte count of a prior revision
2. **Edit summary markers** — summaries containing "revert," "rv," "undo," "rollback"
3. **System tags** — `mw-revert`, `mw-undo`, `mw-rollback`, `mw-manual-revert`
4. **SHA‑1 match** — revision content hash matches a prior revision's hash (definitive)

```sparql
# Quarry SQL: Count reverts for an article
SELECT
  COUNT(*) AS total_revisions,
  SUM(CASE WHEN ct_tag_id IN (
    SELECT ctd_id FROM change_tag_def
    WHERE ctd_name IN ('mw-revert', 'mw-undo', 'mw-rollback')
  ) THEN 1 ELSE 0 END) AS reverts
FROM revision
JOIN change_tag ON ct_rev_id = rev_id
WHERE rev_page = (
  SELECT page_id FROM page
  WHERE page_title = 'ARTICLE_TITLE'
  AND page_namespace = 0
)
```

---

### Signal 5: Editor Distribution — Regime Stewardship Structure

Who edits an article reveals its **regime stewardship model**:

| Pattern | Regime Interpretation |
|---------|---------------------|
| Few editors, many edits each | **Stewardship regime** — small group maintains structural integrity (common for technical articles) |
| Many editors, few edits each | **Open regime** — broad community participation, low individual ownership |
| One dominant editor + many minor | **Gatekeeper regime** — single editor controls structural direction |
| Bot‑heavy edit history | **Automated maintenance regime** — structural upkeep is programmatic |
| IP‑heavy edit history | **Anonymous contribution regime** — lower accountability, higher vandalism risk |

#### Editor Distribution via XTools

The fastest way to see editor distribution is XTools:

```
https://xtools.wmcloud.org/articleinfo/en.wikipedia.org/ARTICLE_TITLE
```

XTools provides:
- Top editors by edit count
- Editor count over time
- Bot vs. human edit ratio
- IP vs. registered editor ratio
- Minor edit percentage

---

## 3 — Regime Phase Classification

Combining all 5 signals, any article can be classified into one of 6 **regime phases**:

| Phase | Rev Count | Rev Rate | Size Trend | Revert Rate | Editor Pattern | Description |
|-------|-----------|----------|------------|-------------|---------------|-------------|
| **Birth** | < 10 | N/A | Rapid growth | Low | 1–2 editors | Just created, initial regime declaration |
| **Expansion** | 10–500 | Rising | Steady growth | Low–moderate | Growing editor pool | Community building out the regime |
| **Negotiation** | 100–5,000 | Variable | Oscillating | Moderate–high | Diverse, competing editors | Structural disputes being resolved |
| **Crystallization** | 500+ | Declining | Plateau approaching | Declining | Core stewards emerging | Consensus forming, regime stabilizing |
| **Maturity** | 1,000+ | Low, stable | Plateau | Low | Stable stewardship | Regime crystallized, minor maintenance only |
| **Perturbation** | Any | Sudden spike | Sudden change | Spike | Influx of new editors | External event disrupted the stable regime |

### Phase Transitions

Articles move between phases. The most common transitions:

```
Birth → Expansion → Negotiation → Crystallization → Maturity
                         ↑                               │
                         └───── Perturbation ─────────────┘
                         (external event resets the cycle)
```

**Key insight:** Most Wikipedia articles that reach Maturity will experience
**periodic perturbation** — external events (news, discoveries, controversies)
that temporarily reset them to the Negotiation phase. The perturbation‑recovery
cycle is the **heartbeat of a living regime**.

---

## 4 — Worked Example: "Pluto"

The Wikipedia article on **Pluto** is a textbook case of regime perturbation:

### Pre‑2006: Stable Maturity

- Classified as the 9th planet since 1930
- Article in Maturity phase — low revision rate, stable stewardship
- Regime declaration: "Pluto is a planet"

### August 2006: Perturbation Event

- IAU reclassifies Pluto as a dwarf planet
- Revision rate spikes from ~5/month to ~500/month
- Article size oscillates wildly (competing edits)
- Revert rate exceeds 40%
- Dozens of new editors arrive

### 2006–2008: Negotiation Phase

- Talk page debates intensify on classification language
- Multiple RfCs on how to describe Pluto's status
- Gradual consensus: "Pluto is a dwarf planet in the Kuiper belt"
- Revert rate declines as competing editors exhaust or accept consensus

### 2008–2015: Re‑Crystallization

- Revision rate returns to baseline
- Core stewardship group re‑establishes
- New regime declaration stabilizes

### July 2015: Second Perturbation

- New Horizons flyby generates massive public interest
- Revision rate spikes again — but this time the perturbation is **additive** (new data), not **structural** (no reclassification dispute)
- Article expands significantly with new scientific data
- Returns to Maturity quickly — no regime conflict, just regime enrichment

### RTT Reading

Pluto's revision history demonstrates:

1. **Regime crystallization** can be disrupted by external authority (IAU decision)
2. **Perturbation type matters** — structural reclassification (2006) causes prolonged Negotiation; data addition (2015) causes brief Expansion
3. **Revert rate is the best regime stress indicator** — it spiked to 40%+ only during the classification dispute
4. **Editor distribution shifts during perturbation** — the stable stewardship group was temporarily overwhelmed by newcomers

---

## 5 — API Patterns for Regime Analysis

### 5.1 — Fetch Full Revision History

```python
import requests

def get_full_history(title, lang="en"):
    """Fetch complete revision history for a Wikipedia article."""
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvlimit": "max",
        "rvprop": "ids|timestamp|user|size|comment|tags",
        "format": "json"
    }

    revisions = []
    while True:
        resp = requests.get(url, params=params,
                            headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
        page = next(iter(resp["query"]["pages"].values()))
        revisions.extend(page.get("revisions", []))

        if "continue" in resp:
            params["rvcontinue"] = resp["continue"]["rvcontinue"]
        else:
            break

    return revisions
```

### 5.2 — Compute Regime Signals

```python
from datetime import datetime
from collections import Counter

def compute_regime_signals(revisions):
    """Extract the 5 regime signals from a revision list."""

    total = len(revisions)

    # Signal 1: Revision count
    print(f"Total revisions: {total}")

    # Signal 2: Monthly revision rate
    months = Counter()
    for rev in revisions:
        ts = datetime.fromisoformat(rev["timestamp"].replace("Z", "+00:00"))
        months[f"{ts.year}-{ts.month:02d}"] += 1

    # Signal 3: Size deltas
    sizes = [rev["size"] for rev in revisions]
    deltas = [sizes[i] - sizes[i+1] for i in range(len(sizes)-1)]

    # Signal 4: Revert rate
    revert_tags = {"mw-revert", "mw-undo", "mw-rollback", "mw-manual-revert"}
    reverts = sum(1 for rev in revisions
                  if any(tag in revert_tags for tag in rev.get("tags", [])))
    revert_rate = reverts / total if total > 0 else 0

    # Signal 5: Editor distribution
    editors = Counter(rev.get("user", "anonymous") for rev in revisions)
    unique_editors = len(editors)
    top_editor_pct = editors.most_common(1)[0][1] / total if total > 0 else 0

    return {
        "revision_count": total,
        "monthly_rates": dict(sorted(months.items())),
        "avg_delta": sum(deltas) / len(deltas) if deltas else 0,
        "max_positive_delta": max(deltas) if deltas else 0,
        "max_negative_delta": min(deltas) if deltas else 0,
        "revert_rate": round(revert_rate, 3),
        "unique_editors": unique_editors,
        "top_editor_share": round(top_editor_pct, 3)
    }
```

### 5.3 — Classify Regime Phase

```python
def classify_regime_phase(signals):
    """Classify an article into one of 6 regime phases."""

    rc = signals["revision_count"]
    rr = signals["revert_rate"]
    ed = signals["unique_editors"]
    delta = signals["avg_delta"]

    if rc < 10:
        return "Birth"
    elif rc < 500 and delta > 50:
        return "Expansion"
    elif rr > 0.15 or (rc > 100 and ed > 50 and delta < 0):
        return "Negotiation"
    elif rr < 0.05 and delta < 10 and rc > 1000:
        return "Maturity"
    elif rr < 0.10 and rc > 500:
        return "Crystallization"
    else:
        return "Perturbation"
```

---

## 6 — Cross‑Referencing With Other Module Files

| File | How Revision History Connects |
|------|------------------------------|
| `Talk_Page_Coherence_Surface.md` | Talk page activity often **precedes** revision spikes — disputes surface on talk before erupting in edit wars |
| `Edit_War_Regime_Transition_Detection.md` | Edit wars are a **subset** of revision history — this file provides the broader context; that file zooms into the conflict mechanics |
| `NPOV_As_Coherence_Operator.md` | NPOV disputes are visible in edit summaries containing "POV," "bias," "neutral" — searchable in revision data |
| `Featured_Article_Validation_Corridor.md` | FA reviews examine revision history as part of quality assessment — articles with unstable histories rarely pass |
| `Wikidata_Ingestion_Format.md` | Wikidata items have their own revision history — combine both for complete temporal coverage of a concept |
| `Category_Taxonomy_Regime_Hierarchy.md` | Category changes appear in revision history — articles moving between categories = regime reclassification events |
| `Cross_Domain_Meta_Operators.md` | Operator 2 (Revision Frequency as Stability Signal) is derived directly from this file's Signal 2 |
| `Wikipedia_RTT_Structural_Mapping.md` | This file implements the temporal structures mapped in Section 2.6 of the master mapping |

---

## 7 — Advanced Patterns

### 7.1 — Revision History Comparison Across Languages

The **same concept** may have radically different revision histories in
different language Wikipedias:

| Concept | English Rev Count | Japanese Rev Count | Arabic Rev Count | Structural Insight |
|---------|------------------|--------------------|-----------------|-------------------|
| World War II | 40,000+ | 8,000+ | 3,000+ | Universal high attention; English most contested |
| Cricket | 15,000+ | 200 | 500 | Culturally specific regime — high attention only in English/Commonwealth |
| Ramadan | 4,000 | 300 | 12,000+ | Cultural regime variance — Arabic Wikipedia treats it as highest importance |

**Method:** Fetch revision counts for the same Wikidata Q‑number across
multiple language editions. Divergences reveal **cultural regime weighting** —
which cultures invest the most structural attention in which concepts.

### 7.2 — Bot vs. Human Revision Ratio

Many Wikipedia articles have 30–60% bot edits (link fixes, formatting,
category maintenance). The **human‑only revision rate** is a more accurate
regime signal than the raw rate:

```python
def human_revision_rate(revisions):
    """Filter out bot edits for cleaner regime signal."""
    human_revs = [r for r in revisions
                  if not r.get("user", "").endswith("Bot")
                  and "bot" not in r.get("tags", [])]
    return len(human_revs), len(human_revs) / len(revisions)
```

### 7.3 — Regime Perturbation Detection Algorithm

```python
def detect_perturbations(monthly_rates, threshold=3.0):
    """Detect months where revision rate exceeds N standard deviations
    above the mean — these are regime perturbation events."""
    import statistics

    values = list(monthly_rates.values())
    if len(values) < 6:
        return []

    mean = statistics.mean(values)
    stdev = statistics.stdev(values)

    if stdev == 0:
        return []

    perturbations = []
    for month, count in monthly_rates.items():
        z_score = (count - mean) / stdev
        if z_score > threshold:
            perturbations.append({
                "month": month,
                "revisions": count,
                "z_score": round(z_score, 2),
                "interpretation": "regime_perturbation"
            })

    return perturbations
```

---

## 8 — Student Exercises

### Exercise 1 — Regime Phase Classification (20 minutes)

1. Pick any Wikipedia article
2. Open its XTools page: `https://xtools.wmcloud.org/articleinfo/en.wikipedia.org/ARTICLE`
3. Record: total revisions, monthly average, revert rate, unique editors, current size
4. Classify it into one of the 6 regime phases from Section 3
5. Does the classification feel right? If not, what additional signal would help?

### Exercise 2 — Perturbation Hunting (30 minutes)

1. Pick an article you expect to have perturbation events (try: a country that had a recent revolution, a scientific theory that was recently challenged, a public figure involved in a recent controversy)
2. Open the revision history and look for **spike months**
3. For each spike, identify: what external event caused it? How long did the perturbation last? Did the article return to its previous regime, or did it crystallize into a new one?
4. Write a 3‑sentence summary: *"The article entered perturbation in [month] due to [event]. The perturbation lasted [duration]. The article [returned to previous regime / crystallized into new regime] because [reason]."*

### Exercise 3 — Cross‑Language Comparison (30 minutes)

1. Pick a concept with strong cultural variance (try: Democracy, Marriage, Colonialism, or a historical conflict)
2. Find the article in English + 2 other language editions
3. For each, record: revision count, article size, revert rate (use XTools with the appropriate language prefix)
4. Answer: *"Which language edition has the most structural attention? Which has the highest revert rate? What does this tell us about how different cultures negotiate this concept's regime?"*

### Exercise 4 — Build a Regime Evolution Curve (45 minutes)

1. Pick an article with 1,000+ revisions
2. Use the API pattern from Section 5.1 to fetch the full revision history
3. Plot article size over time (x = date, y = bytes)
4. Annotate: mark Birth, Expansion, Negotiation, Crystallization, and any Perturbation events
5. Compare your curve to the idealized sigmoid from Section 2 — where does it match? Where does it deviate?

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
