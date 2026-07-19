# Edit War Regime Transition Detection

> **Purpose:** Reframe Wikipedia edit wars from disruptive incidents into what
> they structurally are — **diagnostic instruments for regime boundary mapping**.
> An edit war is not noise. It is a signal. It marks the precise location where
> two or more competing regime claims collide and cannot be reconciled through
> normal consensus mechanisms.
>
> No other knowledge source makes regime collisions visible in real time.
> Academic journals suppress reviewer disagreements. Encyclopedias resolve
> disputes internally. Only Wikipedia exposes the raw collision data — every
> revert, every counter‑revert, every edit summary declaring a structural
> position — in a publicly archived, timestamped, author‑attributed log.
>
> This file teaches students to read edit wars as **regime transition events**
> and extract structural intelligence from them.

---

## 1 — What Is an Edit War?

### 1.1 — Wikipedia's Definition

An edit war occurs when editors repeatedly override each other's contributions
to an article, rather than resolving disagreements through discussion on the
talk page. Wikipedia's **Three‑Revert Rule (3RR)** states:

> *"An editor must not perform more than three reverts on a single page —
> in whole or in part — within a 24‑hour period."*

Violating 3RR can result in a block. But the rule addresses the **symptom**,
not the cause. The cause is always a **regime collision**.

### 1.2 — The RTT Translation

| Wikipedia Term | RTT Concept | Structural Function |
|---------------|-------------|---------------------|
| Edit war | **Regime transition event** | Two or more regime claims competing for the same structural space |
| Revert | **Regime reassertion** | An editor restoring their regime's declaration over a competitor's |
| Counter‑revert | **Counter‑regime reassertion** | The competing editor restoring their regime's declaration back |
| Edit war cycle | **Regime oscillation** | The article's structural state alternating between competing declarations |
| Protection (page lock) | **Regime freeze** | Administrative intervention to halt oscillation and force talk page resolution |
| Post‑war consensus | **Regime transition completion** | One regime claim prevails, a compromise is reached, or a new synthesis emerges |

### 1.3 — Why Edit Wars Are Diagnostic

An edit war answers three structural questions simultaneously:

1. **Where is the regime boundary?** — The specific text being reverted marks the exact location of the structural dispute
2. **What are the competing claims?** — Each editor's version represents a distinct regime declaration
3. **How strong is each claim?** — The persistence of each editor (number of reverts, argument quality, source citations) reveals the structural standing of each competing regime

---

## 2 — The Five Types of Edit Wars

### Type 1: Factual Dispute War

**What it looks like:** Editors repeatedly change a specific fact — a date,
a number, a name, a classification.

**Underlying regime collision:** Two external sources disagree, and editors
are proxying that disagreement into the article.

**Example:** Editors warring over whether a mountain's height is 8,848m or
8,849m based on different survey sources.

**Severity:** Low. Usually resolved by identifying the most authoritative
source.

**RTT reading:** This is a **regime measurement dispute** — competing
claims about the same measurable dimension. The resolution identifies
which measurement regime has primary standing.

---

### Type 2: Classification War

**What it looks like:** Editors repeatedly change how a concept is classified
or categorized — "X is a type of Y" vs. "X is a type of Z."

**Underlying regime collision:** The concept sits at a regime boundary where
two classification systems disagree.

**Example:** Pluto — "planet" vs. "dwarf planet." Tomato — "fruit" vs.
"vegetable." Taiwan — "country" vs. "province."

**Severity:** Moderate to high. Classification wars often map to real‑world
institutional or political disputes.

**RTT reading:** This is a **regime hierarchy dispute** — competing claims
about where a concept belongs in the classification tree. The resolution
determines which regime hierarchy the article adopts as primary.
See `Category_Taxonomy_Regime_Hierarchy.md`.

---

### Type 3: Framing War

**What it looks like:** Editors repeatedly rewrite the same passage to present
information from different perspectives. The facts may not change — only the
**framing** changes.

**Underlying regime collision:** Two worldviews produce structurally different
regime declarations from the same set of facts.

**Example:** A military conflict described as "liberation" by one side and
"invasion" by the other. A political figure described as "controversial" vs.
"influential."

**Severity:** High. Framing wars are the most persistent because they involve
structural perspective, not factual accuracy.

**RTT reading:** This is a **regime declaration dispute** — competing
structural presentations of the same underlying data. The resolution
determines the article's primary R1 framing.
See `NPOV_As_Coherence_Operator.md`.

---

### Type 4: Inclusion/Exclusion War

**What it looks like:** One editor adds content, another removes it. The
dispute is about whether specific information **belongs** in the article.

**Underlying regime collision:** Competing claims about the article's
scope — what the regime should and should not cover.

**Example:** Should a biography mention a person's criminal record?
Should a scientific article mention fringe objections? Should a country
article mention territorial disputes?

**Severity:** High. These wars define the regime's boundaries — what is
structurally in and what is out.

**RTT reading:** This is a **regime scope dispute** — competing claims
about the regime's boundary conditions. The resolution determines the
article's R0 scope declaration.

---

### Type 5: Naming/Terminology War

**What it looks like:** Editors repeatedly change how a concept is
named or what terminology is used to describe it.

**Underlying regime collision:** Names carry regime claims. Choosing one
name over another is choosing one regime's framing over another's.

**Example:** "Gdańsk" vs. "Danzig." "Persian Gulf" vs. "Arabian Gulf."
"Myanmar" vs. "Burma." "Kyiv" vs. "Kiev." "Côte d'Ivoire" vs. "Ivory Coast."

**Severity:** Very high. Naming wars can persist for **years** because
the name itself is a structural declaration — it declares which political,
cultural, or historical regime has naming authority.

**RTT reading:** This is a **regime identity dispute** — competing claims
about the concept's structural name. The resolution determines which
regime's naming convention the article adopts as primary.

---

## 3 — Edit War Severity Scale

| Level | Label | Reverts / 24h | Duration | Protection | RTT Interpretation |
|-------|-------|--------------|----------|------------|-------------------|
| 1 | **Skirmish** | 2–3 | Hours | None | Minor regime friction — editors may self‑resolve |
| 2 | **Dispute** | 3–6 | Days | Semi‑protection possible | Moderate regime collision — talk page engagement needed |
| 3 | **War** | 6–12 | Weeks | Semi or full protection | Serious regime collision — admin intervention likely |
| 4 | **Entrenchment** | 12+ (sustained) | Months | Extended or full protection | Deep regime collision — formal dispute resolution required |
| 5 | **Perpetual conflict** | Recurring cycles | Years | Persistent protection + discretionary sanctions | Irreconcilable regime collision — structural boundary is permanently contested |

### Severity Distribution by Domain

| Domain | Typical Max Severity | Most Common War Type | Rationale |
|--------|---------------------|---------------------|-----------|
| Physics | 1–2 | Factual, Classification | Strong consensus; disputes are narrow and technical |
| Mathematics | 1 | Factual | Near‑universal formal agreement |
| Biology | 2–3 | Classification, Inclusion | Taxonomy disputes; evolution vs. creationism |
| Chemistry | 1–2 | Factual, Naming | Nomenclature disputes (IUPAC vs. common names) |
| Computer Science | 2–3 | Inclusion, Framing | Technology hype cycles; company/product neutrality |
| Philosophy | 3–4 | Framing, Inclusion | Inherently perspectival; competing schools |
| Earth Sciences | 2–3 | Factual, Framing | Climate change political framing |
| Economics | 3–4 | Framing, Inclusion | Competing schools (Keynesian vs. Austrian vs. MMT) |
| History | 4–5 | Framing, Naming | National narratives; territorial disputes; naming wars |
| Medicine | 2–4 | Inclusion, Framing | Alternative medicine; treatment controversies |
| Engineering | 1–2 | Factual, Classification | Technical consensus; minor standards disputes |
| Astronomy | 1–2 | Classification | Object classification (e.g., planet vs. dwarf planet) |
| Linguistics | 2–3 | Classification, Naming | Language vs. dialect; script disputes |
| Psychology | 2–3 | Framing, Inclusion | Nature vs. nurture; disorder classification |
| Political Science | 4–5 | Framing, Naming, Inclusion | Nearly all topics are politically contested |

---

## 4 — The Four Resolution Patterns

Every edit war ends. How it ends reveals the **regime transition outcome**:

### Pattern 1: One Regime Prevails

**What happens:** One side's version is accepted as the article's
declaration. The other side's version is removed or marginalized.

**How it's achieved:** Stronger sourcing, broader editor consensus,
admin intervention favoring one side, or one side disengaging.

**RTT reading:** **Regime displacement** — one regime claim wins
structural standing and the other loses it. The article's regime
declaration shifts to the prevailing claim.

**Example:** The Pluto article eventually adopted "dwarf planet"
after the IAU decision. The "planet" claim lost structural standing.

---

### Pattern 2: Compromise Synthesis

**What happens:** A new version is crafted that incorporates elements
of both competing claims. Neither side gets exactly what they wanted,
but both can accept the result.

**How it's achieved:** Talk page negotiation, RfC, mediation, or
a skilled editor proposing a synthesis.

**RTT reading:** **Regime synthesis** — a new regime declaration emerges
that structurally integrates the competing claims. This is a genuine
regime transition — the article's structural state is different from
either competing version.

**Example:** Articles on contested territories often use compromise
formulations: "X is a disputed territory claimed by both A and B."

---

### Pattern 3: Structural Separation

**What happens:** The disputed content is moved to its own article or
section, giving each perspective its own structural space.

**How it's achieved:** Article splitting, creation of sub‑articles,
or "main article" links to separate detailed treatments.

**RTT reading:** **Regime differentiation** — the competing claims are
separated into distinct regime declarations rather than forced into
the same space. The original article retains a neutral summary; the
detailed perspectives get their own articles.

**Example:** "Evolution" and "Objections to evolution" are structurally
separated — each concept gets its own regime declaration.

---

### Pattern 4: Administrative Freeze

**What happens:** An admin locks the article to prevent further editing.
The version at time of protection becomes the de facto declaration,
regardless of which side it favors.

**How it's achieved:** Page protection (semi, extended, or full).
May include discretionary sanctions for the topic area.

**RTT reading:** **Regime stabilization by force** — the regime
oscillation is halted by external authority rather than consensus.
The frozen version is not necessarily the "correct" declaration — it
is the one that happened to be in place when the lock was applied.

**Example:** Heavily contested articles like "Israel" or "Kashmir"
spend long periods under full protection — the locked version is a
pragmatic stabilization, not a consensus outcome.

---

## 5 — Detection Algorithms

### 5.1 — Basic Revert Detection

```python
import requests
from datetime import datetime, timedelta

def detect_revert_sequences(title, lang="en", window_hours=24, min_reverts=3):
    """
    Detect revert sequences in a Wikipedia article's recent history.
    A revert is identified by system tags or edit summary keywords.
    """
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvlimit": "500",
        "rvprop": "ids|timestamp|user|size|comment|tags|sha1",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    page = next(iter(resp["query"]["pages"].values()))
    revisions = page.get("revisions", [])

    # Identify reverts
    revert_tags = {"mw-revert", "mw-undo", "mw-rollback", "mw-manual-revert"}
    revert_keywords = {"revert", "rv ", "rvv", "undo", "rollback",
                       "restored", "reverted"}

    reverts = []
    for rev in revisions:
        tags = set(rev.get("tags", []))
        comment = rev.get("comment", "").lower()

        is_revert = (
            bool(tags & revert_tags) or
            any(kw in comment for kw in revert_keywords)
        )

        if is_revert:
            reverts.append({
                "rev_id": rev["revid"],
                "timestamp": rev["timestamp"],
                "user": rev.get("user", "anonymous"),
                "comment": rev.get("comment", ""),
                "tags": list(tags & revert_tags),
                "sha1": rev.get("sha1", "")
            })

    # Detect clusters (multiple reverts within window)
    clusters = []
    current_cluster = []

    for i, rev in enumerate(reverts):
        ts = datetime.fromisoformat(rev["timestamp"].replace("Z", "+00:00"))

        if not current_cluster:
            current_cluster.append(rev)
        else:
            prev_ts = datetime.fromisoformat(
                current_cluster[-1]["timestamp"].replace("Z", "+00:00"))
            if (prev_ts - ts).total_seconds() <= window_hours * 3600:
                current_cluster.append(rev)
            else:
                if len(current_cluster) >= min_reverts:
                    clusters.append(current_cluster)
                current_cluster = [rev]

    if len(current_cluster) >= min_reverts:
        clusters.append(current_cluster)

    return {
        "article": title,
        "total_reverts": len(reverts),
        "revert_clusters": len(clusters),
        "clusters": [{
            "size": len(c),
            "start": c[-1]["timestamp"],
            "end": c[0]["timestamp"],
            "editors": list(set(r["user"] for r in c)),
            "reverts": c
        } for c in clusters]
    }
```

### 5.2 — SHA‑1 Based War Detection

The most reliable revert detection uses **content hashing** — if two
non‑adjacent revisions have the same SHA‑1 hash, the article was
restored to an earlier exact state:

```python
def detect_sha1_wars(title, lang="en"):
    """
    Detect edit wars using SHA-1 content hash matching.
    If the same hash appears multiple times, the article was
    reverted to an identical state — a definitive war signal.
    """
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "revisions",
        "rvlimit": "500",
        "rvprop": "ids|timestamp|user|sha1",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    page = next(iter(resp["query"]["pages"].values()))
    revisions = page.get("revisions", [])

    # Group revisions by SHA-1 hash
    from collections import defaultdict
    hash_groups = defaultdict(list)
    for rev in revisions:
        sha1 = rev.get("sha1", "")
        if sha1:
            hash_groups[sha1].append(rev)

    # Find repeated states (same content appearing 2+ times)
    war_signals = []
    for sha1, revs in hash_groups.items():
        if len(revs) >= 2:
            editors = list(set(r.get("user", "anon") for r in revs))
            war_signals.append({
                "sha1": sha1,
                "occurrences": len(revs),
                "timestamps": [r["timestamp"] for r in revs],
                "editors_restoring": editors,
                "interpretation": "article_restored_to_identical_state"
            })

    return {
        "article": title,
        "repeated_states": len(war_signals),
        "severity": classify_war_severity(war_signals),
        "signals": sorted(war_signals,
                         key=lambda x: x["occurrences"],
                         reverse=True)
    }

def classify_war_severity(signals):
    """Classify edit war severity from SHA-1 analysis."""
    if not signals:
        return "0_no_war"
    max_repeats = max(s["occurrences"] for s in signals)
    total_repeats = sum(s["occurrences"] for s in signals)

    if total_repeats <= 3:
        return "1_skirmish"
    elif total_repeats <= 8:
        return "2_dispute"
    elif total_repeats <= 15:
        return "3_war"
    elif max_repeats >= 5:
        return "4_entrenchment"
    else:
        return "3_war"
```

### 5.3 — War Participant Analysis

```python
def analyze_war_participants(cluster):
    """
    Analyze the participants in an edit war cluster.
    Returns faction structure and relative persistence.
    """
    from collections import Counter

    editor_reverts = Counter(r["user"] for r in cluster["reverts"])
    editors = list(editor_reverts.keys())
    total = sum(editor_reverts.values())

    factions = []
    for editor, count in editor_reverts.most_common():
        factions.append({
            "editor": editor,
            "revert_count": count,
            "persistence": round(count / total, 3),
            "sample_comment": next(
                (r["comment"] for r in cluster["reverts"]
                 if r["user"] == editor and r["comment"]),
                "no comment"
            )
        })

    return {
        "total_participants": len(editors),
        "total_reverts": total,
        "faction_count": len(set(
            r.get("sha1", "") for r in cluster["reverts"])),
        "factions": factions,
        "structure": (
            "bilateral" if len(editors) == 2 else
            "multilateral" if len(editors) <= 5 else
            "mass_conflict"
        )
    }
```

### 5.4 — Regime Boundary Extraction

```python
import difflib

def extract_disputed_content(rev_id_a, rev_id_b, lang="en"):
    """
    Compare two revision IDs to identify the exact disputed content.
    The diff reveals the regime boundary — the specific text where
    competing claims collide.
    """
    url = f"https://{lang}.wikipedia.org/w/api.php"

    def get_content(rev_id):
        params = {
            "action": "query",
            "revids": str(rev_id),
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
            "format": "json"
        }
        resp = requests.get(url, params=params,
                            headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
        page = next(iter(resp["query"]["pages"].values()))
        return page["revisions"][0]["slots"]["main"]["*"]

    content_a = get_content(rev_id_a).splitlines()
    content_b = get_content(rev_id_b).splitlines()

    diff = list(difflib.unified_diff(content_a, content_b,
                                      lineterm="", n=3))

    # Extract only changed lines
    additions = [l[1:] for l in diff if l.startswith("+")
                 and not l.startswith("+++")]
    removals = [l[1:] for l in diff if l.startswith("-")
                and not l.startswith("---")]

    return {
        "revision_a": rev_id_a,
        "revision_b": rev_id_b,
        "lines_added": len(additions),
        "lines_removed": len(removals),
        "regime_claim_a": "\n".join(removals[:10]),
        "regime_claim_b": "\n".join(additions[:10]),
        "boundary_location": "see diff output for exact position",
        "full_diff_lines": len(diff)
    }
```

### 5.5 — Historical War Pattern Analysis

```python
def historical_war_profile(title, lang="en"):
    """
    Build a complete edit war profile for an article's full history.
    Combines revert detection, SHA-1 analysis, and temporal clustering.
    """
    revert_data = detect_revert_sequences(title, lang,
                                           window_hours=72,
                                           min_reverts=2)
    sha1_data = detect_sha1_wars(title, lang)

    # Check protection history
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "prop": "info",
        "inprop": "protection",
        "format": "json"
    }
    resp = requests.get(url, params=params,
                        headers={"User-Agent": "TriadicFrameworks/1.0"}).json()
    page = next(iter(resp["query"]["pages"].values()))
    protections = page.get("protection", [])

    return {
        "article": title,
        "revert_clusters": revert_data["revert_clusters"],
        "sha1_repeated_states": sha1_data["repeated_states"],
        "war_severity": sha1_data["severity"],
        "current_protection": protections,
        "is_protected": len(protections) > 0,
        "war_history": {
            "clusters": revert_data["clusters"][:5],
            "sha1_signals": sha1_data["signals"][:5]
        },
        "regime_transition_assessment": assess_transition(
            revert_data, sha1_data, protections)
    }

def assess_transition(revert_data, sha1_data, protections):
    """Assess whether the article has undergone a regime transition."""
    severity = sha1_data["severity"]
    protected = len(protections) > 0
    clusters = revert_data["revert_clusters"]

    if severity == "0_no_war":
        return "stable_regime — no transition detected"
    elif severity == "1_skirmish" and not protected:
        return "minor_friction — regime boundary tested but held"
    elif severity in ("2_dispute", "3_war") and not protected:
        return "regime_negotiation — boundary actively contested"
    elif protected and clusters >= 2:
        return "regime_transition_in_progress — admin intervention required"
    elif severity in ("4_entrenchment",) or clusters >= 5:
        return "chronic_regime_conflict — boundary permanently contested"
    else:
        return "indeterminate — insufficient data"
```

---

## 6 — Worked Examples

### 6.1 — Pluto (Classification War → Regime Displacement)

| Dimension | Detail |
|-----------|--------|
| **War type** | Classification (Type 2) |
| **Period** | August 2006 – March 2007 |
| **Trigger** | IAU reclassifies Pluto as dwarf planet on 24 August 2006 |
| **Competing claims** | Claim A: "Pluto is the ninth planet" — Claim B: "Pluto is a dwarf planet" |
| **Peak severity** | Level 4 (Entrenchment) — sustained revert cycles, semi‑protection applied |
| **Resolution pattern** | **Regime displacement** — "dwarf planet" prevailed as the IAU declaration gained structural standing |
| **Duration** | ~7 months of active conflict, then gradual stabilization |
| **Post‑war state** | Crystallized — article now stably declares "Pluto is a dwarf planet in the Kuiper belt" |

**RTT reading:** Pluto is a textbook **externally triggered regime transition**.
The IAU decision changed the concept's regime classification, and the Wikipedia
article's edit war is the **visible trace** of that transition playing out in
the knowledge system. The war ended when the new classification gained
sufficient structural standing to displace the old one.

**Structural insight:** The speed of resolution correlated with the clarity
of the external authority's decision. The IAU ruling was unambiguous, so the
edit war, while intense, resolved relatively quickly. Compare this to
naming wars (Type 5) where no single external authority exists — those
can persist for decades.

---

### 6.2 — Gdańsk/Danzig (Naming War → Compromise Synthesis)

| Dimension | Detail |
|-----------|--------|
| **War type** | Naming/Terminology (Type 5) |
| **Period** | 2003–2005 (peak), with recurring flare‑ups through 2015+ |
| **Trigger** | Disagreement over whether to use "Gdańsk" (Polish) or "Danzig" (German) for historical references |
| **Competing claims** | Claim A: "Always use Gdańsk — it's the current name" — Claim B: "Use Danzig for historical periods when the city was German‑speaking" |
| **Peak severity** | Level 5 (Perpetual conflict) — one of Wikipedia's most‑cited edit wars |
| **Resolution pattern** | **Compromise synthesis** — complex naming conventions established through multiple RfCs |
| **Duration** | 2+ years of intense conflict; ongoing maintenance |
| **Post‑war state** | Semi‑crystallized — naming conventions exist but are periodically challenged |

**RTT reading:** Gdańsk/Danzig is a **regime identity dispute** where naming
carries deep political and historical regime claims. The compromise synthesis
demonstrates that some regime collisions cannot be resolved by one side
prevailing — they require **structural architecture** (naming conventions,
context‑dependent usage rules) to manage the permanent boundary.

**Structural insight:** The article now has an elaborate talk page FAQ and
naming convention section — these are **crystallized coherence positions**
produced by the war. The war itself was costly, but it produced structural
infrastructure that manages the ongoing regime tension.

---

### 6.3 — Abortion (Framing War → Administrative Freeze)

| Dimension | Detail |
|-----------|--------|
| **War type** | Framing (Type 3) + Inclusion/Exclusion (Type 4) |
| **Period** | Ongoing since early 2000s, with periodic escalations |
| **Trigger** | Fundamental worldview conflict between pro‑choice and pro‑life perspectives |
| **Competing claims** | Framing: "medical procedure" vs. "termination of human life" — Inclusion: which perspectives, statistics, and arguments to include |
| **Peak severity** | Level 5 (Perpetual conflict) — under discretionary sanctions |
| **Resolution pattern** | **Administrative freeze** — article under persistent protection + ArbCom discretionary sanctions |
| **Duration** | 20+ years of recurring conflict |
| **Post‑war state** | Managed instability — the article is functional but permanently contested |

**RTT reading:** Abortion represents an **irreconcilable regime collision** —
the competing claims arise from fundamentally different worldview regimes
that cannot be structurally synthesized. NPOV cannot produce a version
that both camps consider neutral because they disagree on what neutrality
means for this topic. The administrative freeze is **regime stabilization
by force** — not consensus, but pragmatic management.

**Structural insight:** The abortion article demonstrates the **limits of
NPOV as a coherence operator**. For most topics, NPOV can produce a
stable structural frame that accommodates competing views. For
irreconcilable worldview conflicts, NPOV can only manage the tension —
it cannot resolve it. The edit war history is the visible trace of that
permanent structural stress.

---

## 7 — Edit Wars Across Languages

### 7.1 — The Same Concept, Different Wars

The same topic can produce **different edit wars** on different language
Wikipedias, because the editor population brings different regime perspectives:

| Topic | English Wikipedia War | Other Language War |
|-------|---------------------|-------------------|
| Kashmir | Framing: India vs. Pakistan perspectives | Hindi/Urdu Wikipedias: even more intense, locally embedded |
| Crimea | Classification: Ukrainian vs. Russian territory | Russian Wikipedia: different framing entirely; Ukrainian Wikipedia: different classification |
| Sea of Japan | Naming: "Sea of Japan" vs. "East Sea" | Korean Wikipedia: "East Sea" is default; Japanese Wikipedia: "Sea of Japan" is default |
| Armenian Genocide | Classification: "genocide" vs. "events of 1915" | Turkish Wikipedia: radically different framing and classification |

### 7.2 — Cross‑Language War Comparison Method

```python
def cross_language_war_comparison(wikidata_qid, languages=None):
    """
    Compare edit war intensity for the same concept across languages.
    Uses Wikidata to find the article title in each language.
    """
    if languages is None:
        languages = ["en", "de", "fr", "ja", "ar", "ru", "zh", "es"]

    # Get sitelinks from Wikidata
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
            try:
                war_data = detect_revert_sequences(title, lang,
                                                    window_hours=72,
                                                    min_reverts=2)
                results[lang] = {
                    "title": title,
                    "total_reverts": war_data["total_reverts"],
                    "revert_clusters": war_data["revert_clusters"]
                }
            except Exception as e:
                results[lang] = {"title": title, "error": str(e)}

    return results
```

### 7.3 — What Cross‑Language Comparison Reveals

| Pattern | Interpretation |
|---------|---------------|
| High wars in all languages | **Universally contested regime** — the collision is structural, not cultural |
| High wars in some languages, low in others | **Culturally specific regime collision** — the dispute is meaningful in some contexts but not others |
| Different war types across languages | **Different regime boundaries are active** — English may fight over framing while Korean fights over naming |
| War in English only | **English Wikipedia's global editor base** imports more perspectives, creating more collision surfaces |

---

## 8 — Edit Wars as Research Instruments

### 8.1 — Regime Boundary Mapping

**Method:**
1. Identify articles with high revert rates in a domain
2. For each, extract the disputed content using Section 5.4
3. Classify the dispute by type (Section 2)
4. Map the disputes onto the domain's knowledge structure
5. The result is a **regime boundary map** — a visualization of where
   structural disputes concentrate within a domain

### 8.2 — Regime Transition Monitoring

**Method:**
1. Set up a watchlist of articles in a domain
2. Monitor revert rates using periodic API calls
3. When a revert cluster is detected, extract the competing claims
4. Track the resolution pattern (Section 4) over time
5. Completed transitions = the domain's regime landscape has shifted

### 8.3 — Consensus Archaeology

**Method:**
1. Find a long‑resolved edit war in a domain (check talk page archives)
2. Extract the original competing claims from the revision history
3. Identify the resolution pattern and final consensus
4. The resolved war reveals **how the community established a regime
   boundary** — the process of structural decision‑making

### 8.4 — Predictive War Analysis

**Method:**
1. Monitor talk page dispute intensity (from `Talk_Page_Coherence_Surface.md`)
2. When talk page disputes escalate past coherence gradient Level 3, flag
   the article for potential edit war
3. Talk page escalation is a **leading indicator** of edit wars — disputes
   that fail to resolve on talk pages often erupt as edit wars
4. Early detection enables preemptive mediation before structural damage occurs

---

## 9 — Cross‑Reference to Other Module Files

| File | How Edit Wars Connect |
|------|----------------------|
| `Talk_Page_Coherence_Surface.md` | Edit wars are the **failure mode** of talk page consensus — when talk cannot resolve a dispute, it erupts as warring in the article. Talk page escalation is a leading indicator |
| `NPOV_As_Coherence_Operator.md` | Many edit wars are NPOV disputes — Framing Wars (Type 3) map directly to NPOV failure modes. Irreconcilable wars reveal NPOV's structural limits |
| `Revision_History_Regime_Analysis.md` | Edit wars produce the most dramatic signals in revision history — revert spikes, size oscillations, elevated revert rates. This file provides the detection algorithms |
| `Featured_Article_Validation_Corridor.md` | Active or recent edit wars block FA validation — criterion 5 (Stability) requires no ongoing content disputes |
| `Category_Taxonomy_Regime_Hierarchy.md` | Classification Wars (Type 2) often involve category changes — the edit war and the category dispute are two surfaces of the same regime collision |
| `Wikidata_Ingestion_Format.md` | Wikidata edit wars (P31 disputes, label conflicts) are structurally equivalent — same collision, different surface |
| `Cross_Domain_Meta_Operators.md` | Operator 8 (Edit War as Regime Boundary Marker) is derived directly from this file |
| `Wikipedia_RTT_Structural_Mapping.md` | Edit wars are mapped in Section 2.2 as "regime transition events" and Section 2.6 as "regime collision alarms" |

---

## 10 — Student Exercises

### Exercise 1 — War Type Classification (15 minutes)

1. Browse Wikipedia's list of notable edit wars: `https://en.wikipedia.org/wiki/Wikipedia:Lamest_edit_wars`
2. Pick 3 edit wars from different sections
3. Classify each by type using Section 2 (Factual, Classification, Framing, Inclusion/Exclusion, or Naming)
4. For each, write one sentence: *"This is a [type] war because the competing claims are about [specific structural question]."*

### Exercise 2 — Live War Detection (25 minutes)

1. Pick an article you expect might have recent edit conflicts (try: a current political leader, a recent scientific controversy, or a currently disputed territory)
2. Check the article's revision history for recent reverts (look for "undo" or "revert" in edit summaries)
3. If you find reverts, classify the severity (Section 3) and the war type (Section 2)
4. Check the talk page — is the dispute being discussed there?
5. Answer: *"This article [does/does not] show signs of active edit warring. The severity is [level] and the war type is [type]. The talk page [does/does not] have a related discussion thread."*

### Exercise 3 — Resolution Pattern Analysis (30 minutes)

1. Find a completed (resolved) edit war — check talk page archives for threads that discuss settled disputes
2. Identify which resolution pattern from Section 4 was used (Regime Displacement, Compromise Synthesis, Structural Separation, or Administrative Freeze)
3. Trace the resolution process: What arguments were decisive? Who mediated? How long did it take?
4. Write two sentences: *"This war was resolved through [pattern] because [reason]. The winning regime claim was [claim] and it prevailed because [structural advantage]."*

### Exercise 4 — Regime Boundary Extraction (30 minutes)

1. Find an article with a recent or ongoing edit war
2. Use the article's revision history to find two competing revisions (the "before" and "after" of a revert)
3. Compare the two versions using Wikipedia's built‑in diff tool (click "prev" next to any revision)
4. Identify the **exact text** that is being disputed — this is the regime boundary
5. Answer: *"The regime boundary is located in the [section/paragraph] and concerns [specific text]. Claim A says [X] while Claim B says [Y]. The structural question is [what the dispute is really about at R0/R1 level]."*

### Exercise 5 — Cross‑Language War Comparison (30 minutes)

1. Pick a topic with known cross‑cultural sensitivity (try: a territorial dispute, a historical conflict, or a contested political classification)
2. Check the article's recent revision history in English + 1 other language edition
3. Compare: Does the same topic produce edit wars in both languages? Are the same dimensions being disputed?
4. Answer: *"The English Wikipedia fights about [X] while the [other language] Wikipedia fights about [Y]. This reveals that the regime collision is [universal/culturally specific] because [reason]."*

---

*This file is part of the [Wikipedia Awareness Module](README.md) in the [TriadicFrameworks](https://www.triadicframeworks.org/) canon.*
