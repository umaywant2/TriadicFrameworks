### 🗂️ Where to Capture Remix JSON Output

| Purpose | Path | Notes |
|--------|------|-------|
| 🪙 Single remixed coin | `/docs/Coeus/coins/remixed_coin.json` | Default export from `coin_remixer.py`  
| 🧬 Remix lineage archive | `/docs/Coeus/coins/coin_archive.json` | Append each remix with timestamp, mutation type, and parent ID  
| 🧪 Tournament use | `/docs/Coeus/tournaments/class/results.json` | If remixed coin is used in benchmarking  
| 🧑‍⚖️ Validator review | `/docs/Coeus/validators/pending_remix.json` | If remix requires approval or annotation  
| 🪙 Token prep | `/docs/Coeus/tokens/token_queue.json` | If remix is queued for tokenization  

---

### 🧬 Example Entry for `coin_archive.json`

```json
{
  "id": "b7f3a2d4-9c1e-4f3e-9f1a-2a7e3d9c8f4b",
  "name": "ElectroniumRedux_v2",
  "type": "remix",
  "mutation": "emotional",
  "parent_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "created": "2025-10-16T17:00:00Z"
}
```
