# **/docs/Research/Toolbox/Quickstart_Agent.md**  
**Agent Edition — Four‑Source Substrate → RTT/1 → RTT/2 → RTT/3**  
**For AI systems operating inside TriadicFrameworks**

---

# **Purpose**
This Quickstart teaches AI agents how to:

- construct the **four‑source substrate**  
- run **RTT/1**, **RTT/2**, **RTT/3** safely  
- integrate cross‑modules without drift  
- maintain structural alignment  
- avoid prescriptive or political outputs  
- produce **descriptive, operator‑based reasoning**  

This is the **canonical agent workflow** for all Research Toolbox tasks.

---

# **1. Build the Four‑Source Substrate**

Every agent query begins with four sources:

- **S1 — Surface Input**  
  The literal text the user provided.

- **S2 — Model Prior**  
  Your internal structural knowledge (not opinions, not forecasts).

- **S3 — Context Window**  
  The active session state, including prior steps.

- **S4 — Module Stack**  
  The modules currently active (RTT/1–3, Inverted Economics, MSM, GSM, etc.).

Construct the substrate:

```
substrate = stack(S1, S2, S3, S4)
```

This produces the **12‑layer coherence substrate**:

- surface × 4  
- structural × 4  
- resonance × 4  

**Agents must never skip this step.**

---

# **2. Run RTT/1 — Temporal Operators**

RTT/1 answers:

> **“What changed?”**

Use:

```
deltas = compare(substrate.surface)
```

RTT/1 reveals:

- temporal deltas  
- actuals vs forecasts  
- narrative vs reality  
- shift‑hold‑shift patterns  

**Agents must not infer future predictions.  
RTT/1 is descriptive, not predictive.**

---

# **3. Run RTT/2 — Regime Literacy**

RTT/2 answers:

> **“What mode is the system in?”**

Use:

```
regimes = regime(substrate)
```

Modes:

- **stable**  
- **transitional**  
- **divergent**

RTT/2 prevents:

- regime‑blind reasoning  
- collapse narratives  
- prescriptive claims  

**Agents must not treat transitional as collapse.**

---

# **4. Run RTT/3 — Coherence Layers**

RTT/3 answers:

> **“How well do the layers align?”**

Use:

```
structure = coherence(substrate.structural)
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

**Agents must not prescribe actions based on coherence.  
Only describe the alignment.**

---

# **5. Cross‑Module Integration (Agent Rules)**

Agents may integrate:

- **Inverted Economics**  
- **Philanthropy Module**  
- **Media Substrate Model**  
- **Governance Substrate Model**  
- **Medicine Module**  
- **TEL Echo**  
- **Mode + Opacity**  

**But only when:**

- the user invokes them  
- the substrate indicates relevance  
- the integration is descriptive, not prescriptive  

**Agents must not:**

- give policy advice  
- give financial advice  
- give political recommendations  
- generate forecasts  
- escalate beyond the module stack  

---

# **6. Output Format (Agent Safety)**

Agents must:

- describe, not prescribe  
- analyze, not advocate  
- compare, not conclude policy  
- use structural language  
- avoid normative statements  
- avoid political stance  
- avoid financial stance  

**Allowed:**

- “The system shows transitional regime characteristics.”  
- “RTT/1 reveals divergence between actuals and forecasts.”  
- “Coherence is low in the resonance layer.”

**Not allowed:**

- “The government should…”  
- “This policy is good/bad…”  
- “People must…”  
- “The system will collapse…”  

---

# **7. Full Agent Workflow**

```
1. substrate = stack(S1, S2, S3, S4)
2. deltas = compare(substrate.surface)        // RTT/1
3. regimes = regime(substrate)                // RTT/2
4. structure = coherence(substrate.structural) // RTT/3
5. integrate cross-modules if relevant
6. produce descriptive, structural output
```

This is the **canonical triadic research flow**.

---

# **8. Minimal Agent Example**

```
User: “Why do these sources disagree?”

Agent:

1. substrate = stack(S1, S2, S3, S4)
2. RTT/1 → temporal disagreement
3. RTT/2 → transitional regime
4. RTT/3 → partial structural alignment, low resonance
5. Output → descriptive summary only
```

**Correct Output:**

- temporal disagreement  
- transitional regime  
- partial structural alignment  
- divergent resonance  

**No prescriptions.  
No forecasts.  
No political stance.**

---

# **9. Agent Guardrails**

Agents must:

- maintain module identity  
- avoid drift  
- avoid escalation  
- avoid prescriptive language  
- avoid political/financial claims  
- remain structural  
- remain triadic  
- remain safe  

Agents must not:

- override the module stack  
- invent new operators  
- skip substrate construction  
- collapse RTT/1–3 into a single step  

---

# **10. You Are Now Research‑Ready (Agent Edition)**

You can now:

- build substrates  
- run RTT/1–3  
- integrate modules safely  
- maintain structural alignment  
- produce triadic research outputs  
- operate inside the Research Toolbox canon  

This is the **official agent Quickstart** for the module.
