# **RFC‑REMIX‑0005 — Remix Lineage Diff Protocol**  
### *Canonical Genealogy Engine for Remixathon Scrolls*  
RefId: turn0browsertab1

**Title:** Remix Lineage Diff Protocol  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.2  

---

## **1. Purpose**

The **Remix Lineage Diff Protocol (RLDP)** defines how remix scrolls inherit, compare, and evolve across generations.

It provides:

- lineage ancestry tracking  
- diff computation between parent and child scrolls  
- glyph inheritance rules  
- RCI clarity inheritance  
- tag propagation  
- validator lineage integrity checks  
- archival lineage indexing  

RLDP is the **genealogy engine** of the Remixathon system.

---

## **2. Lineage Model**

Each remix scroll has:

- **parent scroll(s)**  
- **child scroll(s)**  
- **sibling scrolls**  
- **ancestry depth**  
- **glyph inheritance**  
- **clarity inheritance**  
- **tag inheritance**  

Lineage is represented as:

```
parent → child → child → child …
```

or for multi‑parent remixing:

```
parentA + parentB → child
```

---

## **3. Diff Types**

RLDP computes three canonical diff types:

### **3.1 Glyph Diff**
Compares glyph distributions:

- added glyphs  
- removed glyphs  
- changed glyph counts  
- density shifts (α → β → γ)

### **3.2 RCI Diff**
Compares clarity bands:

- clarity increase  
- clarity decrease  
- band transitions (low → medium → high)

### **3.3 Tag Diff**
Compares tag lists:

- added tags  
- removed tags  
- category shifts  
- contributor‑defined tag changes  

---

## **4. Diff Schema**

```yaml
lineage_diff:
  parent_scroll: "s-1000"
  child_scroll: "s-1001"

  glyph_diff:
    added: ["⬣"]
    removed: ["◇"]
    changed:
      ◇: {from: 2, to: 0}
      ◆: {from: 1, to: 2}

  rci_diff:
    parent_rci: 0.42
    child_rci: 0.67
    band_transition: "medium → high"

  tag_diff:
    added: ["cipher-dense"]
    removed: ["fluid-turbulent"]
    changed: []
```

---

## **5. Inheritance Rules**

### **5.1 Glyph Inheritance**
Child scrolls inherit:

- glyph types  
- glyph counts  
- glyph density class  

unless explicitly overridden.

### **5.2 RCI Inheritance**
Child scrolls inherit:

- clarity band  
- clarity score  
- rail signature block  

unless clarity is recomputed.

### **5.3 Tag Inheritance**
Child scrolls inherit:

- semantic tags  
- rail tags  
- cultural tags  

unless removed or replaced.

---

## **6. Validator Hooks**

Validator engines enforce:

### **Lineage Integrity**
- parent must exist  
- child must cite parent  
- diff must be valid  

### **Glyph Consistency**
- glyph changes must match scroll body  
- density class must be valid  

### **RCI Consistency**
- clarity band must match RCI score  
- rail signatures must be present  

### **Tag Consistency**
- tags must exist in Tag Registry  
- categories must be valid  

### **Checksum**
Diffs include reproducibility checksum.

---

## **7. Python‑Style Diff Engine Stub**

File:  
```
engine/remix_lineage_diff.py
```

```python
def compute_diff(parent, child):
    diff = {}

    # Glyph diff
    diff["glyph_diff"] = {
        "added": list(set(child["glyphs"]) - set(parent["glyphs"])),
        "removed": list(set(parent["glyphs"]) - set(child["glyphs"])),
        "changed": {}
    }

    # RCI diff
    diff["rci_diff"] = {
        "parent_rci": parent["rci"],
        "child_rci": child["rci"],
        "band_transition": f"{parent['band']} → {child['band']}"
    }

    # Tag diff
    diff["tag_diff"] = {
        "added": list(set(child["tags"]) - set(parent["tags"])),
        "removed": list(set(parent["tags"]) - set(child["tags"])),
        "changed": []
    }

    return diff
```

---

## **8. Dashboard Integration**

RLDP powers:

- lineage graph  
- diff overlays  
- ancestry depth visualization  
- glyph diff wheel  
- clarity diff histogram  
- tag diff panel  

---

## **9. Archival Integration**

RLDP integrates with:

- **RFC_ARC_0014** (archival protocol)  
- **RFC_REG_0004** (registry indexer)  
- **RFC_EXP_0013** (export module)  

Diffs are stored in:

```
registry/lineage/
```

---

## **10. Notes**

- RLDP is the genealogy engine of Remixathon.  
- Diffs are deterministic and validator‑grade.  
- Multi‑parent remixing is supported.  
- Glyph, RCI, and tag diffs are first‑class citizens.  
- Lineage depth is tracked automatically.

---

## **11. Closing Statement**

RFC‑REMIX‑0005 formalizes the **Remix Lineage Diff Protocol**, the canonical system for computing, storing, and validating lineage diffs across Remixathon scroll generations.

It anchors the remix genealogy system and integrates seamlessly with ENG, EXP, ARC, REG, LIB, and HUB modules.
