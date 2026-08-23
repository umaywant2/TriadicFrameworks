```
======================================================================
                              C H A P T E R   7
======================================================================
                   R T T   B A S I C   P R O G R A M M I N G
                     O N   T H E   C O M M O D O R E   6 4
======================================================================
                                                TriadicFrameworks Docs
                                                Print Edition • p. 7‑1
```

# **Chapter 7 — RTT BASIC Programming on the Commodore 64**  
*A complete programming guide for the RTT‑C64 Cartridge*

---

## **Table of Contents (Chapter 7)**  
*(Print Edition — p. 7‑2)*

### **Section I — Foundations**
- 7.1  Substrates ............................................. p. 7‑3  
- 7.2  Fields .................................................. p. 7‑4  
- 7.3  Flows ................................................... p. 7‑5  
- 7.4  Alignment ............................................... p. 7‑6  
- 7.5  Resonance ............................................... p. 7‑7  

### **Section II — Text Effects**
- 7.6  Horizontal Scroll ....................................... p. 7‑8  
- 7.7  Brightness Pulse ........................................ p. 7‑9  
- 7.8  Wave Motion ............................................. p. 7‑10  
- 7.9  Ripple Effect ........................................... p. 7‑11  
- 7.10 Blink Field ............................................. p. 7‑12  

### **Section III — Sprite & Graphics**
- 7.11 Sprite Orbit ............................................ p. 7‑13  
- 7.12 Sprite Wobble ........................................... p. 7‑14  
- 7.13 Resonant Motion ......................................... p. 7‑15  
- 7.14 Sprite Pulse ............................................ p. 7‑16  
- 7.15 Mirror Field ............................................ p. 7‑17  

### **Section IV — SID Audio**
- 7.16 Dual‑Voice Resonance .................................... p. 7‑18  
- 7.17 Pulse Train ............................................. p. 7‑19  
- 7.18 Drone Field ............................................. p. 7‑20  
- 7.19 Tri‑Voice Stack ......................................... p. 7‑21  
- 7.20 Raster Sync Sweep ....................................... p. 7‑22  

### **Appendix — Developer Notes**
- 7.A  Cartridge Architecture .................................. p. 7‑23  
- 7.B  Memory Map .............................................. p. 7‑24  
- 7.C  Timing & IRQ Behavior ................................... p. 7‑25  
- 7.D  Compatibility Notes ..................................... p. 7‑26  

---

```
======================================================================
                               S E C T I O N   I
======================================================================
                         F O U N D A T I O N   C O N C E P T S
======================================================================
                                                Print Edition • p. 7‑3
```

# **7.1 — Substrates**

A **substrate** is a named region of memory or hardware.  
This is the foundation of RTT programming.

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FOR I=1024 TO 2023:POKE I,ASC("*"):NEXT
```

---

# **7.2 — Fields**  
*(p. 7‑4)*

A **field** adds boundary rules to a substrate.

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FIELD 1024,2023 WITH "WRAP"
```

---

# **7.3 — Flows**  
*(p. 7‑5)*

A **flow** is a transformation applied over time.

```basic
10 SUBSTRATE 1024,1279 AS "A"
20 SUBSTRATE 1280,1535 AS "B"
30 FLOW "COPY" FROM "A" TO "B" BY 1
40 FLOW "COPY"
```

---

# **7.4 — Alignment**  
*(p. 7‑6)*

Synchronize flows with raster or CPU cycles.

```basic
10 ALIGN LOOP WITH RASTER 100
20 PRINT "TICK";
30 GOTO 10
```

---

# **7.5 — Resonance**  
*(p. 7‑7)*

Couple two flows into a stable pattern.

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 SUBSTRATE SID2,SID2 AS "BASS"
30 RESONATE "LEAD","BASS" BY 2
```

---

```
======================================================================
                               S E C T I O N   I I
======================================================================
                               T E X T   E F F E C T S
======================================================================
                                                Print Edition • p. 7‑8
```

# **7.6 — Horizontal Scroll**

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FIELD 1024,2023 WITH "WRAP"
30 FLOW "SCROLL" FROM "TEXT" TO "TEXT" BY 1
40 ALIGN "SCROLL" WITH RASTER 120
50 FLOW "SCROLL"
```

---

# **7.7 — Brightness Pulse**  
*(p. 7‑9)*

```basic
10 SUBSTRATE 55296,56295 AS "COLOR"
20 FLOW "BRIGHT" FROM "COLOR" TO "COLOR" BY 1
30 FLOW "DIM" FROM "COLOR" TO "COLOR" BY 2
40 RESONATE "BRIGHT","DIM" BY 1
50 FLOW "BRIGHT"
60 FLOW "DIM"
```

---

# **7.8 — Wave Motion**  
*(p. 7‑10)*

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FLOW "WAVE" FROM "TEXT" TO "TEXT" BY 3
30 ALIGN "WAVE" WITH CYCLE 4
40 FLOW "WAVE"
```

---

# **7.9 — Ripple Effect**  
*(p. 7‑11)*

```basic
10 SUBSTRATE 1024,2023 AS "TEXT"
20 FLOW "UP" FROM "TEXT" TO "TEXT" BY 1
30 FLOW "DOWN" FROM "TEXT" TO "TEXT" BY -1
40 RESONATE "UP","DOWN" BY 2
50 FLOW "UP"
60 FLOW "DOWN"
```

---

# **7.10 — Blink Field**  
*(p. 7‑12)*

```basic
10 SUBSTRATE 55296,56295 AS "COLOR"
20 FIELD 55296,56295 WITH "MIRROR"
30 FLOW "BLINK" FROM "COLOR" TO "COLOR" BY 1
40 FLOW "BLINK"
```

---

```
======================================================================
                              S E C T I O N   I I I
======================================================================
                         S P R I T E   &   G R A P H I C S
======================================================================
                                                Print Edition • p. 7‑13
```

# **7.11 — Sprite Orbit**

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FIELD 8192,8703 WITH "WRAP"
30 FLOW "ORBIT" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
40 FLOW "ORBIT"
```

---

# **7.12 — Sprite Wobble**  
*(p. 7‑14)*

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "WOBBLE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 2
30 ALIGN "WOBBLE" WITH RASTER 80
40 FLOW "WOBBLE"
```

---

# **7.13 — Resonant Motion**  
*(p. 7‑15)*

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "A" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
30 FLOW "B" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 3
40 RESONATE "A","B" BY 4
50 FLOW "A"
60 FLOW "B"
```

---

# **7.14 — Sprite Pulse**  
*(p. 7‑16)*

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FLOW "PULSE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
30 ALIGN "PULSE" WITH CYCLE 8
40 FLOW "PULSE"
```

---

# **7.15 — Mirror Field**  
*(p. 7‑17)*

```basic
10 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
20 FIELD 8192,8703 WITH "MIRROR"
30 FLOW "MIRROR" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
40 FLOW "MIRROR"
```

---

```
======================================================================
                               S E C T I O N   I V
======================================================================
                                S I D   A U D I O
======================================================================
                                                Print Edition • p. 7‑18
```

# **7.16 — Dual‑Voice Resonance**

```basic
10 SUBSTRATE SID1,SID1 AS "A"
20 SUBSTRATE SID2,SID2 AS "B"
30 FLOW "ENV1" FROM "A" TO "A" BY 1
40 FLOW "ENV2" FROM "B" TO "B" BY 2
50 RESONATE "ENV1","ENV2" BY 3
60 FLOW "ENV1"
70 FLOW "ENV2"
```

---

# **7.17 — Pulse Train**  
*(p. 7‑19)*

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 FLOW "PULSE" FROM "LEAD" TO "LEAD" BY 1
30 ALIGN "PULSE" WITH RASTER 100
40 FLOW "PULSE"
```

---

# **7.18 — Drone Field**  
*(p. 7‑20)*

```basic
10 SUBSTRATE SID3,SID3 AS "DRONE"
20 FIELD SID3,SID3 WITH "WRAP"
30 FLOW "DRIFT" FROM "DRONE" TO "DRONE" BY 1
40 FLOW "DRIFT"
```

---

# **7.19 — Tri‑Voice Stack**  
*(p. 7‑21)*

```basic
10 SUBSTRATE SID1,SID1 AS "A"
20 SUBSTRATE SID2,SID2 AS "B"
30 SUBSTRATE SID3,SID3 AS "C"
40 RESONATE "A","B" BY 2
50 RESONATE "B","C" BY 3
60 FLOW "A"
70 FLOW "B"
80 FLOW "C"
```

---

# **7.20 — Raster Sync Sweep**  
*(p. 7‑22)*

```basic
10 SUBSTRATE SID1,SID1 AS "LEAD"
20 FLOW "SWEEP" FROM "LEAD" TO "LEAD" BY 1
30 ALIGN "SWEEP" WITH RASTER 50
40 FLOW "SWEEP"
```

---

```
======================================================================
                               A P P E N D I X
======================================================================
                           D E V E L O P E R   N O T E S
======================================================================
                                                Print Edition • p. 7‑23
```

# **Appendix 7.A — Cartridge Architecture**

The RTT‑C64 cartridge hooks into:

- BASIC token table  
- IRQ vector  
- NMI vector  
- Zero‑page workspace  

All RTT commands dispatch to ROM‑resident routines.

---

# **Appendix 7.B — Memory Map**  
*(p. 7‑24)*

| Region | Purpose |
|--------|---------|
| $8000–$9FFF | RTT ROM (operators, flow engine) |
| $C000–$C7FF | RTT runtime workspace |
| $D000–$DFFF | SID/VIC‑II/CIA (unmodified) |

---

# **Appendix 7.C — Timing & IRQ Behavior**  
*(p. 7‑25)*

- RTT installs a raster‑aware IRQ handler  
- Active flows are stepped each frame  
- `ALIGN` modifies IRQ scheduling  
- `RESONATE` modifies flow coupling tables  

---

# **Appendix 7.D — Compatibility Notes**  
*(p. 7‑26)*

- Compatible with stock C‑64 and C‑64C  
- Compatible with 1541, 1571, SD2IEC  
- Fast‑Load cartridges may conflict unless disabled  
- Works with PAL and NTSC timing (auto‑detect)  
