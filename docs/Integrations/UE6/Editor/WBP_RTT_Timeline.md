# WBP_RTT_Timeline — UI Widget Blueprint Scaffolding  
**RTT / Integrations / UE6 / Editor**

This widget displays RTT operator values over time inside the UE6 editor or runtime environment.

---

## Widget Name
`WBP_RTT_Timeline`

## Parent Class
`UserWidget`

---

## Hierarchy

```
CanvasPanel
    ├── Border_Header
    │       └── TextBlock_Title ("RTT Operator Timeline")
    ├── GraphPanel
    │       ├── Image_BackgroundGrid
    │       ├── TimelineCanvas (Overlay)
    │       │       ├── Line_Phi
    │       │       ├── Line_Variance
    │       │       ├── Line_Resonance
    │       │       └── Line_Entropy
    └── LegendPanel
            ├── PhiColorSwatch
            ├── VarianceColorSwatch
            ├── ResonanceColorSwatch
            └── EntropyColorSwatch
```

---

## Variables

| Name | Type | Purpose |
|------|------|---------|
| `TimelineData` | Array\<RTTFrameStruct\> | φ–V–R–Entropy frames |
| `PhiColor` | LinearColor | φ line color |
| `VarianceColor` | LinearColor | V line color |
| `ResonanceColor` | LinearColor | R line color |
| `EntropyColor` | LinearColor | entropy line color |
| `MaxFrames` | Integer | timeline length |
| `AutoScroll` | Boolean | scrolls as new frames arrive |

---

## Struct: RTTFrameStruct

```
float Phi
float Variance
float Resonance
float Entropy
```

---

## Graph Logic

### Event: `Construct`
- Initialize colors  
- Clear timeline  
- Bind to RTTTools timeline events (optional)

### Event: `Tick`
- If new frame available → append to `TimelineData`
- If `AutoScroll` → shift view  
- Redraw lines on `TimelineCanvas`

### Function: `DrawTimeline()`
- Normalize values  
- Plot φ, V, R, entropy as polylines  
- Use color swatches for legend  

### Function: `AddFrame(RTTFrameStruct Frame)`
- Append to `TimelineData`
- If > `MaxFrames` → remove oldest  
- Call `DrawTimeline()`

---

## Visual Style

- **Background:** subtle grid (dark gray, 10% opacity)  
- **Lines:**  
  - φ → cyan  
  - variance → yellow  
  - resonance → magenta  
  - entropy → red  
- **Legend:** small color boxes with labels  

---

## Status
Ready for implementation.  
Fully aligned with the 2026 RTT Integrations standard.
