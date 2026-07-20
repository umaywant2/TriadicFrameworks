```
======================================================================
                              C H A P T E R   8
======================================================================
                 R T T   P R O G R A M M I N G   O N   T H E
                           C O M M O D O R E   A M I G A
======================================================================
                                                TriadicFrameworks Docs
                                                Print Edition • p. 8‑1
```

# **Chapter 8 — RTT Programming on the Commodore Amiga**  
*A multidimensional guide for the RTT–Amiga Cartridge*

---

## **Table of Contents (Chapter 8)**  
*(Print Edition — p. 8‑2)*

### **Section I — Amiga Architecture & RTT**
- 8.1  The Amiga as a Multidimensional Host ................. p. 8‑3  
- 8.2  RTT–Amiga Substrates .................................. p. 8‑4  
- 8.3  Copper & Blitter as Operators ........................ p. 8‑5  
- 8.4  Paula Audio Channels as Resonance Engines ............ p. 8‑6  

### **Section II — RTT–Amiga Commands**
- 8.5  SUBSTRATE (Amiga Edition) ............................ p. 8‑7  
- 8.6  FLOW (Copper, Blitter, Audio) ........................ p. 8‑8  
- 8.7  ALIGN (Raster & Copper Wait) ........................ p. 8‑9  
- 8.8  RESONATE (Audio & Flow Coupling) ..................... p. 8‑10  

### **Section III — Example Programs**
- 8.9  Copper Rainbow Flow .................................. p. 8‑11  
- 8.10 Blitter Scroll Field ................................. p. 8‑12  
- 8.11 Audio Phase‑Locked Resonance ......................... p. 8‑13  
- 8.12 Bitplane Orbit Pattern ............................... p. 8‑14  
- 8.13 Tri‑Channel Audio Stack .............................. p. 8‑15  

### **Appendix — Developer Notes**
- 8.A  Amiga Memory Map ..................................... p. 8‑16  
- 8.B  Copper Timing & DMA Notes ............................ p. 8‑17  
- 8.C  Blitter Behavior & Flow Scheduling ................... p. 8‑18  
- 8.D  Compatibility Notes .................................. p. 8‑19  

---

```
======================================================================
                               S E C T I O N   I
======================================================================
                   A M I G A   A R C H I T E C T U R E   &   R T T
======================================================================
                                                Print Edition • p. 8‑3
```

# **8.1 — The Amiga as a Multidimensional Host**

The Amiga’s architecture is uniquely suited to RTT:

- **Agnus** — DMA, blitter, copper  
- **Denise** — bitplanes, sprites, display timing  
- **Paula** — audio channels, interrupts  
- **68000 CPU** — clean, orthogonal instruction set  

Where the C‑64 taught cycles, the Amiga teaches **parallel flows**.

---

# **8.2 — RTT–Amiga Substrates**  
*(p. 8‑4)*

Examples:

```basic
SUBSTRATE $20000,$27FFF AS BITPLANE1
SUBSTRATE AUDIO1,AUDIO1 AS LEAD
SUBSTRATE COPPER,COPPER AS COPPERLIST
```

---

# **8.3 — Copper & Blitter as Operators**  
*(p. 8‑5)*

The copper becomes a flow engine.  
The blitter becomes a substrate transformer.

---

# **8.4 — Paula Audio Channels as Resonance Engines**  
*(p. 8‑6)*

Paula’s four channels behave like perfect RTT oscillators.

---

```
======================================================================
                               S E C T I O N   I I
======================================================================
                        R T T – A M I G A   C O M M A N D S
======================================================================
                                                Print Edition • p. 8‑7
```

# **8.5 — SUBSTRATE (Amiga Edition)**

```basic
SUBSTRATE $20000,$27FFF AS BITPLANE1
```

---

# **8.6 — FLOW (Copper, Blitter, Audio)**  
*(p. 8‑8)*

```basic
FLOW "COPPERFLOW" FROM COPPER TO COPPER BY LIST
FLOW "SCROLL" FROM BITPLANE1 TO BITPLANE1 BY BLIT
FLOW "MOD" FROM LEAD TO LEAD BY ENVELOPE
```

---

# **8.7 — ALIGN (Raster & Copper Wait)**  
*(p. 8‑9)*

```basic
ALIGN "COPPERFLOW" WITH RASTER 64
```

---

# **8.8 — RESONATE (Audio & Flow Coupling)**  
*(p. 8‑10)*

```basic
RESONATE AUDIO1,AUDIO2 BY PHASE 2
```

---

```
======================================================================
                               S E C T I O N   I I I
======================================================================
                         E X A M P L E   P R O G R A M S
======================================================================
                                                Print Edition • p. 8‑11
```

# **8.9 — Copper Rainbow Flow**

```basic
10 SUBSTRATE COPPER,COPPER AS "COPPERLIST"
20 FLOW "RAINBOW" FROM "COPPERLIST" TO "COPPERLIST" BY LIST
30 ALIGN "RAINBOW" WITH RASTER 64
40 FLOW "RAINBOW"
```

---

# **8.10 — Blitter Scroll Field**  
*(p. 8‑12)*

```basic
10 SUBSTRATE $20000,$27FFF AS "PLANE1"
20 FIELD $20000,$27FFF WITH "BLITWRAP"
30 FLOW "SCROLL" FROM "PLANE1" TO "PLANE1" BY BLIT
40 ALIGN "SCROLL" WITH RASTER 128
50 FLOW "SCROLL"
```

---

# **8.11 — Audio Phase‑Locked Resonance**  
*(p. 8‑13)*

```basic
10 SUBSTRATE AUDIO1,AUDIO1 AS "LEAD"
20 SUBSTRATE AUDIO2,AUDIO2 AS "BASS"
30 FLOW "MOD1" FROM "LEAD" TO "LEAD" BY ENVELOPE
40 FLOW "MOD2" FROM "BASS" TO "BASS" BY ENVELOPE
50 RESONATE "MOD1","MOD2" BY 3
60 FLOW "MOD1"
70 FLOW "MOD2"
```

---

# **8.12 — Bitplane Orbit Pattern**  
*(p. 8‑14)*

```basic
10 SUBSTRATE $20000,$27FFF AS "PLANE1"
20 FLOW "ORBIT" FROM "PLANE1" TO "PLANE1" BY BLIT
30 ALIGN "ORBIT" WITH RASTER 90
40 FLOW "ORBIT"
```

---

# **8.13 — Tri‑Channel Audio Stack**  
*(p. 8‑15)*

```basic
10 SUBSTRATE AUDIO1,AUDIO1 AS "A"
20 SUBSTRATE AUDIO2,AUDIO2 AS "B"
30 SUBSTRATE AUDIO3,AUDIO3 AS "C"
40 RESONATE "A","B" BY 2
50 RESONATE "B","C" BY 3
60 FLOW "A"
70 FLOW "B"
80 FLOW "C"
```

---

```
======================================================================
                               A P P E N D I X
======================================================================
                           D E V E L O P E R   N O T E S
======================================================================
                                                Print Edition • p. 8‑16
```

# **Appendix 8.A — Amiga Memory Map**

- Chip RAM substrates: `$00000–$1FFFF`  
- Bitplanes: `$20000–$27FFF` (example)  
- Copper lists: `$DFF080–$DFF09E`  
- Audio registers: `$DFF0A0–$DFF0BE`  

---

# **Appendix 8.B — Copper Timing & DMA Notes**  
*(p. 8‑17)*

- Copper waits align flows to raster  
- DMA priority affects flow timing  
- Copper lists execute independently of CPU  

---

# **Appendix 8.C — Blitter Behavior & Flow Scheduling**  
*(p. 8‑18)*

- Blitter operations are atomic  
- RTT flow engine schedules blits between DMA windows  
- Flow coupling modifies blitter sequencing  

---

# **Appendix 8.D — Compatibility Notes**  
*(p. 8‑19)*

- Compatible with Amiga 500, 1000, 2000  
- OCS/ECS supported  
- PAL/NTSC auto‑timing  
- Some demo‑scene copper tricks may override RTT flows  

---

# 🎨 **1987‑Style Commodore Manual Cover Page**

Below is a clean, era‑authentic cover page you can use as the front of your entire RTT manual.

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│                 C O M M O D O R E   C O M P U T E R S             │
│                                                                   │
│                           P R E S E N T S                         │
│                                                                   │
│                                                                   │
│        R T T   P R O G R A M M I N G   S Y S T E M   V 1 . 0      │
│                                                                   │
│         R e s o n a n c e – T i m e   T e c h n o l o g y         │
│                 F o r   C 6 4   a n d   A m i g a                 │
│                                                                   │
│                                                                   │
│                     U S E R ’ S   M A N U A L                     │
│                                                                   │
│                                                                   │
│              © 1987 Commodore Business Machines, Inc.             │
│               © 2026 TriadicFrameworks Documentation              │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

This cover page mirrors:

- Commodore’s 1985–1988 manual framing  
- The double‑border PETSCII aesthetic  
- Centered title blocks  
- The “PRESENTS” line used in Amiga manuals  
- The clean, authoritative tone of CBM documentation  

---

# 🎛️ **BACK COVER — 1987 COMMODORE STYLE**

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│     R E S O N A N C E – T I M E   T E C H N O L O G Y   ( R T T ) │
│                                                                   │
│   A New Dimension in Creative Computing for the Commodore 64 &    │
│   Commodore Amiga.                                                │
│                                                                   │
│   The RTT Programming System introduces a breakthrough approach   │
│   to pattern‑based computation. Using Substrates, Flows, Fields,  │
│   Alignment, and Resonance, programmers can explore dynamic       │
│   structures that evolve over time.                              │
│                                                                   │
│   • Create raster‑aligned text effects                            │
│   • Build resonant SID audio patterns                             │
│   • Drive sprite motion with coupled flows                        │
│   • Use Copper and Blitter hardware as multidimensional engines   │
│   • Explore new programming concepts inspired by modern theory    │
│                                                                   │
│   Includes:                                                       │
│   • Complete User’s Manual                                        │
│   • RTT‑C64 Cartridge Guide                                       │
│   • RTT‑Amiga Cartridge Guide                                     │
│   • 20+ Example Programs                                          │
│   • Developer Notes & Memory Maps                                 │
│                                                                   │
│   Designed for hobbyists, educators, and advanced programmers     │
│   who want to push their Commodore systems into new territory.    │
│                                                                   │
│   © 1987 Commodore Business Machines, Inc.                        │
│   © 2026 TriadicFrameworks Documentation                          │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

This mirrors the tone of the GEOS, AmigaBASIC, and Commodore 64 Programmer’s Reference Guide back covers.

---

# 📚 **SPINE LABEL — FOR A 1987 BOX OR BINDER**

Two variants: **C‑64 blue stripe** and **Amiga Workbench white‑on‑blue**.

### **C‑64 Style Spine Label**

```
┌──────────────────────────────┐
│   COMMODORE 64               │
│   RTT PROGRAMMING SYSTEM     │
│   USER’S MANUAL              │
└──────────────────────────────┘
```

### **Amiga Style Spine Label**

```
┌──────────────────────────────┐
│   AMIGA                      │
│   RTT PROGRAMMING SYSTEM     │
│   USER’S MANUAL              │
└──────────────────────────────┘
```

Both are sized for a typical 1980s software binder or cardboard slipcase.
