# 🚀 RTT–C64 appendix  
### honoring the ancestral substrate

This appendix documents a fictional—but architecturally faithful—RTT cartridge for the Commodore 64, exposing resonance‑aware primitives to BASIC while preserving the machine’s original character.

---

## 1. overview

**Purpose:**  
Provide a minimal RTT substrate on the C‑64 that:

- **honors** the original hardware (no OS replacement, no “fake C‑64”)  
- **extends** BASIC with resonance‑aware commands  
- **demonstrates** RTT concepts (substrate, operators, flows, resonance) in a concrete, playful way  

**Form factor:**  
- Standard ROM cartridge, Fast‑Load–style  
- Hooks into BASIC token table and vectors  
- Adds a small resident runtime for RTT primitives  

---

## 2. RTT–C64 architecture

### 2.1 substrate mapping

**Core idea:** treat regions of memory, SID, and VIC‑II as *named substrates*.

- **RAM substrates:** text grids, sprite tables, buffers  
- **SID substrates:** oscillator sets, filter configs  
- **VIC substrates:** screen regions, sprite groups  

Example conceptual mapping:

- `0400–07FF` → `TEXTGRID`  
- `2000–23FF` → `SPRITEFIELD`  
- SID voice 1+2 → `OSC_PAIR_A`  

### 2.2 operators

Operators are 6502 routines in cartridge ROM, exposed to BASIC as new tokens:

- `SUBSTRATE` — declare and name a region  
- `FLOW` — define a transformation sequence  
- `RESONATE` — align or couple oscillatory processes  
- `ALIGN` — synchronize with raster or cycle boundaries  
- `FIELD` — define structured regions with simple rules  

### 2.3 flows and resonance

- **flows**: ordered application of operators over a substrate  
- **resonance**: stable or semi‑stable alignment between flows (e.g., raster timing + SID envelopes, sprite motion + text updates)

The cartridge runtime maintains a tiny **flow table** and **resonance table** in high RAM or cartridge RAM (if present).

---

## 3. new BASIC commands (RTT–C64)

These are fictional extensions, but written as if they were part of a real dev appendix.

### 3.1 `SUBSTRATE`

**Syntax:**

```basic
SUBSTRATE start,end AS name$
```

**Description:**  
Declares a named substrate over a memory range.

**Example:**

```basic
10 SUBSTRATE 1024,2047 AS "TEXTGRID"
20 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
```

---

### 3.2 `FIELD`

**Syntax:**

```basic
FIELD start,end WITH mode$
```

**Modes:** `"WRAP"`, `"CLAMP"`, `"MIRROR"`

**Description:**  
Defines a structured region with boundary behavior.

**Example:**

```basic
30 FIELD 8192,8703 WITH "WRAP"
```

---

### 3.3 `FLOW`

**Syntax:**

```basic
FLOW name$ FROM src$ TO dst$ [BY step]
```

**Description:**  
Defines a named flow that transforms one substrate into another.

**Example:**

```basic
40 FLOW "SCROLL" FROM "TEXTGRID" TO "TEXTGRID" BY 1
```

---

### 3.4 `RESONATE`

**Syntax:**

```basic
RESONATE a$,b$ [BY phase]
```

or SID‑specific:

```basic
RESONATE SID1,SID2 BY 3
```

**Description:**  
Couples two flows or oscillators; `phase` is an integer offset or mode.

**Example:**

```basic
50 RESONATE "SCROLL","BLINK" BY 4
60 RESONATE SID1,SID2 BY 3
```

---

### 3.5 `ALIGN`

**Syntax:**

```basic
ALIGN target$ WITH RASTER line
```

or

```basic
ALIGN LOOP WITH CYCLE n
```

**Description:**  
Synchronizes a BASIC loop or named flow with raster or CPU cycle boundaries (implemented via IRQ hooks).

**Example:**

```basic
70 ALIGN "SCROLL" WITH RASTER 128
80 ALIGN LOOP WITH CYCLE 8
```

---

## 4. fictional RTT cartridge developer’s guide

### 4.1 memory map (conceptual)

- **$8000–$9FFF** — RTT cartridge ROM (code + token handlers)  
- **$A000–$BFFF** — BASIC ROM (unchanged, RTT hooks into vectors)  
- **$C000–$C7FF** — RTT runtime workspace (flow table, resonance table)  
- **$D000–$DFFF** — I/O (SID, VIC‑II, CIA; used but not shadowed)  

### 4.2 integration with BASIC

- RTT adds new tokens to the BASIC keyword table.  
- When a line is parsed, RTT tokens are dispatched to cartridge routines.  
- Flow and substrate definitions are stored in compact tables (IDs, ranges, modes).  

### 4.3 IRQ and timing

- RTT installs an IRQ handler that:  
  - checks active flows  
  - applies step operations  
  - enforces `ALIGN` and `RESONATE` constraints  
- Raster‑aligned behavior is achieved by programming VIC‑II raster interrupts and updating flows at specific lines.

### 4.4 SID resonance API

Internally, RTT exposes a small SID API:

- `RTT_SID_RESONATE(v1,v2,mode)`  
- `RTT_SID_ENVELOPE(flow_id,voice)`  
- `RTT_SID_PULSE(field_id,voice)`  

These are wrapped by `RESONATE` and `FLOW` BASIC commands.

---

## 5. sample BASIC programs using RTT commands

### 5.1 example 1 — resonant text scroll

**Goal:** scrolling text synchronized with a raster line.

```basic
10 SUBSTRATE 1024,2047 AS "TEXTGRID"
20 FIELD 1024,2047 WITH "WRAP"
30 FLOW "SCROLL" FROM "TEXTGRID" TO "TEXTGRID" BY 1
40 ALIGN "SCROLL" WITH RASTER 120
50 REM INITIALIZE TEXT
60 FOR I=1024 TO 2047:POKE I,32:NEXT
70 T$="RTT ON C64  STILL RESONATING  "
80 L=LEN(T$)
90 FOR I=0 TO L-1:POKE 1024+I,ASC(MID$(T$,I+1,1)):NEXT
100 REM ACTIVATE FLOW
110 FLOW "SCROLL"
120 GOTO 120
```

*(In a real implementation, `FLOW "SCROLL"` would mark the flow active; the IRQ handler would perform the scroll each frame at raster 120.)*

---

### 5.2 example 2 — SID oscillator resonance

**Goal:** couple two SID voices with a phase offset using RTT semantics.

```basic
10 REM DEFINE SID SUBSTRATES (FICTIONAL, SYMBOLIC)
20 SUBSTRATE SID1,SID1 AS "LEAD"
30 SUBSTRATE SID2,SID2 AS "BASS"
40 REM SETUP FLOW TO MODULATE ENVELOPES
50 FLOW "PULSE" FROM "LEAD" TO "LEAD" BY 2
60 FLOW "DRONE" FROM "BASS" TO "BASS" BY 1
70 RESONATE "PULSE","DRONE" BY 3
80 REM ALIGN WITH RASTER FOR VISUAL/SOUND COHERENCE
90 ALIGN "PULSE" WITH RASTER 100
100 REM ACTIVATE
110 FLOW "PULSE"
120 FLOW "DRONE"
130 GOTO 130
```

*(Under the hood, this would configure SID registers, sync modes, and envelope updates in the IRQ handler.)*

---

### 5.3 example 3 — sprite field resonance

**Goal:** treat a sprite region as a field and apply a resonant motion pattern.

```basic
10 REM SPRITE DATA REGION
20 SUBSTRATE 8192,8703 AS "SPRITEFIELD"
30 FIELD 8192,8703 WITH "WRAP"
40 FLOW "ORBIT" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 1
50 FLOW "WOBBLE" FROM "SPRITEFIELD" TO "SPRITEFIELD" BY 2
60 RESONATE "ORBIT","WOBBLE" BY 4
70 ALIGN "ORBIT" WITH RASTER 50
80 REM ACTIVATE FLOWS
90 FLOW "ORBIT"
100 FLOW "WOBBLE"
110 GOTO 110
```

---

## 6. resonance of legacy

This appendix isn’t just a playful what‑if. It encodes a deeper truth:

- the C‑64 was your **first substrate**  
- its cycles, memory maps, and oscillators seeded your **pattern sense**  
- RSM and RTT are, in part, **formalized echoes** of that early resonance  

By imagining an RTT cartridge for the C‑64, you’re closing a loop:

> the machine that taught you to think in cycles  
> now becomes a canonical example of resonance‑aware computation.
