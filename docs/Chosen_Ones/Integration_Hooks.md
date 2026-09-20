# Integration Hooks — Agentic AI Module Interface

**Module:** Chosen Ones | **RTT Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This file defines all integration points for connecting the Chosen Ones module to external agentic AI systems, orchestration frameworks, and downstream TriadicFrameworks modules. The module exposes four hook types: Ingestion, Extraction, Deployment, and Feedback.

---

## Hook Architecture

```
EXTERNAL AGENT / ORCHESTRATOR
        │
        ├──► HOOK-IN-1:  ingest_url(youtube_url) → transcript_object
        ├──► HOOK-IN-2:  ingest_text(raw_text, metadata) → transcript_object
        │
        ├──► HOOK-EX-1:  extract_operators(transcript_object) → manifest
        ├──► HOOK-EX-2:  classify_utterance(text) → fuu_classification
        │
        ├──► HOOK-DP-1:  run_tool(tool_name, input, manifest_id) → tool_output
        ├──► HOOK-DP-2:  generate_content(archetype, medium, length) → content
        ├──► HOOK-DP-3:  correct_drift(drift_description, manifest_id) → drift_output
        │
        └──► HOOK-FB-1:  submit_feedback(manifest_id, correction) → updated_manifest
```

---

## HOOK-IN-1 — ingest_url

**Purpose:** Primary YouTube ingestion entry point. Accepts a YouTube URL and returns a fully structured transcript object ready for operator extraction.

### Signature
```python
def ingest_url(
    youtube_url: str,
    fetch_method: str = "auto",          # "api" | "ytdlp" | "transcript_api" | "auto"
    language: str = "en",
    semantic_chunking: bool = True,
    tqs_threshold: float = 0.65
) -> TranscriptObject
```

### Request Schema
```json
{
  "hook": "HOOK-IN-1",
  "youtube_url": "https://www.youtube.com/watch?v={VIDEO_ID}",
  "options": {
    "fetch_method": "auto",
    "language": "en",
    "semantic_chunking": true,
    "tqs_threshold": 0.65
  }
}
```

### Response Schema
```json
{
  "status": "success | tqs_below_threshold | fetch_failed | language_unavailable",
  "transcript_id": "CO-TX-{VIDEO_ID}-{YYYYMMDD}",
  "transcript_object": { },
  "ready_for_extraction": true,
  "warnings": []
}
```

### Error Conditions

| Status | Cause | Agent Action |
|---|---|---|
| `tqs_below_threshold` | Transcript quality < 0.65 | Flag for human review; do not auto-extract |
| `fetch_failed` | All three fetch methods failed | Return error; prompt user for manual transcript |
| `language_unavailable` | No English captions available | Attempt auto-translate; flag with `translated: true` |

---

## HOOK-IN-2 — ingest_text

**Purpose:** Accepts raw text (manual paste, pre-fetched transcript, or document extract) and wraps it in the structured transcript object with metadata supplied by the caller.

### Signature
```python
def ingest_text(
    raw_text: str,
    source_url: str = None,
    title: str = None,
    channel: str = None,
    duration_s: int = None,
    semantic_chunking: bool = True
) -> TranscriptObject
```

### Request Schema
```json
{
  "hook": "HOOK-IN-2",
  "raw_text": "...",
  "metadata": {
    "source_url": "https://www.youtube.com/watch?v={VIDEO_ID}",
    "title": "{Video Title}",
    "channel": "{Channel Name}",
    "duration_s": 0
  },
  "options": {
    "semantic_chunking": true
  }
}
```

**Use case:** Paste transcript directly from YouTube auto-captions interface, or inject transcript from an upstream agent that has already fetched it.

---

## HOOK-EX-1 — extract_operators

**Purpose:** Core extraction hook. Takes a transcript object and returns a fully assembled RTT operator manifest.

### Signature
```python
def extract_operators(
    transcript_object: TranscriptObject,
    llm_backend: str = "default",        # "openai" | "anthropic" | "azure" | "default"
    prompt_family: str = "P1-A",         # Prompt from Example_Prompts.md
    validate_manifest: bool = True,
    resolve_paradoxes: bool = True
) -> OperatorManifest
```

### Request Schema
```json
{
  "hook": "HOOK-EX-1",
  "transcript_id": "CO-TX-{VIDEO_ID}-{YYYYMMDD}",
  "options": {
    "llm_backend": "default",
    "prompt_family": "P1-A",
    "validate_manifest": true,
    "resolve_paradoxes": true
  }
}
```

### Response Schema
```json
{
  "status": "success | validation_failed | paradox_unresolved",
  "manifest_id": "CO-MANIFEST-{VIDEO_ID}-{YYYYMMDD}",
  "manifest": { },
  "validation_report": { },
  "processing_time_ms": 0
}
```

### Extraction Quality Flags

| Flag | Condition | Meaning |
|---|---|---|
| `low_snr_variance` | All SNR zones < 10% of content | Transcript lacks structural diversity; may be noise-dominated |
| `no_activation_operator` | No Activation family operator in primary set | Transcript may not contain threshold-crossing content |
| `high_paradox_density` | > 3 paradoxes per 10 FUUs | Rich structural tension; verify all resolutions manually |
| `archetype_ambiguous` | Top two archetypes within 5% confidence | Request manual archetype assignment |

---

## HOOK-EX-2 — classify_utterance

**Purpose:** Lightweight single-utterance classifier. No manifest produced — returns only classification tags. Designed for real-time stream processing.

### Signature
```python
def classify_utterance(
    text: str,
    return_operator: bool = True,
    return_intensity: bool = True
) -> FUUClassification
```

### Response Schema
```json
{
  "text": "...",
  "snr_zone": "silence | noise | resonance",
  "set_layer": "substrate | envelope | threshold",
  "dco_stage": "0D | 1D | 3D | 8D | 9D",
  "primary_operator": "...",
  "intensity": 0.0
}
```

**Latency target:** < 800ms for agents requiring real-time classification.

---

## HOOK-DP-1 — run_tool

**Purpose:** Execute any of the four actionable tools (Reframe Generator, Activation Scaffold, Drift Corrector, Resonance Template) against a stored manifest.

### Signature
```python
def run_tool(
    tool_name: str,                      # "reframe" | "scaffold" | "drift" | "template"
    user_input: dict,
    manifest_id: str = None,             # Optional: ground tool in a specific manifest
    archetype_override: str = None       # Optional: force a specific archetype
) -> ToolOutput
```

### Request Schema
```json
{
  "hook": "HOOK-DP-1",
  "tool_name": "reframe | scaffold | drift | template",
  "manifest_id": "CO-MANIFEST-{VIDEO_ID}-{YYYYMMDD}",
  "user_input": {
    "user_text": "...",
    "goal": "...",
    "drift_description": "...",
    "target_medium": "..."
  }
}
```

### Response Schema
```json
{
  "status": "success | manifest_not_found | tool_error",
  "tool": "...",
  "manifest_id": "...",
  "archetype_applied": "...",
  "primary_operator_applied": "...",
  "output": "..."
}
```

---

## HOOK-DP-2 — generate_content

**Purpose:** Generate new motivational content with a specified RTT operator signature. Does not require a source manifest — operates from archetype and operator spec directly.

### Signature
```python
def generate_content(
    archetype: str,
    medium: str,                         # "spoken_word" | "essay" | "social_post" | "agent_prompt"
    length: str,                         # "short" | "medium" | "long"
    operator_set: list = None,           # Override default operator set for archetype
    snr_targets: dict = None             # Override default SNR distribution
) -> GeneratedContent
```

### Response Schema
```json
{
  "status": "success",
  "archetype": "...",
  "medium": "...",
  "snr_distribution_achieved": { "silence": 0.0, "noise": 0.0, "resonance": 0.0 },
  "operators_encoded": [],
  "content": "...",
  "word_count": 0
}
```

---

## HOOK-DP-3 — correct_drift

**Purpose:** Real-time drift correction hook for conversational agents. Accepts a drift description and returns a structured correction script.

### Signature
```python
def correct_drift(
    drift_description: str,
    drift_type: str = "auto",            # "auto" | explicit drift type
    archetype: str = None,
    manifest_id: str = None
) -> DriftCorrection
```

### Response Schema
```json
{
  "status": "success",
  "drift_type_identified": "...",
  "operators_applied": ["D_δ", "S_coh"],
  "damping_sequence": ["Step 1: ...", "Step 2: ...", "Step 3: ..."],
  "coherence_lock_sentence": "...",
  "full_script": "..."
}
```

---

## HOOK-FB-1 — submit_feedback

**Purpose:** Allows downstream agents or human reviewers to submit corrections to an existing manifest. Maintains manifest version history.

### Signature
```python
def submit_feedback(
    manifest_id: str,
    corrections: list,                   # List of {fuu_id, field, old_value, new_value}
    reviewer: str = "agent",             # "agent" | "human"
    reason: str = None
) -> UpdatedManifest
```

### Correction Schema
```json
{
  "fuu_id": "FUU-007",
  "field": "primary_operator",
  "old_value": "D_δ",
  "new_value": "A_θ",
  "reason": "FUU describes threshold crossing, not drift damping"
}
```

---

## Agentic Orchestration Patterns

### Pattern A — Full Auto Pipeline
```
Agent receives YouTube URL
  → HOOK-IN-1 (ingest_url)
  → HOOK-EX-1 (extract_operators)
  → HOOK-DP-1 (run_tool: reframe + scaffold)
  → Return four-tool output to user
```

### Pattern B — Real-Time Conversation Companion
```
User sends message in conversation
  → HOOK-EX-2 (classify_utterance) on user message
  → If drift detected: HOOK-DP-3 (correct_drift)
  → If activation opportunity: HOOK-DP-1 (run_tool: scaffold)
  → If resonance confirmation needed: HOOK-DP-1 (run_tool: reframe)
  → Embed correction/scaffold in conversational response
```

### Pattern C — Corpus Analysis Pipeline
```
Agent receives list of YouTube URLs
  → HOOK-IN-1 × N (batch ingestion)
  → HOOK-EX-1 × N (batch extraction)
  → Cross-manifest analysis (Prompt P4-B)
  → Generate corpus RTT report + canonical operator set
  → Feed canonical operators into HOOK-DP-2 for new content generation
```

### Pattern D — Live Content Evaluation
```
User pastes or speaks a motivational statement
  → HOOK-IN-2 (ingest_text)
  → HOOK-EX-1 (extract_operators)
  → Compare manifest against corpus canonical operators
  → Score RTT fidelity (0.0–1.0)
  → Recommend edits to improve SNR distribution or operator density
```

---

## RTT Context Propagation

**Critical requirement:** The RTT context header must be propagated through every hook call. No hook may operate without it.

```python
RTT_CONTEXT = "rtt=1 | coherence=declared | drift=bounded | paradox=structural"

# Every hook request must include:
{
  "rtt_context": RTT_CONTEXT,
  ...
}
```

Agents must treat `paradox=structural` as a hard constraint: any response that suppresses rather than resolves a paradox is a pipeline failure. The `validate_manifest` step in HOOK-EX-1 enforces this automatically.

---

## TriadicFrameworks Module Cross-Links

| Downstream Module | Integration Point | Data Passed |
|---|---|---|
| QMROOT Engine | HOOK-EX-1 output | Operator manifest, 0D activation events |
| S3 Spine Classifier | HOOK-EX-1 output | Operator family assignments for spine node update |
| DCO Arc Tracker | HOOK-DP-1 scaffold output | Stage transitions, activation events |
| Resonance Field Map | HOOK-EX-2 stream | Real-time utterance classification for field mapping |
| Feedback Loop Module | HOOK-FB-1 | Manifest corrections for model improvement |
