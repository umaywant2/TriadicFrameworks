# 📢 **OpenAdEngine — architecture.md**  
**OpenWarden Suite — Contextual Advertising Substrate**  
**Analyzer Layer:** semantic  
**Regime:** open‑ad‑governance  
**Version:** 1.0  

---

## **1. Architectural Overview**

OpenAdEngine provides a **privacy‑first, drift‑aware, operator‑aligned advertising substrate** within the OpenWarden suite. Its architecture is built around five canonical components:

1. **Dimensional Signature Model**  
2. **Semantic Intent Classifier**  
3. **Resonance Matching Engine**  
4. **Contextual Delivery Layer**  
5. **Governance & Drift Control**

Each component is coherence‑declared and drift‑bounded, ensuring predictable, ethical ad behavior across all OpenWarden modules.

---

## **2. Dimensional Signature Model**

The Dimensional Signature Model defines the **identity** of an ad without referencing personal data.  
It encodes:

- semantic dimension  
- contextual dimension  
- resonance dimension  
- intent dimension  

These signatures allow ads to be matched to content based on **meaning**, not surveillance.

### **2.1 Dimensional Fields**

| Field | Description |
|-------|-------------|
| `ad.dimension.semantic` | Topic or conceptual cluster |
| `ad.dimension.contextual` | Page or module context |
| `ad.dimension.resonance` | Alignment strength |
| `ad.dimension.intent` | Transactional, informational, navigational |

All fields are canonical and drift‑bounded.

---

## **3. Semantic Intent Classifier**

The classifier determines **what the ad is trying to do**, not who it targets.

Intent categories include:

- **Informational** — explain, educate  
- **Transactional** — purchase, sign‑up  
- **Navigational** — direct to a resource  
- **Contextual** — align with page meaning  

The classifier uses OpenWarden’s semantic operator grammar to ensure consistency across modules.

---

## **4. Resonance Matching Engine**

The Resonance Engine determines whether an ad should appear in a given context.

### **4.1 Matching Criteria**

Ads are delivered when:

- semantic intent aligns with page intent  
- dimensional signature matches contextual category  
- resonance exceeds threshold  
- coherence is stable  
- operator grammar is valid  

This creates a predictable, transparent ad ecosystem.

### **4.2 Resonance Calculation**

Resonance is computed using:

- semantic similarity  
- dimensional overlap  
- contextual relevance  
- operator alignment  

All resonance values are drift‑bounded and lineage‑tracked.

---

## **5. Contextual Delivery Layer**

The delivery layer ensures ads appear **only** when contextually appropriate.

### **5.1 Delivery Inputs**

- page topic  
- semantic cluster  
- dimensional signature  
- canonical metadata  
- operator grammar  

### **5.2 Delivery Outputs**

- ad placement  
- ad ordering  
- ad suppression (if drift detected)  
- lineage record  

No personal data is ever used.

---

## **6. Governance & Drift Control**

OpenAdEngine enforces strict governance rules inherited from OpenWarden.

### **6.1 Drift Types Monitored**

- manipulative metadata drift  
- adversarial resonance injection  
- inflated operator values  
- non‑canonical fields  
- semantic misalignment  

### **6.2 Drift Responses**

- flag  
- correct  
- suppress  
- recalibrate  
- lineage update  

### **6.3 Governance Enforcement**

Governance ensures:

- metadata correctness  
- operator grammar compliance  
- resonance stability  
- contextual integrity  

---

## **7. Cross‑Module Integration**

OpenAdEngine integrates with:

- **OpenSEO** — shared semantic operators  
- **OpenSoN** — social context alignment  
- **OpenStream** — streaming recommendation coherence  
- **OpenCatalog** — product metadata alignment  
- **OpenRisk** — anomaly detection for ad drift  
- **OpenIAM** — identity‑safe delivery rules  

All integrations are drift‑bounded and coherence‑declared.

---

## **8. Canonical Metadata Block**

Example metadata fields used by OpenAdEngine:

```html
<meta name="open.ad.dimension" content="semantic:software;resonance:0.87">
<meta name="open.ad.intent" content="transactional">
<meta name="open.ad.resonance" content="0.91">
<meta name="open.ad.coherence" content="0.94">
<meta name="open.ad.structure" content="hierarchy:0.93">
<meta name="open.ad.audience" content="semantic:developers">
<meta name="open.ad.version" content="1.0">
<meta name="open.ad.module" content="OpenAdEngine">
```

---

## **9. File Structure**

- `README.md` — front door  
- `architecture.md` — this file  
- `canonical_metadata.md` — metadata rules  
- `governance.md` — drift & policy rules  
- `operators.md` — operator grammar  
- `index.html` — module front page  
- `module.json` — manifest  
