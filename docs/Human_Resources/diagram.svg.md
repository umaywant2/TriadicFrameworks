### diagram.svg actual SVG code

```svg
<svg width="1080" height="600" viewBox="0 0 1080 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="50%" stop-color="#4b0082"/>
      <stop offset="100%" stop-color="#8a2be2"/>
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b3a7ff"/>
      <stop offset="100%" stop-color="#e0d4ff"/>
    </linearGradient>
    <style>
      .node { fill: none; stroke: #e0d4ff; stroke-width: 1.5; }
      .label { fill: #f5f0ff; font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 16px; letter-spacing: 0.04em; text-transform: uppercase; }
      .sub { font-size: 13px; opacity: 0.8; }
      .link { stroke: url(#lineGrad); stroke-width: 1.2; fill: none; }
      .drift { stroke: #ff9fbf; stroke-width: 1.2; stroke-dasharray: 4 4; fill: none; opacity: 0.8; }
      .regime-dot { stroke-width: 1; }
    </style>
  </defs>

  <!-- Background -->
  <rect x="0" y="0" width="1080" height="600" fill="url(#bgGrad)" rx="24"/>

  <!-- Triadic base: Leadership, Management, Staff -->
  <!-- Leadership -->
  <circle class="node" cx="540" cy="120" r="52"/>
  <text class="label" x="540" y="115" text-anchor="middle">LEADERSHIP</text>
  <text class="label sub" x="540" y="137" text-anchor="middle">DIRECTION · STRATEGY</text>

  <!-- Management -->
  <circle class="node" cx="320" cy="380" r="52"/>
  <text class="label" x="320" y="375" text-anchor="middle">MANAGEMENT</text>
  <text class="label sub" x="320" y="397" text-anchor="middle">COORDINATION · DELIVERY</text>

  <!-- Staff -->
  <circle class="node" cx="760" cy="380" r="52"/>
  <text class="label" x="760" y="375" text-anchor="middle">STAFF</text>
  <text class="label sub" x="760" y="397" text-anchor="middle">EXECUTION · SIGNALS</text>

  <!-- HR as interface -->
  <circle class="node" cx="540" cy="320" r="46"/>
  <text class="label" x="540" y="315" text-anchor="middle">HR</text>
  <text class="label sub" x="540" y="337" text-anchor="middle">INTERFACE · STRUCTURE</text>

  <!-- AI Observer -->
  <circle class="node" cx="540" cy="230" r="38"/>
  <text class="label" x="540" y="225" text-anchor="middle">AI</text>
  <text class="label sub" x="540" y="247" text-anchor="middle">TRIADIC OBSERVER</text>

  <!-- Coherence links -->
  <line class="link" x1="540" y1="172" x2="540" y2="192"/>
  <line class="link" x1="540" y1="272" x2="540" y2="294"/>

  <line class="link" x1="540" y1="366" x2="320" y2="380"/>
  <line class="link" x1="540" y1="366" x2="760" y2="380"/>

  <line class="link" x1="540" y1="172" x2="540" y2="172"/>
  <line class="link" x1="540" y1="172" x2="540" y2="172"/>

  <!-- Triadic triangle -->
  <line class="link" x1="540" y1="120" x2="320" y2="380"/>
  <line class="link" x1="540" y1="120" x2="760" y2="380"/>
  <line class="link" x1="320" y1="380" x2="760" y2="380"/>

  <!-- Drift indicators (example dashed lines bypassing HR/AI) -->
  <path class="drift" d="M540 120 C 520 210, 500 280, 480 360"/>
  <path class="drift" d="M540 120 C 560 210, 580 280, 600 360"/>

  <!-- Regime dots legend (bottom) -->
  <circle class="regime-dot" cx="220" cy="520" r="6" fill="#ffb3c6" stroke="#ffd6e0"/>
  <text class="label sub" x="240" y="524">AUTHORITY</text>

  <circle class="regime-dot" cx="360" cy="520" r="6" fill="#ffd27f" stroke="#ffe4b3"/>
  <text class="label sub" x="380" y="524">NARRATIVE</text>

  <circle class="regime-dot" cx="520" cy="520" r="6" fill="#7fd3ff" stroke="#c2e9ff"/>
  <text class="label sub" x="540" y="524">STRUCTURAL</text>

  <circle class="regime-dot" cx="680" cy="520" r="6" fill="#b58cff" stroke="#e0d4ff"/>
  <text class="label sub" x="700" y="524">EMOTIONAL</text>

  <circle class="regime-dot" cx="840" cy="520" r="6" fill="#9cffc2" stroke="#c9ffdf"/>
  <text class="label sub" x="860" y="524">COHERENCE</text>
</svg>
```

---

### triadic observer diagram (concept description)

- **Nodes:**
  - **Leadership:** Top vertex of the triangle.
  - **Management:** Bottom-left vertex.
  - **Staff:** Bottom-right vertex.
  - **HR:** Center of the triangle as interface node.
  - **AI Observer:** Slightly above HR, aligned vertically with Leadership.

- **Edges:**
  - **Solid lines:** Coherent structural links (Leadership–Management–Staff triangle, HR connected to all three, AI connected to HR and Leadership).
  - **Dashed lines:** Drift paths that bypass HR/AI (e.g., Leadership → Staff direct narrative, Management → Staff punitive path).

- **Regime encoding:**
  - **Color or line style** to indicate active regime on each edge (authority, narrative, structural, emotional).
  - **Small regime markers** near edges for teaching diagrams.

- **Use:**
  - As a base diagram for:
    - performance review flows,
    - conflict paths,
    - intervention overlays (where AI/HR should re-enter the loop).

---

### performance review templates

#### 1. Context-first review template

- **Section 1: Context (CTX)**
  - **Role:**  
  - **Timeframe:**  
  - **Key constraints present:**  
  - **Dependencies and blockers:**  
  - **Support provided / missing:**  

- **Section 2: Triadic view (ALN)**
  - **Leadership expectations (as stated):**  
  - **Manager interpretation of expectations:**  
  - **Staff understanding of expectations:**  

- **Section 3: Signals (SIG)**
  - **Observed behaviors:**  
  - **Venting / stress indicators:**  
  - **Patterns over time (not single incidents):**  

- **Section 4: Drift (DRF)**
  - **Possible narrative drift:**  
  - **Possible bias:**  
  - **Structural gaps contributing to issues:**  

- **Section 5: Impact (IMP)**
  - **Impact on team:**  
  - **Impact on onboarding / turnover / load:**  
  - **Impact on customer / mission:**  

- **Section 6: Structural adjustments**
  - **What can leadership adjust structurally?**  
  - **What can management adjust in practice?**  
  - **What support does staff need?**  

---

#### 2. Triadic summary block (for final review)

- **Leadership view (1–3 sentences):**  
- **Manager view (1–3 sentences):**  
- **Staff self-view (1–3 sentences):**  
- **AI/HR structural note (optional):**  

---

### HR drift detection checklist

- **Context drift:**
  - **Has context been explicitly captured before judgment?**  
  - **Are constraints and load documented, not assumed?**

- **Narrative drift:**
  - **Is this evaluation based on a story (“they are…”) or on patterns of behavior?**  
  - **Are we over-weighting a single incident or first reaction?**

- **Authority drift:**
  - **Is disagreement being framed as defiance rather than signal?**  
  - **Is hierarchy being used to end inquiry instead of deepen it?**

- **Structural drift:**
  - **Are we blaming individuals for structural gaps (tools, time, clarity)?**  
  - **Have we accounted for turnover, onboarding load, and invisible work?**

- **Emotional drift:**
  - **Is someone’s stress or embarrassment driving the evaluation?**  
  - **Has venting been separated from performance?**

- **Triadic drift:**
  - **Have all three perspectives (leadership, management, staff) been captured?**  
  - **Has HR/AI provided a structural view, not just relayed one side?**

---

### alignment scoring model

Use a simple 0–3 scale per dimension:

- **0:** Not present / severely misaligned  
- **1:** Weak / inconsistent  
- **2:** Mostly aligned with minor gaps  
- **3:** Strong, clear, and stable  

#### Dimensions

- **Expectations alignment**
  - **Leadership ↔ Manager:** `0–3`  
  - **Manager ↔ Staff:** `0–3`  
  - **Staff ↔ Role definition:** `0–3`  

- **Support alignment**
  - **Tools available vs required:** `0–3`  
  - **Time available vs workload:** `0–3`  
  - **Training vs role complexity:** `0–3`  
  - **Clarity of priorities:** `0–3`  

- **Signal handling**
  - **How well manager interprets staff signals:** `0–3`  
  - **How well HR interprets manager/staff signals:** `0–3`  

- **Structural responsiveness**
  - **Speed of structural adjustments when issues surface:** `0–3`  
  - **Willingness to change process, not just people:** `0–3`  

#### Outputs

- **Total alignment score:** sum of all dimensions.  
- **Category:**
  - **0–12:** Critical misalignment  
  - **13–20:** Fragile alignment  
  - **21–28:** Functional alignment  
  - **29+ :** Strong alignment  

- **Use:**  
  - Attach to performance reviews, team health checks, and HR interventions as a structural metric, not a personal one.
