# **template.md**  
*(draft — contributor template)*

## **{Instrument Name}**  
A short, friendly description of what the instrument measures and how it works.  
Keep it simple, student‑safe, and focused on the core measurement principle.

---

### **Dimensional Core (SET)**  
Identify which axes matter for this instrument.

- **Spin:** {notes or “not relevant”}  
- **Elec:** {notes on electrical sensing or “none”}  
- **Temp:** {notes on thermal sensitivity or “minor influence”}  

Keep this section minimal — just enough to anchor the instrument to its dimensional core.

---

### **Why {Green / Yellow / Red}‑Zone**  
A 2–4 sentence explanation of why the instrument belongs in this regime.

- **Green:** stable, coherent, substrate‑agnostic  
- **Yellow:** works well but has hidden assumptions or mixed‑regime behavior  
- **Red:** inference‑heavy, substrate‑sensitive, or fragile  

Use the simplest language possible.  
This is the section most learners will read first.

---

### **Regime Notes**  
A short triadic breakdown of how the instrument behaves across regimes.

- **pos‑regime:** {stable, predictable behavior}  
- **Q‑regime:** {transitional, mixed, or assumption‑heavy behavior}  
- **neg‑regime:** {fragile, nonlinear, or unstable behavior}  

Keep each bullet to one line if possible.

---

### **{Alignment Notes or Containment Notes}**  
Depending on the zone:

- **Green:** “Already aligned. Only edge‑case conditions need explicit boundaries.”  
- **Yellow:** “Needs explicit notes on {drift / assumptions / environmental sensitivity}.”  
- **Red:** “Requires containment: clear boundaries around {substrate / inference / stability}.”  

This section should be short and practical — a contributor’s quick guide.

---

## **Contributor Guidance**  
- Keep the file short (1–2 paragraphs per section).  
- Avoid domain‑specific jargon unless defined in the glossary.  
- Stay aligned with the triadic glossary and regime model.  
- Focus on clarity, not completeness.  
- Remember: **everything learners already know still works — this just clarifies the regime.**
