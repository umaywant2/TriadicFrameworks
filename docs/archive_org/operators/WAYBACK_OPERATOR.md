# 🟠 **WAYBACK_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** WAYBACK_OPERATOR  
- **Operator Family:** T‑Ops (Temporal Operators)  
- **Module:** archive_org  
- **Purpose:** Retrieve time‑indexed snapshots from the Internet Archive and measure structural drift across versions.

---

## **Purpose (One Sentence)**
The WAYBACK_OPERATOR retrieves all available snapshots for a target URL and produces a **drift_map**, **continuity_breaks**, and **time‑crystal stability estimate**.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `target` | URL | The webpage or object to analyze. |
| `constraints` | object (optional) | Time range, snapshot limits, or filtering rules. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `snapshots` | Ordered list of IA captures with timestamps + structural metadata. |
| `drift_map` | Structural drift levels between consecutive snapshots. |
| `continuity_breaks` | Missing years, gaps, or discontinuities in the timeline. |
| `time_crystal` | Stability estimate across time (0–1). |

---

## **Operator Guarantees**
- No content‑based reasoning.  
- Drift measured **structurally**, not semantically.  
- All snapshots treated as **structural objects**, not “truth.”  
- Missing snapshots treated as **uncertainty**, not “no change.”  
- Output is **deterministic** given the same IA data.

---

## **Structural Drift Levels**
| Level | Meaning |
|-------|---------|
| **none** | Identical structure. |
| **minor** | Small layout/CSS shifts. |
| **moderate** | Navigation or template changes. |
| **high** | CMS migration, redesign, or rebuild. |

---

## **Continuity Rules**
- A missing year = **continuity uncertainty**, not a break.  
- A missing *sequence* of years = **continuity break**.  
- A redirect = **potential lineage fork** (passed to LINEAGE_OPERATOR).  
- A CMS migration = **high drift** + **regime shift candidate**.

---

## **Time‑Crystal Stability**
A normalized measure of structural consistency across snapshots:

```
1.0   = highly stable (PDF-like)
0.7   = mostly stable
0.4   = moderate drift
0.1   = high drift / unstable
0.0   = no stable structure
```

---

## **Operator Procedure**
1. Query IA for all snapshots of `target`.  
2. Normalize timestamps + structural metadata.  
3. Compare each snapshot to the next:  
   - layout  
   - navigation  
   - DOM structure  
   - template  
   - substrate  
4. Assign drift levels.  
5. Detect continuity breaks.  
6. Compute time‑crystal stability.  
7. Emit outputs for LINEAGE_OPERATOR.

---

## **Failure Modes**
- **No snapshots:** return empty timeline + warning.  
- **Sparse snapshots:** drift_map may be incomplete.  
- **Mixed substrates:** drift may be inflated (handled by PRESERVATION_OPERATOR).  

---

## **Hand‑Off to Next Operator**
Outputs feed directly into:

### **LINEAGE_OPERATOR**
- `snapshots`  
- `drift_map`  
- `continuity_breaks`  
- `time_crystal`

---

## **Example (Synthetic)**
```
Input:
  target = "https://example.gov/records"

Output:
  snapshots = [2014, 2017, 2020, 2023]
  drift_map = {
    "2014→2017": "minor",
    "2017→2020": "high",
    "2020→2023": "minor"
  }
  continuity_breaks = []
  time_crystal = 0.62
```

---

## **RTT/1 Mindset**
- Prefer **structure** over content.  
- Prefer **lineage** over isolated snapshots.  
- Drift is **explicit**, never implied.  
- Missing data is **uncertainty**, not “no change.”  
