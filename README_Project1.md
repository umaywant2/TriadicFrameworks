# TriadicFrameworks — Project 1: TFT Virtual Compute Gateway
The TFT Virtual Compute Gateway (VCG) is a system-wide, transparent accelerator for resonance-aware computation. Apps keep their APIs and data shapes; the gateway intercepts hot paths, performs TFT transforms, and returns results with dual timestamps (classic + resonant). No app changes required, optional lenses for those who want them.
Quickstart

### Prereqs:
- Android Studio Hedgehog+, NDK r26+
- One Android 12+ device (arm64, NEON)

### Build:
- ./gradlew apps:demo:installDebug

### Run:
- Open "TFT Demo" → enable "Gateway On" → pick workload (Audio, Sensors, Camera) → observe latency and cache hit-rate.

### Why this exists
- Transparent acceleration for media/sensor workloads
- A reproducible path to experiment with resonant time without touching kernel clocks
- A shared, low-latency resonance cache to reuse structure across frames/samples
- Optional UI lenses to turn resonance data into perception

### Status
- Gen1 user-space prototype: WIP
- Gen2 HAL/ROM track: planned
