# 🔐 **entft Handshake Sequence (TFT‑Native)**  
*A resonance‑aware secure‑channel negotiation flow*

This is the full handshake lifecycle for entft, expressed in four phases:

1. **init**  
2. **auth**  
3. **resonance‑sync**  
4. **secure‑channel**

Each step is deterministic, domain‑agnostic, and compatible with `nous` and `tops`.

---

## 1. **INIT PHASE**  
The client announces intent to open an entft channel.

### Message: `entft:init`
```json
{
  "entft": {
    "version": "1.0",
    "phase": "init",
    "client_id": "acft-001",
    "domain": "air",
    "nonce": "c7f1a2...",
    "capabilities": ["phrase-auth", "resonance-sync", "governance-ledger"]
  }
}
```

### Server response: `entft:init_ack`
```json
{
  "entft": {
    "phase": "init_ack",
    "server_id": "starfleet_hq",
    "nonce_reply": "c7f1a2...",
    "challenge": "res-field-sample-9b3e..."
  }
}
```

The **challenge** is a resonance‑field sample used later in sync.

---

## 2. **AUTH PHASE**  
The client proves identity using:

- phrase‑based authorization  
- role  
- domain  
- resonance signature  

### Message: `entft:auth`
```json
{
  "entft": {
    "phase": "auth",
    "auth": {
      "phrase": "picard alpha tango 789",
      "role": "commanding_officer",
      "domain": "space",
      "signature": "res-sig-4f9a..."
    }
  }
}
```

### Server response: `entft:auth_ok`
```json
{
  "entft": {
    "phase": "auth_ok",
    "auth_level": "command",
    "session_id": "sess-22d1f",
    "next": "resonance-sync"
  }
}
```

If phrase or signature fails → `auth_fail`.

---

## 3. **RESONANCE‑SYNC PHASE**  
Both sides align to the same coherence field.

This ensures:

- drift‑minimized routing  
- stable packet paths  
- cross‑domain consistency  

### Message: `entft:sync`
```json
{
  "entft": {
    "phase": "resonance-sync",
    "session_id": "sess-22d1f",
    "client_field_sample": "field-sample-a1c2..."
  }
}
```

### Server response: `entft:sync_ok`
```json
{
  "entft": {
    "phase": "sync_ok",
    "coherence_path": "auto",
    "stability": 0.94,
    "next": "secure-channel"
  }
}
```

---

## 4. **SECURE‑CHANNEL PHASE**  
A fully encrypted, resonance‑aligned channel is established.

### Message: `entft:secure`
```json
{
  "entft": {
    "phase": "secure-channel",
    "session_id": "sess-22d1f",
    "cipher": "entft-nonlinear-v3",
    "ready": true
  }
}
```

### Server response: `entft:secure_ack`
```json
{
  "entft": {
    "phase": "secure_ack",
    "status": "encrypted",
    "channel": "open"
  }
}
```

The channel is now live.
