# 🔌 Media Substrate Adapters

Adapters provide the bridge between **raw external signals** and the **Media Substrate Model (MSM)**. They convert platform data, text streams, narrative structures, or distribution graphs into the MSM’s structural primitives:

- MediaVector  
- MediaInvariantState  
- MediaBasinResult  
- MediaModeState  
- MediaDrift  
- MediaTransition  

Adapters allow the MSM Analyzer, Observer, and Simulation Engine to operate on any media ecosystem—social platforms, news environments, narrative corpora, or synthetic simulations.

---

## 🧱 Adapter Purpose

Media ecosystems are diverse: text, video, platform metrics, engagement graphs, narrative structures, distribution networks. The MSM cannot assume a single input format. Adapters solve this by:

- Translating raw signals into the five‑axis vector `[S, D, A, N, T]`
- Extracting metadata relevant to media physics
- Providing optional narrative or semantic hints
- Normalizing heterogeneous inputs into a consistent substrate representation

Adapters do **not** interpret content or ideology. They map structure, not meaning.

---

## 🧩 Core Adapter Interface

All MSM adapters implement a minimal, substrate‑honest interface:

```ts
interface MediaAdapter {
  toVector(input: unknown): MediaVector;

  getMetadata?(input: unknown): Record<string, any>;

  getNarrativeSignals?(input: unknown): {
    coherence?: number;
    conflict?: number;
    volatility?: number;
  };
}
```

### Required
- **toVector** — converts raw input into the five‑axis MediaVector.

### Optional
- **getMetadata** — returns contextual information (platform, timestamps, topology hints).
- **getNarrativeSignals** — provides semantic stability hints (coherence, conflict, volatility).

Adapters may implement only what they need.

---

## 📐 MediaVector Schema

```ts
type MediaVector = {
  S: number; // Signal Integrity
  D: number; // Distribution Topology
  A: number; // Attention Dynamics
  N: number; // Narrative Coherence
  T: number; // Temporal Cadence
};
```

All values normalized to `[0,1]`.

---

## 🧭 Invariant State Schema

```ts
type MediaInvariantState = {
  signalNarrativeCoherence: number;
  distributionAttentionFit: number;
  temporalSignalStability: number;
  attentionNarrativeFeedback: number;
};
```

Each value represents strain (0 = aligned, 1 = broken).

---

## 🌀 Basin Classification Schema

```ts
type MediaBasinResult = {
  basin: "Broadcast" | "Network" | "Fragment" | "Cascade" | "Stagnation" | "Reconstruction" | "Unstable";
  distance: number;
  gateSatisfied: boolean;
};
```

---

## 🧭 Mode State Schema

```ts
type MediaModeState = {
  mode: "Stable" | "Tension" | "Drift" | "Cascade" | "Collapse" | "Reconstruction";
  driftMagnitude: number;
  dominantInvariant: keyof MediaInvariantState;
};
```

---

## 🌀 Drift Schema

```ts
type MediaDrift = {
  delta: MediaVector;
  magnitude: number;
  category: "micro" | "meso" | "macro" | "regime_shift";
};
```

---

## 🔄 Transition Schema

```ts
type MediaTransition = {
  from: string;
  to: string;
  trigger: "invariant_break" | "attention_spike" | "cadence_acceleration" | "signal_collapse" | "narrative_collapse" | "reconstruction";
  severity: number;
};
```

---

## 🧪 Example Adapter Types

### TextStreamMediaAdapter
Maps text streams (articles, transcripts, posts) into vectors.

```ts
class TextStreamMediaAdapter implements MediaAdapter {
  toVector(text: string): MediaVector {
    // compute S, D, A, N, T from linguistic + temporal signals
  }
}
```

Useful for:
- News articles  
- Social posts  
- Long‑form narratives  
- Transcripts  

---

### PlatformMediaAdapter
Maps platform metrics into vectors.

```ts
class PlatformMediaAdapter implements MediaAdapter {
  toVector(metrics: PlatformMetrics): MediaVector {
    // compute vector from engagement, topology, cadence, etc.
  }
}
```

Useful for:
- Social networks  
- Video platforms  
- Forums  
- Messaging ecosystems  

---

### NarrativeMediaAdapter
Maps narrative structures into vectors.

```ts
class NarrativeMediaAdapter implements MediaAdapter {
  toVector(narrative: NarrativeObject): MediaVector {
    // compute coherence, conflict, volatility, cadence
  }
}
```

Useful for:
- Story arcs  
- Topic clusters  
- Meme evolution  
- Ideological ecosystems  

---

### DistributionGraphAdapter
Maps network topology into vectors.

```ts
class DistributionGraphAdapter implements MediaAdapter {
  toVector(graph: Graph): MediaVector {
    // compute D, A, T from connectivity + flow patterns
  }
}
```

Useful for:
- Retweet/repost graphs  
- Link networks  
- Community structures  
- Information flow maps  

---

## 🧬 Adapter Philosophy

Adapters must remain:

- **Substrate‑agnostic** — no platform‑specific assumptions  
- **Minimal** — only structural signals, no content interpretation  
- **Deterministic** — same input → same vector  
- **Composable** — multiple adapters can feed the same Analyzer  
- **Transparent** — clear mapping from raw input to substrate axes  

Adapters are the MSM’s interface to the real world. They allow the substrate to ingest any media environment and express it in the same structural language.
