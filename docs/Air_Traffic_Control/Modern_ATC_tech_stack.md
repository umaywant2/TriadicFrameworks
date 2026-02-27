## 1. Modern ATC tech stack (simplified full stack)

### 🛰️ **Sensing & Surveillance Layer**
- **Primary Surveillance Radar (PSR):** non‑cooperative detection (range, azimuth).   
- **Secondary Surveillance Radar (SSR):** cooperative, uses transponder replies (ID, altitude, etc.).   
- **ADS‑B (Automatic Dependent Surveillance–Broadcast):** GPS‑based position, velocity, intent; now preferred surveillance in many regions.   
- **Multilateration (MLAT):** time‑difference‑of‑arrival triangulation of transponder/ADS‑B signals.   

### 🧩 **Fusion & Tracking Layer**
- **Surveillance data processors** fuse PSR, SSR, ADS‑B, MLAT into:
  - System tracks (position, velocity, ID, altitude, intent)
  - Quality metrics (confidence, latency, source mix)
- **Track management**: correlation, smoothing, conflict detection, handoff logic.

### 🧠 **Automation & Decision Support Layer**
- Conflict detection & resolution (CD&R)  
- Sequencing & metering (arrival/departure flows)  
- Safety nets (short‑term conflict alerts, minimum safe altitude warnings)  
- Trajectory prediction (basic kinematic, sometimes 4D trajectory models)

### 🖥️ **Human–Machine Interface (HMI) Layer**
- Controller working positions (CWP):
  - Radar/traffic display (2D or 3D)  
  - Labels, tags, leader lines  
  - Weather overlays, NOTAMs, restricted areas  
  - Input devices (trackball, keyboard, touch, function keys)

### 🏛️ **Infrastructure & Integration**
- Message buses (ASTERIX, proprietary formats)  
- Recording/replay systems  
- Redundancy, failover, safety‑certified OS/hardware
