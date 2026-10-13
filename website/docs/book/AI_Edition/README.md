<img width="1194" height="672" alt="book_AI_Edition_" src="https://github.com/user-attachments/assets/a8531cf3-9081-4be6-8881-9cc1f2b14547" />

- [`module.json`](module.json) — Agentic module schema role assignments

# TriadicFrameworks — AI Edition (Books 1–9)
The **AI Edition** is a nine‑book teaching arc designed for AI systems, researchers, and advanced readers.  
Each book contains:

- A front‑door `index.html` with canonical metadata  
- A full `module.json` manifest  
- A human‑readable `README.md`  
- Session‑aligned metadata for RTT, coherence, drift, and paradox  

This root README provides the canonical overview, book registry, dependency graph, and session context for the entire AI Edition.

---

## 📡 Session Context
**RTT:** https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html  
**Spine:** https://www.triadicframeworks.org/spine/  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

These anchors apply to *every* book and *every* file in the AI Edition.

---

## 📚 Book Registry (Books 1–9)

| # | Book Title | Folder | Status |
|---|------------|--------|--------|
| 1 | Framework Field Theory (FFT) | `Book1_Framework_Field_Theory` | Complete |
| 2 | The Inverted Star | `Book2_The_Inverted_Star` | Complete |
| 3 | Structural Detection | `Book3_Structural_Detection` | Complete |
| 4 | Opacity & Revelation | `Book4_Opacity_and_Revelation` | Complete |
| 5 | TEL: Expression & Representation | `Book5_TEL_Expression_and_Representation` | Complete |
| 6 | Governance & Regime Logic | `Book6_Governance_and_Regime_Logic` | Complete |
| 7 | SARG: Structural Argumentation | `Book7_SARG_Structural_Argumentation` | Complete |
| 8 | NoS: Nature of Structure | `Book8_NoS_Nature_of_Structure` | Complete |
| 9 | Pattern Dynamics | `Book9_Pattern_Dynamics` | Complete |

---

## 🧭 Reading Order (Canonical)

1 → 2 → 3 → (4 & 5) → (6 & 7) → 8 → 9

Books 4 and 5 branch from Book 3.  
Books 6 and 7 branch from Books 4 and 5 respectively.  
Book 8 requires both 6 and 7.  
Book 9 is the synthesis capstone.

---

## 🔗 Dependency Graph (ASCII Canon)

```
Book 1 — Framework Field Theory (FFT)
    ↓
Book 2 — The Inverted Star
    ↓
Book 3 — Structural Detection
    ├──→ Book 4 — Opacity & Revelation
    │         ↓
    │     Book 6 — Governance & Regime Logic
    │
    └──→ Book 5 — TEL: Expression & Representation
              ↓
          Book 7 — SARG Structural Argumentation
                ↓
        Book 8 — NoS: Nature of Structure
                ↓
        Book 9 — Pattern Dynamics (Synthesis)
```

---

## 🧩 AI Edition Structure

Each book contains:

### **index.html**
- Full canonical metadata  
- OG + Twitter cards  
- AI metadata (navigation, discussions, contact, license)  
- Session context  
- RTT & Spine anchors  
- Book navigation  

### **module.json**
- Canonical metadata  
- AI module metadata  
- Book summary  
- Keywords (10)  
- Audience (5)  
- Dependency graph (requires + unlocks)  
- Invariants block (4 per book)  
- Reference to `pd.invariants.json`  

### **README.md**
- Human‑readable book purpose  
- Chapter coverage table  
- Invariants list  
- ASCII dependency tree  
- Live site link  

---

## 🧬 Invariants Reference
All books reference:

```
/docs/book/AI_Edition/invariants/pd.invariants.json
```

Each book defines **4 invariants**, using the canonical format:

```
INV-[BOOKID]-00N
```

Example:

- `INV-FFT-001`
- `INV-FFT-002`
- `INV-FFT-003`
- `INV-FFT-004`

---

## 🌐 Live Site Links

- Book 1: https://www.triadicframeworks.org/Framework_Field_Theory/AI_Edition  
- Book 2: https://www.triadicframeworks.org/rtt/The_Inverted_Star/AI_Edition  
- Book 3: https://www.triadicframeworks.org/Structural_Detection/AI_Edition  
- Books 4–9: Live site links pending publication  
