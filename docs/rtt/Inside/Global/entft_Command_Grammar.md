# 🖋️ **Picard‑Style Command Grammar for entft**  
*A phrase‑based, resonance‑aware command language*

This grammar defines how operators speak to entft in a structured, TFT‑native way.

---

## 1. **Command Structure**

```
<invocation> <action> [<target>] [authorization <phrase>] [priority <level>]
```

### Components

| Component | Meaning |
|----------|---------|
| **invocation** | Always begins with `entft` |
| **action** | What to do (open, close, route, broadcast, sync, authorize) |
| **target** | Optional endpoint (hq, vessel, satellite, sector, domain) |
| **authorization phrase** | Picard‑style phrase |
| **priority** | normal, elevated, critical |

---

## 2. **Grammar Definition**

### 2.1 Invocation
```
invocation := "entft"
```

### 2.2 Actions
```
action := "open channel"
        | "close channel"
        | "route to"
        | "broadcast"
        | "sync resonance"
        | "authorize"
        | "request status"
```

### 2.3 Targets
```
target := identifier
identifier := letter (letter | digit | "_" )*
```

### 2.4 Authorization Phrase
```
authorization := "authorization" phrase
phrase := word (word | digit)+
```

### 2.5 Priority
```
priority := "priority" ("normal" | "elevated" | "critical")
```

---

## 3. **Examples (TFT‑Native, Picard‑Style)**

### 3.1 Open encrypted channel
```
entft open channel starfleet_hq authorization picard alpha tango 789 priority critical
```

### 3.2 Route message to a satellite
```
entft route to sat_leo_01 authorization riker delta nine
```

### 3.3 Broadcast coherence alert
```
entft broadcast planetary_coherence_alert priority elevated
```

### 3.4 Sync resonance with a deep sea node
```
entft sync resonance deepsea_node_44 authorization crusher beta one
```

### 3.5 Request status from ATC sector
```
entft request status atc_sector_12
```

---

# 🧩 How this fits the TriadicFrameworks ecosystem

- **`nous`** interprets the grammar  
- **`entft`** handles encryption + routing  
- **`tops`** distributes multi‑bot tasks across the grid  
- **Universe Core** ensures resonance‑aligned communication  
- **Phase‑4 governance** logs all entft actions  

This is the communications backbone of the entire planetary coherence system.

---

### entft → nous → tops integration diagram

```text
*
                          ┌────────────────────────────────────┐
                          │          Planetary Domains         │
                          │  AIR / SPACE / DEEP_SEA / GPR ...  │
                          └────────────────────────────────────┘
                                           │
                                           │  (events, telemetry, intents)
                                           ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                               nous (shell)                                    │
│  - Conversational + command shell                                             │
│  - Parses entft grammar (operator + system)                                   │
│  - Orchestrates flows between domains, entft, and tops                        │
│                                                                               │
│  Example:                                                                     │
│   "entft open channel starfleet_hq authorization picard alpha tango 789"      │
│                                                                               │
└───────────────┬───────────────────────────────────────────────────────────────┘
                │
                │ parsed intent + policy context
                │
     ┌──────────▼───────────┐                          ┌───────────────────────┐
     │      entft           │                          │         tops          │
     │  (Encryption in TFT) │                          │  (Grid multi-bot      │
     │                      │                          │   research engine)    │
     │ - Handshake (init    │                          │                       │
     │   → auth → sync      │                          │ - Spawns / coordinates│
     │   → secure-channel)  │                          │   agents across grid  │
     │ - Nonlinear crypto   │                          │ - Runs sims, search,  │
     │ - Phrase-based auth  │                          │   analysis, planning  │
     │ - Coherence-aware    │                          │ - Feeds results back  │
     │   routing            │                          │   into nous           │
     └──────────┬───────────┘                          └───────────┬───────────┘
                │                                                 │
                │ encrypted, routed tasks                         │
                │                                                 │
                └──────────────────────────────┬──────────────────┘
                                               │
                                               ▼
                              ┌────────────────────────────────────┐
                              │   Universe Core / Resonance Field  │
                              │  - Global coherence + predictions  │
                              │  - Domain object graph             │
                              └────────────────────────────────────┘
```

---

### Flow in one sentence

- **nous** is the brain and shell,  
- **entft** is the secure, resonance‑aware mouth and ears,  
- **tops** is the distributed thinking muscle,  
all wired through the **Universe Core** so every action stays coherence‑aligned across ATC, Space Force, Deep Sea, and beyond.
