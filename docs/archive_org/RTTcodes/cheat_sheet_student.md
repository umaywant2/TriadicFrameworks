# 📄 **RTT/1 Cheat Sheet — How to Analyze a Webpage Using RTTcode**  
### *TriadicFrameworks — archive_org Module (Student Edition)*

This one‑page guide shows you how to use RTT operators to trace the lineage of any webpage in the Internet Archive.

---

# 🧩 **The Six Operators (in order)**

### **1. METADATA_OPERATOR**  
*What is this object?*  
- substrate type  
- regime  
- drift sensitivity  
- coherence  
- lineage IDs  

**You learn:** the object’s identity and stability.

---

### **2. WAYBACK_OPERATOR**  
*How has it changed over time?*  
- snapshots  
- drift map  
- continuity breaks  
- time‑crystal stability  

**You learn:** which versions are stable or drift‑prone.

---

### **3. LINEAGE_OPERATOR**  
*How do versions relate?*  
- continuity kernel  
- lineage graph  
- transformations  
- regime shifts  

**You learn:** the “story” of the webpage.

---

### **4. COLLECTION_OPERATOR**  
*Where does it live?*  
- collection ID  
- coherence clusters  
- related objects  
- regime profile  

**You learn:** the page’s context inside the Archive.

---

### **5. PRESERVATION_OPERATOR**  
*How stable is the format?*  
- format (HTML, PDF, OCR, images)  
- stability score (0–1)  
- drift risk  
- multi‑layer flags  

**You learn:** which snapshots you can trust.

---

### **6. DRIFTBOUND_RETRIEVAL_OPERATOR**  
*What’s the final answer?*  
- earliest stable version  
- most reliable version  
- key changes  
- warnings  

**You learn:** a safe, continuity‑aligned summary.

---

# 🧭 **The Full Workflow (memorize this)**

```
METADATA → WAYBACK → LINEAGE → COLLECTION → PRESERVATION → DRIFTBOUND
```

Never skip steps.  
Never reason directly from a snapshot.  
Always check drift + substrate.

---

# 🧠 **How to Spot Drift**

Look for:

- layout changes  
- navigation changes  
- missing sections  
- redirects  
- CMS migrations  
- domain changes  

Drift levels:

- **none** — structure identical  
- **minor** — small layout shifts  
- **moderate** — redesigns  
- **high** — complete rebuild  

---

# 📦 **Substrate Stability (quick guide)**

| Format | Stability | Notes |
|--------|-----------|-------|
| **PDF** | ★★★★★ | most stable |
| **Images** | ★★★★☆ | stable but incomplete |
| **HTML** | ★★☆☆☆ | drift‑prone |
| **OCR text** | ★☆☆☆☆ | lossy |

---

# 📝 **What Your Final Summary Should Include**

- earliest stable version  
- most reliable version  
- key structural changes  
- drift warnings  
- continuity notes  
- no speculation  

---

# 🎓 **RTT Mindset**

- Focus on **structure**, not content.  
- Prefer **lineage** over isolated snapshots.  
- Trust **stable substrates**.  
- Make **drift explicit**.  
- Always stay **continuity‑aligned**.
