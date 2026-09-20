# Transcript Ingestion Pipeline

**Module:** Chosen Ones | **RTT Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This pipeline governs the full workflow from raw YouTube URL to clean, structured transcript text ready for operator extraction. It has four stages: Fetch, Clean, Chunk, and Tag.

---

## Pipeline Overview

```
[YOUTUBE URL]
      ↓
  STAGE 1: FETCH
  Pull transcript via YouTube API / yt-dlp / transcript scraping
      ↓
  STAGE 2: CLEAN
  Strip artifacts, normalize text, resolve speaker ambiguity
      ↓
  STAGE 3: CHUNK
  Divide into timestamp-anchored segments
      ↓
  STAGE 4: TAG
  Apply metadata envelope (source, theme, archetype estimate)
      ↓
[STRUCTURED TRANSCRIPT OBJECT]
      ↓
  → Operator_Extraction_Pipeline.md
```

---

## Stage 1 — Fetch

### 1.1 Preferred Method: YouTube Data API v3 + Captions Endpoint

```
GET https://www.googleapis.com/youtube/v3/captions
  ?part=snippet
  &videoId={VIDEO_ID}
  &key={API_KEY}
```

Retrieve the caption track ID, then fetch the raw caption file:
```
GET https://www.googleapis.com/youtube/v3/captions/{CAPTION_ID}
  ?tfmt=srt
  &key={API_KEY}
```

**Supported formats:** SRT (preferred), VTT, TTML. SRT is preferred for timestamp fidelity.

### 1.2 Fallback Method: yt-dlp

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  --output "%(id)s.%(ext)s" \
  "https://www.youtube.com/watch?v={VIDEO_ID}"
```

Auto-generated captions are acceptable for this module. Note: auto-captions carry ~3–8% word error rate; apply Stage 2 cleaning accordingly.

### 1.3 Fallback Method: youtube-transcript-api (Python)

```python
from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript(
    video_id,
    languages=['en']
)
# Returns: list of {text, start, duration} dicts
```

### 1.4 Fetch Output Schema

```json
{
  "video_id": "oDgMc7X8HCM",
  "fetch_method": "youtube_transcript_api",
  "fetch_timestamp": "2026-09-20T07:38:00-04:00",
  "language": "en",
  "caption_type": "auto",
  "raw_segments": [
    { "text": "...", "start": 0.0, "duration": 4.2 },
    { "text": "...", "start": 4.2, "duration": 3.8 }
  ],
  "total_duration_s": 0,
  "segment_count": 0
}
```

---

## Stage 2 — Clean

### 2.1 Artifact Removal

Remove all non-linguistic content from raw caption text:

| Artifact Type | Pattern | Action |
|---|---|---|
| Music markers | `[Music]`, `[♪]`, `♪ ... ♪` | Remove |
| Applause/crowd | `[Applause]`, `[Laughter]` | Remove |
| Filler sounds | `um`, `uh`, `mm`, standalone | Remove |
| Speaker labels | `SPEAKER:`, `[Male voice]:` | Strip label, keep text |
| SRT index numbers | Line-starting integers | Remove |
| Timestamp codes | `00:00:00,000 --> 00:00:04,200` | Extract to metadata, remove from text |
| Repeated duplicate segments | Consecutive identical text | Deduplicate, keep first |

### 2.2 Text Normalization

1. **Sentence boundary reconstruction:** YouTube auto-captions break mid-sentence. Reconstruct by merging segments where end-of-segment does not end with `.`, `?`, `!`, or `,`.
2. **Capitalization:** Apply standard sentence-case. Preserve all-caps for emphasis only if speaker appears to be shouting (high-energy segment, density > 0.8).
3. **Contraction normalization:** Preserve contractions as-is (they carry cadence information useful for Stage 4 tagging).
4. **Number normalization:** Convert numeric digits to words where they appear in motivational context (`"1 person"` → `"one person"`).

### 2.3 Speaker Ambiguity Resolution

If the video has multiple speakers (interview, dialogue):
- Assign `SPEAKER_A` (primary motivational voice) and `SPEAKER_B` (interviewer/respondent)
- Run operator extraction on `SPEAKER_A` only, unless `SPEAKER_B` content also qualifies
- Flag multi-speaker transcripts with `multi_speaker: true` in Stage 4 metadata

### 2.4 Quality Score

Assign a **Transcript Quality Score (TQS)** from 0.0–1.0 based on:

```
TQS = (1 - error_rate) × completeness × coherence_score
```

| Metric | Method |
|---|---|
| `error_rate` | Estimated word error rate: 0.0 (manual captions) to 0.12 (poor auto-captions) |
| `completeness` | Segment coverage: (total clean words) / (estimated spoken words from duration × avg_wpm) |
| `coherence_score` | Ratio of grammatically complete sentences to total reconstructed sentences |

**TQS threshold for processing:** ≥ 0.65. Below this, flag for manual review before operator extraction.

---

## Stage 3 — Chunk

Chunking divides the clean transcript into **Processing Windows (PWs)** — fixed-time segments used as the unit of analysis in Stage 4 and the Operator Extraction Pipeline.

### 3.1 Default Chunking Parameters

| Parameter | Value | Rationale |
|---|---|---|
| Window size | 60 seconds | Long enough for one complete structural arc (Silence→Noise→Resonance) |
| Window overlap | 15 seconds | Captures cross-boundary FUUs that span chunk edges |
| Minimum window content | 40 words | Windows below this are merged with adjacent window |

### 3.2 Semantic Chunking (Preferred)

Where possible, override fixed-window chunking with **semantic chunking** — split at natural structural breaks rather than time boundaries:

- Detect topic shifts using sentence embedding cosine similarity (threshold: < 0.55 between adjacent sentences)
- Detect cadence breaks (silence > 1.5 seconds in audio, or `[pause]` annotation)
- Detect explicit structural markers: "Now...", "Here's the thing...", "Let me tell you something...", "But here's what I want you to understand..."

### 3.3 Chunk Output Schema

```json
{
  "chunk_id": "PW-003",
  "video_id": "oDgMc7X8HCM",
  "start_s": 120.0,
  "end_s": 181.4,
  "overlap_with_prev_s": 15.0,
  "word_count": 187,
  "text": "...",
  "semantic_break_detected": true,
  "break_type": "cadence"
}
```

---

## Stage 4 — Tag

Tagging applies the metadata envelope that contextualizes operator extraction.

### 4.1 Source Metadata

```json
{
  "source_url": "https://www.youtube.com/watch?v=oDgMc7X8HCM",
  "video_id": "oDgMc7X8HCM",
  "title": "[Video Title]",
  "channel": "[Channel Name]",
  "upload_date": "[YYYY-MM-DD]",
  "duration_s": 0,
  "view_count": 0,
  "like_count": 0
}
```

### 4.2 Thematic Pre-Classification

Before operator extraction, apply a lightweight theme classifier to the full transcript to establish a prior for Stage 2 of the extraction pipeline:

| Theme Label | Detection Keywords / Patterns |
|---|---|
| `unseen_genius` | "never noticed", "hidden", "didn't see", "room didn't know", "building in silence" |
| `magnetic_presence` | "walk in", "room shifts", "don't have to announce", "they feel it", "magnetism" |
| `chosen_recognition` | "chosen", "always knew", "destined", "finally see", "they see it now" |
| `non_chase_posture` | "stop chasing", "don't need", "not for them", "let them come", "detach from outcome" |
| `threshold_crossing` | "decide", "moment", "can't go back", "once you", "the leap" |
| `ancestral_calling` | "ancestors", "lineage", "before you were born", "carried to you", "bigger than you" |
| `long_arc_patience` | "years", "they didn't know yet", "one day", "long game", "outlast" |

Multiple theme labels can be assigned. The primary theme (highest confidence) becomes `dominant_theme`.

### 4.3 Archetype Estimate

Map `dominant_theme` to an archetype from `Triadic_Substrate_Map.md §4`:

```python
THEME_TO_ARCHETYPE = {
    "unseen_genius":       "The Unseen Genius",
    "magnetic_presence":   "The Magnetic Presence",
    "chosen_recognition":  "The Recognition Moment",
    "non_chase_posture":   "The Non-Chase Posture",
    "threshold_crossing":  "The Threshold Crosser",
    "ancestral_calling":   "The Ancestral Calling",
    "long_arc_patience":   "The Long Arc / Patience"
}
```

### 4.4 Structured Transcript Object (Final Output)

```json
{
  "transcript_id": "CO-TX-[VIDEO_ID]-[YYYYMMDD]",
  "rtt_context": "rtt=1 | coherence=declared | drift=bounded | paradox=structural",
  "source": { },
  "fetch": { },
  "quality": { "tqs": 0.0, "flag_for_review": false },
  "chunks": [],
  "theme_labels": [],
  "dominant_theme": "",
  "archetype_estimate": "",
  "multi_speaker": false,
  "ready_for_extraction": true
}
```

---

## Supported YouTube Corpus — Module Test Cases

| Video ID | URL | Dominant Theme | Archetype Estimate |
|---|---|---|---|
| `y9SEykMNIeI` | youtube.com/watch?v=y9SEykMNIeI | `threshold_crossing` + `non_chase_posture` | The Threshold Crosser |
| `bvnQHdXx-Mc` | youtube.com/watch?v=bvnQHdXx-Mc | `magnetic_presence` | The Magnetic Presence |
| `PeZyNW1NgGw` | youtube.com/watch?v=PeZyNW1NgGw | `chosen_recognition` + `ancestral_calling` | The Recognition Moment |
| `_LlfssWA67w` | youtube.com/watch?v=_LlfssWA67w | `long_arc_patience` + `unseen_genius` | The Long Arc / Patience |
| `oDgMc7X8HCM` | youtube.com/watch?v=oDgMc7X8HCM | `unseen_genius` + `chosen_recognition` | The Unseen Genius |
