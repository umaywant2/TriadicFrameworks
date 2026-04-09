# 🎮 **RTT BASIC Demonstrations**  
### *Sample Programs for the RTT–C64 Cartridge*

---

# **1. Raster‑Aligned Text Scroll**  
Demonstrates: `SUBSTRATE`, `FIELD`, `FLOW`, `ALIGN`

```basic
10 REM === RTT TEXT SCROLL DEMO ===
20 SUBSTRATE 1024,2047 AS "TEXTGRID"
30 FIELD 1024,2047 WITH "WRAP"
40 FLOW "SCROLL" FROM "TEXTGRID" TO "TEXTGRID" BY 1
50 ALIGN "SCROLL" WITH RASTER 120
60 REM INITIAL TEXT
70 T$="RTT ON C64  STILL RESONATING  "
80 L=LEN(T$)
90 FOR I=0 TO L-1:POKE 1024+I,ASC(MID$(T$,I+1,1)):NEXT
100 REM ACTIVATE FLOW
110 FLOW "SCROLL"
120 GOTO 120
```

**What it does:**  
A smooth hardware‑timed text scroll that updates *only* at raster line 120, giving a stable, flicker‑free effect.

---

# **2. SID Oscillator Resonance**  
Demonstrates: `SUBSTRATE`, `FLOW`, `RESONATE`, `ALIGN`

```basic
10 REM === RTT SID RESONANCE DEMO ===
20 SUBSTRATE SID1,SID1 AS "LEAD"
30 SUBSTRATE SID2,SID2 AS "BASS"
40 FLOW "ENV1" FROM "LEAD" TO "LEAD" BY 2
50 FLOW "ENV2" FROM "BASS" TO "BASS" BY 1
60 RESONATE "ENV1","ENV2" BY 3
70 ALIGN "ENV1" WITH RASTER 100
80 FLOW "ENV1"
90 FLOW "ENV2"
100 GOTO 100
```

**What it does:**  
Two SID voices modulate each other in phase‑locked resonance, with envelope updates synced to raster 100.

---

# **3. Sprite Orbit Field**  
Demonstrates: `SUBSTRATE`, `FIELD`, `FLOW`, `RESONATE`

```basic
10 REM === RTT SPRITE ORBIT DEMO ===
20 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
30 FIELD 8192,8703 WITH "WRAP"
40 FLOW "ORBIT" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
50 FLOW "WOBBLE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 2
60 RESONATE "ORBIT","WOBBLE" BY 4
70 FLOW "ORBIT"
80 FLOW "WOBBLE"
90 GOTO 90
```

**What it does:**  
Creates a resonant motion pattern where sprites orbit and wobble in a coupled flow.

---

# **4. Copper‑Style Color Cycling (C‑64 Edition)**  
Demonstrates: `FLOW`, `ALIGN`

```basic
10 REM === RTT COLOR CYCLE DEMO ===
20 SUBSTRATE 53280,53281 AS "BORDER"
30 FLOW "CYCLE" FROM "BORDER" TO "BORDER" BY 1
40 ALIGN "CYCLE" WITH RASTER 50
50 FLOW "CYCLE"
60 GOTO 60
```

**What it does:**  
A C‑64‑style “copper bar” effect — color cycling synchronized to raster 50.

---

# **5. Dual‑Flow Text Pulse**  
Demonstrates: `FLOW`, `RESONATE`

```basic
10 REM === RTT TEXT PULSE DEMO ===
20 SUBSTRATE 1024,2047 AS "TEXTGRID"
30 FLOW "BRIGHT" FROM "TEXTGRID" TO "TEXTGRID" BY 1
40 FLOW "DIM" FROM "TEXTGRID" TO "TEXTGRID" BY 2
50 RESONATE "BRIGHT","DIM" BY 1
60 FLOW "BRIGHT"
70 FLOW "DIM"
80 GOTO 80
```

**What it does:**  
Two flows alternately brighten and dim characters in a resonant pulse pattern.

---

# **6. Cycle‑Aligned Loop (RTT Timing Demo)**  
Demonstrates: `ALIGN`

```basic
10 REM === RTT CYCLE ALIGN DEMO ===
20 ALIGN LOOP WITH CYCLE 8
30 PRINT "TICK";
40 GOTO 20
```

**What it does:**  
Prints “TICK” at a perfectly stable rhythm, aligned to CPU cycle boundaries.

---

# **7. Substrate‑to‑Substrate Transformation**  
Demonstrates: `SUBSTRATE`, `FLOW`

```basic
10 REM === RTT SUBSTRATE TRANSFORM DEMO ===
20 SUBSTRATE 1024,1279 AS "A"
30 SUBSTRATE 1280,1535 AS "B"
40 FLOW "COPY" FROM "A" TO "B" BY 1
50 FLOW "COPY"
60 GOTO 60
```

**What it does:**  
Copies one text region into another using an RTT flow instead of manual loops.
