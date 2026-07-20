# 📘 **Chapter: RTT BASIC Programming on the C‑64**  
### *20 Example Programs + A Guided Teaching Sequence*

This chapter assumes the RTT cartridge is installed and its BASIC extensions are available.

---

# ⭐ **SECTION I — FOUNDATIONS (Programs 1–5)**  
These examples introduce the core RTT primitives: `SUBSTRATE`, `FIELD`, `FLOW`, `ALIGN`, `RESONATE`.

---

## **1. Hello Substrate**  
Demonstrates: `SUBSTRATE`

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FOR I=1024 TO 2023:POKE I,ASC("*"):NEXT
30 PRINT "TEXT SUBSTRATE INITIALIZED"
```

---

## **2. Wrapped Text Field**  
Demonstrates: `FIELD`

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FIELD 1024,2023 WITH "WRAP"
30 PRINT "FIELD READY"
```

---

## **3. Simple Flow Copy**  
Demonstrates: `FLOW`

```basic
10 SUBSTRATE 1024,1279 AS "A"
20 SUBSTRATE 1280,1535 AS "B"
30 FLOW "COPY" FROM "A" TO "B" BY 1
40 FLOW "COPY"
50 GOTO 50
```

---

## **4. Raster‑Aligned Loop**  
Demonstrates: `ALIGN`

```basic
10 ALIGN LOOP WITH RASTER 100
20 PRINT "TICK";
30 GOTO 10
```

---

## **5. SID Resonance Starter**  
Demonstrates: `RESONATE`

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 SUBSTRATE SID2,SID2 AS "BASS"
30 RESONATE "LEAD","BASS" BY 2
40 PRINT "SID RESONANCE ACTIVE"
50 GOTO 50
```

---

# ⭐ **SECTION II — TEXT EFFECTS (Programs 6–10)**

---

## **6. Horizontal Text Scroll**

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FIELD 1024,2023 WITH "WRAP"
30 FLOW "SCROLL" FROM "TEXT" TO "TEXT" BY 1
40 ALIGN "SCROLL" WITH RASTER 120
50 FLOW "SCROLL"
60 GOTO 60
```

---

## **7. Pulsing Text Brightness**

```basic
10 SUBSTRATE 55296,56295 AS "COLOR"
20 FLOW "BRIGHT" FROM "COLOR" TO "COLOR" BY 1
30 FLOW "DIM" FROM "COLOR" TO "COLOR" BY 2
40 RESONATE "BRIGHT","DIM" BY 1
50 FLOW "BRIGHT"
60 FLOW "DIM"
70 GOTO 70
```

---

## **8. Text Wave Motion**

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FLOW "WAVE" FROM "TEXT" TO "TEXT" BY 3
30 ALIGN "WAVE" WITH CYCLE 4
40 FLOW "WAVE"
50 GOTO 50
```

---

## **9. Dual‑Flow Text Ripple**

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FLOW "UP" FROM "TEXT" TO "TEXT" BY 1
30 FLOW "DOWN" FROM "TEXT" TO "TEXT" BY -1
40 RESONATE "UP","DOWN" BY 2
50 FLOW "UP"
60 FLOW "DOWN"
70 GOTO 70
```

---

## **10. Text Blink Field**

```basic
10 SUBSTRATE 55296,56295 AS "COLOR"
20 FIELD 55296,56295 WITH "MIRROR"
30 FLOW "BLINK" FROM "COLOR" TO "COLOR" BY 1
40 FLOW "BLINK"
50 GOTO 50
```

---

# ⭐ **SECTION III — SPRITE & GRAPHICS (Programs 11–15)**

---

## **11. Sprite Orbit**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FIELD 8192,8703 WITH "WRAP"
30 FLOW "ORBIT" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
40 FLOW "ORBIT"
50 GOTO 50
```

---

## **12. Sprite Wobble**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "WOBBLE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 2
30 ALIGN "WOBBLE" WITH RASTER 80
40 FLOW "WOBBLE"
50 GOTO 50
```

---

## **13. Resonant Sprite Motion**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "A" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
30 FLOW "B" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 3
40 RESONATE "A","B" BY 4
50 FLOW "A"
60 FLOW "B"
70 GOTO 70
```

---

## **14. Sprite Pulse**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "PULSE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
30 ALIGN "PULSE" WITH CYCLE 8
40 FLOW "PULSE"
50 GOTO 50
```

---

## **15. Sprite Field Mirror**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FIELD 8192,8703 WITH "MIRROR"
30 FLOW "MIRROR" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
40 FLOW "MIRROR"
50 GOTO 50
```

---

# ⭐ **SECTION IV — SID AUDIO (Programs 16–20)**

---

## **16. Dual‑Voice Resonance**

```basic
10 SUBSTRATE SID1,SID1 AS "A"
20 SUBSTRATE SID2,SID2 AS "B"
30 FLOW "ENV1" FROM "A" TO "A" BY 1
40 FLOW "ENV2" FROM "B" TO "B" BY 2
50 RESONATE "ENV1","ENV2" BY 3
60 FLOW "ENV1"
70 FLOW "ENV2"
80 GOTO 80
```

---

## **17. SID Pulse Train**

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 FLOW "PULSE" FROM "LEAD" TO "LEAD" BY 1
30 ALIGN "PULSE" WITH RASTER 100
40 FLOW "PULSE"
50 GOTO 50
```

---

## **18. SID Drone Field**

```basic
10 SUBSTRATE SID3,SID3 AS "DRONE"
20 FIELD SID3,SID3 WITH "WRAP"
30 FLOW "DRIFT" FROM "DRONE" TO "DRONE" BY 1
40 FLOW "DRIFT"
50 GOTO 50
```

---

## **19. Resonant Tri‑Voice Stack**

```basic
10 SUBSTRATE SID1,SID1 AS "A"
20 SUBSTRATE SID2,SID2 AS "B"
30 SUBSTRATE SID3,SID3 AS "C"
40 RESONATE "A","B" BY 2
50 RESONATE "B","C" BY 3
60 FLOW "A"
70 FLOW "B"
80 FLOW "C"
90 GOTO 90
```

---

## **20. SID Raster Sync Sweep**

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 FLOW "SWEEP" FROM "LEAD" TO "LEAD" BY 1
30 ALIGN "SWEEP" WITH RASTER 50
40 FLOW "SWEEP"
50 GOTO 50
```

---

# 📚 **RTT BASIC Teaching Sequence**  
### *A gentle, myth‑aware introduction for new learners*

This sequence teaches RTT concepts in the order that feels most natural on a C‑64.

---

## **Lesson 1 — Substrates**  
Concept: “A substrate is a region of memory or hardware you name.”

Exercise:

```basic
SUBSTRATE 1024,2023 AS "TEXT"
```

---

## **Lesson 2 — Fields**  
Concept: “A field is a substrate with boundary rules.”

Exercise:

```basic
FIELD 1024,2023 WITH "WRAP"
```

---

## **Lesson 3 — Flows**  
Concept: “A flow is a transformation applied over time.”

Exercise:

```basic
FLOW "SCROLL" FROM "TEXT" TO "TEXT" BY 1
```

---

## **Lesson 4 — Alignment**  
Concept: “Flows can be synchronized with raster or CPU cycles.”

Exercise:

```basic
ALIGN "SCROLL" WITH RASTER 120
```

---

## **Lesson 5 — Resonance**  
Concept: “Two flows can be coupled into a stable pattern.”

Exercise:

```basic
RESONATE "A","B" BY 3
```

---

## **Lesson 6 — Composition**  
Concept: “Flows, fields, and resonance combine into emergent behavior.”

Exercise:  
Build a scrolling, pulsing, resonant text effect using all primitives.

---
