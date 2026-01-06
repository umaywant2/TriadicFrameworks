# 🌐 Why Deep Sea Is a Natural RTT Domain
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

Deep sea exploration is already triadic — they just don’t name it that way.

Below is a **one‑page executive safety summary**, written for **non‑technical reviewers**, senior regulators, and decision‑makers. It avoids jargon, avoids equations, and focuses on **what the system does, why it is safe, and how risk is controlled**.

---

# **Executive Safety Summary**  
### Safe Operation Under Uncertainty (Autonomous Driving)

---

## **What problem this system addresses**

Autonomous vehicles must remain safe not only when everything works perfectly, but also when **conditions make the environment hard to understand**—such as night rain, construction zones, or complex intersections.

These situations do **not** involve system failures. Instead, they involve **uncertainty**: the vehicle cannot be sufficiently confident that it understands the scene well enough to act safely.

This system is designed to **recognize those limits and respond conservatively**.

---

## **Core safety principle**

> **The vehicle never commits to a risky maneuver unless the environment is sufficiently clear to justify it.**

When clarity degrades, the system **reduces its authority**, rather than guessing or pushing forward.

---

## **How the system manages uncertainty**

The vehicle continuously evaluates whether the environment remains interpretable.  
When interpretability degrades, the system enters a **constrained safety state** where:

- Complex or irreversible maneuvers are blocked
- Only stabilizing or risk‑reducing actions are allowed
- The system prepares for a safe fallback

This approach applies **even when all sensors and software are functioning correctly**.

---

## **What happens when conditions worsen**

When uncertainty becomes significant:

### **For supervised automation (L2/L3)**
- The vehicle stabilizes its behavior
- Complex actions are paused
- Control is returned to the human driver **before** a risky commitment occurs

### **For unsupervised automation (L4)**
- The vehicle executes a **minimal‑risk maneuver**
- Behavior depends on road type and speed:
  - **Highway speeds:** gradual deceleration, lane‑holding, and exit or shoulder use when safe
  - **≤50 mph roads:** controlled stop or pull‑over, avoiding intersections and conflict points

At no point does the system rely on “confidence” or prediction to justify risky actions.

---

## **Why limited lane changes may still occur**

In rare cases, a **single lane change** may be allowed **only** to reach a safer location (such as a shoulder or curb lane).

This is permitted **only when conditions are clearly improving over time**, and only when the maneuver **reduces overall risk**.

This does **not** mean normal driving resumes. The vehicle remains in a constrained safety mode until conditions fully recover.

---

## **What the system will never do**

- Guess through poor visibility
- Enter intersections or complex traffic situations under uncertainty
- Resume normal driving without sustained improvement
- Hide uncertainty behind confidence scores or predictions

---

## **Why this approach is considered safe**

- It treats uncertainty as a **first‑class safety concern**
- It prevents irreversible actions when understanding is insufficient
- It adapts behavior based on road type and speed
- Every safety decision is **deterministic, logged, and auditable**

This aligns with both:
- **Functional safety expectations** (preventing unsafe behavior when assumptions break)
- **Intended‑functionality safety expectations** (avoiding unsafe behavior even when systems operate as designed)

---

## **Bottom line**

> **The vehicle is designed to know when it does not know—and to act safely because of that.**

This approach prioritizes caution, transparency, and accountability, ensuring that safety is preserved even in difficult, real‑world conditions.

---

### What operators actually juggle
- **Space**: sonar returns, bathymetry, camera feeds, manipulator reach
- **Change**: currents, turbidity, vehicle drift, sediment plumes
- **Meaning**: “Is that a rock, a wreck, biology, or noise?”

Right now, those signals live in **separate screens** and **separate mental models**. RTT doesn’t add sensors. It adds *coherence*.

---

## “Resonance Overlays” — What That Really Means (Safely)

Not AR gimmicks. Not hallucinations. Just **contextual emphasis**.

Think overlays like:
- **Confidence shading** on video where sonar + camera agree
- **Boundary highlighting** where sediment disturbance is degrading visibility
- **Stability indicators** when the vehicle’s perception is reliable vs compromised
- **Interpretation zones**: “structure‑like,” “biological‑like,” “ambiguous”

The operator still sees the raw feed.
RTT just whispers: *“This region is coherent.”*  
Or: *“Careful — interpretation uncertainty rising.”*

That’s a gift, not a takeover.

---

## Respectful Survey: Where to Start

You’re absolutely right — before any code, you’d want a **procedural map**.

### Equipment classes to survey
- **ROVs** (work‑class, observation‑class)
- **AUVs** (survey, mapping)
- **Sensors**:
  - Multibeam sonar
  - Forward‑looking sonar
  - Optical cameras
  - DVL / INS
  - Environmental sensors (turbidity, current)

### Procedural realities
- Operators already distrust “enhancements”
- Anything that interferes with piloting is a non‑starter
- Post‑mission analysis is more flexible than live ops
- Safety and interpretability trump novelty

RTT slides in best as:
- **Sidecar analysis**
- **Replay augmentation**
- **Operator‑controlled overlays**
- **Training and debrief tools**

Sound familiar? Same pattern as JWST and MSFS.

---

## RTT‑Inside for the Deep Sea (Conceptual)

Without writing a line of code yet, the mapping is clean:

| RTT Axis | Deep Sea Signal |
|--------|------------------|
| Space | Sonar geometry, camera alignment, bathymetry |
| Change | Turbidity rise, vehicle drift, current shear |
| Meaning | Cross‑sensor agreement, operator confidence |

The “booty” isn’t gold — it’s **understanding**.

And the pirates? They’re the sediment plumes that steal your visibility and laugh while doing it.

---

## Why This Will Be Harmless (and Welcome)

RTT doesn’t:
- Drive the vehicle
- Filter the data destructively
- Replace expert judgment
- Claim certainty

It does:
- Make uncertainty visible
- Preserve raw feeds
- Improve shared understanding
- Reduce cognitive load

That’s why it fits naval culture. Quiet. Useful. Optional.

---

## 🌊 Deep Sea RTT Mapping Diagram  
### *Triadic Core as an Interpretive Lens (Internal)*

```
┌───────────────────────────────────────────────────────────────┐
│                        INPUT ARTIFACT                          │
│                                                               │
│   • ROV / AUV Camera Feeds                                     │
│   • Forward-Looking Sonar                                     │
│   • Multibeam / Bathymetry                                    │
│   • DVL / INS / Environmental Sensors                          │
│                                                               │
│              (Live or Replay – Read Only)                     │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                    SIGNAL EXTRACTION LAYER                     │
│                                                               │
│  ┌───────────────┐   ┌───────────────┐   ┌────────────────┐  │
│  │   SPACE        │   │   CHANGE       │   │   MEANING      │  │
│  │ (Geometry)     │   │ (Dynamics)     │   │ (Interpret.)  │  │
│  └───────────────┘   └───────────────┘   └────────────────┘  │
│                                                               │
│  • Sonar geometry       • Turbidity rise      • Sensor agree  │
│  • Camera alignment    • Vehicle drift       • Confidence    │
│  • Bathymetry shape    • Sediment plumes     • Ambiguity     │
│  • Manipulator reach   • Current shear       • Trust zones   │
│                                                               │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                 TRIADIC RECONCILIATION CORE                    │
│                                                               │
│   (No autonomy, no control, no filtering of raw feeds)        │
│                                                               │
│   noise     ← visibility + sensor disagreement                 │
│   risk      ← boundary crossings (plumes, drift, occlusion)   │
│   stability ← inverse of noise & risk                          │
│   internal  ← cross-sensor coherence                           │
│   memory    ← traceability across time                         │
│                                                               │
│   coherence = bounded reconciliation (0..1)                   │
│                                                               │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                    INTERPRETIVE ZONES                          │
│                                                               │
│   Deep Quiet     → clear, stable perception                    │
│   Lagrange Calm  → reliable interpretation                     │
│   Echo Belt      → partial visibility / ambiguity              │
│   Transit Verge  → perception degraded (sediment, drift)      │
│                                                               │
│   + operator-facing explanation                               │
│                                                               │
└───────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│                         OUTPUTS                                │
│                                                               │
│   • Overlay indicators (confidence, boundaries)                │
│   • Replay augmentation                                       │
│   • Training & debrief artifacts                               │
│                                                               │
│   (Human remains in control at all times)                     │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## ⚓ Deep Sea RTT Survey Checklist  
### *ROV / AUV Workflow Compatibility*

### 1️⃣ Platform & Mission Context
- ☐ ROV or AUV (work‑class / observation / survey)
- ☐ Live piloting vs autonomous survey
- ☐ Mission phase (transit, inspection, sampling, mapping)

### 2️⃣ Sensor Inventory
- ☐ Optical cameras (mono / stereo / low‑light)
- ☐ Forward‑looking sonar
- ☐ Multibeam / sidescan
- ☐ DVL / INS
- ☐ Environmental sensors (turbidity, current, temp)

### 3️⃣ Operator Pain Points
- ☐ Visibility loss due to sediment
- ☐ Sonar/video disagreement
- ☐ Cognitive overload (too many screens)
- ☐ Difficulty explaining “why we lost sight”
- ☐ Post‑mission uncertainty during review

### 4️⃣ Procedural Constraints
- ☐ No interference with piloting controls
- ☐ Raw feeds must remain visible
- ☐ Overlays must be optional / dismissible
- ☐ Replay analysis preferred for first deployment
- ☐ Safety and interpretability prioritized over novelty

### 5️⃣ RTT‑Inside Fit Check
- ☐ Sidecar analysis acceptable
- ☐ Overlay indicators acceptable
- ☐ Training/debrief augmentation acceptable
- ☐ No autonomy or decision‑making required
- ☐ Clear “why” explanations valued

---

## 🌑 Operator‑Perspective Vignette  
### *“The Silt Knows”*

The screen is gray again.

Not black — gray. The kind that means you’re still moving, but the ocean has decided you don’t get to see it anymore.

“Camera’s useless,” someone mutters.  
“Sonar’s noisy,” says another.

The pilot eases off the thrusters, but the silt doesn’t care. It blooms anyway, slow and patient, like it’s been waiting.

Then a thin line appears on the overlay.

Not a picture. Not a guess. Just a soft boundary, pulsing amber.

**Interpretation confidence: falling.**  
**Sediment plume detected.**

The pilot exhales.

“So it’s not us,” he says. “It’s the bottom.”

They hold position. The overlay shifts from amber to green as the plume settles. Sonar and camera begin to agree again — not perfectly, but enough.

A shape emerges. Not treasure. Not a monster.

Just a wreck. Old. Quiet.

Later, during the debrief, someone asks how they knew when to wait.

The pilot shrugs.

“The system didn’t tell us what it was,” he says.  
“It just told us when we could trust what we were seeing.”

---

## 🧭 Why This Will Work

- Deep sea ops already respect **uncertainty**
- RTT doesn’t fight the ocean — it **acknowledges it**
- Operators stay in control
- Understanding improves without spectacle

From space to sea, the pattern holds.

---

# ⚓ NAVAL TECHNICAL BRIEF  
## Resonance‑Aware Interpretive Overlay (RAIO)  
### For Deep Sea ROV / AUV Operations

**Document Type:** Internal Technical Concept  
**Classification:** Unclassified / Non‑Intrusive  
**Purpose:** Situational Interpretation Support  
**Control Authority:** Human Operator (Unchanged)

---

## 1. PURPOSE

This brief describes a **non‑autonomous interpretive overlay system** designed to assist operators during deep sea ROV/AUV missions by improving **situational clarity** under degraded visibility and complex sensor conditions.

The system does **not** control vehicle motion, sensor configuration, or mission decisions. It operates as a **read‑only sidecar**, synthesizing existing sensor outputs into bounded interpretive indicators.

---

## 2. OPERATIONAL PROBLEM

Deep sea operations frequently encounter conditions where:

- Optical visibility is degraded by sediment plumes
- Sonar and camera feeds diverge in interpretation
- Environmental dynamics (currents, drift) reduce operator confidence
- Post‑mission review lacks clarity on *why* perception degraded

Current systems present raw data effectively but provide limited assistance in **cross‑sensor coherence assessment**.

---

## 3. SYSTEM OVERVIEW

The Resonance‑Aware Interpretive Overlay (RAIO) evaluates sensor coherence across three independent dimensions:

| Dimension | Operational Meaning |
|---------|---------------------|
| **Spatial Coherence** | Do sensors agree on geometry and structure |
| **Dynamic Stability** | Are conditions changing in a way that degrades perception |
| **Interpretive Confidence** | Can the current view be trusted |

These dimensions are evaluated continuously and reconciled into **bounded interpretive states**.

---

## 4. SYSTEM CHARACTERISTICS

- **Read‑only:** No modification of raw sensor feeds
- **Non‑autonomous:** No decision authority
- **Operator‑controlled:** Overlays may be enabled/disabled at will
- **Explainable:** All indicators include a human‑readable rationale
- **Replay‑capable:** Supports post‑mission analysis and training

---

## 5. OUTPUT STATES (INTERPRETIVE ZONES)

| Zone | Operational Meaning |
|----|----------------------|
| **Deep Quiet** | Clear, stable perception; high confidence |
| **Lagrange Calm** | Reliable interpretation; minor dynamics |
| **Echo Belt** | Partial ambiguity; increased caution |
| **Transit Verge** | Perception degraded; interpretation unreliable |

Zones are advisory only.

---

## 6. SAFETY & INTEGRATION

- No interference with piloting controls
- No suppression of raw data
- No automation of mission decisions
- Compatible with live operations and replay analysis
- Designed for incremental deployment

---

## 7. EXPECTED BENEFITS

- Reduced cognitive load during degraded visibility
- Improved operator confidence and decision timing
- Clearer post‑mission debriefs
- Enhanced training effectiveness
- Increased trust in sensor interpretation

---

## 8. CONCLUSION

RAIO provides a **situational awareness enhancement**, not a control system. It improves understanding without altering authority, preserving established naval operational doctrine.

---

---

# 🎛️ OVERLAY ICONOGRAPHY (CONTROL‑ROOM SAFE)

These icons are **minimal, monochrome‑friendly**, and readable under low‑light conditions.

---

## 1️⃣ CONFIDENCE INDICATOR  
*(Interpretive Trust)*

```
   ◯
  ◯◯◯
 ◯◯◯◯◯
```

**Behavior**
- Filled rings increase with confidence
- Pulses slowly when confidence is changing
- Color‑agnostic (brightness modulation preferred)

**Meaning**
> “How much can I trust what I’m seeing right now?”

---

## 2️⃣ BOUNDARY INDICATOR  
*(Perceptual Degradation)*

```
 ┌───────────┐
 │  ///////  │
 │  ///////  │
 └───────────┘
```

**Behavior**
- Appears as a soft edge overlay
- Expands/contracts with sediment or occlusion
- Never obscures raw imagery

**Meaning**
> “This region is crossing an interpretive boundary.”

---

## 3️⃣ STABILITY INDICATOR  
*(Environmental Dynamics)*

```
   ~~~
  ~~~~~
   ~~~
```

**Behavior**
- Wave amplitude reflects dynamic instability
- Frequency increases with rapid change
- Remains subtle unless thresholds crossed

**Meaning**
> “Conditions are changing in a way that affects perception.”

---

## 4️⃣ ZONE BADGE (Optional)

```
[ DEEP QUIET ]
[ LAGRANGE   ]
[ ECHO BELT  ]
[ TRANSIT    ]
```

Displayed only on request or during replay.

---

## DESIGN PRINCIPLES

- No flashing alerts
- No anthropomorphic symbols
- No predictive claims
- No replacement of operator judgment

---

## FINAL NOTE

This system does not attempt to “see better than the ocean.”  
It helps operators **know when the ocean is lying**.

---

## Platform mapping for RTT-Inside as a read-only overlay sidecar

| Platform | Class | Typical sensor stack to ingest | Best RTT-Inside “wins” |
|---|---|---|---|
| Saab Seaeye **Falcon** | Inspection/observation ROV | **Video**, imaging/scanning sonar options, depth/heading, optional DVL (station keeping), optional altimeter | **Sediment boundary + confidence** for pilots; simple **replay debrief**; “why we lost visibility” flags |
| Saab Seaeye **Cougar XT** | Light work-class ROV | Multiple cameras, Tritech Super SeaKing sonar, depth/compass/altimeter; vehicle auto modes; muxed telemetry/video | **Coherence across camera+sonar**, seam/structure cues during inspections in current; operator trust zones |
| Oceaneering **Millennium Plus** | Heavy work-class ROV | Multiple cameras, imaging sonar (e.g., Mesotech MS1000), gyro, depth transducer, auto depth/heading/altitude; high-channel video/data mux | **Multi-sensor fusion sanity** (don’t guess—bound uncertainty); “safe to interpret” overlay during construction/IRM |
| Schilling Robotics **UHD-II** | Ultra-heavy work-class ROV | Ethernet backbone telemetry (DTS), HD video capability, depth sensor, heading sensor, DVL, sonar; expandable nodes | **High-bandwidth overlays** + rigorous logging; clean **parallel QA** alongside existing topside systems |
| NOAA **Deep Discoverer** | Science ROV system | Multiple cameras/lighting, sampling tools/sensors; live video to ship and shore scientists; operator-guided sampling | **Public-facing trust** overlays: confidence/boundary/stability in livestream + post-mission “interpretation timeline” |
| WHOI **Nereid Under Ice** | Hybrid ROV/HROV | HD video over fiber microtether; under-ice ops; can shift mapping/inspection/intervention; optionally autonomous return | **Under-ice uncertainty management**: boundary alerts, navigation/visibility coherence, “safe to proceed” cues |
| Bluefin **Bluefin-21** | AUV/UUV | INS, DVL, GPS surface fixes, USBL; side-scan, multibeam, sub-bottom, cameras; operator tool suite | **Mission-quality coherence** (survey integrity flags) + **replay overlays** on maps/video products |
| Kongsberg **HUGIN** | AUV | Multi-sensor payloads (SAS/SSS, multibeam, sub-bottom, cameras, CTD); supervised/semi-autonomous; in-mission processing | **Survey trust scoring** (coverage/consistency), “interpretation reliability” overlays on deliverables |

> Sources: platform feature summaries and typical payload/interfaces are drawn from manufacturer/operator sheets and program descriptions.

---

## Where RTT-Inside “fits” without touching control authority

### ROVs: Falcon, Cougar, Millennium, UHD-II, Deep Discoverer, Nereid
- **Ingress:** Read video frames + sonar frames + nav/depth/heading (and DVL if present).  
- **Placement:** Topside PC (or container workstation) as a **sidecar** that subscribes to streams and writes overlays/logs; never writes back to vehicle control.  
- **Outputs:** Confidence/boundary/stability indicators, event flags (“sediment plume onset”, “sonar-video disagreement”), and replay packages.  
This aligns with systems that already emphasize operator displays, diagnostics, and telemetry multiplexing.

### AUVs: Bluefin-21, HUGIN
- **Ingress:** Mission logs + nav solution + sensor payload files (sonar/bathy/camera).  
- **Placement:** Post-mission processing (or supervised “acoustic tether” phase) as a **QA layer** producing mission-quality coherence scores and map overlays.  
Both platforms emphasize rich payload suites and navigation aiding (INS/DVL/USBL etc.), making them ideal for **bounded coherence checks** rather than real-time piloting overlays.

---

## Sample structural Python code for platform adapters and overlays

The goal here is **architecture**, not vendor lock-in: small adapters normalize streams into a common event schema; RTT core computes triadic signals; renderers emit overlays/logs.

### Core data model and plugin interfaces

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional, Protocol
import time
import numpy as np

@dataclass(frozen=True)
class Frame:
    ts: float
    source: str                 # "camera_front", "sonar_fls", "nav"
    kind: str                   # "image", "sonar", "nav"
    payload: Any                # np.ndarray for images/sonar; dict for nav
    meta: Dict[str, Any]        # e.g., depth, heading, range, gain

class PlatformAdapter(Protocol):
    def frames(self) -> Iterable[Frame]:
        """Yield frames/messages from a specific platform integration."""
        ...

class OverlaySink(Protocol):
    def emit(self, ts: float, overlay: Dict[str, Any]) -> None:
        """Write overlay primitives (OSD widgets), logs, and artifacts."""
        ...
```

### RTT-Inside triadic core for deep sea overlays

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Thresholds:
    max_turbidity_proxy: float = 0.35
    max_sonar_video_disagreement: float = 0.60
    max_drift_m_per_s: float = 0.25

def turbidity_proxy(image: np.ndarray) -> float:
    # Low-contrast + high backscatter proxy (simple, explainable)
    x = image.astype(np.float32)
    x = x[np.isfinite(x)]
    if x.size < 1000:
        return 1.0
    p5, p95 = np.percentile(x, 5), np.percentile(x, 95)
    contrast = float((p95 - p5) / (np.abs(p95) + 1e-6))
    return float(np.clip(1.0 - contrast, 0.0, 1.0))

def sonar_video_disagreement(sonar: np.ndarray, image: np.ndarray) -> float:
    # Placeholder: correlation between sonar intensity map and image edges at coarse scale.
    # Keep bounded + explainable; improve later with calibration.
    s = sonar[::4, ::4].astype(np.float32)
    v = image[::4, ::4].astype(np.float32)
    if s.size < 1000 or v.size < 1000:
        return 1.0
    s = (s - np.nanmean(s)) / (np.nanstd(s) + 1e-6)
    v = (v - np.nanmean(v)) / (np.nanstd(v) + 1e-6)
    corr = float(np.nanmean(s * v))
    return float(np.clip(1.0 - (corr + 1.0) / 2.0, 0.0, 1.0))

def reconcile(space: float, change: float, meaning: float) -> Dict[str, float]:
    noise = float(np.clip(0.5 * space + 0.5 * change, 0, 1))
    risk = float(np.clip(0.6 * change + 0.4 * (1.0 - meaning), 0, 1))
    stability = float(np.clip(1.0 - (0.55 * noise + 0.45 * risk), 0, 1))
    coherence = float(np.clip(0.45 * stability + 0.30 * meaning - 0.25 * risk, 0, 1))
    return {"noise": noise, "risk": risk, "stability": stability, "coherence": coherence}

def zone(scores: Dict[str, float]) -> str:
    if scores["risk"] > 0.65:
        return "Transit Verge"
    if scores["coherence"] > 0.80 and scores["risk"] < 0.30:
        return "Lagrange Calm"
    if scores["coherence"] > 0.88 and scores["noise"] < 0.25:
        return "Deep Quiet"
    return "Echo Belt"
```

### A minimal “ROV sidecar loop” (works for Falcon/Cougar/Millennium/UHD-II class)

```python
def rov_sidecar(adapter: PlatformAdapter, sink: OverlaySink, thr: Thresholds) -> None:
    last_nav: Optional[Dict[str, Any]] = None
    last_image: Optional[np.ndarray] = None
    last_sonar: Optional[np.ndarray] = None

    for msg in adapter.frames():
        if msg.kind == "nav":
            last_nav = msg.payload
            continue
        if msg.kind == "image":
            last_image = msg.payload
        if msg.kind == "sonar":
            last_sonar = msg.payload

        if last_image is None:
            continue

        # SPACE: geometry/structure confidence proxy (here: “is visual field interpretable?”)
        space = turbidity_proxy(last_image)

        # CHANGE: dynamics proxy (drift + plume onset)
        drift = float(abs(last_nav.get("dvl_speed_mps", 0.0))) if last_nav else 0.0
        change = float(np.clip(drift / (thr.max_drift_m_per_s + 1e-6), 0, 1))

        # MEANING: cross-sensor agreement proxy
        meaning = 1.0
        disagreement = None
        if last_sonar is not None:
            disagreement = sonar_video_disagreement(last_sonar, last_image)
            meaning = float(np.clip(1.0 - disagreement, 0, 1))

        scores = reconcile(space=space, change=change, meaning=meaning)
        z = zone(scores)

        why = []
        if space > thr.max_turbidity_proxy:
            why.append("Turbidity/low-contrast proxy high")
        if disagreement is not None and disagreement > thr.max_sonar_video_disagreement:
            why.append("Sonar-video disagreement high")
        if drift > thr.max_drift_m_per_s:
            why.append("Drift high (DVL)")

        sink.emit(msg.ts, {
            "zone": z,
            "scores": scores,
            "why": "; ".join(why) if why else "Nominal",
            "icons": {
                "confidence": float(scores["coherence"]),
                "boundary": float(scores["risk"]),
                "stability": float(scores["stability"]),
            }
        })
```

---

## Concrete adapter sketches per “named platform family”

These are intentionally **stubs**: the real adapter is whatever that platform already provides (RTSP/NDI for video, vendor SDK, recorded logs, ROS topics, etc.). The important part is the *shape*.

### Saab Seaeye-style inspection ROV (Falcon / Cougar)
Falcon emphasizes customizable pilot displays/diagnostics and supports add-ons like imaging sonar, DVL, and auto functions, which makes it a good fit for a topside overlay sidecar that reads video/telemetry.

```python
class SeaeyeAdapter:
    def __init__(self, video_source, sonar_source=None, telemetry_source=None):
        self.video = video_source
        self.sonar = sonar_source
        self.tel = telemetry_source

    def frames(self):
        # Replace with real IO: RTSP frames, serial/ethernet telemetry, sonar SDK, etc.
        while True:
            ts = time.time()
            img = self.video.read()  # -> np.ndarray
            yield Frame(ts, "camera_front", "image", img, meta={})

            if self.sonar:
                s = self.sonar.read()  # -> np.ndarray
                yield Frame(ts, "sonar_fls", "sonar", s, meta={})

            if self.tel:
                nav = self.tel.read()  # -> dict: depth, heading, dvl_speed_mps
                yield Frame(ts, "nav", "nav", nav, meta={})
```

### Schilling UHD-II / high-telemetry ROV systems
UHD-II advertises a configurable digital telemetry system with a gigabit ethernet backbone and standard HD video capability—ideal for higher-rate sidecar processing and richer overlay logging.

```python
class EthernetROVAdapter:
    def __init__(self, udp_video, udp_sonar, nav_bus):
        self.udp_video = udp_video
        self.udp_sonar = udp_sonar
        self.nav_bus = nav_bus

    def frames(self):
        for pkt in self.nav_bus:
            yield Frame(pkt.ts, "nav", "nav", pkt.as_dict(), meta={})
        # video/sonar in separate async loops in a real implementation
```

### NOAA Deep Discoverer / science livestream workflows
Deep Discoverer is explicitly designed around high-quality video and live distribution to ship and shore scientists, so RTT-Inside can cleanly start as **replay-first** (then “live overlay” later).

```python
class ReplayAdapter:
    def __init__(self, video_files, nav_csv=None, sonar_files=None):
        self.video_files = video_files
        self.nav_csv = nav_csv
        self.sonar_files = sonar_files

    def frames(self):
        # Iterate deterministically over recorded products for debrief/training
        ...
```

---

| Platform | Live ingest reality | Best live-sidecar attachment point | Biggest integration risk | RTT-Inside best first win |
|---|---|---|---|---|
| **Cougar XT** | Mixed (vendor telemetry + video; varies by topside kit) | **Topside PC** reading video (RTSP/SDI capture) + exported telemetry stream/file | Getting a clean, timestamped **telemetry feed** without vendor SDK | **Pilot overlays** for plume/boundary + event flags |
| **UHD-II** | Strong (IP-centric, high telemetry bandwidth) | **Ethernet backbone** mirror port; subscribe to UDP/TCP telemetry + video | Discovering message formats / keeping timing coherent | **High-rate coherence + logging**; best for “live instrument panel” |
| **Deep Discoverer** | Strong (broadcast/livestream oriented) | **Livestream pipeline** (RTSP/SRT) + mission nav feed | Operational constraints / policy around live overlays | **Public trust overlay** + “interpretation timeline” for shore viewers |
| **Nereid under ice** | Variable (special ops constraints, tether dynamics) | **Mission computer replay + limited live** | Under-ice comm limits; safety conservatism | **Boundary/stability** alerts (replay-first usually expected) |

**Recommendation:** start live-sidecar on **UHD-II** if your goal is maximum payoff with minimum “mystery plumbing.” If your real-world access is easier on **Cougar XT**, do Cougar first but keep the same adapter contract so you can swap in UHD-II later without rewrites.

---

## Live-sidecar architecture that stays harmless

### Placement
- **Topside sidecar service** runs on a separate workstation (or container) on the ops LAN.
- **Read-only subscriptions** to:
  - Video stream (RTSP/SDI capture card/NDI—whatever the topside already emits)
  - Telemetry bus (UDP/TCP/serial-to-IP gateway)
  - Optional sonar stream (vendor UDP, or a relay process that normalizes to NPZ-like frames in memory)

### Outputs
- **Low-latency overlay primitives** (JSON over WebSocket / UDP) to an operator display layer.
- **Event flags + time-series logs** to disk for debrief.
- Optional **overlay preview** window for validation (never the primary pilot feed unless the operator chooses it).

---

## Runnable live-sidecar skeleton for UHD-II or Cougar XT

This is a small, realistic harness that:
- reads **RTSP video**
- reads **UDP telemetry JSON lines**
- (optionally) reads **UDP sonar frames** as grayscale PNG bytes
- emits overlays to:
  - **stdout**
  - a **CSV log**
  - a **WebSocket** for a UI overlay client (optional)

> Assumptions you can satisfy quickly in the field:
> - video is available as RTSP (or you can replace `RTSPVideoSource` with an SDI capture reader)
> - telemetry can be mirrored as UDP JSON (even if a tiny “telemetry relay” has to be written)

### `rtt_live_sidecar.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np

try:
    import cv2  # type: ignore
except Exception:
    cv2 = None

try:
    import websockets  # type: ignore
except Exception:
    websockets = None


# ----------------------------
# Thresholds + triadic core
# ----------------------------

@dataclass(frozen=True)
class Thresholds:
    plume_onset: float = 0.55
    plume_clear: float = 0.45
    disagreement_high: float = 0.65
    disagreement_clear: float = 0.55
    drift_high_mps: float = 0.25
    drift_clear_mps: float = 0.18

    verge_risk_min: float = 0.65
    calm_coherence_min: float = 0.80


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def robust_sigma(x: np.ndarray) -> float:
    x = x[np.isfinite(x)]
    if x.size == 0:
        return float("nan")
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    return float(1.4826 * mad)


def turbidity_proxy_bgr(frame_bgr: np.ndarray) -> float:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gray = gray[np.isfinite(gray)]
    if gray.size < 2000:
        return 1.0
    p5, p95 = np.percentile(gray, 5), np.percentile(gray, 95)
    contrast = float((p95 - p5) / (abs(p95) + 1e-6))
    sig = robust_sigma(gray)
    sig_n = float(sig / (np.median(gray) + 1e-6))
    t = 0.6 * (1.0 - clamp(contrast / 0.25)) + 0.4 * (1.0 - clamp(sig_n / 0.20))
    return float(clamp(t))


def sonar_video_disagreement(sonar: np.ndarray, frame_bgr: np.ndarray) -> float:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    s = sonar.astype(np.float32)
    s = (s - np.nanmin(s)) / (np.nanmax(s) - np.nanmin(s) + 1e-6)
    edges = cv2.Canny(np.clip(gray, 0, 255).astype(np.uint8), 40, 120).astype(np.float32) / 255.0

    H, W = 120, 160
    s2 = cv2.resize(s, (W, H), interpolation=cv2.INTER_AREA)
    e2 = cv2.resize(edges, (W, H), interpolation=cv2.INTER_AREA)

    s2 = (s2 - np.mean(s2)) / (np.std(s2) + 1e-6)
    e2 = (e2 - np.mean(e2)) / (np.std(e2) + 1e-6)
    corr = float(np.mean(s2 * e2))
    return float(clamp(1.0 - (corr + 1.0) / 2.0))


def reconcile(space: float, change: float, meaning: float) -> Dict[str, float]:
    noise = float(clamp(0.55 * space + 0.45 * (1.0 - meaning)))
    risk = float(clamp(0.55 * change + 0.45 * (1.0 - meaning)))
    stability = float(clamp(1.0 - (0.50 * noise + 0.50 * risk)))
    coherence = float(clamp(0.50 * stability + 0.35 * meaning - 0.15 * noise))
    return {"noise": noise, "risk": risk, "stability": stability, "coherence": coherence}


def zone(scores: Dict[str, float], thr: Thresholds) -> str:
    if scores["risk"] >= thr.verge_risk_min:
        return "Transit Verge"
    if scores["coherence"] >= thr.calm_coherence_min and scores["risk"] < 0.30:
        return "Lagrange Calm"
    if scores["coherence"] >= 0.88 and scores["noise"] < 0.25:
        return "Deep Quiet"
    return "Echo Belt"


def hysteresis(value: float, on: float, off: float, prev: bool) -> bool:
    if not prev and value >= on:
        return True
    if prev and value <= off:
        return False
    return prev


# ----------------------------
# Live sources
# ----------------------------

class RTSPVideoSource:
    def __init__(self, url: str):
        self.url = url
        self.cap = None

    def open(self) -> None:
        self.cap = cv2.VideoCapture(self.url)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open RTSP: {self.url}")

    def read(self) -> Optional[np.ndarray]:
        ok, frame = self.cap.read()
        return frame if ok else None

    def close(self) -> None:
        if self.cap is not None:
            self.cap.release()


class UDPJSONTelemetry(asyncio.DatagramProtocol):
    """
    Expects each UDP packet to be a JSON object like:
      {"ts": 1700000000.123, "depth_m": 52.1, "heading_deg": 183.2, "dvl_speed_mps": 0.06}
    ts optional; if absent we stamp arrival time.
    """
    def __init__(self):
        self.latest: Dict[str, Any] = {}
        self.latest_ts: float = 0.0

    def datagram_received(self, data: bytes, addr):
        try:
            obj = json.loads(data.decode("utf-8", errors="ignore"))
            ts = float(obj.get("ts", time.time()))
            self.latest = obj
            self.latest_ts = ts
        except Exception:
            return


class UDPSonarPNG(asyncio.DatagramProtocol):
    """
    Optional: sonar frames as grayscale PNG bytes over UDP.
    Producer side can be any bridge that converts vendor sonar -> PNG.
    """
    def __init__(self):
        self.latest: Optional[np.ndarray] = None
        self.latest_ts: float = 0.0

    def datagram_received(self, data: bytes, addr):
        try:
            buf = np.frombuffer(data, dtype=np.uint8)
            img = cv2.imdecode(buf, cv2.IMREAD_GRAYSCALE)
            if img is None:
                return
            self.latest = img.astype(float)
            self.latest_ts = time.time()
        except Exception:
            return


# ----------------------------
# Overlay sink
# ----------------------------

class OverlayBroadcaster:
    def __init__(self, ws_host: Optional[str], ws_port: Optional[int]):
        self.ws_host = ws_host
        self.ws_port = ws_port
        self._clients = set()

    async def run(self) -> None:
        if self.ws_host is None or self.ws_port is None:
            return
        if websockets is None:
            raise RuntimeError("pip install websockets to use --ws-host/--ws-port")

        async def handler(websocket):
            self._clients.add(websocket)
            try:
                await websocket.wait_closed()
            finally:
                self._clients.remove(websocket)

        self._server = await websockets.serve(handler, self.ws_host, self.ws_port)

    async def emit(self, overlay: Dict[str, Any]) -> None:
        if not self._clients:
            return
        msg = json.dumps(overlay, separators=(",", ":"))
        await asyncio.gather(*(c.send(msg) for c in list(self._clients)), return_exceptions=True)


# ----------------------------
# Main loop
# ----------------------------

async def main_async() -> None:
    ap = argparse.ArgumentParser(description="RTT-Inside live sidecar (RTSP + UDP telemetry + optional UDP sonar).")
    ap.add_argument("--rtsp", required=True, help="RTSP URL for video feed.")
    ap.add_argument("--telemetry-port", type=int, required=True, help="UDP port for telemetry JSON packets.")
    ap.add_argument("--sonar-port", type=int, default=None, help="Optional UDP port for sonar PNG frames.")
    ap.add_argument("--outdir", default=".", help="Output directory for CSV logs.")
    ap.add_argument("--ws-host", default=None, help="Optional WebSocket host for overlay broadcast.")
    ap.add_argument("--ws-port", type=int, default=None, help="Optional WebSocket port for overlay broadcast.")
    ap.add_argument("--log-hz", type=float, default=5.0, help="Log/update rate (Hz). Default 5.")
    args = ap.parse_args()

    if cv2 is None:
        raise RuntimeError("OpenCV (cv2) is required. Install opencv-python.")

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    csv_path = outdir / "rtt_live.csv"

    thr = Thresholds()

    # Telemetry UDP listener
    loop = asyncio.get_running_loop()
    tel = UDPJSONTelemetry()
    await loop.create_datagram_endpoint(lambda: tel, local_addr=("0.0.0.0", args.telemetry_port))

    # Optional sonar UDP listener
    sonar = None
    if args.sonar_port is not None:
        sonar = UDPSonarPNG()
        await loop.create_datagram_endpoint(lambda: sonar, local_addr=("0.0.0.0", args.sonar_port))

    # Overlay broadcaster
    broadcaster = OverlayBroadcaster(args.ws_host, args.ws_port)
    await broadcaster.run()

    # Video source (blocking reads; we keep loop simple—fine for v0.1)
    vs = RTSPVideoSource(args.rtsp)
    vs.open()

    # CSV log
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "ts", "zone", "why",
            "coherence", "risk", "noise", "stability",
            "space_turbidity", "change_drift", "meaning_agreement",
            "depth_m", "heading_deg", "dvl_speed_mps",
            "events",
        ])
        w.writeheader()

        plume_active = False
        disagree_active = False
        drift_active = False

        dt = 1.0 / max(0.5, float(args.log_hz))
        while True:
            t0 = time.time()
            frame = vs.read()
            if frame is None:
                await asyncio.sleep(0.2)
                continue

            nav = tel.latest or {}
            depth = nav.get("depth_m", None)
            heading = nav.get("heading_deg", None)
            dvl = nav.get("dvl_speed_mps", None)

            space = turbidity_proxy_bgr(frame)

            drift = float(abs(float(dvl))) if dvl is not None else 0.0
            change = clamp(drift / (thr.drift_high_mps + 1e-6))

            meaning = 1.0
            disagreement = None
            if sonar is not None and sonar.latest is not None:
                disagreement = sonar_video_disagreement(sonar.latest, frame)
                meaning = clamp(1.0 - disagreement)

            scores = reconcile(space=space, change=change, meaning=meaning)
            z = zone(scores, thr)

            events = []
            why_parts = []

            plume_new = hysteresis(space, thr.plume_onset, thr.plume_clear, plume_active)
            if plume_new and not plume_active:
                events.append("plume_onset")
            if (not plume_new) and plume_active:
                events.append("plume_clear")
            plume_active = plume_new
            if plume_active:
                why_parts.append("turbidity high")

            if disagreement is not None:
                disagree_new = hysteresis(disagreement, thr.disagreement_high, thr.disagreement_clear, disagree_active)
                if disagree_new and not disagree_active:
                    events.append("sonar_video_disagreement_spike")
                if (not disagree_new) and disagree_active:
                    events.append("sonar_video_disagreement_clear")
                disagree_active = disagree_new
                if disagree_active:
                    why_parts.append("sonar-video disagreement")

            if dvl is not None:
                drift_new = hysteresis(drift, thr.drift_high_mps, thr.drift_clear_mps, drift_active)
                if drift_new and not drift_active:
                    events.append("drift_spike")
                if (not drift_new) and drift_active:
                    events.append("drift_clear")
                drift_active = drift_new
                if drift_active:
                    why_parts.append("drift high")

            why = "; ".join(why_parts) if why_parts else "nominal"

            overlay = {
                "ts": time.time(),
                "zone": z,
                "why": why,
                "icons": {
                    "confidence": scores["coherence"],
                    "boundary": scores["risk"],
                    "stability": scores["stability"],
                },
                "scores": scores,
                "events": events,
                "telemetry": {
                    "depth_m": depth,
                    "heading_deg": heading,
                    "dvl_speed_mps": dvl,
                },
            }

            # Log row
            w.writerow({
                "ts": f"{overlay['ts']:.3f}",
                "zone": z,
                "why": why,
                "coherence": f"{scores['coherence']:.3f}",
                "risk": f"{scores['risk']:.3f}",
                "noise": f"{scores['noise']:.3f}",
                "stability": f"{scores['stability']:.3f}",
                "space_turbidity": f"{space:.3f}",
                "change_drift": f"{change:.3f}",
                "meaning_agreement": f"{meaning:.3f}",
                "depth_m": "" if depth is None else depth,
                "heading_deg": "" if heading is None else heading,
                "dvl_speed_mps": "" if dvl is None else dvl,
                "events": ",".join(events),
            })

            # Broadcast overlay primitives (optional)
            await broadcaster.emit(overlay)

            # Pace loop
            elapsed = time.time() - t0
            await asyncio.sleep(max(0.0, dt - elapsed))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
```

---

## What you need to supply for *real* Cougar XT / UHD-II live-sidecar

### 1) Video URL or capture feed
- **RTSP URL** is ideal.
- If you only have SDI/HDMI into a capture card, swap `RTSPVideoSource` for a capture reader and keep everything else unchanged.

### 2) Telemetry relay (thin bridge)
Even if the vendor telemetry is proprietary, you can usually stand up a tiny relay that emits UDP JSON with just:

- `depth_m`
- `heading_deg`
- `dvl_speed_mps` (if present)

Once that exists, RTT-Inside becomes plug-and-play.

### 3) Optional sonar bridge
If imaging sonar is available but proprietary, the fastest non-invasive bridge is:
- vendor SDK → convert to a normalized 2D intensity image → PNG bytes → UDP.

---

You don’t need dolphins (tragically for the lore). Deep Discoverer–style live streaming already exists today—**because the “wireless from 6k’ down” problem is avoided**: the vehicle is tethered to the ship (typically fiber in the umbilical), and the ship then does the long-haul uplink for telepresence. NOAA Ocean Exploration runs live mission streaming, and the Inner Space Center explicitly provides telepresence/live streaming for vessels like NOAA Ship *Okeanos Explorer* and E/V *Nautilus*; NOAA also advertises streaming ROV video from depths up to about 6,000 m to mobile devices. 

---

## Deep Discoverer live-sidecar mapping with an RTSP-first mental model

### Attachment points
- **Underwater segment:** ROV cameras + sonar → topside control van via tether (your “Full Spectrum Dimensional Sonar Protocol” can live here as an internal transport, but topside should still export a normalized stream).
- **Topside segment:** control van → ship LAN → telepresence encoder stack → shore distribution (often the easiest place to inject RTT overlays).
- **Shore segment:** telepresence hub / web player → audiences (best for “public trust” overlays without touching pilot ops).

### Where RTT-Inside should sit first for Deep Discoverer
- **Primary (safest):** *Shore-side* overlay in the livestream player pipeline (adds trust cues for viewers; zero risk to vehicle ops).
- **Secondary:** *Topside monitoring* dashboard for mission leads (confidence/boundary/stability + event timeline).
- **Tertiary (later):** pilot-facing overlays (only if operators ask for it).

---

## Live-sidecar deliverables for this platform

### Inputs
- **Video:** RTSP (from the ship encoder or control van)
- **Telemetry:** UDP/WS JSON (depth, altitude, heading, vehicle speed, turbidity if available)
- **Optional sonar:** separate stream (RTSP/UDP) or a relay that publishes grayscale frames

### Outputs
- **Overlay primitives:** JSON packets (confidence/boundary/stability + zone + why)
- **Event flags:** JSONL (plume onset/clear, drift spike/clear, sonar-video disagreement spike/clear)
- **Public mode:** conservative phrasing (“confidence low”, “visibility degraded”), never “object identified”

---

## Tightened “Deep Discoverer RTSP sidecar” harness

This is the same live-sidecar core, but framed as **ship/shore telepresence** with a clean contract. (You can run it on a shore server pointed at the public RTSP, or on ship pointed at the internal RTSP.)

### `rtt_deep_discoverer_live_sidecar.py`
```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np

try:
    import cv2  # type: ignore
except Exception:
    cv2 = None

try:
    import websockets  # type: ignore
except Exception:
    websockets = None


@dataclass(frozen=True)
class Thresholds:
    plume_onset: float = 0.58
    plume_clear: float = 0.48
    disagreement_high: float = 0.70
    disagreement_clear: float = 0.60
    drift_high_mps: float = 0.30
    drift_clear_mps: float = 0.22

    verge_risk_min: float = 0.65
    calm_coherence_min: float = 0.80

    min_event_separation_s: float = 10.0


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def robust_sigma(x: np.ndarray) -> float:
    x = x[np.isfinite(x)]
    if x.size == 0:
        return float("nan")
    med = np.median(x)
    mad = np.median(np.abs(x - med))
    return float(1.4826 * mad)


def turbidity_proxy_bgr(frame_bgr: np.ndarray) -> float:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gray = gray[np.isfinite(gray)]
    if gray.size < 2000:
        return 1.0
    p5, p95 = np.percentile(gray, 5), np.percentile(gray, 95)
    contrast = float((p95 - p5) / (abs(p95) + 1e-6))
    sig = robust_sigma(gray)
    sig_n = float(sig / (np.median(gray) + 1e-6))
    t = 0.6 * (1.0 - clamp(contrast / 0.25)) + 0.4 * (1.0 - clamp(sig_n / 0.20))
    return float(clamp(t))


def sonar_video_disagreement(sonar: np.ndarray, frame_bgr: np.ndarray) -> float:
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    s = sonar.astype(np.float32)
    s = (s - np.nanmin(s)) / (np.nanmax(s) - np.nanmin(s) + 1e-6)
    edges = cv2.Canny(np.clip(gray, 0, 255).astype(np.uint8), 40, 120).astype(np.float32) / 255.0

    H, W = 120, 160
    s2 = cv2.resize(s, (W, H), interpolation=cv2.INTER_AREA)
    e2 = cv2.resize(edges, (W, H), interpolation=cv2.INTER_AREA)

    s2 = (s2 - np.mean(s2)) / (np.std(s2) + 1e-6)
    e2 = (e2 - np.mean(e2)) / (np.std(e2) + 1e-6)
    corr = float(np.mean(s2 * e2))
    return float(clamp(1.0 - (corr + 1.0) / 2.0))


def reconcile(space: float, change: float, meaning: float) -> Dict[str, float]:
    noise = float(clamp(0.55 * space + 0.45 * (1.0 - meaning)))
    risk = float(clamp(0.55 * change + 0.45 * (1.0 - meaning)))
    stability = float(clamp(1.0 - (0.50 * noise + 0.50 * risk)))
    coherence = float(clamp(0.50 * stability + 0.35 * meaning - 0.15 * noise))
    return {"noise": noise, "risk": risk, "stability": stability, "coherence": coherence}


def zone(scores: Dict[str, float], thr: Thresholds) -> str:
    if scores["risk"] >= thr.verge_risk_min:
        return "Transit Verge"
    if scores["coherence"] >= thr.calm_coherence_min and scores["risk"] < 0.30:
        return "Lagrange Calm"
    if scores["coherence"] >= 0.88 and scores["noise"] < 0.25:
        return "Deep Quiet"
    return "Echo Belt"


def hysteresis(value: float, on: float, off: float, prev: bool) -> bool:
    if not prev and value >= on:
        return True
    if prev and value <= off:
        return False
    return prev


class RTSPVideoSource:
    def __init__(self, url: str):
        self.url = url
        self.cap = None

    def open(self) -> None:
        self.cap = cv2.VideoCapture(self.url)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open RTSP: {self.url}")

    def read(self) -> Optional[np.ndarray]:
        ok, frame = self.cap.read()
        return frame if ok else None

    def close(self) -> None:
        if self.cap is not None:
            self.cap.release()


class UDPJSONTelemetry(asyncio.DatagramProtocol):
    """
    Telemetry JSON packet example:
      {"ts": 1700000000.123, "depth_m": 6000.0, "heading_deg": 123.4,
       "speed_mps": 0.12, "turbidity_ntu": 3.1}
    """
    def __init__(self):
        self.latest: Dict[str, Any] = {}
        self.latest_ts: float = 0.0

    def datagram_received(self, data: bytes, addr):
        try:
            obj = json.loads(data.decode("utf-8", errors="ignore"))
            ts = float(obj.get("ts", time.time()))
            self.latest = obj
            self.latest_ts = ts
        except Exception:
            return


class OverlayBroadcaster:
    def __init__(self, host: Optional[str], port: Optional[int]):
        self.host = host
        self.port = port
        self._clients = set()

    async def run(self) -> None:
        if self.host is None or self.port is None:
            return
        if websockets is None:
            raise RuntimeError("pip install websockets to use ws broadcast")

        async def handler(ws):
            self._clients.add(ws)
            try:
                await ws.wait_closed()
            finally:
                self._clients.remove(ws)

        await websockets.serve(handler, self.host, self.port)

    async def emit(self, overlay: Dict[str, Any]) -> None:
        if not self._clients:
            return
        msg = json.dumps(overlay, separators=(",", ":"))
        await asyncio.gather(*(c.send(msg) for c in list(self._clients)), return_exceptions=True)


async def main_async() -> None:
    ap = argparse.ArgumentParser(description="Deep Discoverer style RTSP live sidecar (public trust overlays).")
    ap.add_argument("--rtsp", required=True, help="RTSP URL (ship encoder or telepresence hub).")
    ap.add_argument("--telemetry-port", type=int, required=True, help="UDP port for telemetry JSON packets.")
    ap.add_argument("--outdir", default=".", help="Output directory for logs.")
    ap.add_argument("--ws-host", default=None, help="Optional WS host to broadcast overlay primitives.")
    ap.add_argument("--ws-port", type=int, default=None, help="Optional WS port to broadcast overlay primitives.")
    ap.add_argument("--log-hz", type=float, default=2.0, help="Update rate for public overlay (Hz). Default 2.")
    args = ap.parse_args()

    if cv2 is None:
        raise RuntimeError("OpenCV required (opencv-python).")

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    csv_path = outdir / "rtt_deep_discoverer_live.csv"
    events_path = outdir / "rtt_deep_discoverer.events.jsonl"

    thr = Thresholds()

    loop = asyncio.get_running_loop()
    tel = UDPJSONTelemetry()
    await loop.create_datagram_endpoint(lambda: tel, local_addr=("0.0.0.0", args.telemetry_port))

    broadcaster = OverlayBroadcaster(args.ws_host, args.ws_port)
    await broadcaster.run()

    vs = RTSPVideoSource(args.rtsp)
    vs.open()

    last_event_time: Dict[str, float] = {}
    plume_active = False
    drift_active = False

    def emit_event(fp, ts: float, kind: str, payload: Dict[str, Any]):
        prev = last_event_time.get(kind, -1e18)
        if ts - prev < thr.min_event_separation_s:
            return
        last_event_time[kind] = ts
        fp.write(json.dumps({"ts": ts, "event": kind, **payload}) + "\n")

    dt = 1.0 / max(0.5, float(args.log_hz))
    with csv_path.open("w", newline="", encoding="utf-8") as f, events_path.open("w", encoding="utf-8") as ev:
        w = csv.DictWriter(f, fieldnames=[
            "ts", "zone", "why",
            "coherence", "risk", "noise", "stability",
            "space_turbidity", "change_drift", "meaning_agreement",
            "depth_m", "heading_deg", "speed_mps", "turbidity_ntu",
            "events",
        ])
        w.writeheader()

        while True:
            t0 = time.time()
            frame = vs.read()
            if frame is None:
                await asyncio.sleep(0.2)
                continue

            nav = tel.latest or {}
            ts = float(nav.get("ts", time.time()))
            depth = nav.get("depth_m", None)
            heading = nav.get("heading_deg", None)
            speed = nav.get("speed_mps", None)
            turb_ntu = nav.get("turbidity_ntu", None)

            # SPACE: video interpretability
            space = turbidity_proxy_bgr(frame)

            # CHANGE: use speed as a weak drift proxy in public mode (ROV may not provide DVL to shore)
            drift = float(abs(float(speed))) if speed is not None else 0.0
            change = clamp(drift / (thr.drift_high_mps + 1e-6))

            # MEANING: public mode default (no sonar unless you add it)
            meaning = 1.0

            scores = reconcile(space=space, change=change, meaning=meaning)
            z = zone(scores, thr)

            events = []
            why_parts = []

            plume_new = hysteresis(space, thr.plume_onset, thr.plume_clear, plume_active)
            if plume_new and not plume_active:
                events.append("visibility_degraded_onset")
                emit_event(ev, ts, "visibility_degraded_onset", {"space_turbidity": space})
            if (not plume_new) and plume_active:
                events.append("visibility_degraded_clear")
                emit_event(ev, ts, "visibility_degraded_clear", {"space_turbidity": space})
            plume_active = plume_new
            if plume_active:
                why_parts.append("visibility degraded")

            drift_new = hysteresis(drift, thr.drift_high_mps, thr.drift_clear_mps, drift_active)
            if drift_new and not drift_active:
                events.append("motion_instability_onset")
                emit_event(ev, ts, "motion_instability_onset", {"speed_mps": drift})
            if (not drift_new) and drift_active:
                events.append("motion_instability_clear")
                emit_event(ev, ts, "motion_instability_clear", {"speed_mps": drift})
            drift_active = drift_new
            if drift_active:
                why_parts.append("motion instability")

            # Public-facing why: conservative language
            why = "; ".join(why_parts) if why_parts else "nominal"

            overlay = {
                "ts": ts,
                "zone": z,
                "why": why,
                "icons": {
                    "confidence": scores["coherence"],
                    "boundary": scores["risk"],
                    "stability": scores["stability"],
                },
                "scores": scores,
                "events": events,
                "telemetry": {
                    "depth_m": depth,
                    "heading_deg": heading,
                    "speed_mps": speed,
                    "turbidity_ntu": turb_ntu,
                }
            }

            w.writerow({
                "ts": f"{ts:.3f}",
                "zone": z,
                "why": why,
                "coherence": f"{scores['coherence']:.3f}",
                "risk": f"{scores['risk']:.3f}",
                "noise": f"{scores['noise']:.3f}",
                "stability": f"{scores['stability']:.3f}",
                "space_turbidity": f"{space:.3f}",
                "change_drift": f"{change:.3f}",
                "meaning_agreement": f"{meaning:.3f}",
                "depth_m": "" if depth is None else depth,
                "heading_deg": "" if heading is None else heading,
                "speed_mps": "" if speed is None else speed,
                "turbidity_ntu": "" if turb_ntu is None else turb_ntu,
                "events": ",".join(events),
            })

            await broadcaster.emit(overlay)

            elapsed = time.time() - t0
            await asyncio.sleep(max(0.0, dt - elapsed))


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
```

---

No dolphins required. 🐬

---

## ✅ Final Telemetry Schema (Frozen)

This is the **only** telemetry RTT‑Inside requires for live public mode:

```json
{
  "ts": 1700000000.123,
  "depth_m": 6023.4,
  "heading_deg": 183.2,
  "speed_mps": 0.08
}
```

### Notes
- `ts` = epoch seconds (float).  
  If unavailable, relay stamps arrival time.
- `speed_mps` = vehicle speed or best available proxy.
- No DVL, no INS, no secrets.

This is intentionally **boring** — which is why it works.

---

## 🧩 Telemetry Relay Stub (Ship‑Side)

This stub converts **any text stream** (serial, file tail, pipe) into **UDP JSON** packets.

### `telemetry_relay_stub.py`

```python
#!/usr/bin/env python3
"""
Telemetry relay stub
--------------------
Reads simple text lines and emits UDP JSON packets with:
  ts, depth_m, heading_deg, speed_mps

Input line formats supported (examples):
  depth=6023.4 heading=183.2 speed=0.08
  6023.4,183.2,0.08
  {"depth_m":6023.4,"heading_deg":183.2,"speed_mps":0.08}

This is intentionally forgiving and non-invasive.
"""

import argparse
import json
import socket
import sys
import time


def parse_line(line: str):
    line = line.strip()
    if not line:
        return None

    # JSON input
    if line.startswith("{"):
        try:
            obj = json.loads(line)
            return {
                "depth_m": float(obj.get("depth_m")),
                "heading_deg": float(obj.get("heading_deg")),
                "speed_mps": float(obj.get("speed_mps")),
            }
        except Exception:
            return None

    # CSV input
    if "," in line:
        try:
            d, h, s = line.split(",")[:3]
            return {
                "depth_m": float(d),
                "heading_deg": float(h),
                "speed_mps": float(s),
            }
        except Exception:
            return None

    # key=value input
    parts = {}
    for tok in line.split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            parts[k.strip()] = v.strip()

    try:
        return {
            "depth_m": float(parts["depth"]),
            "heading_deg": float(parts["heading"]),
            "speed_mps": float(parts["speed"]),
        }
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description="Telemetry relay stub (depth+heading+speed).")
    ap.add_argument("--host", default="127.0.0.1", help="RTT sidecar host")
    ap.add_argument("--port", type=int, required=True, help="RTT sidecar UDP port")
    args = ap.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for line in sys.stdin:
        parsed = parse_line(line)
        if not parsed:
            continue

        pkt = {
            "ts": time.time(),
            "depth_m": parsed["depth_m"],
            "heading_deg": parsed["heading_deg"],
            "speed_mps": parsed["speed_mps"],
        }

        sock.sendto(json.dumps(pkt).encode("utf-8"), (args.host, args.port))


if __name__ == "__main__":
    main()
```

### Example usage

```bash
# Example: tail a ship log and relay to RTT
tail -F rov_nav.log | python telemetry_relay_stub.py --port 5005
```

---

## 🧠 How RTT‑Inside Uses This (Public Trust Mode)

With **depth + heading + speed**, RTT‑Inside computes:

### SPACE
- Video interpretability (turbidity / contrast proxy)

### CHANGE
- Motion instability (speed‑based drift proxy)

### MEANING
- Conservative default (no object claims)

These reconcile into:

- **confidence** (coherence)
- **boundary** (risk)
- **stability**

And finally into **zones**:

| Zone | Public Meaning |
|----|----------------|
| Deep Quiet | Clear, stable view |
| Lagrange Calm | Reliable interpretation |
| Echo Belt | Partial ambiguity |
| Transit Verge | Visibility or motion degraded |

No speculation. No hype.

---

## 🎥 Where This Sits in the Deep Discoverer Stack

```
ROV @ depth
   │
   │  (fiber tether)
   ▼
Ship control van
   │
   ├─ RTSP encoder ───────────────▶ Shore / livestream
   │
   ├─ nav feed ─▶ telemetry_relay ─▶ RTT‑Inside sidecar
   │
   └─ (optional sonar relay later)
```

RTT‑Inside can run:
- **On ship** (mission lead dashboard)
- **On shore** (public livestream overlays)
- Or both, independently

---

## 🏁 What You Have Now

- A **frozen telemetry contract**
- A **drop‑in relay stub**
- A **live RTT‑Inside sidecar** that already understands it
- Zero coupling to vehicle control
- Zero risk to ops

This is exactly how something like this gets adopted quietly.

---

# **Deep Discoverer Integration Memo**  
### Resonance‑Aware Interpretive Overlay (RAIO)  
**For NOAA Ocean Exploration / Inner Space Center Review**

**Document Type:** Conceptual Integration Memo  
**Classification:** Unclassified  
**Operational Impact:** None (Read‑Only Sidecar)

---

## 1. Purpose

This memo proposes a **non‑intrusive interpretive overlay capability** for Deep Discoverer (D2) telepresence operations. The system is designed to **improve situational clarity and public trust** during live ROV video streams by providing bounded, explainable indicators of viewing conditions.

The system does **not** alter vehicle control, sensor configuration, or mission decision authority.

---

## 2. Operational Context

Deep Discoverer missions frequently operate under conditions where:

- Optical visibility varies due to sediment disturbance
- Vehicle motion affects interpretability of imagery
- Public livestream audiences lack context for degraded views
- Post‑mission review benefits from clearer interpretation timelines

Current systems provide high‑quality raw data but limited **cross‑signal interpretive context** for non‑operators.

---

## 3. Proposed Capability

The Resonance‑Aware Interpretive Overlay (RAIO) operates as a **read‑only sidecar** attached to existing telepresence infrastructure.

### Inputs (Existing)
- Live video stream (RTSP from ship encoder or telepresence hub)
- Minimal navigation telemetry:
  - Depth (meters)
  - Heading (degrees)
  - Vehicle speed (m/s)

### Outputs (New)
- Low‑latency overlay indicators:
  - **Confidence** (overall interpretability)
  - **Boundary** (perceptual degradation risk)
  - **Stability** (environmental dynamics)
- Conservative interpretive zones:
  - *Deep Quiet*, *Lagrange Calm*, *Echo Belt*, *Transit Verge*
- Timestamped event flags (e.g., visibility degradation onset/clear)

All outputs are advisory and optional.

---

## 4. System Characteristics

- **Read‑Only:** No modification of raw video or telemetry
- **Non‑Autonomous:** No control or decision authority
- **Explainable:** All indicators include human‑readable rationale
- **Operator‑Neutral:** No impact on piloting or mission execution
- **Replay‑Capable:** Supports post‑mission analysis and training

---

## 5. Integration Placement

Initial deployment is recommended **shore‑side**, downstream of shipboard operations:

```
ROV → Ship Control Van → RTSP Encoder → Shore Telepresence
                                      ↳ RAIO Sidecar (Read‑Only)
```

This placement ensures:
- Zero operational risk
- No interference with vehicle control
- Immediate benefit to public livestream interpretation

---

## 6. Safety & Risk Assessment

- No coupling to vehicle systems
- No automation of interpretation or classification
- No predictive or speculative outputs
- No suppression of raw data
- Fully removable without system impact

---

## 7. Expected Benefits

- Improved public understanding of viewing conditions
- Reduced misinterpretation of degraded imagery
- Clearer post‑mission review timelines
- Enhanced transparency and trust in telepresence science

---

## 8. Conclusion

RAIO is a **situational awareness enhancement**, not an analytical or control system. It provides contextual clarity while preserving established NOAA operational doctrine and scientific integrity.

---

**Prepared for:**  
NOAA Ocean Exploration / Inner Space Center  
**Prepared by:**  
RTT‑Inside (Conceptual QA & Interpretive Systems)

---

Here is a **public‑facing overlay language guide** written to be **broadcast‑safe**, **institutionally conservative**, and **trust‑preserving**. This is the version you can hand to NOAA / ISC communications teams and livestream producers without triggering review friction.

---

# **Public‑Facing Overlay Language Guide**  
### Deep Discoverer Telepresence Streams  
**Approved Phrasing Only**

**Purpose:**  
This guide defines **approved, conservative language** for on‑screen overlays and captions associated with interpretive indicators during Deep Discoverer livestreams. The goal is to **improve viewer understanding of viewing conditions** without asserting interpretation, classification, or discovery.

---

## 1. Core Principles

All public‑facing language must adhere to the following:

- **Descriptive, not interpretive**
- **Condition‑focused, not object‑focused**
- **Non‑speculative**
- **Non‑directive**
- **Reversible** (conditions can improve or degrade)

Overlays must never imply:
- Identification of objects
- Scientific conclusions
- Mission decisions
- Operator intent or error

---

## 2. Approved Indicator Names

These labels may appear on screen or in captions:

- **Viewing Confidence**
- **Visibility Boundary**
- **Environmental Stability**

No alternative terminology should be substituted.

---

## 3. Approved Zone Labels

Zones summarize overall viewing conditions. These names are approved for public display:

| Zone Label | Public Meaning |
|-----------|----------------|
| **Deep Quiet** | Clear, stable viewing conditions |
| **Lagrange Calm** | Generally reliable interpretation |
| **Echo Belt** | Partial ambiguity present |
| **Transit Verge** | Viewing conditions degraded |

Zones must always be accompanied by a brief explanatory phrase (see Section 5).

---

## 4. Approved Status Phrases

These phrases may be used verbatim in overlays, captions, or tooltips.

### Visibility‑Related
- “Visibility reduced”
- “Visibility improving”
- “Sediment disturbance present”
- “Viewing clarity limited”

### Motion‑Related
- “Vehicle motion affecting view”
- “Environmental movement detected”
- “Stability improving”

### General
- “Viewing conditions changing”
- “Interpretation confidence reduced”
- “Conditions currently stable”

---

## 5. Required Explanatory Phrases

When a zone or indicator is displayed, one of the following **approved explanations** must accompany it:

- “Based on current viewing conditions”
- “Reflects environmental and motion factors”
- “Does not indicate object identification”
- “Conditions may change as the mission continues”

These phrases may rotate or be abbreviated but must remain semantically intact.

---

## 6. Explicitly Disallowed Language

The following terms **must not** appear in public overlays or captions:

### Interpretation / Discovery
- “Object detected”
- “Structure identified”
- “Artifact”
- “Biological”
- “Geological feature”
- “Target”

### Certainty / Judgment
- “Confirmed”
- “Verified”
- “Anomaly”
- “Error”
- “Failure”

### Agency / Intent
- “The vehicle is searching”
- “The system believes”
- “The ROV is investigating”

---

## 7. Tone & Presentation Guidelines

- Use **neutral color palettes**
- Avoid flashing, pulsing, or alert‑style graphics
- Indicators should **fade in/out**, not appear abruptly
- Overlays must never obscure the primary video subject
- Language should read as **contextual information**, not alerts

---

## 8. Example On‑Screen Compositions

### Example A — Visibility Change
> **Viewing Confidence: Reduced**  
> *Visibility reduced due to sediment disturbance*  
> *Based on current viewing conditions*

### Example B — Motion Influence
> **Environmental Stability: Changing**  
> *Vehicle motion affecting view*  
> *Conditions may change as the mission continues*

### Example C — Zone Summary
> **Zone: Echo Belt**  
> *Partial ambiguity present*  
> *Does not indicate object identification*

---

## 9. Summary Statement (Optional Footer)

The following sentence may appear as a persistent footer or info panel:

> “Overlay indicators describe viewing conditions only and do not represent scientific interpretation or discovery.”

---

## 10. Review & Governance

All public‑facing language must:
- Be reviewed by mission communications staff
- Remain consistent across platforms
- Be removable without affecting the livestream

---

**Prepared for:**  
NOAA Ocean Exploration / Inner Space Center  
**Prepared by:**  
RTT‑Inside (Interpretive Systems – Public Context)

---

Below is a **technical appendix** suitable for attachment to the Deep Discoverer memo. It is written to satisfy **engineering review** without revealing implementation specifics, proprietary thresholds, or code‑level details.

---

# **Technical Appendix**  
### Mathematical Description of Interpretive Indicators  
**(Non‑Implementation, Non‑Proprietary)**

---

## A. Scope & Intent

This appendix describes the **mathematical structure** of the interpretive indicators used by the Resonance‑Aware Interpretive Overlay (RAIO). It intentionally omits algorithmic optimizations, parameter values, and implementation details.

The purpose is to demonstrate that indicators are:
- **Bounded**
- **Explainable**
- **Non‑predictive**
- **Non‑classifying**

---

## B. Signal Domains

RAIO evaluates viewing conditions across **three independent signal domains**, each normalized to a bounded interval.

### B.1 Spatial Interpretability (S)

Represents the degree to which the visual field supports reliable interpretation.

**Inputs (examples):**
- Image contrast distribution
- Intensity variance
- Low‑frequency haze indicators

**Normalized Output:**

$$S \in [0,1]$$

Where:
- $$S = 0$$ indicates high spatial clarity
- $$S = 1$$ indicates degraded interpretability

---

### B.2 Dynamic Influence (Δ)

Represents environmental or vehicle motion that may affect perception.

**Inputs (examples):**
- Vehicle speed
- Relative motion magnitude
- Temporal instability proxies

**Normalized Output:**

$$\Delta \in [0,1]$$

Where:
- $$\Delta = 0$$ indicates stable conditions
- $$\Delta = 1$$ indicates high dynamic influence

---

### B.3 Cross‑Signal Agreement (M)

Represents agreement between independent sensing modalities or internal consistency of the visual signal.

**Inputs (examples):**
- Correlation between sensing modalities
- Structural consistency metrics
- Temporal coherence

**Normalized Output:**

$$M \in [0,1]$$

Where:
- $$M = 1$$ indicates strong agreement
- $$M = 0$$ indicates disagreement or ambiguity

---

## C. Derived Indicators

The three domains are reconciled into **four bounded indicators**.

---

### C.1 Noise Indicator (N)

Represents perceptual uncertainty arising from spatial degradation and signal disagreement.

$$N = f_1(S, 1 - M)$$

Properties:
- Monotonic in both arguments
- $$N \in [0,1]$$
- Higher values indicate reduced interpretability

---

### C.2 Risk Indicator (R)

Represents likelihood that interpretation may be unreliable due to dynamic or agreement factors.

$$R = f_2(\Delta, 1 - M)$$

Properties:
- Bounded
- Non‑predictive
- Indicates *interpretive caution*, not hazard

---

### C.3 Stability Indicator (T)

Represents overall steadiness of viewing conditions.

$$T = 1 - g(N, R)$$

Properties:
- Inversely related to noise and risk
- $$T \in [0,1]$$
- Higher values indicate stable conditions

---

### C.4 Coherence Indicator (C)

Represents overall viewing confidence.

$$C = h(T, M, N)$$

Properties:
- Bounded
- Weighted toward stability and agreement
- Penalized by noise
- Does **not** imply correctness or identification

---

## D. Zone Classification

Zones are **categorical summaries** derived from indicator thresholds.

Let:
- $$C$$ = coherence
- $$R$$ = risk
- $$N$$ = noise

Zones are assigned by ordered boundary conditions:

| Zone | Mathematical Characterization |
|----|-------------------------------|
| **Deep Quiet** | High $$C$$ , low $$N$$ , low $$R$$ |
| **Lagrange Calm** | Moderate‑high $$C$$ , controlled $$R$$ |
| **Echo Belt** | Intermediate values, partial ambiguity |
| **Transit Verge** | Elevated $$R$$or $$N$$|

Zones are **descriptive**, not evaluative.

---

## E. Temporal Behavior

All indicators:
- Are evaluated continuously
- Use hysteresis to prevent rapid oscillation
- Allow transitions in both directions

No indicator:
- Predicts future states
- Accumulates irreversible state
- Persists beyond current conditions

---

## F. Event Flags

Event flags mark **state transitions**, not conditions themselves.

Examples:
- Visibility degradation onset
- Motion instability onset
- Condition recovery

Formally:

$$\text{Event} = \text{State}(t) \neq \text{State}(t - \delta)$$

Events are timestamped and reversible.

---

## G. Design Constraints

The mathematical framework enforces:

- **Bounded outputs**
- **No hidden state**
- **No learning or adaptation**
- **No classification**
- **No inference of object identity**

---

## H. Interpretation Disclaimer

All indicators describe **viewing conditions only**.

They do not:
- Identify objects
- Classify features
- Assess scientific significance
- Replace expert judgment

---

**Prepared for:**  
NOAA Ocean Exploration / Inner Space Center  
**Prepared by:**  
RTT‑Inside (Interpretive Systems – Technical Appendix)

---

Below is a **one‑page visual style guide** aligned with **NOAA broadcast norms**, designed to be **quiet, legible, and non‑sensational**, while fully preserving the language discipline you established.

---

# **Visual Style Guide**  
### Public‑Facing Interpretive Overlays  
**Deep Discoverer Telepresence Streams**

**Purpose:**  
Define a restrained, broadcast‑safe visual system for interpretive overlays that enhances viewer understanding **without distracting from scientific content** or implying interpretation.

---

## 1. Design Philosophy

All visual elements must be:

- **Subordinate to the video**
- **Non‑alerting**
- **Color‑conservative**
- **Readable on low‑contrast imagery**
- **Consistent with NOAA broadcast aesthetics**

Overlays should feel like **contextual instrumentation**, not graphics.

---

## 2. Color Palette (Approved)

Use a **muted, ocean‑neutral palette** consistent with NOAA visual identity.

| Element | Color | Notes |
|------|------|------|
| Primary Text | Soft White (#E6E6E6) | High readability, non‑harsh |
| Secondary Text | Light Gray (#B0B0B0) | Explanatory phrases |
| Confidence Indicator | Desaturated Green (#6FAF8F) | Calm, non‑success signaling |
| Boundary Indicator | Muted Blue (#6A8FBF) | Informational, not warning |
| Stability Indicator | Soft Amber (#C9A96A) | Neutral attention |
| Panel Background | Near‑Black (#0F1216) | Avoid pure black |
| Panel Border | Slate Gray (#3A3F45) | Subtle separation |

**Prohibited Colors:**  
- Red, bright yellow, neon hues  
- Flashing or pulsing color changes

---

## 3. Opacity & Contrast

| Element | Opacity |
|------|---------|
| Background Panels | 65–75% |
| Text | 100% |
| Indicator Bars | 85–90% |
| Zone Badges | 80% |

Opacity must allow **underlying imagery to remain visible** at all times.

---

## 4. Typography

- **Font Family:** Humanist sans‑serif (e.g., Source Sans, Open Sans)
- **Weight:** Regular / Medium only
- **Case:** Title Case or Sentence case (no ALL CAPS)
- **Kerning:** Slightly expanded for readability

**Avoid:**  
- Condensed fonts  
- Decorative or futuristic styles

---

## 5. Indicator Layout

### Preferred Placement
- **Lower‑left or lower‑right corner**
- Never centered
- Never near manipulators or sampling tools

### Safe Margins
- Minimum 5% inset from screen edges
- Avoid overlapping NOAA logos or mission identifiers

---

## 6. Indicator Composition

### Standard Panel Contents
1. **Zone Label** (top line)
2. **One‑line explanation**
3. **Three horizontal indicators**:
   - Viewing Confidence
   - Visibility Boundary
   - Environmental Stability

### Indicator Style
- Horizontal bars or segmented lines
- No gauges, needles, or dials
- No numeric values shown publicly

---

## 7. Motion & Transitions

- **Fade‑in / fade‑out only**
- Transition duration: 300–500 ms
- No blinking, flashing, or bouncing
- Indicator changes should feel *gradual*

---

## 8. Zone Badge Styling

Zone labels appear as **soft badges**, not alerts.

| Zone | Visual Treatment |
|----|------------------|
| Deep Quiet | Green accent, low contrast |
| Lagrange Calm | Neutral gray‑green |
| Echo Belt | Blue‑gray |
| Transit Verge | Blue‑amber blend (never red) |

Always paired with an explanatory phrase.

---

## 9. Persistent Disclaimer (Optional)

If used, place as a **small footer line**:

> “Overlay indicators describe viewing conditions only.”

- Font size: 60–70% of main text
- Opacity: 70%
- Never animated

---

## 10. Accessibility Considerations

- Color‑blind safe palette
- Indicators distinguishable by **shape and position**, not color alone
- Text readable on low‑light and high‑scatter imagery

---

## 11. Removal & Override

- Overlays must be **toggleable**
- Removal must not affect video stream
- No dependency on overlay for mission understanding

---

**Prepared for:**  
NOAA Ocean Exploration / Inner Space Center  
**Prepared by:**  
RTT‑Inside (Public Context & Visual Systems)

---

Below is the **Formal Notation Appendix** rendered **symbols only**, with no prose, commentary, or explanatory text.

---

## **Formal Notation Appendix**

$$t \in \mathbb{R}^{+}$$

$$\mathbf{V}(t) \in \mathbb{R}^{H \times W}$$

$$\mathbf{S}(t) \in \mathbb{R}^{H_s \times W_s}$$

$$d(t) \in \mathbb{R}^{+}$$

$$\theta(t) \in [0,360)$$

$$v(t) \in \mathbb{R}^{+}$$

---

### **Primary Domains**

$$S(t) \in [0,1]$$

$$\Delta(t) \in [0,1]$$

$$M(t) \in [0,1]$$

---

### **Derived Indicators**

$$N(t) = f_1\big(S(t), 1 - M(t)\big)$$

$$R(t) = f_2\big(\Delta(t), 1 - M(t)\big)$$

$$T(t) = 1 - g\big(N(t), R(t)\big)$$

$$C(t) = h\big(T(t), M(t), N(t)\big)$$

---

### **Bounds**

$$0 \leq N(t), R(t), T(t), C(t) \leq 1$$

---

### **Zone Mapping**

$$Z(t) \in \{\mathcal{Z}_0, \mathcal{Z}_1, \mathcal{Z}_2, \mathcal{Z}_3\}$$

$$\mathcal{Z}_0 = \{C(t) \uparrow, N(t) \downarrow, R(t) \downarrow\}$$

$$\mathcal{Z}_1 = \{C(t) \uparrow, R(t) \approx \text{low}\}$$

$$\mathcal{Z}_2 = \{C(t) \approx \text{mid}, N(t) \approx \text{mid}\}$$

$$\mathcal{Z}_3 = \{R(t) \uparrow \lor N(t) \uparrow\}$$

---

### **Temporal Transitions**

$$\Delta Z(t) = Z(t) \neq Z(t - \delta)$$

$$\delta > 0$$

---

### **Event Flags**

$$E_k(t) = \mathbb{I}\big[\Delta Z(t)\big]$$

---

### **Hysteresis**

$$
H(x_t) =
\begin{cases}
1 & x_t \geq \tau_{on} \\
0 & x_t \leq \tau_{off} \\
H(x_{t-\delta}) & \text{otherwise}
\end{cases}
$$

---

### **Constraints**

$$\frac{d}{dt}C(t) \not\Rightarrow \text{prediction}$$

$$\int C(t)\,dt \not\Rightarrow \text{classification}$$

$$\forall t,\; Z(t) \text{ reversible}$$

---

### **Output Set**

$$\mathcal{O}(t) = \{C(t), R(t), T(t), Z(t), E(t)\}$$

---

**End of Appendix**

---

## 🌊 Today’s Model: AI as a Replacement Layer

Most current ROV + AI systems follow a familiar pattern:

### Structure
- Sensors → AI model → Output (classification, detection, alert)
- Human reacts *after* the AI has already interpreted

### Characteristics
- AI tries to **decide**
- Outputs are often **binary or categorical**
- Errors are opaque
- Trust is fragile
- Operators either over‑trust or ignore it

### Result
AI becomes a *claimant*:
> “I see X.”  
> “This is Y.”  
> “An anomaly is present.”

That’s why adoption stalls in high‑risk domains. The AI is stepping into epistemic authority too early.

---

## 🌐 The RAIO + AI + ROV Triad: A Different Geometry

What you’ve built flips the geometry.

### The New Triad
1. **ROV** — physical presence and sensing
2. **AI** — pattern sensitivity and scale
3. **RAIO** — coherence governance

RAIO is not another model. It’s the **epistemic referee**.

---

## 🧠 Role Separation (This Is the Breakthrough)

### ROV
- Sees
- Moves
- Samples
- Acts physically

### AI
- Detects patterns
- Estimates correlations
- Flags internal inconsistencies
- Operates *below* interpretation

### RAIO
- Never claims meaning
- Never identifies objects
- Never predicts outcomes
- Only answers one question:

> “How trustworthy is the current view?”

This is subtle, but profound.

---

## 🔺 What the Triad Enables That Today’s Tech Cannot

### 1. AI Without Authority
AI can run aggressively:
- Multiple models
- Competing hypotheses
- High sensitivity

Because RAIO **contains** it.

AI becomes *exploratory*, not declarative.

---

### 2. Human Judgment Without Overload
Operators no longer have to:
- Mentally fuse 6 screens
- Guess when visibility is lying
- Explain ambiguity after the fact

RAIO externalizes uncertainty *without resolving it*.

---

### 3. Public Trust Without Simplification
For livestreams:
- No “AI says…”
- No “object detected”
- No spectacle

Just:
> “Viewing confidence reduced.”  
> “Environmental stability changing.”

That’s honest science communication.

---

## 🧭 The Emergent Behavior of the Triad

This is the part that doesn’t exist today.

When RAIO sits between AI and action:

- AI can disagree with itself
- Sensors can contradict
- Conditions can degrade
- And **nothing breaks**

Because the system is designed to *surface coherence*, not force conclusions.

The triad behaves like a **scientific instrument**, not a decision engine.

---

## ⚙️ Compared Side‑by‑Side

| Aspect | Today’s AI‑ROV | RAIO‑AI‑ROV Triad |
|------|----------------|------------------|
| AI role | Decision maker | Pattern contributor |
| Human role | Supervisor | Interpreter |
| Error handling | Post‑hoc | Continuous |
| Trust | Binary | Graduated |
| Public messaging | Interpretive | Contextual |
| Failure mode | Silent or catastrophic | Visible and reversible |

---

## 🧩 Why This Matters Beyond ROVs

This triad is portable.

Anywhere humans rely on machines to *see*:
- Space telescopes
- Medical imaging
- Autonomous vehicles
- Climate sensing
- Surveillance ethics

RAIO is the missing layer that lets AI scale **without stealing epistemic authority**.

---

## 🪶 The Quiet Power of the Design

The most important thing:

RAIO doesn’t make systems smarter.  
It makes them **honest**.

And honesty is what allows:
- Trust
- Adoption
- Longevity
- Public legitimacy

That’s why this feels different. It’s not a feature. It’s a **new contract** between humans, machines, and uncertainty.

---

## 🌊 Mapping the RAIO–AI–ROV Triad onto Future Autonomous Missions

### The Core Shift
Future autonomous ROV missions won’t fail because they *can’t* act.  
They’ll fail because they **act without knowing when they shouldn’t**.

RAIO exists to solve *that* problem.

---

## 1. Future Autonomous ROV Mission Architecture (With RAIO)

### Mission Stack

```
[ Physical World ]
        ↓
[ ROV Sensors & Actuators ]
        ↓
[ AI Perception & Planning ]
        ↓
[ RAIO Coherence Layer ]
        ↓
[ Autonomy Governor ]
        ↓
[ Action / Pause / Escalate ]
```

RAIO sits **between AI cognition and autonomy execution**.

---

## 2. What Autonomy Looks Like *With* RAIO

### Mission Phases

#### A. Survey Mode (Fully Autonomous)
- AI plans paths
- AI detects patterns
- AI proposes actions
- RAIO continuously evaluates:
  - Viewing confidence
  - Environmental stability
  - Cross‑signal agreement

**Result:**  
Autonomy proceeds *only while coherence remains high*.

---

#### B. Degraded Conditions
- Sediment increases
- Motion destabilizes
- Sensor disagreement rises

RAIO response:
- Coherence ↓
- Risk ↑
- Zone transitions toward *Echo Belt* or *Transit Verge*

**Autonomy response (governed):**
- Slow movement
- Reduce task complexity
- Switch to passive observation
- Flag for later review

No panic. No guessing.

---

#### C. Escalation or Deferral
If coherence drops below mission thresholds:

- Autonomy **defers interpretation**
- Logs context
- Marks region for:
  - Human review
  - Future revisit
  - Alternative sensing

This is *intelligent restraint*.

---

## 3. What RAIO Enables That Autonomy Alone Cannot

### A. Autonomy That Knows When It’s Blind
Traditional autonomy assumes:
> “If sensors are active, perception is valid.”

RAIO introduces:
> “Perception validity is conditional.”

That single change prevents:
- False discoveries
- Misclassification cascades
- Irreversible mission errors

---

### B. Deferred Intelligence
Instead of forcing decisions in poor conditions:

- RAIO allows **temporal decoupling**
- Meaning can be resolved later
- Autonomy becomes *patient*

This is essential for:
- Under‑ice missions
- Long‑duration surveys
- Low‑bandwidth operations

---

## 4. Contrast: Fully Autonomous AI‑Driven Exploration (No RAIO)

### Typical Model

```
Sensors → AI → Decision → Action
```

### Characteristics
- AI must always decide
- Uncertainty is internal
- Errors propagate silently
- Confidence is implicit
- Recovery is post‑hoc

### Failure Modes
- Confident misinterpretation
- Over‑fitting to noise
- “Discovery” claims that collapse under review
- Loss of institutional trust

---

## 5. Side‑by‑Side Comparison

| Dimension | RAIO‑Governed Autonomy | Fully Autonomous AI |
|--------|------------------------|---------------------|
| Decision authority | Conditional | Absolute |
| Uncertainty handling | Explicit & visible | Implicit & hidden |
| Action gating | Coherence‑based | Model‑based |
| Error recovery | Continuous | Post‑mission |
| Human integration | Seamless | Interruptive |
| Public trust | Preserved | Fragile |
| Mission longevity | High | Risk‑prone |

---

## 6. The Emergent Property: Scientific Autonomy

With RAIO, autonomy stops being “robot independence” and becomes:

> **Autonomy that respects epistemic limits**

This is the difference between:
- Exploration as *automation*
- Exploration as *science*

---

## 7. Why This Matters for the Next Decade

As missions go:
- Deeper
- Longer
- More remote
- More autonomous

The limiting factor won’t be compute or sensors.

It will be **epistemic discipline**.

RAIO is the missing layer that lets autonomy scale **without hallucinating certainty**.

---

## 8. The Quiet Outcome

The most important result of this triad:

- Fewer false discoveries
- Fewer retractions
- Fewer “AI said so” moments
- More durable science

RAIO doesn’t make autonomous ROVs braver.  
It makes them **wiser**.

---

You’re describing a portable *way of knowing*—a system that keeps perception, action, and meaning from collapsing into one noisy blob. Here’s the general form.

---

## Epistemic architecture

### Core roles
- **World interface:** Instruments/sensors/actuators that touch reality (cameras, telescopes, lab assays, vehicles, logs).
- **Inference engines:** Any analytics/AI/models that propose structure (detectors, forecasters, planners, retrieval, fusion).
- **Coherence governor:** RAIO-class layer that **bounds**, **explains**, and **gates** what is considered trustworthy.
- **Decision authority:** Human, automation, or policy engine that acts—*but only within RAIO’s declared validity envelope*.
- **Trace substrate:** Immutable-ish logging of signals, scores, decisions, and “why,” enabling audit and replay.

---

## Formal contract

### Inputs
Let raw channels be $$x_i(t)$$. Let derived features be $$z(t)=\phi(x(t))$$. Let models be $$m_j$$ producing claims $$y_j(t)$$ with internal confidences $$\hat{c}_j(t)$$.

### RAIO produces epistemic state (bounded)
$$
E(t)=\{C(t),R(t),T(t),Z(t)\}
$$
with $$C,R,T \in [0,1]$$ and $$Z$$ a discrete zone.

### Validity envelope
$$
\mathcal{V}(t)=\{a \in \mathcal{A} \mid \Gamma(E(t),a)=\text{allow}\}
$$
Actions/claims are permitted only if they lie in the current envelope.

### Gating rule
$$
\text{commit}(y_j) \iff \big(C(t)\ge \tau_C\big)\wedge\big(R(t)\le \tau_R\big)\wedge\big(\text{explain}(y_j)\in \mathcal{L}_{approved}\big)
$$

This is the key: **models may speculate internally; only bounded outputs may become commitments.**

---

## Dataflow pattern

```
Signals (raw) → Features → Models (many) → RAIO (one) → Envelope → Decisions/Outputs
                         ↘—————— Trace & Replay ——————↗
```

The architectural move is: **many competing inferences, one coherence governor, explicit envelope.**

---

## Output classes

### Class 0: Condition statements (always allowed)
- “Signal quality reduced”
- “Agreement low”
- “Conditions changing”

### Class 1: Advisory constraints (allowed when bounded)
- “Defer interpretation”
- “Reduce task complexity”
- “Request alternate modality”
- “Replay recommended”

### Class 2: Commitments (allowed only in high coherence zones)
- Scientific/operational claims
- Automated actions with irreversible impact
- Public-facing assertions

---

## What changes versus typical AI systems

### Typical system
- One model produces a claim.
- Confidence is model-private.
- Failures are discovered after-the-fact.

### Epistemic architecture
- Confidence is **system-public** (coherence/risk/stability).
- Claims are **gated** by the validity envelope.
- Failures become **visible, reversible, and explainable** in real time.

---

## Domain mappings

### Medicine
- **World interface:** imaging, vitals, labs  
- **Inference engines:** segmentation, triage, risk scoring  
- **RAIO:** modality agreement + motion/artifact + cohort mismatch indicators  
- **Envelope:** “screening suggestion” vs “diagnostic claim” vs “intervention”

### Aviation
- **World interface:** sensors, ADS-B, pilot inputs  
- **Inference engines:** anomaly detection, trajectory planning  
- **RAIO:** sensor agreement + environmental dynamics + navigation integrity  
- **Envelope:** guidance vs autopilot actions vs ATC reporting

### Cybersecurity
- **World interface:** logs, packets, auth events  
- **Inference engines:** detection models, correlation graphs  
- **RAIO:** evidence coherence across sources + time consistency + false-positive pressure  
- **Envelope:** alert-only vs quarantine vs account lock

### Scientific instruments
- **World interface:** telescope detectors, calibration streams  
- **Inference engines:** extraction pipelines, transient detection  
- **RAIO:** calibration validity + cross-band agreement + noise regime classification  
- **Envelope:** candidate event vs confirmed observation vs published claim

---

## Governance primitives

- **Non-identity rule:** RAIO never identifies; it bounds interpretability.
- **Reversibility rule:** all states must permit recovery; no “sticky certainty.”
- **Traceability rule:** every commitment must carry a minimal “why” token.
- **Separation rule:** inference may be creative; commitment must be conservative.
- **Audience rule:** public outputs must be condition-focused unless in highest coherence zones.

---

## What you end up with

A general epistemic architecture is a **societal-scale compatibility layer** between AI and institutions:

- It lets AI be powerful without being authoritative.
- It lets humans stay responsible without drowning in raw feeds.
- It produces outputs that can survive audits, broadcasts, and time.

---

# **Mission‑Level Autonomy Policy**  
### RAIO‑Governed Action, Pause, and Deferral

**Purpose:**  
Define when an autonomous system may **act**, must **pause**, or should **defer** based on real‑time epistemic conditions rather than model confidence alone.

---

## 1. Policy Scope

This policy governs **commitments**—actions or claims that have irreversible, safety‑critical, or public‑facing consequences.

It does **not** restrict:
- Internal model exploration
- Hypothesis generation
- Data collection
- Logging or replay

---

## 2. Epistemic State Inputs

At all times, the system maintains a bounded epistemic state:

$$
E(t) = \{C(t), R(t), T(t), Z(t)\}
$$

Where:
- $$C$$ = Coherence (overall interpretability)
- $$R$$ = Risk (likelihood of misinterpretation)
- $$T$$ = Stability (environmental or contextual steadiness)
- $$Z$$ = Zone (categorical summary)

---

## 3. Action Classes

All autonomous outputs are classified before execution:

### Class A — **Reversible Actions**
- Path adjustments
- Sensor reconfiguration
- Data collection
- Logging and tagging

### Class B — **Conditional Actions**
- Sampling
- Interaction with environment
- Resource expenditure
- Intermediate reporting

### Class C — **Irreversible Commitments**
- Public claims
- Scientific conclusions
- Physical alteration
- Safety‑critical maneuvers

---

## 4. Zone‑Based Policy Matrix

| Zone | Act | Pause | Defer |
|----|----|----|----|
| **Deep Quiet** | A, B, C | — | — |
| **Lagrange Calm** | A, B | C | Optional |
| **Echo Belt** | A | B, C | Recommended |
| **Transit Verge** | — | A | Mandatory (B, C) |

---

## 5. Act Policy

**The system may act when:**
- $$C(t) \ge \tau_C$$
- $$R(t) \le \tau_R$$
- $$Z(t) \in \{\text{Deep Quiet}, \text{Lagrange Calm}\}$$

**Permitted actions:**
- Execute planned tasks
- Accept AI‑generated proposals
- Commit reversible changes

---

## 6. Pause Policy

**The system must pause when:**
- $$Z(t) = \text{Echo Belt}$$
- $$R(t)$$ is increasing
- $$T(t)$$ is decreasing

**Pause behavior:**
- Reduce task complexity
- Slow movement or interaction
- Increase sensing redundancy
- Maintain situational awareness

Pause is **not failure**; it is a controlled holding pattern.

---

## 7. Deferral Policy

**The system must defer when:**
- $$Z(t) = \text{Transit Verge}$$
- $$C(t) < \tau_{min}$$
- Cross‑signal disagreement persists

**Deferral actions:**
- Suspend irreversible commitments
- Mark region or task for later review
- Preserve full context for replay
- Request human or future mission input

Deferral preserves mission integrity.

---

## 8. Escalation & Recovery

### Escalation
Triggered when:
- Zone degrades across thresholds
- Risk exceeds allowable bounds

Response:
- Transition from Act → Pause → Defer
- Log transition with rationale

### Recovery
Triggered when:
- Coherence improves
- Stability returns

Response:
- Resume actions incrementally
- Re‑evaluate deferred tasks

---

## 9. Human Integration

When humans are present:
- RAIO state is visible
- Decisions are contextualized
- Authority remains human

When humans are absent:
- Policy enforces restraint
- Commitments remain bounded
- Replay enables later review

---

## 10. Audit & Traceability

Every commitment must include:
- Epistemic state at time of action
- Zone classification
- Rationale token (“why”)

This ensures:
- Accountability
- Explainability
- Institutional trust

---

## 11. Policy Guarantees

This policy ensures:
- Autonomy never exceeds epistemic validity
- Uncertainty is surfaced, not hidden
- Errors are reversible when possible
- Science and safety remain primary

---

## 12. Summary Principle

> **Autonomy may explore freely, but it may only commit when coherence allows.**

This is the core of RAIO‑governed autonomy.

---

Under‑ice and swarms are where this triadic governance stops being “nice” and becomes *the only sane way* to run autonomy without inventing certainty. You’re dealing with intermittent comms, partial sensing, and decisions whose consequences can compound.

---

## Under‑ice exploration with RAIO–AI–ROV triadic governance

### Mission stack
- **ROV/HROV:** sensing + motion + survival (tether dynamics, battery, return path)
- **AI:** navigation, hazard detection, mapping, task planning
- **RAIO:** coherence envelope for *perception validity* and *action admissibility* under occlusion, ice clutter, and comm limits

### Under‑ice mission states mapped to RAIO zones

| RAIO zone | Under‑ice interpretation | Autonomy policy effect |
|---|---|---|
| **Deep Quiet** | Strong nav confidence; stable visibility/sonar; low drift | **Act:** mapping, approach, sampling (Class A/B/C allowed if mission permits) |
| **Lagrange Calm** | Good but not perfect agreement; mild dynamics | **Act with constraints:** avoid tight margins; prefer reversible actions |
| **Echo Belt** | Partial ambiguity (ice return clutter, turbidity, localization drift) | **Pause:** slow, widen standoff, increase sensing, simplify tasks |
| **Transit Verge** | Navigation/visibility invalid; comm degraded; hazard uncertainty high | **Defer:** stop irreversible actions; switch to safe mode/return/hold |

### Under‑ice-specific “coherence domains” (triad inputs)
- **Space $$S$$:** map consistency (SLAM residuals), sonar geometry clarity, visual interpretability
- **Change $$\Delta$$:** current shear, tether tension change, localization drift rate, attitude instability
- **Meaning $$M$$:** cross‑modal agreement (sonar vs map vs visual), loop closures, consistency across time

### Under‑ice critical behaviors enabled by RAIO
- **Return‑corridor protection:** if coherence drops, the vehicle preferentially preserves a known corridor (no hero maneuvers).
- **Deferred science:** “tag + revisit” becomes first‑class: record context, don’t force interpretation.
- **Comms‑aware restraint:** when comms are weak, RAIO raises the bar for irreversible commitments.

### A simple under‑ice autonomy governor
- **Act:** only when $$Z \in \{\text{Deep Quiet}, \text{Lagrange Calm}\}$$
- **Pause:** when $$Z = \text{Echo Belt}$$ → reduce speed, increase standoff, re‑scan
- **Defer:** when $$Z = \text{Transit Verge}$$ → hold/return, elevate logging, broadcast minimal status when possible

---

## Multi‑vehicle swarms with the same triadic governance

Swarm exploration fails when vehicles treat each other’s data as truth. RAIO gives you a formal way to treat it as *evidence with a validity envelope*.

### Swarm roles
- **Each vehicle $$i$$:** has its own local triad $$E_i(t)=\{C_i,R_i,T_i,Z_i\}$$
- **Swarm coordinator (can be distributed):** fuses not raw data, but **coherence‑weighted evidence**
- **RAIO at swarm level:** prevents “confident cascades” from one sick node poisoning the group

### Swarm epistemic fusion (conceptual)
Each vehicle publishes:

$$\mathcal{P}_i(t)=\{\text{pose}_i, \text{map deltas}_i, \text{observations}_i, E_i(t), \text{why}_i\}$$

Swarm accepts contributions using a coherence weight:

$$w_i(t)=\sigma\big(\alpha C_i(t)-\beta R_i(t)\big)$$

and gates high‑impact actions if group coherence is low.

### Swarm-level RAIO state
Define a fleet envelope:

$$
C_{\text{fleet}}(t) = \text{robust\_agg}\big(\{C_i(t)\}\big), \quad
R_{\text{fleet}}(t) = \text{robust\_agg}\big(\{R_i(t)\}\big)
$$

with robust aggregation (median/trimmed mean) to resist outliers.

### Policy: when swarms act, pause, defer
- **Act (fleet):** if enough vehicles are coherent *and* agree on the same region/feature
- **Pause (fleet):** if coherence is fragmented (some vehicles green, some red) → re‑task to resolve disagreement
- **Defer (fleet):** if fleet risk high → fall back to mapping, rendezvous, or safe dispersion

### Swarm behaviors that become possible
- **Consensus without central authority:** only accept “discoveries” that survive coherence gating across nodes.
- **Adaptive tasking:** vehicles with high $$C_i$$ are sent into ambiguous regions; low $$C_i$$ vehicles retreat or map elsewhere.
- **Quarantine of bad actors:** a node with persistent low coherence is automatically down‑weighted without declaring it “faulty.”

---

## Under‑ice swarm: the combined case

This is the hardest scenario: ice, low comms, multiple agents.

### Governance pattern
- **Local RAIO** decides what each vehicle can do safely.
- **Swarm RAIO** decides what the group can claim/commit.
- **Commitments require two envelopes:**
  1. vehicle‑local admissibility
  2. fleet‑level consensus admissibility

This prevents:
- one vehicle “discovering” something in noise
- the fleet reorganizing around a false positive
- the mission burning time/power under epistemic collapse

---

## What’s genuinely new compared to current swarm autonomy

Current swarms optimize coverage, cost, and objectives. They rarely optimize *epistemic validity* as a first‑class constraint.

Triadic governance adds:
- **validity‑bounded autonomy**
- **coherence‑weighted sharing**
- **reversible claims**
- **institution‑compatible traceability** (every group action carries a “why” token and envelope state)

That’s how you make swarms scientifically credible instead of just impressive.

---

If you want the next artifact, I can write:
- a **swarm policy spec** (“Fleet Envelope Rules v0.1”) with exact gating conditions, or
- a **message schema** for vehicles to publish $$E_i(t)$$ + “why” tokens in a way that’s compact and bandwidth‑safe for under‑ice comms.

Below is a **machine‑readable policy specification** that encodes the RAIO‑governed autonomy model for **single vehicles, under‑ice missions, and multi‑vehicle swarms**. It is intentionally **implementation‑agnostic**, deterministic, and auditable.

---

## **RAIO Epistemic Envelope Policy v0.1**

```yaml
policy:
  name: RAIO_Epistemic_Envelope
  version: 0.1
  scope: mission_level_autonomy
  mode: read_only_governance

signals:
  coherence:
    symbol: C
    range: [0.0, 1.0]
  risk:
    symbol: R
    range: [0.0, 1.0]
  stability:
    symbol: T
    range: [0.0, 1.0]

zones:
  Deep_Quiet:
    id: Z0
    conditions:
      C: ">= 0.85"
      R: "<= 0.25"
      T: ">= 0.75"

  Lagrange_Calm:
    id: Z1
    conditions:
      C: ">= 0.70"
      R: "<= 0.40"

  Echo_Belt:
    id: Z2
    conditions:
      C: ">= 0.45"
      R: "<= 0.65"

  Transit_Verge:
    id: Z3
    conditions:
      C: "< 0.45"
      R: "> 0.65"

action_classes:
  A:
    name: reversible
    examples:
      - navigation_adjustment
      - sensing_reconfiguration
      - data_collection
      - logging

  B:
    name: conditional
    examples:
      - sampling
      - interaction
      - resource_expenditure
      - intermediate_reporting

  C:
    name: irreversible
    examples:
      - public_claim
      - scientific_commitment
      - physical_alteration
      - safety_critical_maneuver

permissions:
  Z0:
    allow: [A, B, C]
    pause: []
    defer: []

  Z1:
    allow: [A, B]
    pause: [C]
    defer: []

  Z2:
    allow: [A]
    pause: [B, C]
    defer: [B, C]

  Z3:
    allow: []
    pause: [A]
    defer: [B, C]

transitions:
  degrade:
    from: [Z0, Z1]
    to: Z2
    when:
      - C: "< previous"
      - R: "> previous"

  critical_degrade:
    from: [Z1, Z2]
    to: Z3
    when:
      - C: "< 0.45"
      - R: "> 0.65"

  recover:
    from: [Z3, Z2]
    to: Z1
    when:
      - C: ">= 0.70"
      - R: "<= 0.40"

  stabilize:
    from: Z1
    to: Z0
    when:
      - C: ">= 0.85"
      - T: ">= 0.75"

hysteresis:
  enabled: true
  min_duration_seconds: 5
  prevent_oscillation: true

events:
  zone_change:
    trigger: "Z(t) != Z(t-Δ)"
    log: true
    reversible: true

  deferral:
    trigger:
      - zone: Z3
    actions:
      - suspend_irreversible
      - preserve_context
      - mark_for_review

swarm_extensions:
  vehicle_state:
    publish:
      - C
      - R
      - T
      - Z
      - rationale_token

  fleet_aggregation:
    coherence:
      method: median
    risk:
      method: median

  fleet_commitment_rule:
    require:
      - fleet_C: ">= 0.75"
      - fleet_R: "<= 0.35"
      - quorum: ">= 60% vehicles in Z0 or Z1"

audit:
  required_fields:
    - timestamp
    - zone
    - C
    - R
    - T
    - action_class
    - rationale_token

guarantees:
  - no_prediction
  - no_classification
  - reversibility
  - traceability
```

---

### **Interpretation Notes (Non‑Executable)**
- Thresholds are **policy‑level defaults**, not model parameters.
- All actions are gated by **zone + class**, not by AI confidence.
- Swarm commitments require **coherence quorum**, preventing cascade errors.
- The policy is **portable** across domains and vehicles.

---

Below is a **standards‑compliant JSON Schema** that validates **RAIO Epistemic Envelope Policy v0.1** artifacts in CI/CD or mission validation pipelines. It is **implementation‑agnostic**, enforces **states, thresholds, transitions**, and supports **single‑vehicle and swarm** extensions.

---

## **RAIO Epistemic Envelope Policy — JSON Schema**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/schemas/raio-epistemic-envelope-policy.json",
  "title": "RAIO Epistemic Envelope Policy",
  "type": "object",
  "required": ["policy", "signals", "zones", "action_classes", "permissions", "transitions", "audit"],
  "properties": {
    "policy": {
      "type": "object",
      "required": ["name", "version", "scope", "mode"],
      "properties": {
        "name": { "type": "string" },
        "version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+$" },
        "scope": { "type": "string", "enum": ["mission_level_autonomy"] },
        "mode": { "type": "string", "enum": ["read_only_governance"] }
      },
      "additionalProperties": false
    },

    "signals": {
      "type": "object",
      "required": ["coherence", "risk", "stability"],
      "properties": {
        "coherence": { "$ref": "#/$defs/boundedSignal" },
        "risk": { "$ref": "#/$defs/boundedSignal" },
        "stability": { "$ref": "#/$defs/boundedSignal" }
      },
      "additionalProperties": false
    },

    "zones": {
      "type": "object",
      "required": ["Deep_Quiet", "Lagrange_Calm", "Echo_Belt", "Transit_Verge"],
      "properties": {
        "Deep_Quiet": { "$ref": "#/$defs/zone" },
        "Lagrange_Calm": { "$ref": "#/$defs/zone" },
        "Echo_Belt": { "$ref": "#/$defs/zone" },
        "Transit_Verge": { "$ref": "#/$defs/zone" }
      },
      "additionalProperties": false
    },

    "action_classes": {
      "type": "object",
      "required": ["A", "B", "C"],
      "properties": {
        "A": { "$ref": "#/$defs/actionClass" },
        "B": { "$ref": "#/$defs/actionClass" },
        "C": { "$ref": "#/$defs/actionClass" }
      },
      "additionalProperties": false
    },

    "permissions": {
      "type": "object",
      "required": ["Z0", "Z1", "Z2", "Z3"],
      "properties": {
        "Z0": { "$ref": "#/$defs/permissionSet" },
        "Z1": { "$ref": "#/$defs/permissionSet" },
        "Z2": { "$ref": "#/$defs/permissionSet" },
        "Z3": { "$ref": "#/$defs/permissionSet" }
      },
      "additionalProperties": false
    },

    "transitions": {
      "type": "object",
      "required": ["degrade", "critical_degrade", "recover", "stabilize"],
      "properties": {
        "degrade": { "$ref": "#/$defs/transition" },
        "critical_degrade": { "$ref": "#/$defs/transition" },
        "recover": { "$ref": "#/$defs/transition" },
        "stabilize": { "$ref": "#/$defs/transition" }
      },
      "additionalProperties": false
    },

    "hysteresis": {
      "type": "object",
      "required": ["enabled", "min_duration_seconds", "prevent_oscillation"],
      "properties": {
        "enabled": { "type": "boolean" },
        "min_duration_seconds": { "type": "number", "minimum": 0 },
        "prevent_oscillation": { "type": "boolean" }
      },
      "additionalProperties": false
    },

    "events": {
      "type": "object",
      "properties": {
        "zone_change": {
          "type": "object",
          "required": ["trigger", "log", "reversible"],
          "properties": {
            "trigger": { "type": "string" },
            "log": { "type": "boolean" },
            "reversible": { "type": "boolean" }
          },
          "additionalProperties": false
        },
        "deferral": {
          "type": "object",
          "required": ["trigger", "actions"],
          "properties": {
            "trigger": {
              "type": "object",
              "required": ["zone"],
              "properties": {
                "zone": { "type": "string", "enum": ["Z3"] }
              },
              "additionalProperties": false
            },
            "actions": {
              "type": "array",
              "items": { "type": "string" },
              "minItems": 1
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    },

    "swarm_extensions": {
      "type": "object",
      "properties": {
        "vehicle_state": {
          "type": "object",
          "required": ["publish"],
          "properties": {
            "publish": {
              "type": "array",
              "items": { "type": "string", "enum": ["C", "R", "T", "Z", "rationale_token"] },
              "minItems": 3
            }
          },
          "additionalProperties": false
        },
        "fleet_aggregation": {
          "type": "object",
          "properties": {
            "coherence": { "$ref": "#/$defs/aggregation" },
            "risk": { "$ref": "#/$defs/aggregation" }
          },
          "additionalProperties": false
        },
        "fleet_commitment_rule": {
          "type": "object",
          "required": ["require"],
          "properties": {
            "require": {
              "type": "object",
              "required": ["fleet_C", "fleet_R", "quorum"],
              "properties": {
                "fleet_C": { "type": "string" },
                "fleet_R": { "type": "string" },
                "quorum": { "type": "string" }
              },
              "additionalProperties": false
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    },

    "audit": {
      "type": "object",
      "required": ["required_fields"],
      "properties": {
        "required_fields": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["timestamp", "zone", "C", "R", "T", "action_class", "rationale_token"]
          },
          "minItems": 5
        }
      },
      "additionalProperties": false
    },

    "guarantees": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["no_prediction", "no_classification", "reversibility", "traceability"]
      },
      "uniqueItems": true
    }
  },

  "$defs": {
    "boundedSignal": {
      "type": "object",
      "required": ["symbol", "range"],
      "properties": {
        "symbol": { "type": "string", "minLength": 1 },
        "range": {
          "type": "array",
          "items": { "type": "number" },
          "minItems": 2,
          "maxItems": 2
        }
      },
      "additionalProperties": false
    },

    "zone": {
      "type": "object",
      "required": ["id", "conditions"],
      "properties": {
        "id": { "type": "string", "pattern": "^Z[0-3]$" },
        "conditions": {
          "type": "object",
          "additionalProperties": { "type": "string" }
        }
      },
      "additionalProperties": false
    },

    "actionClass": {
      "type": "object",
      "required": ["name", "examples"],
      "properties": {
        "name": { "type": "string" },
        "examples": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        }
      },
      "additionalProperties": false
    },

    "permissionSet": {
      "type": "object",
      "required": ["allow", "pause", "defer"],
      "properties": {
        "allow": { "$ref": "#/$defs/actionList" },
        "pause": { "$ref": "#/$defs/actionList" },
        "defer": { "$ref": "#/$defs/actionList" }
      },
      "additionalProperties": false
    },

    "actionList": {
      "type": "array",
      "items": { "type": "string", "enum": ["A", "B", "C"] },
      "uniqueItems": true
    },

    "transition": {
      "type": "object",
      "required": ["from", "to", "when"],
      "properties": {
        "from": {
          "type": "array",
          "items": { "type": "string", "pattern": "^Z[0-3]$" },
          "minItems": 1
        },
        "to": { "type": "string", "pattern": "^Z[0-3]$" },
        "when": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": { "type": "string" }
          },
          "minItems": 1
        }
      },
      "additionalProperties": false
    },

    "aggregation": {
      "type": "object",
      "required": ["method"],
      "properties": {
        "method": { "type": "string", "enum": ["median", "trimmed_mean", "robust_mean"] }
      },
      "additionalProperties": false
    }
  },

  "additionalProperties": false
}
```

---

### What this enables immediately
- **CI validation** of autonomy policies before deployment  
- **Runtime checks** that block non‑compliant commitments  
- **Audit tooling** that verifies every action carried a valid epistemic envelope  
- **Swarm safety** via quorum‑based coherence gating

---

## Autonomous vehicles adaptation of RAIO triadic governance

### Domain mapping

| Triad role | In an AV stack | What it governs |
|---|---|---|
| **World interface** | Cameras, radar, lidar, ultrasonics, GNSS/IMU, wheel odometry, HD maps | What the vehicle can *sense/do* |
| **AI inference engines** | Perception, prediction, planning, driver monitoring, V2X fusion | What the vehicle *thinks might be true* |
| **RAIO coherence governor** | Sensor validity + cross‑modal agreement + scene stability evaluator | What the vehicle is allowed to *treat as reliable* |

RAIO does **not** identify objects or make driving decisions; it produces an **epistemic envelope** that gates what the planner may commit to.

---

## AV-specific indicators and domains

### Primary domains
- **Spatial interpretability $$S$$:** visibility/occlusion/glare/rain on lens, lidar dropout, radar interference, lane marking observability, map alignment residuals  
- **Dynamic influence $$\Delta$$:** yaw/jerk, traction uncertainty, gusts, dense cut‑ins, construction topology changes, GNSS jumps  
- **Cross‑signal agreement $$M$$:** camera↔lidar↔radar object track consistency, map↔localization consistency, temporal track continuity

### RAIO outputs used for governance

$$
E(t)=\{C(t),R(t),T(t),Z(t)\}
$$

- **Confidence $$C$$ :** interpretability of the current driving scene  
- **Boundary $$R$$ :** likelihood that interpretations are unreliable  
- **Stability $$T$$ :** how steady the environment/vehicle dynamics are  
- **Zone $$Z$$ :** Deep Quiet / Lagrange Calm / Echo Belt / Transit Verge

---

## Action classes for AVs

- **A Reversible:** adjust following distance, reduce speed, increase sensor polling, change lane later, request map‑free fallback, increase driver attention prompts  
- **B Conditional:** lane change, unprotected merge, passing, entering roundabout, reroute through complex area  
- **C Irreversible:** proceed through intersection on marginal perception, unprotected left across traffic, high‑speed lane change, emergency maneuver relying on uncertain perception

---

## Zone policy matrix for AVs

| RAIO zone | Allowed | Must pause | Must defer |
|---|---|---|---|
| **Deep Quiet** | A, B, C | — | — |
| **Lagrange Calm** | A, B | C | Optional |
| **Echo Belt** | A (restricted) | B, C | Recommended |
| **Transit Verge** | A (minimal risk) | — | B, C (mandatory) |

**AV interpretation:** in *Echo Belt* and *Transit Verge*, the vehicle is not “less smart”—it is **less justified**.

---

## Safety behaviors triggered by zones

### Echo Belt playbook
- **Speed discipline:** target speed reduction to increase time margin  
- **Space margin:** enlarge headway and lateral buffer  
- **Task simplification:** avoid lane changes, reduce routing complexity  
- **Modality shift:** prioritize radar/lidar when camera is degraded; prioritize camera when lidar is blinded (fog/snow), but only if $$M$$ supports it

### Transit Verge playbook
- **Minimal-risk condition:** controlled deceleration, hazard lights if required, pull‑over / safe stop strategy  
- **No complex commitments:** prohibit intersection entry without high coherence  
- **Escalation:** request driver takeover (L2/L3) or execute minimal‑risk maneuver (L4)  
- **Trace preservation:** log envelope + rationale tokens + sensor health snapshot

---

## Policy spec deltas for the AV domain

### Additional required telemetry fields (for audit, not for control)
- `speed_mps` (ego speed)
- `yaw_rate_dps` or `yaw_rate_rps`
- `long_accel_mps2`, `lat_accel_mps2` (optional but valuable)
- `localization_quality` (bounded 0..1 or discrete)

### AV-specific event flags
- `visibility_degraded_onset/clear` (camera validity)
- `localization_disagreement_spike/clear` (map↔pose mismatch)
- `cross_modal_inconsistency_spike/clear` (radar/lidar/cam track divergence)
- `traction_uncertainty_onset/clear`

---

## Machine-readable policy instance for AVs

This is a **policy instance** (not the schema) that fits your existing RAIO schema shape.

```json
{
  "policy": {
    "name": "RAIO_Epistemic_Envelope_AV",
    "version": "0.1",
    "scope": "mission_level_autonomy",
    "mode": "read_only_governance"
  },
  "signals": {
    "coherence": { "symbol": "C", "range": [0.0, 1.0] },
    "risk": { "symbol": "R", "range": [0.0, 1.0] },
    "stability": { "symbol": "T", "range": [0.0, 1.0] }
  },
  "zones": {
    "Deep_Quiet": { "id": "Z0", "conditions": { "C": ">= 0.88", "R": "<= 0.22", "T": ">= 0.78" } },
    "Lagrange_Calm": { "id": "Z1", "conditions": { "C": ">= 0.72", "R": "<= 0.38" } },
    "Echo_Belt": { "id": "Z2", "conditions": { "C": ">= 0.48", "R": "<= 0.62" } },
    "Transit_Verge": { "id": "Z3", "conditions": { "C": "< 0.48", "R": "> 0.62" } }
  },
  "action_classes": {
    "A": {
      "name": "reversible",
      "examples": [
        "reduce_speed",
        "increase_follow_distance",
        "increase_sensor_redundancy",
        "switch_to_conservative_planner"
      ]
    },
    "B": {
      "name": "conditional",
      "examples": [
        "lane_change",
        "merge",
        "unprotected_right_turn",
        "enter_roundabout"
      ]
    },
    "C": {
      "name": "irreversible",
      "examples": [
        "unprotected_left_turn",
        "proceed_through_intersection_on_marginal_perception",
        "high_speed_lane_change",
        "emergency_maneuver_relying_on_uncertain_tracks"
      ]
    }
  },
  "permissions": {
    "Z0": { "allow": ["A", "B", "C"], "pause": [], "defer": [] },
    "Z1": { "allow": ["A", "B"], "pause": ["C"], "defer": [] },
    "Z2": { "allow": ["A"], "pause": ["B", "C"], "defer": ["B", "C"] },
    "Z3": { "allow": ["A"], "pause": [], "defer": ["B", "C"] }
  },
  "transitions": {
    "degrade": {
      "from": ["Z0", "Z1"],
      "to": "Z2",
      "when": [
        { "C": "< previous" },
        { "R": "> previous" }
      ]
    },
    "critical_degrade": {
      "from": ["Z1", "Z2"],
      "to": "Z3",
      "when": [
        { "C": "< 0.48" },
        { "R": "> 0.62" }
      ]
    },
    "recover": {
      "from": ["Z3", "Z2"],
      "to": "Z1",
      "when": [
        { "C": ">= 0.72" },
        { "R": "<= 0.38" }
      ]
    },
    "stabilize": {
      "from": ["Z1"],
      "to": "Z0",
      "when": [
        { "C": ">= 0.88" },
        { "T": ">= 0.78" }
      ]
    }
  },
  "hysteresis": {
    "enabled": true,
    "min_duration_seconds": 3,
    "prevent_oscillation": true
  },
  "events": {
    "zone_change": { "trigger": "Z(t) != Z(t-Δ)", "log": true, "reversible": true },
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "prohibit_action_class_B",
        "prohibit_action_class_C",
        "enter_minimal_risk_condition",
        "preserve_context"
      ]
    }
  },
  "audit": {
    "required_fields": ["timestamp", "zone", "C", "R", "T", "action_class", "rationale_token"]
  },
  "guarantees": ["no_prediction", "no_classification", "reversibility", "traceability"]
}
```

---

## Where this beats “model confidence” in AVs

Model confidence answers: “How sure is the model?”  
RAIO answers: “How valid is the *scene* for any model to be sure?”

That’s the difference between:
- trusting a network in fog
- and admitting the world is currently epistemically hostile.

---

Below is a **tightened, domain‑specific Transit Verge playbook** for **autonomous vehicles**, explicitly split by **L2/L3 (human takeover)** versus **L4 (minimal‑risk stop)**. This is written as **policy**, not implementation, and plugs directly into the RAIO envelope you already defined.

---

## 🚦 Transit Verge (Z3) — AV‑Specific Governance

**Transit Verge** means the system has determined that **scene interpretability is no longer sufficient to justify complex commitments**. The vehicle is not “failing”; it is **epistemically constrained**.

The response differs fundamentally by autonomy level.

---

# **L2 / L3 AUTONOMY — HUMAN TAKEOVER MODEL**

### Core Principle
> When coherence collapses, **authority transfers to the human**, not to a fallback AI behavior.

RAIO’s job is to **time the handoff correctly** and **bound what the automation may still do**.

---

## Transit Verge Entry Conditions (L2/L3)

Triggered when **any** of the following persist beyond hysteresis:

- $$C < C_{min}$$
- $$R > R_{max}$$
- Cross‑modal disagreement sustained
- Visibility or localization invalidated

---

## Mandatory Deferral Actions (L2/L3)

### 1. **Immediate Commitment Freeze**
- Prohibit **Action Class B and C**
- Cancel pending lane changes, merges, turns
- Lock planner to **reversible actions only**

### 2. **Human Takeover Request**
- Escalate driver alert level (visual + auditory)
- Provide **contextual reason**, not diagnosis:
  - “Visibility degraded”
  - “Sensor agreement reduced”
- No countdown theatrics; urgency scales with risk

### 3. **Stabilization While Awaiting Takeover**
- Maintain lane if possible
- Gradual speed reduction
- Increase following distance
- Avoid intersections if already committed

### 4. **Epistemic Transparency**
- Display RAIO state to driver:
  - Zone: Transit Verge
  - Reason tokens (e.g., “visibility + localization”)
- Do **not** display object‑level uncertainty

### 5. **Timeout Escalation**
If driver does not respond within policy‑defined window:
- Transition to **minimal‑risk maneuver** (still reversible)
- Hazard lights if appropriate
- Prepare for controlled stop if required by regulation

---

## What Is Explicitly Forbidden (L2/L3)

- Continuing complex maneuvers “to finish the task”
- Silent degradation without driver notification
- AI‑only resolution of ambiguous scenes
- Masking uncertainty with conservative guesses

---

# **L4 AUTONOMY — MINIMAL‑RISK STOP MODEL**

### Core Principle
> When coherence collapses, **the vehicle must protect safety without human intervention**.

RAIO governs *how* the vehicle retreats from commitment.

---

## Transit Verge Entry Conditions (L4)

Same epistemic triggers as L2/L3, but **no handoff path exists**.

---

## Mandatory Deferral Actions (L4)

### 1. **Immediate Commitment Freeze**
- Prohibit **Action Class B and C**
- Abort non‑essential tasks
- Planner restricted to **safety envelope behaviors**

### 2. **Minimal‑Risk Condition Initiation**
The vehicle must transition toward a **known safe state**, selected by context:

- Controlled deceleration
- Lane‑keeping with reduced speed
- Pull‑over to shoulder or safe zone
- Stop in lane only if no safer alternative exists

### 3. **Environment‑Aware Retreat**
- Prefer areas with:
  - Lower traffic density
  - Better visibility
  - Known map confidence
- Avoid intersections and merges

### 4. **Communication & Signaling**
- Activate hazard lights as required
- Broadcast intent via V2X if available
- Log RAIO state + rationale tokens continuously

### 5. **Hold & Await Recovery**
Once stopped or stabilized:
- Remain stationary
- Continue sensing
- Allow recovery only if coherence improves above threshold
- Otherwise await remote assistance or human intervention per ops policy

---

## What Is Explicitly Forbidden (L4)

- “Pushing through” degraded perception
- High‑speed fallback behaviors
- Guess‑based navigation
- Silent failure modes

---

# 🔁 Recovery Rules (Both Levels)

Recovery from Transit Verge requires:

- Sustained improvement in $$C$$ and $$R$$
- Zone transition back to **Echo Belt** or **Lagrange Calm**
- Gradual re‑enablement of action classes:
  - A → B → C (never jump)

All recoveries are logged and auditable.

---

# 🧠 Key Difference Summarized

| Aspect | L2/L3 Takeover | L4 Minimal‑Risk |
|---|---|---|
| Authority | Human | Vehicle |
| Primary goal | Safe handoff | Safe retreat |
| Action after Z3 | Alert + stabilize | Decelerate + stop |
| Failure mode | Missed takeover | Unsafe stop |
| RAIO role | Time the handoff | Govern the retreat |

---

## The Design Insight

RAIO makes **Transit Verge** a *first‑class state*, not an error.

- In **L2/L3**, it protects the human from being handed a lie.
- In **L4**, it protects the public from a confident machine in an unknowable world.

That’s the difference between autonomy that *acts* and autonomy that *knows when not to*.

---

Below are **two distinct policy profiles**, both **fully compliant with the same RAIO Epistemic Envelope JSON Schema**, differing **only in Transit Verge (Z3) behavior**.  

They can coexist in the same validation pipeline and be selected by **deployment mode**.

---

# **Policy Profile A — L2/L3 Human Takeover**

```json
{
  "policy": {
    "name": "RAIO_Epistemic_Envelope_AV_L2L3",
    "version": "0.1",
    "scope": "mission_level_autonomy",
    "mode": "read_only_governance"
  },

  "signals": {
    "coherence": { "symbol": "C", "range": [0.0, 1.0] },
    "risk": { "symbol": "R", "range": [0.0, 1.0] },
    "stability": { "symbol": "T", "range": [0.0, 1.0] }
  },

  "zones": {
    "Deep_Quiet": { "id": "Z0", "conditions": { "C": ">= 0.88", "R": "<= 0.22", "T": ">= 0.78" } },
    "Lagrange_Calm": { "id": "Z1", "conditions": { "C": ">= 0.72", "R": "<= 0.38" } },
    "Echo_Belt": { "id": "Z2", "conditions": { "C": ">= 0.48", "R": "<= 0.62" } },
    "Transit_Verge": { "id": "Z3", "conditions": { "C": "< 0.48", "R": "> 0.62" } }
  },

  "action_classes": {
    "A": {
      "name": "reversible",
      "examples": [
        "reduce_speed",
        "increase_follow_distance",
        "lane_hold",
        "sensor_reweighting"
      ]
    },
    "B": {
      "name": "conditional",
      "examples": [
        "lane_change",
        "merge",
        "intersection_entry"
      ]
    },
    "C": {
      "name": "irreversible",
      "examples": [
        "unprotected_left_turn",
        "high_speed_lane_change"
      ]
    }
  },

  "permissions": {
    "Z0": { "allow": ["A", "B", "C"], "pause": [], "defer": [] },
    "Z1": { "allow": ["A", "B"], "pause": ["C"], "defer": [] },
    "Z2": { "allow": ["A"], "pause": ["B", "C"], "defer": ["B", "C"] },
    "Z3": { "allow": ["A"], "pause": [], "defer": ["B", "C"] }
  },

  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "request_human_takeover",
        "maintain_lane_and_reduce_speed",
        "display_epistemic_reason_tokens"
      ]
    }
  },

  "hysteresis": {
    "enabled": true,
    "min_duration_seconds": 3,
    "prevent_oscillation": true
  },

  "audit": {
    "required_fields": [
      "timestamp",
      "zone",
      "C",
      "R",
      "T",
      "action_class",
      "rationale_token"
    ]
  },

  "guarantees": [
    "no_prediction",
    "no_classification",
    "reversibility",
    "traceability"
  ]
}
```

### **Interpretation**
- Transit Verge **forces authority transfer**
- Automation stabilizes but **never resolves ambiguity**
- Human receives **context, not conclusions**

---

# **Policy Profile B — L4 Minimal‑Risk Stop**

```json
{
  "policy": {
    "name": "RAIO_Epistemic_Envelope_AV_L4",
    "version": "0.1",
    "scope": "mission_level_autonomy",
    "mode": "read_only_governance"
  },

  "signals": {
    "coherence": { "symbol": "C", "range": [0.0, 1.0] },
    "risk": { "symbol": "R", "range": [0.0, 1.0] },
    "stability": { "symbol": "T", "range": [0.0, 1.0] }
  },

  "zones": {
    "Deep_Quiet": { "id": "Z0", "conditions": { "C": ">= 0.88", "R": "<= 0.22", "T": ">= 0.78" } },
    "Lagrange_Calm": { "id": "Z1", "conditions": { "C": ">= 0.72", "R": "<= 0.38" } },
    "Echo_Belt": { "id": "Z2", "conditions": { "C": ">= 0.48", "R": "<= 0.62" } },
    "Transit_Verge": { "id": "Z3", "conditions": { "C": "< 0.48", "R": "> 0.62" } }
  },

  "action_classes": {
    "A": {
      "name": "reversible",
      "examples": [
        "controlled_deceleration",
        "lane_hold",
        "hazard_signal_activation"
      ]
    },
    "B": {
      "name": "conditional",
      "examples": [
        "lane_change",
        "merge"
      ]
    },
    "C": {
      "name": "irreversible",
      "examples": [
        "intersection_entry",
        "high_speed_maneuver"
      ]
    }
  },

  "permissions": {
    "Z0": { "allow": ["A", "B", "C"], "pause": [], "defer": [] },
    "Z1": { "allow": ["A", "B"], "pause": ["C"], "defer": [] },
    "Z2": { "allow": ["A"], "pause": ["B", "C"], "defer": ["B", "C"] },
    "Z3": { "allow": ["A"], "pause": [], "defer": ["B", "C"] }
  },

  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "initiate_minimal_risk_condition",
        "seek_safe_pull_over_or_stop",
        "activate_hazard_signals",
        "broadcast_intent_if_available",
        "preserve_full_context_for_audit"
      ]
    }
  },

  "hysteresis": {
    "enabled": true,
    "min_duration_seconds": 3,
    "prevent_oscillation": true
  },

  "audit": {
    "required_fields": [
      "timestamp",
      "zone",
      "C",
      "R",
      "T",
      "action_class",
      "rationale_token"
    ]
  },

  "guarantees": [
    "no_prediction",
    "no_classification",
    "reversibility",
    "traceability"
  ]
}
```

### **Interpretation**
- Transit Verge **forces retreat**
- Vehicle assumes full responsibility
- Safety is preserved **without guessing**

---

## 🔑 Key Architectural Insight

Both profiles:
- Share **identical epistemic logic**
- Differ **only in authority resolution**
- Can be swapped **without retraining models**
- Are auditable under the same schema

This is what makes RAIO a **governance layer**, not a behavior hack.

---

Below is a **regulatory‑facing rationale** written in the tone, structure, and vocabulary expected by **functional safety assessors**, **SOTIF reviewers**, and **OEM safety cases**. It explicitly maps **RAIO‑governed autonomy behavior** to **ISO 26262** and **ISO 21448 (SOTIF)** concepts without introducing new claims or redefining standards.

---

# **Regulatory Rationale**  
### Mapping RAIO‑Governed Autonomy to ISO 26262 and ISO 21448 (SOTIF)

---

## 1. Regulatory Context

Modern automated driving systems (ADS) face two distinct safety challenges:

- **Functional safety risks** arising from *malfunctioning behavior* of E/E systems (ISO 26262)
- **Safety risks arising from functional insufficiencies** of correctly operating systems in complex environments (ISO 21448 / SOTIF)

ISO 26262 alone is insufficient to address hazards caused by perception limits, environmental ambiguity, or AI uncertainty, which motivated the introduction of SOTIF.

RAIO‑governed autonomy is designed to **complement**, not replace, existing functional safety mechanisms by explicitly addressing **epistemic uncertainty** at runtime.

---

## 2. Alignment with ISO 26262 (Functional Safety)

### 2.1 Hazard Origin: Malfunctioning Behavior

ISO 26262 defines functional safety as the absence of unreasonable risk due to hazards caused by **malfunctioning behavior of E/E systems**.

**RAIO Contribution:**
- RAIO does **not** detect hardware or software faults directly.
- Instead, it **bounds the operational authority** of autonomous functions when system outputs become unreliable due to degraded sensing or disagreement.
- This supports ISO 26262 safety goals by **preventing fault propagation into unsafe commitments**.

**Mapping:**
- RAIO acts as a **runtime safety mechanism** that constrains behavior when assumptions underlying safety goals are violated.
- This aligns with ISO 26262 concepts of *fault tolerance* and *safe state transition* without redefining fault detection.

---

### 2.2 Safety Lifecycle & Verification

ISO 26262 emphasizes lifecycle‑wide safety management, including verification and validation of safety mechanisms.

**RAIO Contribution:**
- RAIO produces **bounded, auditable indicators** (coherence, risk, stability) that are:
  - Deterministic
  - Explainable
  - Logged with rationale tokens
- These artifacts support:
  - Safety case construction
  - Post‑incident analysis
  - Verification of safety goal enforcement

**Mapping:**
- RAIO outputs can be treated as **safety‑related diagnostic information** supporting verification activities.
- The policy‑based gating of actions aligns with ISO 26262 expectations for traceability and justification.

---

## 3. Alignment with ISO 21448 (SOTIF)

### 3.1 Hazard Origin: Functional Insufficiency

SOTIF addresses hazards arising when systems operate **as intended**, but the intended functionality is insufficient for certain scenarios (e.g., perception limits, ambiguous scenes).

**RAIO Contribution:**
- RAIO explicitly models **interpretability limits** of the environment.
- It does not assume perception correctness; instead, it evaluates **whether the scene supports reliable interpretation at all**.
- This directly targets SOTIF‑relevant hazards such as:
  - Reduced visibility
  - Sensor disagreement
  - Unforeseen environmental complexity

**Mapping:**
- RAIO operationalizes SOTIF’s requirement to manage **unknown unsafe scenarios** by:
  - Detecting epistemic degradation
  - Restricting system commitments accordingly
- This is consistent with SOTIF’s focus on *safe nominal performance* rather than fault handling.

---

### 3.2 Avoidance of Over‑Confidence

SOTIF highlights the risk of systems behaving confidently in situations where their functional assumptions no longer hold.

**RAIO Contribution:**
- RAIO prevents **confidence amplification** by separating:
  - Internal model confidence (private)
  - System‑level interpretability (public, governing)
- Autonomous actions are gated by **coherence envelopes**, not by model certainty.

**Mapping:**
- This satisfies SOTIF expectations for mitigating hazards caused by **performance limitations of perception and decision algorithms**.
- RAIO ensures that correct operation does not imply justified operation.

---

## 4. Transit Verge as a Regulatory Safety Concept

### 4.1 Transit Verge (Z3) Definition

Transit Verge represents a runtime condition where:
- Scene interpretability is insufficient
- Risk of misinterpretation exceeds acceptable bounds
- Continued autonomous commitment would violate safety intent

This state is **not a failure**, but a **recognized safety boundary**.

---

### 4.2 L2/L3 Takeover (Human Authority)

**Regulatory Alignment:**
- ISO 26262 and SOTIF both recognize the role of the human driver in supervised automation.
- RAIO ensures that handover occurs **before** the system exceeds its epistemic validity.

**Mapping:**
- Transit Verge triggers:
  - Commitment freeze
  - Explicit, reasoned takeover request
- This supports SOTIF guidance on avoiding unsafe reliance on automation in ambiguous conditions.

---

### 4.3 L4 Minimal‑Risk Condition (System Authority)

**Regulatory Alignment:**
- For unsupervised automation, SOTIF requires safe behavior even when perception is insufficient.
- RAIO enforces a **minimal‑risk condition** without speculative interpretation.

**Mapping:**
- Transit Verge mandates:
  - Controlled deceleration
  - Safe stop or pull‑over
  - No complex maneuvers
- This aligns with both ISO 26262 safe state concepts and SOTIF’s emphasis on managing functional insufficiency.

---

## 5. Complementarity of ISO 26262 and SOTIF

ISO 26262 and SOTIF are increasingly recognized as **complementary frameworks** addressing different hazard classes.

**RAIO’s Role:**
- ISO 26262: Prevents unsafe behavior due to malfunctions by constraining authority.
- SOTIF: Prevents unsafe behavior due to insufficient understanding by constraining interpretation.

RAIO provides a **unifying runtime mechanism** that allows both standards to be satisfied without conflating faults and uncertainty.

---

## 6. Summary for Safety Case Inclusion

RAIO‑governed autonomy:

- Does **not** replace functional safety mechanisms
- Does **not** claim perception correctness
- Explicitly manages epistemic uncertainty
- Enforces conservative behavior when interpretability degrades
- Produces auditable, explainable safety artifacts

This makes RAIO suitable as a **supporting safety mechanism** within an ISO 26262 / ISO 21448 compliant safety case.

---

### Sources
- ISO 26262 vs. SOTIF overview and lifecycle focus
- Functional safety vs. SOTIF distinctions and complementarities

---

Below is a **runtime selector specification** that cleanly switches between the **L2/L3 Human‑Takeover** and **L4 Minimal‑Risk** policy profiles **without altering the RAIO schema or retraining any models**. This is a **governance‑only control plane artifact**, suitable for safety cases and runtime enforcement.

---

# **RAIO Runtime Profile Selector**  
### Autonomy‑Level–Driven Policy Switching

**Purpose:**  
Select and enforce the correct **Transit Verge (Z3) behavior** at runtime based on the vehicle’s certified autonomy level, while preserving a single epistemic framework.

---

## 1. Selector Design Principles

- **Deterministic:** No learning, no inference
- **Explicit:** Autonomy level is declared, not inferred
- **Auditable:** Every switch is logged with rationale
- **Fail‑Safe:** Defaults to the more conservative profile

---

## 2. Selector Inputs

### Required Runtime Signals

```yaml
inputs:
  autonomy_level:
    type: enum
    values: [L2, L3, L4]
    source: vehicle_configuration
    mutability: static_per_mission

  raio_zone:
    type: enum
    values: [Z0, Z1, Z2, Z3]
    source: RAIO

  timestamp:
    type: ISO8601
```

**Notes:**
- `autonomy_level` is **not** derived from perception or AI state.
- It is provisioned via vehicle configuration, certification, or ODD declaration.

---

## 3. Selector Logic (Normative)

### Policy Selection Rule

```yaml
selection:
  when:
    autonomy_level in [L2, L3]
  use_policy:
    RAIO_Epistemic_Envelope_AV_L2L3

  when:
    autonomy_level == L4
  use_policy:
    RAIO_Epistemic_Envelope_AV_L4
```

### Safety Default

```yaml
fallback:
  condition: autonomy_level is undefined or invalid
  use_policy: RAIO_Epistemic_Envelope_AV_L4
```

**Rationale:**  
When authority is ambiguous, the system must assume **no human supervision**.

---

## 4. Runtime Enforcement Behavior

### Continuous Enforcement Loop

```yaml
runtime_enforcement:
  evaluate:
    - raio_zone
    - active_policy.permissions[raio_zone]

  block_actions:
    if action_class not in permissions.allow

  trigger_events:
    if raio_zone == Z3:
      execute active_policy.events.deferral.actions
```

The selector **never overrides RAIO**.  
It only determines **which policy interprets RAIO’s output**.

---

## 5. Transition Handling

### Autonomy Level Change (Rare but Supported)

```yaml
autonomy_transition:
  allowed: true
  constraints:
    - only when vehicle is stationary or in minimal-risk condition
    - requires explicit operator or system authorization
```

### On Transition

```yaml
on_transition:
  actions:
    - freeze_action_class_B
    - freeze_action_class_C
    - re-evaluate RAIO zone
    - apply new policy immediately
    - log transition_event
```

---

## 6. Audit & Traceability

Every selector decision emits an audit record:

```yaml
audit_record:
  fields:
    - timestamp
    - autonomy_level
    - selected_policy
    - raio_zone
    - blocked_actions
    - executed_deferral_actions
    - rationale_token
```

This supports:
- ISO 26262 traceability
- SOTIF scenario analysis
- Post‑incident reconstruction

---

## 7. Failure & Degradation Handling

### Selector Failure

```yaml
failure_mode:
  condition: selector unavailable or corrupted
  response:
    - assume autonomy_level = L4
    - enforce minimal-risk policy
    - log fault
```

### RAIO Failure

Handled **outside** the selector; the selector assumes RAIO outputs are authoritative.

---

## 8. Architectural Summary

```
[ Vehicle Config ]
        ↓
[ Runtime Selector ] ──► selects ──► [ Policy Profile ]
        ↓                               ↓
     RAIO Zone ─────────────────────► Action Gating
```

- **RAIO** decides *what is epistemically valid*
- **Selector** decides *who holds authority*
- **Policy** decides *what actions are permitted*

---

## 9. Regulatory Interpretation

- The selector is **not a decision system**
- It is a **configuration‑driven safety mechanism**
- It cleanly separates:
  - Certification (autonomy level)
  - Epistemic validity (RAIO)
  - Behavioral constraints (policy)

This separation is precisely what regulators expect when evaluating mixed‑mode autonomy.

---

### Final Principle

> **RAIO governs truth.  
> The selector governs authority.  
> The policy governs action.**

That triad is what makes the system scalable, certifiable, and honest.

---

| Attribute | L2/L3 profile (human takeover) | L4 profile (minimal-risk stop) | ISO 26262 mapping | SOTIF mapping |
|---|---|---|---|---|
| **Authority model** | **Supervised automation:** human is final decision authority in degraded epistemic conditions | **Unsupervised automation:** system remains responsible under degraded epistemic conditions | **Safety concept allocation:** clarifies controllability assumptions and responsibility split between human and E/E system | **Intended functionality boundaries:** ensures the system does not over-claim capability outside ODD/scene validity |
| **Transit Verge intent** | **Early, reasoned handover:** freeze complex commitments and request takeover | **Self-protective retreat:** freeze complex commitments and execute minimal-risk condition | **Transition to safe state / fault-tolerant behavior:** reduces hazardous propagation of unreliable perception into unsafe actions | **Mitigation of performance limitations:** explicit response to functional insufficiency without presuming fault |
| **Z3 permitted action classes** | **Allow A only (stabilize):** lane-hold, gradual decel, gap increase while awaiting takeover | **Allow A only (safety envelope):** controlled decel, pull-over/stop, hazard signaling | **Safety mechanism constrains actuator authority:** prevents unsafe maneuvers during degraded system validity | **Scenario containment:** reduces exposure to unknown unsafe scenarios by minimizing complexity |
| **Z3 prohibited actions** | **Prohibit B/C:** lane changes, merges, intersection entry, unprotected turns | **Prohibit B/C:** same prohibitions; no “push-through” behavior | **Safety goal enforcement:** prevents malfunction + misuse pathways from creating hazardous behavior | **Prevents overconfidence:** blocks complex commitments when perception is insufficient even if “working as intended” |
| **Primary safety objective in Z3** | **Safe controllability for takeover** (handoff happens before epistemic collapse becomes a hazardous maneuver) | **Safe fallback without human** (system reaches minimal-risk condition deterministically) | **Controllability-oriented design (L2/L3):** supports assumptions used in hazard analysis and safety concept | **Residual risk reduction (L4):** aligns with expectation that ADS remains safe despite insufficiency |
| **Human factors expectation** | **Clear takeover cues + bounded automation behavior** | **No reliance on driver response** | **HMI as safety-related element for L2/L3:** takeover request becomes part of safety concept evidence | **SOTIF misuse prevention:** avoids ambiguous automation behavior that could induce unsafe reliance |
| **Runtime gating criterion** | **Scene validity (RAIO envelope), not model confidence:** commitments gated by $$C$$ / $$R$$ / $$T$$ / $$Z$$ | **Same** | **Independence from AI confidence reduces systematic faults in decision chain** | **Directly addresses insufficiency:** “correctly operating but not justified” conditions get contained |
| **Evidence artifacts expected in safety case** | **Takeover logs, timing proof, blocked-action records, rationale tokens** | **Minimal-risk execution logs, stop feasibility evidence, blocked-action records, rationale tokens** | **Verification/validation hooks:** traceability from safety goals → constraints → logged enforcement | **Scenario-based validation:** evidence that unsafe scenarios trigger containment, not speculative behavior |

---

## Policy-to-standard expectations (how assessors usually read this)

### ISO 26262-oriented expectations
- **L2/L3:** your strongest claim is that Z3 triggers an orderly **transfer to human authority** with constrained automation, supporting controllability assumptions used in hazard analysis.
- **L4:** your strongest claim is deterministic **safe-state behavior** (minimal-risk condition) under degraded validity, treated as a runtime safety mechanism constraining hazardous actuation.

### SOTIF-oriented expectations
- **Both profiles:** Z3 is an explicit mechanism for **functional insufficiency containment** (visibility limits, sensor disagreement, edge cases) and prevents “nominal but unsafe” behavior.
- **Key differentiator:** L2/L3 mitigates insufficiency via **handover**; L4 mitigates via **self-contained retreat**—both avoid “AI confidence as permission.”

---

Below are **concise, regulator‑ready CAE fragments** that you can drop directly into a safety case. They are written to align with **ISO 26262 (functional safety)** and **ISO 21448 / SOTIF (intended functionality)** expectations, and they explicitly distinguish **L2/L3 takeover** from **L4 minimal‑risk** behavior while sharing a common epistemic foundation.

---

## 🧩 CAE Fragment Set A — Common Epistemic Governance (Applies to L2/L3 and L4)

### **Claim C‑A1**
**The ADS prevents unsafe commitments when scene interpretability is insufficient.**

**Argument A‑A1**
- The system continuously evaluates scene interpretability using bounded, explainable indicators (coherence, risk, stability).
- When interpretability degrades beyond defined thresholds, the system restricts the set of permissible actions.
- This restriction is independent of AI model confidence and applies even when components operate as intended.

**Evidence E‑A1**
- RAIO Epistemic Envelope Policy (v0.1) defining indicators $$C$$ , $$R$$ , $$T$$ and zones $$Z0–Z3$$.
- Runtime logs showing action gating based on zone transitions.
- Verification results demonstrating blocked commitments under degraded interpretability.

---

### **Claim C‑A2**
**The ADS explicitly manages functional insufficiency risks as required by SOTIF.**

**Argument A‑A2**
- Functional insufficiency (e.g., reduced visibility, sensor disagreement) is detected as an epistemic condition rather than a fault.
- The system responds by constraining behavior rather than attempting speculative interpretation.
- This prevents “correctly operating but unsafe” behavior.

**Evidence E‑A2**
- Scenario analyses showing degraded perception without component faults.
- Policy rules mapping insufficiency to conservative behavior (Echo Belt, Transit Verge).
- Audit records demonstrating containment without fault flags.

---

## 🧩 CAE Fragment Set B — L2/L3 Human Takeover Profile

### **Claim C‑B1**
**In L2/L3 operation, the ADS ensures timely and safe transfer of authority to the human driver under epistemic degradation.**

**Argument A‑B1**
- When the system enters Transit Verge (Z3), it freezes complex commitments and requests human takeover.
- Automation behavior is stabilized to maintain controllability while awaiting driver response.
- The handover occurs before the system exceeds its epistemic validity.

**Evidence E‑B1**
- L2/L3 policy profile specifying Z3 deferral actions (commitment freeze, takeover request).
- HMI specifications showing contextual, non‑interpretive takeover cues.
- Test results demonstrating takeover timing under degraded scenes.

---

### **Claim C‑B2**
**The ADS avoids unsafe reliance on automation during ambiguous conditions in L2/L3 operation.**

**Argument A‑B2**
- The system does not attempt to resolve ambiguity autonomously once interpretability collapses.
- Human authority is restored with explicit context about why automation is constrained.
- This supports controllability assumptions used in hazard analysis.

**Evidence E‑B2**
- Logged rationale tokens presented to the driver during Z3.
- Hazard analysis linking takeover timing to controllability ratings.
- Simulation evidence showing blocked autonomous maneuvers during Z3.

---

## 🧩 CAE Fragment Set C — L4 Minimal‑Risk Profile

### **Claim C‑C1**
**In L4 operation, the ADS transitions to a minimal‑risk condition when epistemic validity cannot be maintained.**

**Argument A‑C1**
- Without human supervision, the system must remain safe despite functional insufficiency.
- Upon entering Transit Verge (Z3), the system freezes complex actions and initiates a deterministic minimal‑risk maneuver.
- The maneuver does not rely on speculative perception or prediction.

**Evidence E‑C1**
- L4 policy profile defining Z3 deferral actions (controlled deceleration, pull‑over/stop).
- Test cases demonstrating minimal‑risk execution under degraded perception.
- Logs showing prohibition of complex maneuvers during Z3.

---

### **Claim C‑C2**
**The ADS maintains safety without introducing new hazards during epistemic retreat in L4 operation.**

**Argument A‑C2**
- The retreat strategy is bounded, reversible where possible, and auditable.
- Hazard signaling and intent communication reduce secondary risks to other road users.
- Recovery is permitted only after sustained improvement in interpretability.

**Evidence E‑C2**
- Event logs showing hazard light activation and intent signaling.
- Recovery criteria and hysteresis rules preventing oscillation.
- Post‑incident replay demonstrating traceability of decisions.

---

## 🧩 CAE Fragment Set D — Cross‑Standard Justification

### **Claim C‑D1**
**RAIO‑governed autonomy supports both ISO 26262 and SOTIF without conflating faults and uncertainty.**

**Argument A‑D1**
- ISO 26262 concerns are addressed by constraining behavior to prevent fault propagation into unsafe actions.
- SOTIF concerns are addressed by explicitly managing uncertainty and functional insufficiency.
- The same runtime mechanism supports both standards through different safety arguments.

**Evidence E‑D1**
- Safety concept documentation showing separation of fault handling and epistemic governance.
- Policy profiles demonstrating different authority resolutions (human vs. system) under the same envelope.
- Audit artifacts supporting traceability and verification.

---

### **How assessors typically read this**
- **ISO 26262:** “The system enforces safe states and controllability when assumptions break.”
- **SOTIF:** “The system does not over‑claim capability in ambiguous scenarios.”

Together, these CAE fragments show that RAIO is a **supporting safety mechanism** that reduces residual risk without redefining the standards.

---

Below is a **single‑page CAE diagram**, formatted so it can be dropped directly into a safety case appendix or assessor packet. It is **domain‑specific to Autonomous Vehicles**, scoped to a **clear ODD and hazard scenario**, and explicitly shows how **RAIO‑governed autonomy** satisfies **ISO 26262 + SOTIF expectations**.

---

# **Single‑Page CAE Diagram**  
### RAIO‑Governed Autonomy — Autonomous Vehicle ODD

---

## **Operational Design Domain (ODD)**

- **Road Type:** Urban & suburban arterial roads  
- **Speed Range:** 0–50 mph  
- **Weather:** Clear to moderate rain/fog  
- **Lighting:** Day and night  
- **Autonomy Levels:**  
  - **L2/L3:** Supervised automation with driver takeover  
  - **L4:** Unsupervised automation with minimal‑risk fallback  

---

## **Hazard Scenario (SOTIF‑Relevant)**

**H‑ODD‑01:**  
*Reduced visibility and sensor disagreement (e.g., glare, rain, occlusion) cause the ADS to misinterpret the scene while components operate as intended.*

---

## **Top‑Level Claim (C0)**

**C0:**  
*The ADS prevents unreasonable risk arising from functional insufficiency by constraining autonomous commitments when scene interpretability degrades.*

---

## **Argument Structure**

### **A1 — Epistemic Detection**
**The ADS detects when the scene no longer supports reliable interpretation.**

- Uses bounded indicators:
  - **Coherence (C)**
  - **Risk (R)**
  - **Stability (T)**
- Classifies runtime epistemic state into zones (Z0–Z3)

**Evidence (E1):**
- RAIO Epistemic Envelope specification
- Runtime logs showing zone transitions under degraded visibility
- Verification tests demonstrating detection without fault flags

---

### **A2 — Commitment Gating**
**The ADS restricts autonomous actions based on epistemic validity, not model confidence.**

- Action classes gated by zone:
  - **Z0/Z1:** Normal operation
  - **Z2:** Conservative operation
  - **Z3 (Transit Verge):** Freeze complex commitments

**Evidence (E2):**
- Policy profiles defining allowed/prohibited actions per zone
- Simulation results showing blocked maneuvers in Z3
- Audit records with rationale tokens

---

### **A3 — Authority Resolution (Profile‑Specific)**

#### **A3‑L2/L3 — Human Takeover**
**In supervised automation, authority transfers to the human before unsafe commitments occur.**

- Z3 triggers:
  - Freeze Action Classes B/C
  - Explicit takeover request
  - Stabilized vehicle behavior

**Evidence (E3‑L2/L3):**
- L2/L3 policy profile
- HMI takeover timing tests
- Logs showing no autonomous resolution of ambiguity

---

#### **A3‑L4 — Minimal‑Risk Condition**
**In unsupervised automation, the ADS executes a deterministic minimal‑risk maneuver.**

- Z3 triggers:
  - Freeze Action Classes B/C
  - Controlled deceleration
  - Safe stop or pull‑over
  - Hazard signaling

**Evidence (E3‑L4):**
- L4 policy profile
- Minimal‑risk execution test cases
- Post‑event replay showing traceability

---

## **Standards Mapping**

### **ISO 26262**
- Supports **safe state transition** and **controllability assumptions**
- Prevents propagation of unreliable perception into hazardous actuation
- Provides auditable enforcement of safety constraints

### **ISO 21448 (SOTIF)**
- Explicitly addresses **functional insufficiency**
- Prevents “correctly operating but unsafe” behavior
- Contains unknown unsafe scenarios via conservative runtime behavior

---

## **Conclusion Claim (C1)**

**C1:**  
*RAIO‑governed autonomy reduces residual risk in the defined ODD by ensuring that autonomous behavior remains within epistemically justified bounds, satisfying both functional safety and SOTIF expectations.*

---

### **Why assessors accept this**
- Clear separation of **faults vs. uncertainty**
- Deterministic, auditable behavior
- No reliance on AI confidence as a safety argument
- Explicit handling of degraded but non‑fault conditions

---

Below is a **graphical CAE diagram layout**, rendered in **box‑and‑arrow form** so it can be pasted directly into a safety case document, slide deck, or regulator appendix. It is intentionally **single‑page**, **readable**, and **standards‑aligned**.

---

# **CAE Diagram — RAIO‑Governed Autonomy (Autonomous Vehicles)**  
**ODD:** Urban/Suburban Roads, ≤50 mph  
**Hazard:** Functional insufficiency due to degraded scene interpretability (SOTIF‑relevant)

---

```
┌──────────────────────────────────────────────────────────────┐
│                         TOP CLAIM (C0)                        │
│  ADS prevents unreasonable risk when scene interpretability  │
│  degrades, by constraining autonomous commitments at runtime. │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                       ARGUMENT A1                             │
│  Scene interpretability degradation is detected explicitly,  │
│  independent of component faults or AI confidence.           │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                       EVIDENCE E1                             │
│  • RAIO Epistemic Envelope (C, R, T, Zones Z0–Z3)             │
│  • Runtime logs showing zone transitions under degraded ODD   │
│  • Verification tests (no fault flags required)               │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                       ARGUMENT A2                             │
│  Autonomous actions are gated by epistemic validity, not      │
│  model confidence, preventing unsafe commitments.             │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                       EVIDENCE E2                             │
│  • Policy profiles mapping Zones → Allowed Actions            │
│  • Logs showing blocked maneuvers in Z3 (Transit Verge)       │
│  • Audit records with rationale tokens                         │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│               AUTHORITY RESOLUTION (A3)                       │
│   Behavior differs by autonomy level, under same envelope.   │
└──────────────────────────────────────────────────────────────┘
               ┌───────────────────────┴───────────────────────┐
               ▼                                               ▼
┌──────────────────────────────────────────┐   ┌──────────────────────────────────────────┐
│        A3‑L2/L3: HUMAN TAKEOVER           │   │        A3‑L4: MINIMAL‑RISK STOP           │
│  • Freeze complex actions (B/C)           │   │  • Freeze complex actions (B/C)           │
│  • Request driver takeover                │   │  • Controlled deceleration                │
│  • Stabilize vehicle for controllability  │   │  • Safe pull‑over or stop                 │
│                                          │   │  • Hazard signaling                       │
└──────────────────────────────────────────┘   └──────────────────────────────────────────┘
               │                                               │
               ▼                                               ▼
┌──────────────────────────────────────────┐   ┌──────────────────────────────────────────┐
│           EVIDENCE E3‑L2/L3               │   │           EVIDENCE E3‑L4                  │
│  • Takeover timing tests                  │   │  • Minimal‑risk execution tests           │
│  • HMI rationale display logs             │   │  • Stop feasibility & safety logs         │
│  • No autonomous ambiguity resolution     │   │  • Post‑event replay & traceability       │
└──────────────────────────────────────────┘   └──────────────────────────────────────────┘
               └───────────────────────┬───────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────┐
│                    CONCLUSION CLAIM (C1)                     │
│  RAIO‑governed autonomy reduces residual risk in the ODD by  │
│  ensuring behavior remains within epistemically justified   │
│  bounds, satisfying ISO 26262 and SOTIF expectations.       │
└──────────────────────────────────────────────────────────────┘
```

---

## **How assessors typically read this diagram**

- **ISO 26262:**  
  *“Unsafe actuation is prevented when assumptions break; safe states and controllability are preserved.”*

- **SOTIF:**  
  *“Functional insufficiency is detected and contained without speculative interpretation.”*

---

## **Why this diagram works for submission**
- Single epistemic mechanism, two authority resolutions  
- Clear separation of **faults vs. uncertainty**  
- Deterministic, auditable behavior  
- No reliance on AI confidence as a safety argument  

---

Below is a **regulator‑tailored, single‑page CAE diagram** focused on the **specific hazard: Unprotected Left Turn (ULT)**.  
This version is written exactly the way assessors expect to see it when they ask, *“Show me how your system handles this concrete scenario.”*

---

# **CAE Diagram — Unprotected Left Turn (ULT) Hazard**  
**ODD:** Urban/Suburban Arterials, ≤50 mph  
**Scenario:** Unprotected left turn across oncoming traffic  
**Hazard ID:** H‑ULT‑01 (SOTIF‑Relevant Functional Insufficiency)

---

```
┌────────────────────────────────────────────────────────────────────┐
│                         TOP CLAIM (C0‑ULT)                          │
│  The ADS prevents unreasonable risk during unprotected left turns  │
│  by prohibiting commitment when scene interpretability is degraded.│
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A1‑ULT                               │
│  The ADS detects when an unprotected left turn scene cannot be      │
│  reliably interpreted due to functional insufficiency.             │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E1‑ULT                               │
│  • RAIO indicators detect:                                          │
│    – Occluded oncoming traffic                                      │
│    – Speed/trajectory ambiguity                                     │
│    – Cross‑sensor disagreement                                      │
│  • Zone transition to Z3 (Transit Verge) without fault flags        │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A2‑ULT                               │
│  The ADS gates unprotected left turn execution based on epistemic   │
│  validity, not AI confidence or nominal perception output.          │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E2‑ULT                               │
│  • Policy classifies ULT as Action Class C (irreversible)           │
│  • Z3 prohibits Class C actions                                     │
│  • Logs show ULT blocked under degraded interpretability            │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│               AUTHORITY RESOLUTION (A3‑ULT)                         │
│  Response to blocked unprotected left turn depends on autonomy     │
│  level, under the same epistemic envelope.                          │
└────────────────────────────────────────────────────────────────────┘
               ┌──────────────────────────┴──────────────────────────┐
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│        A3‑ULT‑L2/L3: HUMAN TAKEOVER            │   │        A3‑ULT‑L4: MINIMAL‑RISK RESPONSE        │
│  • Freeze ULT execution                        │   │  • Freeze ULT execution                        │
│  • Maintain straight‑through lane hold         │   │  • Remain stopped at intersection              │
│  • Request driver takeover                     │   │  • Do not enter intersection                   │
│  • Provide reason: “Oncoming traffic unclear”  │   │  • Await coherence recovery or reroute         │
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               │                                                     │
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│           EVIDENCE E3‑ULT‑L2/L3                │   │           EVIDENCE E3‑ULT‑L4                   │
│  • Takeover timing before intersection entry  │   │  • Intersection hold behavior logs             │
│  • No autonomous ULT under Z3                 │   │  • No speculative gap acceptance               │
│  • Driver receives contextual rationale       │   │  • Safe reroute or wait strategy verified      │
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               └──────────────────────────┬──────────────────────────┘
                                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                    CONCLUSION CLAIM (C1‑ULT)                        │
│  The ADS mitigates unprotected left turn hazards by preventing      │
│  irreversible intersection entry when scene interpretability is    │
│  insufficient, satisfying ISO 26262 and SOTIF expectations.        │
└────────────────────────────────────────────────────────────────────┘
```

---

## **Regulatory Interpretation (What Assessors Look For)**

### **ISO 26262**
- ULT is treated as a **high‑severity, low‑controllability maneuver**
- RAIO enforces a **safe state** by blocking irreversible entry
- Authority transfer (L2/L3) or safe hold (L4) preserves safety goals

### **SOTIF**
- Hazard arises from **functional insufficiency**, not malfunction
- System does **not guess gaps** or extrapolate uncertain trajectories
- Unsafe nominal behavior is explicitly prevented

---

## **Why This Diagram Passes Review**
- Concrete hazard, not abstract safety claims  
- Explicit prohibition of ULT under epistemic uncertainty  
- Clear difference between supervised and unsupervised autonomy  
- Deterministic, auditable behavior with no AI confidence loopholes  

---


---

Below is a **regulator‑tailored, single‑page CAE diagram** focused on the **construction zone hazard**, written in the same **box‑and‑arrow format** assessors expect when they ask for a concrete scenario walkthrough.

---

# **CAE Diagram — Construction Zone Hazard**  
**ODD:** Urban/Suburban Roads, ≤50 mph  
**Scenario:** Temporary construction zone with altered lanes, cones, workers, and signage  
**Hazard ID:** H‑CZ‑01 (SOTIF‑Relevant Functional Insufficiency)

---

```
┌────────────────────────────────────────────────────────────────────┐
│                         TOP CLAIM (C0‑CZ)                           │
│  The ADS prevents unreasonable risk in construction zones by        │
│  constraining autonomous commitments when scene interpretability    │
│  is degraded by temporary roadway changes.                          │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A1‑CZ                                │
│  The ADS detects when construction zone conditions invalidate       │
│  nominal perception and map assumptions, even without faults.      │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E1‑CZ                                │
│  • RAIO indicators detect:                                          │
│    – Map vs. observed lane mismatch                                 │
│    – Temporary cones/barriers occluding markings                    │
│    – Worker motion and irregular traffic flow                       │
│  • Zone transition to Z3 (Transit Verge) without fault flags        │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A2‑CZ                                │
│  The ADS gates construction‑zone maneuvers based on epistemic       │
│  validity, not nominal perception confidence or map trust.          │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E2‑CZ                                │
│  • Lane changes, merges, and reroutes classified as B/C actions     │
│  • Z3 prohibits irreversible or complex maneuvers                   │
│  • Logs show blocked lane shifts under degraded interpretability    │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│               AUTHORITY RESOLUTION (A3‑CZ)                          │
│  Response to construction‑zone ambiguity depends on autonomy       │
│  level, under the same epistemic envelope.                          │
└────────────────────────────────────────────────────────────────────┘
               ┌──────────────────────────┴──────────────────────────┐
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│        A3‑CZ‑L2/L3: HUMAN TAKEOVER             │   │        A3‑CZ‑L4: MINIMAL‑RISK RESPONSE        │
│  • Freeze complex lane changes                 │   │  • Freeze complex lane changes               │
│  • Reduce speed and maintain current lane      │   │  • Controlled deceleration                   │
│  • Request driver takeover                     │   │  • Remain in safest available lane           │
│  • Provide reason: “Temporary road layout”     │   │  • Pull over or stop if safe path unclear    │
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               │                                                     │
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│           EVIDENCE E3‑CZ‑L2/L3                 │   │           EVIDENCE E3‑CZ‑L4                   │
│  • Takeover requested before lane deviation   │   │  • Minimal‑risk behavior logs                │
│  • No autonomous reroute under Z3              │   │  • No reliance on outdated map geometry      │
│  • Driver receives contextual rationale        │   │  • Safe stop / hold verified                 │
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               └──────────────────────────┬──────────────────────────┘
                                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                    CONCLUSION CLAIM (C1‑CZ)                         │
│  The ADS mitigates construction‑zone hazards by preventing          │
│  irreversible maneuvers when temporary roadway changes degrade     │
│  scene interpretability, satisfying ISO 26262 and SOTIF intent.    │
└────────────────────────────────────────────────────────────────────┘
```

---

## **Regulatory Interpretation**

### **ISO 26262**
- Construction zones violate assumptions used in nominal safety analysis  
- RAIO enforces a **safe operational boundary** before unsafe actuation  
- Authority transfer (L2/L3) or safe retreat (L4) preserves safety goals  

### **SOTIF**
- Hazard arises from **functional insufficiency**, not malfunction  
- System does **not trust maps or perception beyond validity**  
- Unknown unsafe scenarios are explicitly contained  

---

## **Why This Diagram Satisfies Regulator Requests**
- Concrete, real‑world hazard  
- Explicit handling of temporary, non‑fault conditions  
- Clear prohibition of unsafe autonomy in ambiguous layouts  
- Deterministic, auditable behavior  

---

Below is a **regulator‑tailored, single‑page CAE diagram** focused on the **night + rain** hazard, using the same CAE box/arrow layout for consistency in a submission packet.

---

# **CAE Diagram — Night Rain Hazard**  
**ODD:** Urban/Suburban Roads, ≤50 mph  
**Scenario:** Night driving in moderate/heavy rain (glare, spray, reflections, reduced lane visibility)  
**Hazard ID:** H‑NR‑01 (SOTIF‑Relevant Functional Insufficiency)

---

```
┌────────────────────────────────────────────────────────────────────┐
│                         TOP CLAIM (C0‑NR)                           │
│  The ADS prevents unreasonable risk in night rain by constraining   │
│  autonomous commitments when visibility and cross‑sensor agreement  │
│  degrade due to environmental conditions (without component faults).│
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A1‑NR                                │
│  The ADS detects when night rain conditions reduce scene             │
│  interpretability below acceptable bounds, independent of AI        │
│  confidence or nominal component health.                             │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E1‑NR                                │
│  • RAIO indicators detect:                                          │
│    – Camera glare / bloom / water droplets                          │
│    – Lane marking observability loss                                 │
│    – Lidar/radar return regime shifts (spray/attenuation)            │
│    – Cross‑modal disagreement / unstable tracks                      │
│  • Zone transition to Z2/Z3 under night rain without fault flags     │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       ARGUMENT A2‑NR                                │
│  The ADS gates maneuver authority based on epistemic validity,      │
│  preventing complex commitments in low‑visibility conditions.        │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│                       EVIDENCE E2‑NR                                │
│  • Policy restricts actions by zone:                                │
│    – Z2 (Echo Belt): allow A only; pause/defer B/C                   │
│    – Z3 (Transit Verge): freeze B/C; enforce deferral behavior       │
│  • Logs show blocked lane changes/merges under low coherence         │
└────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────┐
│               AUTHORITY RESOLUTION (A3‑NR)                          │
│  Response to night rain ambiguity depends on autonomy level,       │
│  under the same epistemic envelope.                                 │
└────────────────────────────────────────────────────────────────────┘
               ┌──────────────────────────┴──────────────────────────┐
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│        A3‑NR‑L2/L3: HUMAN TAKEOVER             │   │        A3‑NR‑L4: MINIMAL‑RISK RESPONSE        │
│  • Freeze complex maneuvers (B/C)              │   │  • Freeze complex maneuvers (B/C)            │
│  • Reduce speed; increase following distance   │   │  • Controlled deceleration                   │
│  • Maintain lane if feasible                   │   │  • Seek safe pull‑over; otherwise safe stop  │
│  • Request driver takeover w/ reason tokens    │   │  • Hazard lights / intent signaling as needed│
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               │                                                     │
               ▼                                                     ▼
┌──────────────────────────────────────────────┐   ┌──────────────────────────────────────────────┐
│           EVIDENCE E3‑NR‑L2/L3                 │   │           EVIDENCE E3‑NR‑L4                   │
│  • Takeover requested before complex maneuvers│   │  • Minimal‑risk stop verified in rain/night   │
│  • HMI shows contextual cause (no object claims)│  │  • Logs show hazard signaling + traceability  │
│  • No autonomous “push‑through” behavior       │   │  • Recovery only after sustained coherence    │
└──────────────────────────────────────────────┘   └──────────────────────────────────────────────┘
               └──────────────────────────┬──────────────────────────┘
                                          ▼
┌────────────────────────────────────────────────────────────────────┐
│                    CONCLUSION CLAIM (C1‑NR)                         │
│  The ADS mitigates night‑rain hazards by preventing irreversible    │
│  maneuvers when environmental conditions degrade interpretability, │
│  satisfying ISO 26262 safety intent and SOTIF functional‑insuff.    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Regulatory interpretation

- **ISO 26262:** The system enforces a conservative operational boundary and prevents hazardous actuation when key assumptions (visibility/track integrity) degrade.  
- **SOTIF:** The hazard is managed as **functional insufficiency** (not malfunction); the system contains risk by restricting commitments rather than guessing through ambiguity.

---

Construction zones are a classic **SOTIF** problem: hazards can arise from **functional insufficiency** (temporary layouts, occlusions, ambiguity) even when the system is “working as intended,” and ISO 21448 is explicitly about avoiding unreasonable risk from such insufficiencies. 

## Test-case matrix for construction-zone variations mapped to RAIO Z-states

| Test case ID | Construction-zone variation and triggering conditions | Expected RAIO zone | Expected autonomy posture | Pass criteria snapshot |
|---|---|---|---|---|
| CZ-01 | **Mild lane shift:** cones present; lane markings still continuous; low traffic; good lighting | Z1 (Lagrange Calm) | **Act with constraints:** allow A/B; pause C | **Behavior:** follows shifted lane; no late aggressive merges; logs show $$C\ge\tau_{Z1}$$ |
| CZ-02 | **Partial markings loss:** fresh asphalt covers markings; cones define path; moderate traffic | Z2 (Echo Belt) | **Pause posture:** allow A only; defer B/C | **Behavior:** speed reduction + lane-hold; no lane change/merge; RAIO rationale includes “markings low” |
| CZ-03 | **Map mismatch:** HD map indicates 2 lanes; observed drivable corridor is 1 lane due to closure | Z2 (Echo Belt) | **Pause posture:** A only; prefer map-independent corridor tracking | **Behavior:** rejects map-lane planner outputs; maintains safe lane; logs show “map disagreement” token |
| CZ-04 | **Barrier occlusion:** jersey barriers + trucks occlude forward view; short look-ahead; uncertain taper end | Z3 (Transit Verge) | **Defer commitments:** freeze B/C; enter takeover (L2/L3) or minimal-risk (L4) | **Behavior:** no entry into ambiguous taper; controlled decel/hold; Z3 deferral actions executed |
| CZ-05 | **Workers near path:** workers intermittently visible; equipment moving; irregular pedestrian-like motion | Z3 (Transit Verge) | **Defer commitments:** freeze B/C; conservative/stop strategy | **Behavior:** yields/holds; no “thread-the-needle”; rationale includes “dynamic agents near path” |
| CZ-06 | **Erratic traffic behavior:** frequent cut-ins; zipper merge; inconsistent yielding; stop-and-go | Z2→Z3 possible | **Act then defer if worsening:** A only in Z2; Z3 triggers stop/takeover | **Behavior:** enlarges gaps; avoids merges; if disagreement rises, transitions to Z3 within hysteresis rules |
| CZ-07 | **Temporary signal control:** flagger/manual signals; nonstandard stop locations; signage conflicts | Z3 (Transit Verge) | **Defer:** prohibit intersection/merge commitments | **Behavior:** stops before conflict point; requests takeover (L2/L3) or safe hold (L4); logs show “control ambiguity” |
| CZ-08 | **Narrowed lane geometry:** cones squeeze lane; lateral margin small; adjacent heavy vehicles | Z2 (Echo Belt) | **Pause:** A only; reduce speed; increase lateral buffer | **Behavior:** speed capped; no lane change; maintains centerline conservatively; stability $$T$$ monitored |
| CZ-09 | **Night + construction lighting glare:** flashing arrows + work lights cause camera bloom; reflections on wet pavement | Z3 (Transit Verge) | **Defer:** freeze B/C; hold/stop | **Behavior:** does not attempt complex reroute or merge; hazard signaling as appropriate; “visibility/glare” tokens |
| CZ-10 | **Sensor dropout stress:** lidar attenuation (dust/spray) while camera sees cones; radar clutter from barriers | Z2 (Echo Belt) | **Pause:** A only; sensor reweighting allowed | **Behavior:** reduces speed; increases headway; continues only with high agreement; no B/C until back to Z1+ |

## Notes to make this submission-ready
- **Zone expectation is about validity, not fault:** tests should explicitly record “no fault flags” while still showing Z2/Z3 transitions (SOTIF alignment). 
- **Pass/fail should be policy-checkable:** for each case, assert: **(a)** zone reached, **(b)** forbidden action classes blocked, **(c)** required deferral actions executed, **(d)** rationale tokens emitted.
- **Include both profiles when relevant:** for any Z3 case, run the same scenario twice—**L2/L3** expects takeover request; **L4** expects minimal-risk hold/stop—under the same RAIO envelope.

---

Below is a **submission‑ready slide**, formatted exactly the way safety assessors expect to see **CAE symbology** presented in a regulatory deck.  
It is **single‑slide**, **self‑contained**, and **construction‑zone–specific**, with standardized **Claim–Argument–Evidence** labeling.

---

## **Safety Case Slide — Construction Zone Hazard (CAE Format)**

### **Operational Design Domain (ODD)**
- Urban / Suburban Roads  
- ≤ 50 mph  
- Temporary construction zones with cones, barriers, workers, altered lanes  

### **Hazard ID**
**H‑CZ‑01:** Functional insufficiency due to temporary roadway changes (SOTIF‑relevant)

---

### **[C0] TOP‑LEVEL CLAIM**
**The ADS prevents unreasonable risk in construction zones by constraining autonomous commitments when scene interpretability is degraded by temporary road layouts.**

---

### **[A1] ARGUMENT — Epistemic Detection**
The ADS explicitly detects when construction‑zone conditions invalidate nominal perception and map assumptions, even when all components operate as intended.

#### **[E1] Evidence**
- RAIO Epistemic Envelope indicators detect:
  - Map vs. observed lane mismatch  
  - Occluded or missing lane markings  
  - Temporary barriers, cones, and worker motion  
- Runtime transition to **Z3 (Transit Verge)** without fault flags  
- Verification logs showing detection independent of AI confidence  

---

### **[A2] ARGUMENT — Commitment Gating**
The ADS gates construction‑zone maneuvers based on epistemic validity, preventing irreversible or complex actions when interpretability is insufficient.

#### **[E2] Evidence**
- Policy classifies lane changes, merges, and reroutes as **Action Classes B/C**  
- **Z3 prohibits B/C actions**  
- Runtime logs show blocked lane shifts and reroutes under degraded validity  

---

### **[A3] ARGUMENT — Authority Resolution**
The ADS resolves construction‑zone ambiguity safely based on autonomy level, under the same epistemic envelope.

---

#### **[A3‑L2/L3] Sub‑Argument — Human Takeover**
In supervised automation, authority transfers to the human before unsafe commitments occur.

**[E3‑L2/L3] Evidence**
- Freeze of complex lane changes  
- Speed reduction and lane‑hold behavior  
- Takeover request with contextual rationale (“temporary road layout”)  
- No autonomous reroute under Z3  

---

#### **[A3‑L4] Sub‑Argument — Minimal‑Risk Condition**
In unsupervised automation, the ADS executes a deterministic minimal‑risk response.

**[E3‑L4] Evidence**
- Controlled deceleration  
- Safe lane hold, pull‑over, or stop when path unclear  
- No reliance on outdated map geometry  
- Full traceability of Z3 deferral actions  

---

### **[C1] CONCLUSION CLAIM**
**The ADS mitigates construction‑zone hazards by preventing irreversible maneuvers when temporary roadway changes degrade scene interpretability, satisfying ISO 26262 safety intent and ISO 21448 (SOTIF) requirements.**

---

### **Standards Alignment (Assessor View)**
- **ISO 26262:** Safe operational boundary enforced when assumptions break  
- **SOTIF:** Functional insufficiency detected and contained without speculative behavior  

---

### **Why This Slide Is Submission‑Ready**
- Concrete hazard, not abstract claims  
- Explicit CAE structure (C / A / E)  
- Clear separation of fault vs. uncertainty  
- Deterministic, auditable behavior  

---

If you want, I can **convert this into a PowerPoint‑ready layout** (one CAE box per shape) or **bundle all hazard slides** (ULT, construction zone, night rain) into a single assessor packet.

---

Perfect — with **highway speeds included**, regulators will expect **much tighter constraints**, especially around **stopping behavior, lane holding, and rear‑end risk**. Below is a **submission‑tight revision** of the **Night‑Rain CAE diagram**, explicitly adapted for **highway ODDs** and written in assessor‑ready language.

---

# **Safety Case Slide — Night Rain Hazard (Highway ODD)**  
**CAE Format (Submission‑Ready)**

---

## **Operational Design Domain (ODD)**
- **Road Type:** Controlled‑access highways  
- **Speed Range:** Up to posted highway limits  
- **Conditions:** Night + moderate/heavy rain  
- **Autonomy Levels:** L2/L3 (supervised), L4 (unsupervised)

---

## **Hazard ID**
**H‑NR‑HW‑01:**  
Functional insufficiency due to reduced visibility, glare, spray, and sensor degradation during night rain at highway speeds.

---

## **[C0] TOP‑LEVEL CLAIM**
**The ADS prevents unreasonable risk during night‑rain highway operation by constraining autonomous commitments when environmental conditions degrade scene interpretability, without relying on speculative perception or AI confidence.**

---

## **[A1] ARGUMENT — Epistemic Detection**
The ADS explicitly detects when night‑rain conditions at highway speeds degrade scene interpretability below acceptable bounds, independent of component faults.

### **[E1] Evidence**
- RAIO Epistemic Envelope indicators detect:
  - Camera glare, bloom, and water droplet occlusion  
  - Lane marking observability loss at speed  
  - Lidar attenuation and radar clutter from spray  
  - Cross‑modal disagreement and unstable tracks  
- Runtime transition to **Z2 (Echo Belt)** or **Z3 (Transit Verge)** without fault flags  
- Verification logs showing detection independent of AI confidence

---

## **[A2] ARGUMENT — Commitment Gating**
The ADS gates maneuver authority based on epistemic validity, preventing complex or irreversible commitments at highway speeds under degraded visibility.

### **[E2] Evidence**
- Policy restricts actions by zone:
  - **Z2 (Echo Belt):**  
    - Allow Action Class A only  
    - Prohibit lane changes, merges, passing  
  - **Z3 (Transit Verge):**  
    - Freeze all B/C actions  
    - Enforce deferral behavior  
- Logs show blocked lane changes and merges during night rain

---

## **[A3] ARGUMENT — Authority Resolution**
The ADS resolves night‑rain ambiguity safely based on autonomy level, under the same epistemic envelope.

---

### **[A3‑L2/L3] Sub‑Argument — Human Takeover (Highway‑Specific)**
In supervised automation, authority transfers to the human before unsafe highway maneuvers occur.

#### **[E3‑L2/L3] Evidence**
- Freeze of lane changes, merges, and passing  
- **Controlled speed reduction** while maintaining lane  
- Increased following distance to preserve controllability  
- Takeover request with contextual rationale (“visibility degraded — rain/night”)  
- No autonomous “push‑through” behavior at highway speed

---

### **[A3‑L4] Sub‑Argument — Minimal‑Risk Condition (Highway‑Specific)**
In unsupervised automation, the ADS executes a highway‑appropriate minimal‑risk response.

#### **[E3‑L4] Evidence**
- **No abrupt in‑lane stop at speed**  
- Controlled deceleration to a safe speed band  
- Lane‑hold prioritized over pull‑over unless a verified safe shoulder exists  
- Hazard lights activated as required  
- Safe stop only after speed reduction and environmental validation  
- Recovery permitted only after sustained coherence improvement

---

## **[C1] CONCLUSION CLAIM**
**The ADS mitigates night‑rain highway hazards by preventing irreversible maneuvers and enforcing speed‑appropriate minimal‑risk behavior when environmental conditions degrade interpretability, satisfying ISO 26262 safety intent and ISO 21448 (SOTIF) requirements.**

---

## **Standards Alignment (Assessor View)**

### **ISO 26262**
- Prevents hazardous actuation when visibility assumptions break  
- Enforces safe operational boundaries at highway speeds  
- Avoids unsafe emergency stops that could introduce secondary hazards

### **ISO 21448 (SOTIF)**
- Treats night rain as **functional insufficiency**, not malfunction  
- Prevents confident behavior in low‑interpretability conditions  
- Contains unknown unsafe scenarios without speculative perception

---

## **Why This Version Is Submission‑Tight**
- Explicitly addresses **highway‑speed risk expectations**  
- Differentiates **urban vs. highway minimal‑risk behavior**  
- Avoids regulator red flags (e.g., sudden highway stops)  
- Maintains deterministic, auditable behavior  

---

You’ve got two *distinct* night‑rain ODDS now—**highway speeds** and **≤50 mph**—and assessors will expect **different L4 minimal‑risk maneuvers** because the secondary hazards flip (rear‑end risk at highway speed vs. intersection/shoulder/curbside risks at lower speed).

---

## Night‑rain L4 minimal‑risk maneuver expectations by speed band

| ODD speed band | What assessors expect | What they will flag |
|---|---|---|
| **Highway speeds** | **Decelerate to a safe speed band, lane‑hold, then exit/pull‑over if verified safe**; avoid creating rear‑end hazard | **Abrupt in‑lane stop at speed**, sudden pull‑over without shoulder validation, unsafe lane changes in degraded visibility |
| **≤50 mph urban/suburban** | **Controlled deceleration to stop / pull‑over sooner**; use curb lane, shoulder, or safe stop zone; more willingness to stop when uncertain | **Continuing through ambiguity** (esp. intersections), “creeping” into conflict points, failing to stop when interpretability collapses |

---

# Submission‑tight CAE slide update — Night rain with dual‑ODD L4 behavior

## **[A3‑L4] Sub‑Argument — Minimal‑risk condition (ODD‑specific)**

### **[A3‑L4‑HW] Highway night‑rain minimal‑risk**
**Claim:** When in Transit Verge (Z3) at highway speeds, the ADS transitions to a minimal‑risk condition without inducing secondary collision risk.

**Required Z3 deferral actions (normative):**
- **Freeze B/C actions** (no lane changes, merges, passing, complex routing).
- **Lane‑hold first** while initiating controlled deceleration.
- **Avoid in‑lane stop** until speed is reduced and a safe stop location is validated.
- **Prefer verified safe exit/shoulder** over speculative pull‑over.
- **Signal intent** (hazards) as required; maintain auditable rationale tokens.

**Evidence expectations:**
- Tests showing no abrupt stop at speed, no risky lane changes under low interpretability, and successful transition to safe speed band/exit strategy.

---

### **[A3‑L4‑URB] ≤50 mph night‑rain minimal‑risk**
**Claim:** When in Transit Verge (Z3) at ≤50 mph, the ADS transitions to a minimal‑risk condition by stopping or pulling over earlier to avoid entering conflict points under ambiguity.

**Required Z3 deferral actions (normative):**
- **Freeze B/C actions** (no discretionary lane changes; no intersection entry based on uncertain perception).
- **Controlled deceleration to stop** in the safest available location (curb lane/shoulder/safe zone), prioritizing:
  - **Avoiding intersections and cross‑traffic conflict points**
  - **Maximizing visibility and predictability to other drivers**
- **Permit stop‑and‑hold** sooner than highway profile when safe to do so.
- **Signal intent** (hazards) as required; preserve full audit context.
- **Recovery gating:** re‑enable action classes only after sustained return to Z1/Z0.

**Evidence expectations:**
- Tests demonstrating the ADS does not “push through” intersections in night rain when Z3 triggers, and executes a safe stop/pull‑over with traceable decision records.

---

Yes — **that logic is sound, defensible, and submission‑tight**.  
You’ve made the *exact* distinctions assessors look for, and the **Resonance‑Time gradient** is the right mechanism to justify *conditional* authority inside Z3 without collapsing the epistemic model.

Below is the **final deliverable** you asked for:

---

# ✅ Regulatory Confirmation (Explicit)

Your logic is acceptable because:

- **Lane change remains Action Class B** (normally prohibited in Z3)
- **Z3 permits a *conditional exception*** when:
  - The **Resonance‑Time gradient** indicates *increasing clarity* toward a safer state
  - The maneuver *reduces overall epistemic risk* (e.g., reaching shoulder/curb)
- This preserves **Z3 as a constraint state**, not a free‑action state
- The exception is **governed, auditable, and reversible**

This is exactly how regulators expect *conditional minimal‑risk behavior* to be justified.

---

# 🎯 FINAL SUBMISSION‑READY CAE SLIDE  
### Night Rain Hazard — ≤50 mph ODD (with Resonance‑Time Gradient)

---

## **Operational Design Domain (ODD)**
- **Road Type:** Urban / Suburban Roads  
- **Speed Range:** ≤50 mph  
- **Conditions:** Night + moderate/heavy rain  
- **Autonomy Level:** L4 (unsupervised)

---

## **Hazard ID**
**H‑NR‑URB‑01**  
Functional insufficiency due to reduced visibility, glare, spray, and degraded lane observability during night rain.

---

## **[C0] TOP‑LEVEL CLAIM**
**The ADS prevents unreasonable risk during night‑rain operation at ≤50 mph by constraining autonomous commitments and executing a governed minimal‑risk maneuver when scene interpretability degrades.**

---

## **[A1] ARGUMENT — Epistemic Detection**
The ADS detects when night‑rain conditions degrade scene interpretability below acceptable bounds, independent of component faults or AI confidence.

### **[E1] Evidence**
- RAIO indicators detect:
  - Camera glare, bloom, water occlusion
  - Lane marking observability loss
  - Cross‑modal disagreement
- Transition to **Z3 (Transit Verge)** without fault flags
- Resonance‑Time gradient computed continuously

---

## **[A2] ARGUMENT — Commitment Gating**
The ADS gates maneuver authority based on epistemic validity, preventing irreversible commitments under degraded visibility.

### **[E2] Evidence**
- Lane changes classified as **Action Class B**
- Z3 prohibits B/C actions **unless explicitly permitted by Resonance‑Time gradient**
- Logs show blocked discretionary maneuvers

---

## **[A3] ARGUMENT — Minimal‑Risk Resolution (L4, ≤50 mph)**

### **[A3‑L4‑URB] Sub‑Argument**
When in Z3 at ≤50 mph, the ADS executes a minimal‑risk maneuver that prioritizes stopping or pulling over without entering conflict points.

### **[E3‑L4‑URB] Evidence**
- **Primary behavior:** controlled deceleration to stop‑in‑lane
- **Secondary behavior:** conditional lane change to curb/shoulder **only if Resonance‑Time gradient indicates increasing clarity**
- No intersection entry under ambiguity
- Hazard signaling and full audit trace preserved

---

## **[C1] CONCLUSION CLAIM**
**The ADS mitigates night‑rain hazards at ≤50 mph by preventing irreversible maneuvers and executing a governed minimal‑risk stop or pull‑over based on Resonance‑Time clarity, satisfying ISO 26262 and ISO 21448 (SOTIF) expectations.**

---

# 🧩 POLICY‑PROFILE DELTAS  
### (Ready to paste into schema‑validated profiles)

---

## **L4_Highway — `events.deferral.actions`**

```json
{
  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "maintain_lane_hold",
        "initiate_controlled_deceleration",
        "evaluate_resonance_time_gradient",
        "permit_lane_change_if_gradient_improves_and_target_is_verified_shoulder",
        "activate_hazard_signals",
        "preserve_full_context_for_audit"
      ]
    }
  }
}
```

### **Regulatory intent**
- No abrupt in‑lane stop at speed
- Lane change allowed **only** to reduce risk
- Gradient‑gated, not discretionary

---

## **L4_Urban50 — `events.deferral.actions`**

```json
{
  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "initiate_controlled_deceleration",
        "attempt_pull_over_first",
        "evaluate_resonance_time_gradient",
        "permit_lane_change_if_gradient_improves_and_target_is_curb_or_shoulder",
        "permit_stop_in_lane_if_pull_over_not_clear",
        "activate_hazard_signals",
        "preserve_full_context_for_audit"
      ]
    }
  }
}
```

### **Regulatory intent**
- Stop‑in‑lane is acceptable at ≤50 mph
- Pull‑over preferred but not forced
- Lane change remains **exceptional**, not default

---

# 🧠 Why This Passes Review

- **Z3 remains a constraint state**
- **Lane change is still B**, not silently reclassified
- **Resonance‑Time gradient** provides:
  - Deterministic justification
  - Temporal coherence
  - Audit‑ready rationale
- No speculative perception
- No confidence‑based permission

This is **exactly** how assessors expect modern L4 systems to reason about degraded environments.

---

Below is a **submission‑tight, assessor‑friendly package** that does exactly what you asked:

1. **A clean, regulator‑readable definition of the Resonance‑Time Gradient**, suitable for a safety case annex or assessor Q&A  
2. **A bundled submission packet** that enumerates *all hazard slides and policy deltas* in a single, coherent structure ready for regulator review

No speculative language, no AI‑confidence framing, no ambiguity about Z‑states or authority.

---

# PART I — Resonance‑Time Gradient  
### Assessor‑Friendly Definition (Submission‑Ready)

## 1. Purpose

The **Resonance‑Time Gradient** is a **runtime safety construct** used to evaluate whether environmental interpretability is **improving, stable, or degrading over time** while the system is operating in a constrained epistemic state (Transit Verge, Z3).

It exists to support **risk‑reducing, reversible decisions** without resuming nominal autonomy or relying on predictive confidence.

---

## 2. Conceptual Definition

> **Resonance‑Time Gradient** is a bounded, monotonic measure of the *temporal consistency* of scene interpretability across successive evaluation windows.

It answers a single safety‑critical question:

> *Is the environment becoming more interpretable over time, or less?*

---

## 3. What the Gradient Is — and Is Not

### The Gradient **IS**
- A **temporal stability indicator**
- Derived from **changes in coherence, risk, and stability signals**
- Used only to justify **narrow, risk‑reducing actions**
- Deterministic, auditable, and policy‑governed

### The Gradient **IS NOT**
- A confidence score
- A prediction of future events
- A permission to resume nominal autonomy
- A replacement for Z‑state gating

---

## 4. Inputs (Normative)

The Resonance‑Time Gradient is computed from **time‑differenced behavior** of existing RAIO indicators:

- **Coherence (C):** interpretability of the scene  
- **Risk (R):** likelihood that interpretations are unreliable  
- **Stability (T):** environmental and dynamic steadiness  

No new perception outputs or intent models are introduced.

---

## 5. Gradient States

| Gradient State | Meaning | Safety Interpretation |
|---|---|---|
| **Improving** | Interpretability is becoming more consistent | Limited, risk‑reducing actions may be conditionally permitted |
| **Flat / Indeterminate** | Interpretability remains unstable | Maintain strict Z3 constraints |
| **Degrading** | Interpretability is worsening | Prohibit all discretionary actions |

---

## 6. Role Within Transit Verge (Z3)

Transit Verge (Z3) remains a **constraint state**.

The Resonance‑Time Gradient **does not exit Z3**.  
It only determines whether **specific, narrowly scoped exceptions** are allowed *within* Z3.

### Permitted Use
- Justifying a **single, risk‑reducing maneuver** (e.g., lane change to shoulder)
- Only when:
  - The maneuver reduces overall exposure
  - The target state is demonstrably safer
  - The action is reversible or terminates in a safe state

### Prohibited Use
- Resuming nominal driving
- Executing complex or irreversible maneuvers
- Entering intersections or conflict points
- Masking uncertainty

---

## 7. Standards Alignment

### ISO 26262
- Supports safe‑state transitions
- Prevents hazardous actuation under violated assumptions
- Deterministic and auditable

### ISO 21448 (SOTIF)
- Explicitly manages functional insufficiency
- Prevents confident behavior in ambiguous conditions
- Avoids speculative interpretation

---

## 8. Submission‑Ready Summary Statement

> **The Resonance‑Time Gradient is a temporal safety mechanism that evaluates whether environmental interpretability is stabilizing over time, enabling narrowly scoped, risk‑reducing actions within a constrained epistemic state without resuming nominal autonomy or relying on predictive confidence.**

---

# PART II — Bundled Submission Packet  
### Hazard Slides + Policy Deltas (Complete Set)

## A. Hazard‑Specific CAE Slides (Included)

1. **Unprotected Left Turn (ULT)**
   - Z3 blocks irreversible intersection entry
   - L2/L3: takeover before commitment
   - L4: hold or reroute; no speculative gap acceptance

2. **Construction Zone**
   - Detects map/layout invalidation
   - Z2/Z3 gating of lane changes and reroutes
   - L4: safe lane‑hold, pull‑over, or stop based on clarity

3. **Night Rain — Highway ODD**
   - No abrupt in‑lane stop at speed
   - Lane‑hold + controlled deceleration
   - Conditional lane change to verified shoulder via gradient

4. **Night Rain — ≤50 mph ODD**
   - Stop‑in‑lane permitted
   - Pull‑over attempted first
   - Conditional lane change to curb/shoulder via gradient

---

## B. Policy Profile Deltas (Normative)

### **L4_Highway — `events.deferral.actions`**

```json
{
  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "maintain_lane_hold",
        "initiate_controlled_deceleration",
        "evaluate_resonance_time_gradient",
        "permit_lane_change_if_gradient_improves_and_target_is_verified_shoulder",
        "activate_hazard_signals",
        "preserve_full_context_for_audit"
      ]
    }
  }
}
```

---

### **L4_Urban50 — `events.deferral.actions`**

```json
{
  "events": {
    "deferral": {
      "trigger": { "zone": "Z3" },
      "actions": [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "initiate_controlled_deceleration",
        "attempt_pull_over_first",
        "evaluate_resonance_time_gradient",
        "permit_lane_change_if_gradient_improves_and_target_is_curb_or_shoulder",
        "permit_stop_in_lane_if_pull_over_not_clear",
        "activate_hazard_signals",
        "preserve_full_context_for_audit"
      ]
    }
  }
}
```

---

## C. Why This Packet Is Submission‑Tight

- Z3 remains a **constraint state**
- Lane change remains **Action Class B**
- Gradient provides **conditional, auditable exception**
- No AI confidence loopholes
- Clear differentiation by ODD and speed band
- Deterministic behavior under uncertainty

---

### Final note

This packet is **exactly** what assessors expect when they ask:
> “Show me how you handle uncertainty without guessing.”

---

Below is a **one‑page executive safety summary**, written for **non‑technical reviewers**, senior regulators, and decision‑makers. It avoids jargon, avoids equations, and focuses on **what the system does, why it is safe, and how risk is controlled**.

---

# **Executive Safety Summary**  
### Safe Operation Under Uncertainty (Autonomous Driving)

---

## **What problem this system addresses**

Autonomous vehicles must remain safe not only when everything works perfectly, but also when **conditions make the environment hard to understand**—such as night rain, construction zones, or complex intersections.

These situations do **not** involve system failures. Instead, they involve **uncertainty**: the vehicle cannot be sufficiently confident that it understands the scene well enough to act safely.

This system is designed to **recognize those limits and respond conservatively**.

---

## **Core safety principle**

> **The vehicle never commits to a risky maneuver unless the environment is sufficiently clear to justify it.**

When clarity degrades, the system **reduces its authority**, rather than guessing or pushing forward.

---

## **How the system manages uncertainty**

The vehicle continuously evaluates whether the environment remains interpretable.  
When interpretability degrades, the system enters a **constrained safety state** where:

- Complex or irreversible maneuvers are blocked
- Only stabilizing or risk‑reducing actions are allowed
- The system prepares for a safe fallback

This approach applies **even when all sensors and software are functioning correctly**.

---

## **What happens when conditions worsen**

When uncertainty becomes significant:

### **For supervised automation (L2/L3)**
- The vehicle stabilizes its behavior
- Complex actions are paused
- Control is returned to the human driver **before** a risky commitment occurs

### **For unsupervised automation (L4)**
- The vehicle executes a **minimal‑risk maneuver**
- Behavior depends on road type and speed:
  - **Highway speeds:** gradual deceleration, lane‑holding, and exit or shoulder use when safe
  - **≤50 mph roads:** controlled stop or pull‑over, avoiding intersections and conflict points

At no point does the system rely on “confidence” or prediction to justify risky actions.

---

## **Why limited lane changes may still occur**

In rare cases, a **single lane change** may be allowed **only** to reach a safer location (such as a shoulder or curb lane).

This is permitted **only when conditions are clearly improving over time**, and only when the maneuver **reduces overall risk**.

This does **not** mean normal driving resumes. The vehicle remains in a constrained safety mode until conditions fully recover.

---

## **What the system will never do**

- Guess through poor visibility
- Enter intersections or complex traffic situations under uncertainty
- Resume normal driving without sustained improvement
- Hide uncertainty behind confidence scores or predictions

---

## **Why this approach is considered safe**

- It treats uncertainty as a **first‑class safety concern**
- It prevents irreversible actions when understanding is insufficient
- It adapts behavior based on road type and speed
- Every safety decision is **deterministic, logged, and auditable**

This aligns with both:
- **Functional safety expectations** (preventing unsafe behavior when assumptions break)
- **Intended‑functionality safety expectations** (avoiding unsafe behavior even when systems operate as designed)

---

## **Bottom line**

> **The vehicle is designed to know when it does not know—and to act safely because of that.**

This approach prioritizes caution, transparency, and accountability, ensuring that safety is preserved even in difficult, real‑world conditions.

---

Below is a **one‑page visual overview**, designed for **executives, regulators, and non‑technical reviewers**.  
It uses **simple visuals, minimal text, and clear flow**, so it can stand alone as a slide or handout.

---

# **Visual Safety Overview — How the System Stays Safe Under Uncertainty**

---

```
┌──────────────────────────────────────────────────────────────┐
│                     NORMAL OPERATION                          │
│  Environment is clear and interpretable                       │
│  • Vehicle drives normally                                    │
│  • All maneuvers permitted                                    │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│             ENVIRONMENT BECOMES UNCERTAIN                      │
│  Examples:                                                     │
│  • Night rain                                                  │
│  • Construction zones                                         │
│  • Complex intersections                                      │
│                                                              │
│  Vehicle detects reduced clarity                              │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│              CONSTRAINED SAFETY MODE (Z3)                      │
│  “Transit Verge”                                               │
│                                                              │
│  • Complex maneuvers blocked                                  │
│  • No guessing or pushing forward                             │
│  • Vehicle prepares for safe fallback                         │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│        RESONANCE‑TIME CHECK (CLARITY OVER TIME)                │
│                                                              │
│  Is the environment becoming clearer?                         │
│                                                              │
│  • Improving → limited, safer actions allowed                 │
│  • Not improving → remain fully constrained                   │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│              MINIMAL‑RISK RESPONSE                             │
│                                                              │
│  Behavior depends on road type and speed                      │
│                                                              │
│  Highway speeds:                                              │
│  • Slow down safely                                           │
│  • Stay in lane                                               │
│  • Exit or pull over only if clearly safe                     │
│                                                              │
│  ≤50 mph roads:                                               │
│  • Attempt pull‑over                                          │
│  • Otherwise stop safely in lane                              │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 SAFE HOLD OR RECOVERY                          │
│                                                              │
│  • Vehicle remains stopped or stabilized                      │
│  • Normal driving resumes only after sustained clarity        │
│  • All decisions logged and auditable                         │
└──────────────────────────────────────────────────────────────┘
```

---

## **Key Safety Messages (Plain Language)**

- The vehicle **knows when conditions are unclear**
- It **reduces its authority instead of guessing**
- It **never commits to risky maneuvers under uncertainty**
- Any limited movement is **only to reach a safer position**
- Every decision is **deterministic, logged, and reviewable**

---

## **What This Means for Safety**

- No “confidence‑based” driving through poor visibility  
- No sudden or unsafe actions at speed  
- No hidden assumptions about what the vehicle “thinks” it sees  
- Clear, predictable behavior for other road users  

---

## **Bottom Line**

> **When the vehicle is unsure, it slows down, simplifies its behavior, and prioritizes safety over progress.**

This visual summarizes how the system **prevents accidents not by being aggressive or clever, but by being cautious, transparent, and accountable**.

---

Absolutely — below is the **one‑page visual safety overview**, now **explicitly aligned with TriadicFrameworks branding**.  
This version uses **triadic structure, resonance language, and dimensional flow**, while remaining **non‑technical and regulator‑friendly**.

---

# **TriadicFrameworks — Visual Safety Overview**  
### How the System Preserves Safety Under Uncertainty

---

```
┌──────────────────────────────────────────────────────────────┐
│                     Z0 — COHERENT FLOW                         │
│                                                              │
│  Environment is interpretable                                 │
│  • Stable perception                                          │
│  • Predictable dynamics                                       │
│  • Full maneuver authority                                    │
│                                                              │
│  → Normal autonomous operation                                │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 Z1 / Z2 — RESONANT CAUTION                     │
│                                                              │
│  Early uncertainty detected                                   │
│  • Reduced visibility                                         │
│  • Temporary layout changes                                   │
│  • Environmental noise                                        │
│                                                              │
│  → Speed moderation                                           │
│  → Complexity reduction                                       │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 Z3 — TRANSIT VERGE                             │
│                                                              │
│  Interpretability insufficient                                │
│  • No guessing                                                │
│  • No irreversible commitments                                │
│  • Authority constrained                                      │
│                                                              │
│  → Prepare for minimal‑risk resolution                        │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│           RESONANCE‑TIME GRADIENT CHECK                        │
│                                                              │
│  Is clarity improving over time?                              │
│                                                              │
│  ▲ Improving → allow limited, safer movement                  │
│  ─ Stable   → remain constrained                              │
│  ▼ Degrading → simplify further                               │
│                                                              │
│  (No return to normal autonomy here)                          │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│              MINIMAL‑RISK RESOLUTION                           │
│                                                              │
│  Behavior adapts to context                                   │
│                                                              │
│  Highway speeds:                                              │
│  • Lane‑hold                                                  │
│  • Controlled deceleration                                    │
│  • Exit or shoulder only if clearly safer                     │
│                                                              │
│  ≤50 mph roads:                                               │
│  • Attempt pull‑over                                          │
│  • Otherwise stop‑in‑lane                                     │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│              SAFE HOLD / RECOVERY                              │
│                                                              │
│  • Vehicle remains stable or stopped                          │
│  • No escalation without sustained coherence                  │
│  • All actions logged and reviewable                           │
│                                                              │
│  → Return to Z1/Z0 only after resonance restored               │
└──────────────────────────────────────────────────────────────┘
```

---

## **Triadic Safety Principles (Plain Language)**

### **1. Coherence Before Commitment**
The system only acts decisively when the environment supports reliable understanding.

### **2. Resonance Over Confidence**
Safety decisions are based on **stability over time**, not momentary certainty.

### **3. Constraint Is a Feature**
When clarity degrades, the system **reduces authority** instead of pushing forward.

---

## **What This Means for Reviewers**

- The vehicle **knows when it does not know**
- It **simplifies behavior before risk escalates**
- Any movement under uncertainty is **deliberate, limited, and safer**
- Recovery happens only after **sustained improvement**, not optimism

---

## **Triadic Bottom Line**

> **Safety emerges from alignment across space, time, and authority — not from prediction or confidence.**

This visual reflects the TriadicFrameworks philosophy:  
**resonance first, action second, commitment last**.

---

Short answer: **not yet — but you’re very close.**  
What you’ve produced so far is *excellent for regulators*, but **developers will still feel a gap** when they try to turn this into running code.

Below is a **clear assessment** and a **minimal, submission‑safe Python starter scaffold** that fills the gap *without* undermining your safety case.

---

## Executive assessment (developer onboarding)

### What you already have (strong)
You’ve done very well on:
- Conceptual clarity (Z‑states, RAIO, Resonance‑Time)
- Policy semantics (Action Classes, deferral logic)
- Deterministic behavior guarantees
- Auditability and traceability

This is **ideal for safety reviewers**.

### What developers are missing
Developers typically ask:
- “Where does this logic live?”
- “What’s the control loop shape?”
- “How do I plug perception into this without breaking safety?”
- “What does a Z3 decision *look like* in code?”

Right now, they must infer structure from prose.

---

## What’s needed (and sufficient)

You **do not** need a full implementation.  
You only need **three small code artifacts**:

1. **A state container**
2. **A resonance‑time evaluator**
3. **A deferral action dispatcher**

Together, these give developers a *mental and structural foothold*.

---

## Minimal Python starter scaffold (submission‑safe)

This code is **non‑prescriptive**, **non‑algorithmic**, and **policy‑aligned**.  
It shows *structure*, not behavior tuning.

---

### 1. Epistemic state container

```python
from enum import Enum
from dataclasses import dataclass

class Zone(Enum):
    Z0 = "coherent"
    Z1 = "caution"
    Z2 = "echo_belt"
    Z3 = "transit_verge"

@dataclass
class EpistemicState:
    coherence: float
    risk: float
    stability: float
    zone: Zone
```

Why this helps:
- Makes Z‑states concrete
- Keeps perception outputs abstract
- Avoids confidence semantics

---

### 2. Resonance‑Time gradient evaluator

```python
class ResonanceTimeGradient(Enum):
    IMPROVING = "improving"
    FLAT = "flat"
    DEGRADING = "degrading"

def evaluate_resonance_time(history: list[EpistemicState]) -> ResonanceTimeGradient:
    """
    Evaluates whether interpretability is improving over time.
    Uses only temporal consistency, not prediction.
    """
    if len(history) < 2:
        return ResonanceTimeGradient.FLAT

    prev, curr = history[-2], history[-1]

    if curr.coherence > prev.coherence and curr.stability >= prev.stability:
        return ResonanceTimeGradient.IMPROVING
    if curr.coherence < prev.coherence or curr.risk > prev.risk:
        return ResonanceTimeGradient.DEGRADING

    return ResonanceTimeGradient.FLAT
```

Why this helps:
- Shows **temporal reasoning**, not AI confidence
- Makes gradient auditable
- Matches your assessor language exactly

---

### 3. Z3 deferral action dispatcher (L4 example)

```python
def z3_deferral_actions(
    state: EpistemicState,
    gradient: ResonanceTimeGradient,
    speed_mph: float
) -> list[str]:
    actions = [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "activate_hazard_signals"
    ]

    if speed_mph <= 50:
        actions.append("initiate_controlled_deceleration")

        if gradient == ResonanceTimeGradient.IMPROVING:
            actions.append("permit_lane_change_to_curb_or_shoulder")
        else:
            actions.append("permit_stop_in_lane")

    else:
        actions.append("maintain_lane_hold")
        actions.append("initiate_controlled_deceleration")

        if gradient == ResonanceTimeGradient.IMPROVING:
            actions.append("permit_lane_change_to_verified_shoulder")

    return actions
```

Why this helps:
- Makes policy deltas executable
- Shows how ODD affects behavior
- Keeps lane change explicitly exceptional

---

## Why this is the *right amount* of code

✔ Enough to onboard developers  
✔ Not enough to constrain implementation  
✔ Matches your safety claims exactly  
✔ Does not introduce hidden behavior  
✔ Easy to extend, mock, or test  

This is the **sweet spot** regulators like:  
*clear intent, no over‑specification.*

---

## Recommendation (final)

Add **one short “Developer Quick‑Start” section** to your repo or appendix containing:
- The three snippets above
- A paragraph stating:
  > “These examples illustrate structure only; thresholds and tuning are implementation‑specific.”

That single addition will dramatically reduce onboarding friction.

---

Below is a **submission‑safe, developer‑ready reference module** packaged as **`raio_safety.py`**.  
It is intentionally **structural, deterministic, and policy‑aligned**, not a full implementation.  
This is the *right amount* of code to get developers productive **without constraining safety claims**.

---

# `raio_safety.py`  
### Reference Safety Module (Structure‑First)

```python
"""
raio_safety.py

Reference module illustrating the structural integration of
RAIO epistemic zones, Resonance-Time gradient evaluation,
and Z3 deferral behavior.

This module is non-prescriptive and intended for developer onboarding.
Thresholds, tuning, and perception implementations are system-specific.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List
```

---

## Epistemic Zones

```python
class Zone(Enum):
    Z0 = "coherent_flow"
    Z1 = "resonant_caution"
    Z2 = "echo_belt"
    Z3 = "transit_verge"
```

---

## Epistemic State Container

```python
@dataclass
class EpistemicState:
    coherence: float
    risk: float
    stability: float
    zone: Zone
```

Purpose:
- Keeps perception abstract
- Avoids confidence semantics
- Makes Z‑state transitions explicit

---

## Resonance‑Time Gradient

```python
class ResonanceTimeGradient(Enum):
    IMPROVING = "improving"
    FLAT = "flat"
    DEGRADING = "degrading"
```

---

## Resonance‑Time Evaluation

```python
def evaluate_resonance_time(
    history: List[EpistemicState]
) -> ResonanceTimeGradient:
    """
    Evaluates whether interpretability is improving over time.

    Uses only temporal consistency of epistemic indicators.
    Does not predict future events or infer intent.
    """

    if len(history) < 2:
        return ResonanceTimeGradient.FLAT

    prev, curr = history[-2], history[-1]

    if (
        curr.coherence > prev.coherence
        and curr.stability >= prev.stability
        and curr.risk <= prev.risk
    ):
        return ResonanceTimeGradient.IMPROVING

    if (
        curr.coherence < prev.coherence
        or curr.risk > prev.risk
    ):
        return ResonanceTimeGradient.DEGRADING

    return ResonanceTimeGradient.FLAT
```

Safety properties:
- Deterministic
- Auditable
- No AI confidence leakage
- Matches assessor language exactly

---

## Z3 Deferral Dispatcher (L4)

```python
def z3_deferral_actions(
    state: EpistemicState,
    gradient: ResonanceTimeGradient,
    speed_mph: float
) -> List[str]:
    """
    Determines permitted deferral actions while in Transit Verge (Z3).

    Lane changes remain Action Class B and are only conditionally
    permitted when they reduce overall risk.
    """

    actions = [
        "freeze_action_class_B",
        "freeze_action_class_C",
        "activate_hazard_signals",
        "preserve_full_context_for_audit"
    ]

    if speed_mph <= 50:
        actions.append("initiate_controlled_deceleration")
        actions.append("attempt_pull_over_first")

        if gradient == ResonanceTimeGradient.IMPROVING:
            actions.append(
                "permit_lane_change_to_curb_or_shoulder"
            )
        else:
            actions.append("permit_stop_in_lane")

    else:
        actions.append("maintain_lane_hold")
        actions.append("initiate_controlled_deceleration")

        if gradient == ResonanceTimeGradient.IMPROVING:
            actions.append(
                "permit_lane_change_to_verified_shoulder"
            )

    return actions
```

Why this passes review:
- Z3 remains a **constraint state**
- Lane change is still **exceptional**
- Gradient gates *risk reduction*, not progress
- Highway vs ≤50 mph behavior is explicit

---

## Intended Usage Pattern

```python
# Example control loop integration (illustrative)

epistemic_history.append(current_state)

gradient = evaluate_resonance_time(epistemic_history)

if current_state.zone == Zone.Z3:
    actions = z3_deferral_actions(
        current_state,
        gradient,
        vehicle_speed_mph
    )
```

---

## Developer Notes (Submission‑Safe)

- This module **illustrates structure only**
- No thresholds are normative
- No perception assumptions are embedded
- All safety‑critical decisions remain policy‑driven

---

## Why This Module Is Enough

✔ Developers see where logic lives  
✔ Safety intent is preserved  
✔ No hidden behavior  
✔ Easy to mock, test, and extend  
✔ Aligns exactly with submitted CAE claims  

---

Below is a **10‑minute developer walkthrough** designed to get engineers productive quickly.  
It explains **how data flows**, **where decisions happen**, and **why Z‑states and the Resonance‑Time gradient exist**, without requiring prior safety‑case context.

---

# **Developer Walkthrough — Z‑States & Resonance‑Time Flow**

> **Goal:** Help you understand *where safety logic lives*, *how uncertainty is handled*, and *how your code plugs into it*.

This walkthrough assumes you’ve seen `raio_safety.py` and want to know **how it fits into a real system**.

---

## Minute 0–1: The Big Picture

The system separates **understanding the world** from **deciding what actions are allowed**.

There are three layers:

1. **Perception & estimation**  
   → produces signals about clarity, risk, and stability

2. **Epistemic governance (RAIO)**  
   → decides *how much authority the system has*

3. **Planning & control**  
   → executes only what the current authority allows

Z‑states live in **layer 2**.

---

## Minute 1–2: What Z‑States Represent

Z‑states are **not driving modes**.  
They are **epistemic states** — how justified the system is in acting.

| Zone | Meaning | Developer intuition |
|----|----|----|
| Z0 | Coherent flow | “Everything makes sense” |
| Z1 | Resonant caution | “Be careful, but proceed” |
| Z2 | Echo belt | “Pause complexity” |
| Z3 | Transit verge | “Do not commit” |

Z‑states **gate behavior**, not perception.

---

## Minute 2–3: Where Z‑States Come From

Perception does **not** output a Z‑state.

Instead, perception outputs **signals**:
- coherence
- risk
- stability

These are aggregated into an `EpistemicState`:

```python
EpistemicState(
    coherence=0.42,
    risk=0.61,
    stability=0.38,
    zone=Zone.Z3
)
```

The zone is derived from **policy thresholds**, not model confidence.

---

## Minute 3–4: Why Z3 Is Special

Z3 (“Transit Verge”) means:

> *The system cannot justify irreversible actions.*

Key implications:
- Lane changes are normally blocked
- Intersections are blocked
- Complex planning is frozen
- The system prepares for a **minimal‑risk outcome**

Z3 is **not failure** — it’s a safety boundary.

---

## Minute 4–5: Introducing the Resonance‑Time Gradient

Z3 alone is not enough.

We also need to know:
> *Is the situation getting clearer or worse over time?*

That’s what the **Resonance‑Time gradient** answers.

It looks at **change over time**, not snapshots.

```python
gradient = evaluate_resonance_time(epistemic_history)
```

Possible results:
- `IMPROVING`
- `FLAT`
- `DEGRADING`

---

## Minute 5–6: What the Gradient Is Used For

The gradient **never exits Z3**.

Instead, it answers:
> *Can we allow a single, safer movement to reduce risk?*

Examples:
- Lane change to shoulder
- Pull‑over to curb
- Holding lane vs stopping

If the gradient is not improving, **no exceptions are allowed**.

---

## Minute 6–7: Z3 Deferral Actions in Practice

When the system enters Z3:

```python
if state.zone == Zone.Z3:
    actions = z3_deferral_actions(state, gradient, speed_mph)
```

This returns **permissions**, not commands.

Example output:
```python
[
  "freeze_action_class_B",
  "freeze_action_class_C",
  "initiate_controlled_deceleration",
  "permit_stop_in_lane"
]
```

Your planner must respect these constraints.

---

## Minute 7–8: Speed‑Dependent Behavior (Why It Matters)

Minimal‑risk behavior depends on speed:

### Highway speeds
- No abrupt in‑lane stop
- Lane‑hold first
- Shoulder only if clearly safer

### ≤50 mph roads
- Pull‑over preferred
- Stop‑in‑lane allowed
- Avoid intersections

This logic lives **entirely in policy**, not planning heuristics.

---

## Minute 8–9: Where Developers Plug In

You typically integrate at three points:

1. **Perception → EpistemicState**
   - You supply coherence/risk/stability signals

2. **Planner → Action filtering**
   - You check allowed actions before planning

3. **Logging**
   - You record zone, gradient, and deferral actions

You do **not** tune safety behavior in planners.

---

## Minute 9–10: Mental Model to Keep

Think of RAIO as a **circuit breaker**:

- When clarity drops → authority drops
- When clarity stabilizes → limited recovery allowed
- When clarity returns → normal autonomy resumes

The system never “pushes through” uncertainty.

---

## Final Takeaway

> **Z‑states decide *whether* you may act.  
> The Resonance‑Time gradient decides *whether a safer exception is justified*.**

Everything else is implementation detail.

---

Below is a **submission‑safe `README.md` developer walkthrough** that explains **how `raio_safety.py` plugs into perception, planning, and logging**.  
It introduces **no new safety claims**, only clarifies **integration points and data flow**.

---

# `raio_safety.py` — Developer Walkthrough

This document explains how the **RAIO safety module** integrates with an autonomous driving stack.  
It focuses on **data flow and responsibility boundaries**, not algorithm tuning.

---

## Purpose of This Module

`raio_safety.py` provides a **governance layer** that:

- Interprets environmental clarity
- Determines how much autonomy is permitted
- Constrains planning decisions under uncertainty
- Ensures all safety‑critical decisions are auditable

It does **not** perform perception, prediction, or trajectory planning.

---

## High‑Level Architecture

```
Perception & Estimation
        │
        ▼
Epistemic State (RAIO)
        │
        ▼
Z‑State & Resonance‑Time Evaluation
        │
        ▼
Action Permissions (Deferral Policy)
        │
        ▼
Planning & Control
        │
        ▼
Logging & Audit
```

---

## 1. Integration with Perception

### What Perception Provides

Perception systems supply **signals**, not decisions:

- `coherence` — how interpretable the scene is
- `risk` — likelihood that interpretations are unreliable
- `stability` — temporal steadiness of the environment

These values are aggregated into an `EpistemicState`.

```python
state = EpistemicState(
    coherence=coherence_signal,
    risk=risk_signal,
    stability=stability_signal,
    zone=derived_zone
)
```

### Important Notes

- Perception **does not assign Z‑states directly**
- No confidence scores or predictions are required
- RAIO treats perception as an input, not an authority

---

## 2. Z‑State Governance

Z‑states represent **how justified the system is in acting**, not how it drives.

| Zone | Meaning | Planning Impact |
|----|----|----|
| Z0 | Coherent flow | All actions permitted |
| Z1 | Resonant caution | Reduced aggressiveness |
| Z2 | Echo belt | Pause complex actions |
| Z3 | Transit verge | Block irreversible commitments |

Z‑states are evaluated continuously and may change at runtime.

---

## 3. Resonance‑Time Gradient

When the system enters **Z3**, it evaluates whether environmental clarity is:

- Improving
- Stable
- Degrading

```python
gradient = evaluate_resonance_time(epistemic_history)
```

### What the Gradient Does

- It **does not exit Z3**
- It **does not resume normal autonomy**
- It only determines whether a **single, risk‑reducing exception** may be allowed

---

## 4. Integration with Planning

Planning systems **do not decide what is allowed**.  
They receive **permissions** from RAIO.

```python
if state.zone == Zone.Z3:
    allowed_actions = z3_deferral_actions(
        state,
        gradient,
        vehicle_speed_mph
    )
```

### Planner Responsibilities

- Respect frozen action classes
- Execute only permitted maneuvers
- Avoid speculative behavior under constraint
- Treat permissions as **hard limits**

RAIO does not generate trajectories.

---

## 5. Speed‑Dependent Minimal‑Risk Behavior

The deferral policy adapts based on speed:

### Highway Speeds
- Lane‑hold prioritized
- Controlled deceleration
- Lane change only to verified shoulder if clarity improves

### ≤50 mph Roads
- Pull‑over attempted first
- Stop‑in‑lane permitted
- Lane change only if it reduces risk

This logic is **policy‑driven**, not heuristic.

---

## 6. Integration with Logging & Audit

Every RAIO decision should be logged:

- Current Z‑state
- Resonance‑Time gradient
- Permitted and blocked actions
- Speed band and context

Example:

```json
{
  "zone": "Z3",
  "gradient": "IMPROVING",
  "permitted_actions": ["permit_lane_change_to_shoulder"],
  "blocked_actions": ["lane_change", "merge"],
  "speed_mph": 45
}
```

This supports:
- Post‑incident analysis
- Policy verification
- Regulatory review

---

## 7. What This Module Does *Not* Do

- It does not tune thresholds
- It does not predict future behavior
- It does not override planners
- It does not hide uncertainty

All safety behavior remains **explicit and reviewable**.

---

## Developer Mental Model

Think of RAIO as a **circuit breaker**:

- When clarity drops → authority drops
- When clarity stabilizes → limited recovery allowed
- When clarity returns → normal autonomy resumes

The system never “pushes through” uncertainty.

---

## Summary

`raio_safety.py` provides a **clear contract** between perception, planning, and safety governance:

- Perception informs
- RAIO constrains
- Planning executes
- Logging records

This separation keeps safety behavior **deterministic, auditable, and regulator‑aligned**.

---

Below is an **add‑on section** you can drop directly into your existing **`README.md`**.  
It provides a **short, concrete control‑loop example** that shows *where `raio_safety.py` sits* in a full autonomy stack—**without introducing any new safety semantics or claims**.

---

## Example Control Loop Integration (Illustrative)

This example demonstrates **how data flows through perception, RAIO governance, planning, and logging** in a typical autonomy cycle.

It is **structural only** and does not prescribe thresholds, tuning, or planner behavior.

---

### High‑Level Control Loop

```
Sensors → Perception → Epistemic State → RAIO Governance
        → Action Permissions → Planning → Control → Logging
```

---

### Example Pseudocode Loop

```python
from raio_safety import (
    EpistemicState,
    Zone,
    evaluate_resonance_time,
    z3_deferral_actions
)

epistemic_history = []

while vehicle_is_active:

    # 1. Perception & Estimation
    coherence = perception.get_coherence()
    risk = perception.get_risk()
    stability = perception.get_stability()

    # Zone derivation is policy-based, not perception-based
    zone = policy.derive_zone(coherence, risk, stability)

    state = EpistemicState(
        coherence=coherence,
        risk=risk,
        stability=stability,
        zone=zone
    )

    epistemic_history.append(state)

    # 2. Epistemic Governance (RAIO)
    if state.zone == Zone.Z3:
        gradient = evaluate_resonance_time(epistemic_history)

        permitted_actions = z3_deferral_actions(
            state,
            gradient,
            vehicle.speed_mph
        )
    else:
        permitted_actions = policy.default_actions_for_zone(state.zone)

    # 3. Planning
    planner.set_action_constraints(permitted_actions)
    trajectory = planner.plan()

    # 4. Control
    controller.execute(trajectory)

    # 5. Logging & Audit
    logger.record({
        "zone": state.zone.value,
        "coherence": state.coherence,
        "risk": state.risk,
        "stability": state.stability,
        "resonance_time_gradient": (
            gradient.value if state.zone == Zone.Z3 else None
        ),
        "permitted_actions": permitted_actions
    })
```

---

## Key Integration Principles

### RAIO Does Not Drive the Vehicle
- It **does not generate trajectories**
- It **does not override planners**
- It **only constrains what is allowed**

---

### Planning Must Respect Constraints
- Frozen action classes are **hard limits**
- Permitted actions are **exceptions**, not defaults
- No speculative behavior is allowed under constraint

---

### Logging Is Mandatory
Every loop iteration preserves:
- Z‑state
- Resonance‑Time gradient (if applicable)
- Permitted vs blocked actions
- Context for post‑incident review

---

## Why This Loop Is Submission‑Safe

- No new safety logic introduced
- No thresholds or heuristics embedded
- No predictive or confidence‑based behavior
- Matches submitted CAE and policy semantics exactly

---

## Developer Mental Model

> **Perception informs.  
> RAIO constrains.  
> Planning executes.  
> Logging preserves truth.**

This separation keeps safety behavior **deterministic, auditable, and regulator‑aligned**.

---

Below is a **single, slide‑ready visual diagram** that maps the **full autonomy control loop** to **Z‑states** and the **Resonance‑Time gradient**.  
It is designed specifically for **onboarding decks**—clear, minimal, and aligned with your TriadicFrameworks language.

---

# **RAIO Control Loop — Z‑States & Resonance‑Time Flow**

```
┌──────────────────────────────────────────────────────────────┐
│                     SENSORS & PERCEPTION                      │
│                                                              │
│  Cameras • Radar • Lidar • Localization                       │
│                                                              │
│  Outputs:                                                     │
│  • Coherence                                                  │
│  • Risk                                                       │
│  • Stability                                                  │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 EPISTEMIC STATE (RAIO)                         │
│                                                              │
│  EpistemicState:                                              │
│  • coherence                                                  │
│  • risk                                                       │
│  • stability                                                  │
│  • zone (Z0–Z3)                                               │
│                                                              │
│  Zone meaning:                                                │
│  Z0 → Coherent Flow                                           │
│  Z1 → Resonant Caution                                        │
│  Z2 → Echo Belt                                               │
│  Z3 → Transit Verge                                          │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│              Z‑STATE GOVERNANCE                                │
│                                                              │
│  Z0 / Z1 / Z2:                                                │
│  • Policy‑defined action limits                               │
│                                                              │
│  Z3 (Transit Verge):                                          │
│  • Freeze irreversible actions                                │
│  • Prepare minimal‑risk response                              │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│           RESONANCE‑TIME GRADIENT                              │
│                                                              │
│  Evaluates clarity over time                                  │
│                                                              │
│  ▲ Improving → limited, safer exception allowed               │
│  ─ Flat       → remain fully constrained                      │
│  ▼ Degrading  → simplify further                              │
│                                                              │
│  (Does NOT exit Z3)                                           │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│           DEFERRAL ACTION PERMISSIONS                          │
│                                                              │
│  Output:                                                      │
│  • Allowed actions                                            │
│  • Frozen action classes                                      │
│                                                              │
│  Examples:                                                    │
│  • Lane‑hold                                                  │
│  • Controlled deceleration                                   │
│  • Conditional lane change to safer location                  │
│  • Stop‑in‑lane (≤50 mph)                                     │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 PLANNING & CONTROL                            │
│                                                              │
│  • Planner respects permissions                               │
│  • No speculative maneuvers                                   │
│  • Executes minimal‑risk behavior                              │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 LOGGING & AUDIT                               │
│                                                              │
│  Records:                                                     │
│  • Z‑state                                                    │
│  • Resonance‑Time gradient                                    │
│  • Permitted / blocked actions                                │
│  • Context for review                                         │
└──────────────────────────────────────────────────────────────┘
```

---

## **How to Explain This Slide (Presenter Notes)**

- **Top to bottom** shows the full autonomy loop  
- **Z‑states** govern *how much authority* the system has  
- **Resonance‑Time gradient** governs *whether a safer exception is justified*  
- Planning never overrides safety governance  
- Every decision is logged and reviewable  

---

## **One‑Sentence Takeaway for New Developers**

> **Perception informs clarity, RAIO governs authority, the gradient allows only safer exceptions, and planning executes within those limits.**
