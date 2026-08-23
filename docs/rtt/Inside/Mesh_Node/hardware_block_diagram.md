### RTT‑Inside underground mesh node — hardware block diagram (text)

Here’s a clean, implementation‑ready block diagram we can drop into `docs/_ideas/RTT-Inside_Coal_Mesh_Node_Hardware.md`.

---

```text
*
┌───────────────────────────────────────────────────────────────┐
│                 RTT-INSIDE MESH NODE (HARDWARE)               │
└───────────────────────────────────────────────────────────────┘

                 ┌───────────────────────────────┐
                 │        POWER STAGE            │
                 │                               │
                 │  • Battery (LiFePO4 / AA)     │
                 │  • Optional: vibration harv.  │
                 │  • Buck/boost regulator       │
                 │  • Power switch / fuse        │
                 └───────────────┬───────────────┘
                                 │ Vcc
                                 ▼

┌───────────────────────────────┐      ┌───────────────────────────────┐
│       MICROCONTROLLER         │      │        RADIO / PHY            │
│  (Low-power MCU, e.g. ARM-M0) │      │  (Sub-GHz RF or acoustic)     │
│                               │      │                               │
│  • CPU core                   │      │  • RF transceiver / modem     │
│  • Flash (firmware)           │◀────▶│  • Matching network          │
│  • RAM                        │  SPI │  • Antenna / transducer       │
│  • GPIO / ADC / I2C / UART    │      │                               │
└───────────────┬───────────────┘      └───────────────┬───────────────┘
                │                                      │
                │                                      │
                ▼                                      ▼

┌───────────────────────────────┐      ┌───────────────────────────────┐
│        SENSOR BLOCK           │      │       LOCAL I/O (OPTIONAL)    │
│                               │      │                               │
│  • Vibration sensor           │      │  • Status LEDs (G/Y/R)        │
│    - MEMS accel or geophone   │      │  • Buzzer (alarm)             │
│                               │      │  • Config button              │
│  • Gas sensor                 │      │  • Simple text display        │
│    - Methane / CO / dust      │      │    (for foreman handheld)     │
│                               │      │                               │
│  • Pressure / strain sensor   │      └───────────────────────────────┘
│    - Roof load proxy          │
│                               │
│  • Temperature / humidity     │
└───────────────────────────────┘

                ┌───────────────────────────────┐
                │     POWER MANAGEMENT          │
                │                               │
                │  • Battery monitor (ADC)      │
                │  • Sleep / wake control       │
                │  • Brown-out protection       │
                └───────────────────────────────┘
```

---

**Key ideas:**

- **MCU at the center**: runs RTT‑Inside invariant logic, resonance math, mesh protocol.  
- **Sensor block**: vibration + gas + pressure are first‑class; everything else is optional.  
- **Radio/PHY**: sub‑GHz RF where possible; acoustic transducer where RF dies.  
- **Power stage**: cheap battery, optionally topped up by vibration harvesting from the mine itself.  
- **Local I/O**: just enough for a miner or foreman to see “green / yellow / red” and hear an alarm.
