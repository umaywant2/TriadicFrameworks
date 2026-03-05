# 🔌 Adapter Integration

Adapters are the bridge between external media environments and the MSM Analyzer. They convert raw, platform‑specific signals into normalized MSM vectors and optional metadata. The Analyzer itself is substrate‑agnostic—it does not know or care where the data comes from. Adapters ensure that every environment can be evaluated using the same structural grammar.

Adapters do **not** interpret content, sentiment, ideology, or topics. Their job is to extract **structural signals** that map cleanly onto the five MSM axes.

---

## 🧱 Role of Adapters in the MSM Ecosystem

Adapters serve three core functions:

- **Translation** — convert raw platform signals into MSM‑aligned primitives  
- **Normalization** — ensure all values fall within `[0.0, 1.0]`  
- **Contextualization** — provide optional metadata that refines invariant and mode evaluation  

The Analyzer expects a consistent input shape regardless of the platform or data source.

---

## 📐 Required Output: MediaVector

Every adapter must produce a normalized **MediaVector**:

```
{
  S: number,  // Signal Integrity
  D: number,  // Distribution Topology
  A: number,  // Attention Dynamics
  N: number,  // Narrative Coherence
  T: number   // Temporal Cadence
}
```

Each axis must be in the range:

```
0.0 = minimum expression
1.0 = maximum expression
```

Adapters may compute these values using any platform‑appropriate method, as long as the mapping is consistent.

---

## 🧩 Optional Output: Metadata

Adapters may also provide metadata that helps the Analyzer refine its interpretation:

- **Volatility indicators** (attention spikes, churn signatures)  
- **Narrative conflict markers** (semantic divergence, contradiction density)  
- **Cadence hints** (posting frequency, cycle compression)  
- **Signal quality markers** (noise ratio, distortion, missing data)  
- **Distribution structure hints** (cluster maps, centrality, fragmentation)  

Metadata is optional but improves accuracy, especially in mode and transition detection.

---

## 🛰 Mapping External Signals to MSM Axes

Adapters must translate platform‑specific signals into the five MSM axes. Examples:

### **Signal Integrity (S)**
- Noise ratio  
- Verification density  
- Redundancy and cross‑validation  
- Data completeness  

### **Distribution Topology (D)**
- Network centrality  
- Fragmentation index  
- Cross‑cluster connectivity  
- Broadcast vs networked flow  

### **Attention Dynamics (A)**
- Engagement volatility  
- Spike frequency  
- Saturation and burnout patterns  
- Temporal clustering  

### **Narrative Coherence (N)**
- Semantic similarity  
- Topic alignment  
- Conflict markers  
- Narrative half‑life  

### **Temporal Cadence (T)**
- Posting frequency  
- Cycle acceleration  
- Compression of update intervals  
- Burstiness  

Adapters may use any computational method—statistical, graph‑based, semantic, or heuristic—as long as the mapping is consistent.

---

## 🧭 Normalization Requirements

All values must be normalized to `[0.0, 1.0]`.  
Normalization ensures:

- Cross‑platform comparability  
- Stable invariant evaluation  
- Consistent drift measurement  
- Reliable transition detection  

Adapters may use min‑max scaling, logistic transforms, or domain‑specific normalization.

---

## 🔄 How the Analyzer Uses Adapter Output

Once the adapter produces a MediaVector (and optional metadata), the Analyzer:

1. Validates and normalizes the vector  
2. Computes invariant strain  
3. Classifies basin membership  
4. Determines behavioral mode  
5. Measures drift  
6. Detects transitions  

The adapter’s job ends once the vector is produced.  
The Analyzer handles all structural interpretation.

---

## 📦 Example Adapter Output

```
{
  S: 0.62,
  D: 0.48,
  A: 0.71,
  N: 0.39,
  T: 0.83,
  metadata: {
    volatility: 0.77,
    narrativeConflict: 0.52,
    cadenceAcceleration: 0.81
  }
}
```

The Analyzer will use the vector directly and incorporate metadata where relevant.

---

## 🧬 Adapter Philosophy

Adapters should be:

- **Minimal** — only extract what is structurally necessary  
- **Consistent** — use stable mappings across time  
- **Transparent** — document how each axis is computed  
- **Platform‑agnostic** — avoid assumptions about content or ideology  

The MSM Analyzer is designed to work with any media environment as long as the adapter respects these principles.
