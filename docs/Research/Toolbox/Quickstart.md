# **Research Toolbox — Quickstart (Student Edition)**  
**Four‑Source Substrate → RTT/1 → RTT/2 → RTT/3**

This Quickstart teaches the **entire Research Toolbox workflow** in under 30 seconds.

---

## **1. Start with the four sources**
Every research question begins with:

- **S1 — Surface Input** (what you typed or provided)  
- **S2 — Model Prior** (what the AI already knows structurally)  
- **S3 — Context Window** (conversation/session state)  
- **S4 — Module Stack** (RTT/1–3 + selected modules)

You don’t choose these — they’re always present.

```
substrate = stack(S1, S2, S3, S4)
```

This produces the **12‑layer coherence substrate**:

- surface × 4  
- structural × 4  
- resonance × 4  

---

## **2. Run RTT/1 — Temporal Operators**
Ask how things *changed*.

```
compare(substrate.surface)
```

RTT/1 reveals:

- temporal deltas  
- actuals vs forecasts  
- shift‑hold‑shift patterns  
- narrative vs reality gaps  

---

## **3. Run RTT/2 — Regime Literacy**
Ask what *mode* the system is in.

```
regime(substrate)
```

Modes:

- **stable**  
- **transitional**  
- **divergent**

RTT/2 prevents regime‑blind reasoning.

---

## **4. Run RTT/3 — Coherence Layers**
Ask how the layers *align*.

```
coherence(substrate.structural)
```

Layers:

- **surface coherence**  
- **structural coherence**  
- **resonance coherence**

RTT/3 reveals:

- alignment  
- drift  
- hidden attractors  
- structural stability  

---

## **5. The whole workflow**
In one line:

```
stack → compare → regime → coherence
```

This is the **canonical research pattern** used across TriadicFrameworks.

---

## **Minimal Example**

```
Q: “Why do these sources disagree?”

1. substrate = stack(S1, S2, S3, S4)
2. deltas = compare(substrate.surface)
3. regimes = regime(substrate)
4. structure = coherence(substrate.structural)

Output:
- temporal disagreement
- transitional regime
- partial structural alignment
- divergent resonance
```

---

## **You’re now research‑ready**
This Quickstart gives you:

- the substrate  
- the operators  
- the triadic engine flow  
- the minimal example  
- the safe, canonical pattern  

Use this for **every** Research Toolbox exercise.


