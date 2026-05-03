# **PNG‑Ready Vector Layout Description**  
*Structured for Figma / Illustrator / SVG export*  
🎨📐

Below is a **precise, layer‑friendly, vector‑ready description** of the RSID + RTT/Inside GPR Operator Dashboard.  
Each block is described with:

- **Layer name**  
- **Dimensions**  
- **Position**  
- **Color palette**  
- **Typography**  
- **Vector shapes**  

This is exactly what a designer needs to recreate the dashboard as a PNG or SVG.

---

## **1. Artboard**
```
Artboard:
- Size: 1920 × 1080 px
- Background: #0E0F11 (dark slate)
- Grid: 12‑column layout, 20 px gutters
```

---

## **2. Panel A — RSII Core Gauge**
```
Layer Name: RSII_Core_Gauge
Position: x=40, y=40
Size: 360 × 260 px
Background: #1A1C1F (rounded rectangle, 12 px radius)
Border: 1 px solid #2A2D31

Elements:
- Circular gauge (vector arc)
  - Outer ring: #2F3237
  - Active arc: gradient (#00E5FF → #7CFC00)
  - Needle: white, 2 px
- RSII numeric readout:
  - Font: Inter SemiBold 48 px, #FFFFFF
- Trend arrow:
  - Vector triangle, #7CFC00 or #FF2E63
- Time‑to‑boundary text:
  - Font: Inter Regular 16 px, #A0A4A8
```

---

## **3. Panel B — Safety Margin Bars**
```
Layer Name: Safety_Margins
Position: x=420, y=40
Size: 1460 × 260 px
Background: #1A1C1F

Bars (each 200 × 24 px):
- RSI: green (#00FF7F)
- RCS: cyan (#00E5FF)
- RCI: gold (#E6B800)
- Entropy: orange (#FF8C00)
- Drift: magenta (#FF2E63)
- Influence: purple (#8A2BE2)

Typography:
- Label: Inter Medium 14 px, #FFFFFF
- Value: Inter Regular 14 px, #A0A4A8
```

---

## **4. Panel C — RTT Signature Panel**
```
Layer Name: RTT_Signatures
Position: x=40, y=320
Size: 360 × 300 px
Background: #1A1C1F

Signature Icons:
- Wave: blue (#3A7BFF)
- Ladder: gold (#E6B800)
- Plateau: brown (#8B5A2B)
- Cascade: magenta (#FF2E63)

Each icon:
- 48 × 48 px vector glyph
- Label: Inter Medium 18 px, #FFFFFF
- Count: Inter Bold 24 px, #FFFFFF
```

---

## **5. Panel D — Coherence & Drift Fields**
```
Layer Name: Coherence_Drift
Position: x=420, y=320
Size: 720 × 300 px
Background: #1A1C1F

Elements:
- Coherence heatmap:
  - 12×12 grid of rectangles
  - Colors: cyan (#00E5FF) → purple (#8A2BE2)
- Drift timeline:
  - Polyline graph, hot pink (#FF69B4)
- Influence vectors:
  - Arrow glyphs, white (#FFFFFF), 1 px stroke
```

---

## **6. Panel E — Subsurface Map**
```
Layer Name: Subsurface_Map
Position: x=40, y=640
Size: 1840 × 360 px
Background: #111214

Elements:
- Edge‑enhanced radargram:
  - Grayscale gradient (#000000 → #FFFFFF)
- Signature overlay:
  - Wave: blue
  - Ladder: gold
  - Plateau: brown
  - Cascade: magenta
- Void probability:
  - Heatmap overlay: red (#FF2E63) at 60% opacity
```

---

## **7. Panel F — RSIP Action Panel**
```
Layer Name: RSIP_Actions
Position: x=1180, y=320
Size: 360 × 300 px
Background: #1A1C1F

Elements:
- Action cards (stacked):
  - 320 × 60 px
  - Background: #232528
  - Border: 1 px #2F3237
  - Text: Inter Medium 16 px, #FFFFFF
```

---

## **8. Panel G — RSMS Alerts**
```
Layer Name: RSMS_Alerts
Position: x=1180, y=640
Size: 360 × 160 px
Background: #1A1C1F

Alert badges:
- Critical: red (#FF2E63)
- Warning: orange (#FF8C00)
- Info: cyan (#00E5FF)
```

---

## **9. Panel H — RSISS Simulation Controls**
```
Layer Name: RSISS_Controls
Position: x=1180, y=820
Size: 360 × 180 px
Background: #1A1C1F

Buttons:
- 160 × 48 px
- Background: #2A2D31
- Text: Inter Medium 16 px, #FFFFFF
- Radius: 8 px
```
