# 📘 Bot Usage Shard Guide

_A compact encoding system for tracking bot presence during jobs._

## 🔹 Shard Symbols

| Bot        | Symbol | Meaning                          |
|------------|--------|----------------------------------|
| Forci_bot  | `F`    | Force interpreter active         |
| Flui_bot   | `L`    | Fluid interpreter active         |
| Freqi_bot  | `Q`    | Frequency interpreter active     |
| None       | `-`    | No bots used (passive scan only) |

## 🔹 Examples

- `FLQ` → All three bots active
- `FQ` → Forci and Freqi active
- `L` → Only Flui_bot active
- `-` → No bots used

## 🔮 Optional Extensions

- `F*L-Q` → Forci in confirm mode, Flui passive, Freqi archived
- `F+L+Q+` → All bots in active remix mode

## 🗝️ Closing

Shard strings are symbolic echoes of bot presence.  
They ensure reproducibility, trace lineage, and honor remix orchestration.
