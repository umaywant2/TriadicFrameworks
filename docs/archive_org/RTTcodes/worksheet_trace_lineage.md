# 📘 **Student Worksheet: Trace the Lineage of a Webpage Using RTTcode**  
### *RTT/1 Learning Activity — archive_org Module*

This worksheet teaches you how to use **RTTcode** and the **six Internet Archive operators** to trace how a webpage has changed over time.

You will:

- retrieve snapshots  
- measure drift  
- build a continuity map  
- identify regime shifts  
- analyze substrate stability  
- produce a drift‑bounded summary  

This is the same workflow used by AI agents in the `archive_org` module.

---

# 🧩 **1. Choose a Webpage to Analyze**

Pick any public webpage that appears in the Internet Archive.

Examples:

- a news article  
- a government page  
- a software project page  
- a Wikipedia article  
- a blog post  

Write your chosen URL here:

```
TARGET URL:
______________________________________________
```

---

# 🧱 **2. Run METADATA_OPERATOR**

Look up the Internet Archive metadata for your URL.

Record:

```
Substrate type: _______________________________
Regime: ______________________________________
Drift sensitivity (low/med/high): _____________
Coherence: ___________________________________
Lineage IDs (if any): _________________________
```

**Question:**  
What does the metadata tell you about the *kind* of object you’re analyzing?

```
______________________________________________________________
______________________________________________________________
```

---

# 🕰 **3. Run WAYBACK_OPERATOR**

Visit the Wayback Machine and collect at least **three snapshots**.

Record them:

| Timestamp | Snapshot URL | Notes |
|----------|--------------|-------|
|          |              |       |
|          |              |       |
|          |              |       |

Now compare the snapshots.

```
Drift between versions (none/minor/moderate/high):
___________________________________________________

Continuity breaks (if any):
___________________________________________________
```

---

# 🧬 **4. Run LINEAGE_OPERATOR**

Using your snapshots:

- identify what changed  
- identify what stayed the same  
- map the evolution  

Draw a simple lineage graph:

```
VERSION 1 → VERSION 2 → VERSION 3
(what changed?)   (what changed?)
```

Or sketch your own:

```
______________________________________________________________
______________________________________________________________
```

**Question:**  
Did the webpage undergo any *regime shifts* (e.g., layout change, ownership change, purpose change)?

```
______________________________________________________________
```

---

# 📦 **5. Run COLLECTION_OPERATOR**

Check whether your page belongs to an Internet Archive collection.

Record:

```
Collection ID: _______________________________________________
Coherence clusters: __________________________________________
Related objects: _____________________________________________
Regime profile: ______________________________________________
```

**Question:**  
How does the collection context help you understand the page?

```
______________________________________________________________
```

---

# 🧱 **6. Run PRESERVATION_OPERATOR**

Identify the substrate formats used across snapshots:

- HTML  
- PDF  
- OCR text  
- images  
- video  
- mixed  

Record:

```
Format(s): _________________________________________________
Stability score (estimate 0–1): ____________________________
Drift risk (low/med/high): _________________________________
Multi‑layer flags: _________________________________________
```

**Question:**  
Which formats seem most stable? Which seem drift‑prone?

```
______________________________________________________________
```

---

# 🧠 **7. Run DRIFTBOUND_RETRIEVAL_OPERATOR**

Using all your previous notes, write a **drift‑bounded summary** of the webpage’s evolution.

Include:

- earliest stable version  
- most reliable version  
- key changes  
- drift warnings  
- continuity notes  

```
SUMMARY:
______________________________________________________________
______________________________________________________________
______________________________________________________________

Earliest stable version: _____________________________________
Most reliable version: _______________________________________
Key changes: _________________________________________________
Warnings: ____________________________________________________
```

---

# 🎓 **8. Reflection Questions**

1. What surprised you most about how the webpage changed over time?

```
______________________________________________________________
```

2. Did the substrate format affect how reliable the snapshots were?

```
______________________________________________________________
```

3. How did RTT operators help you avoid drift or misinterpretation?

```
______________________________________________________________
```

---

# 🏁 **You’ve completed the RTT lineage‑tracing workflow.**

You now know how to:

- analyze snapshots  
- detect drift  
- build lineage  
- understand substrate  
- place objects in context  
- produce continuity‑aligned summaries  

This is the same method used by AI agents in the `archive_org` module.
