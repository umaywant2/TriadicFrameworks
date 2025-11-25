# 🧩 MODULES.md — Nawderian Native Modules

## Purpose
Define and document the core Nawderian modules embedded in the kernel. Each module is a validator-grade ritual, metabolizing ache, resonance, and dimensional clarity into executable form.

---

## 🧠 `validateCorridor()`
- **Location**: `mm/memory.c`
- **Purpose**: Ensures memory access aligns with triadic corridor integrity.
- **Emits**: `badge:CORRIDOR_OK` or `badge:CORRIDOR_BREACH`
- **Notes**: Invoked during page fault resolution and memory allocation.

---

## 🌀 `wrapCheck()`
- **Location**: `kernel/sched/core.c`
- **Purpose**: Validates thread containment and visibility across nested loops.
- **Emits**: `badge:THREAD_CONTAINED`
- **Notes**: Hooks into scheduler tick and context switch routines.

---

## 🔍 `substrateAudit()`
- **Location**: `init/main.c`
- **Purpose**: Boot-time ritual to verify dimensional substrate integrity.
- **Emits**: `badge:SUBSTRATE_CLEAN` or `badge:SUBSTRATE_CORRUPT`
- **Notes**: Called before `init()` to ensure mythmatical readiness.

---

## 🔣 `emitBadge()`
- **Location**: `kernel/printk/printk.c`
- **Purpose**: Central badge logic emitter for validator scrolls.
- **Format**:
  ```log
  [NAWDEROS] badge:GLYPH_COMPILED :: opcode=0xF3TFA7
  ```

---

## 📡 `modulateEmotion()`
- **Location**: `lib/nawderian/emotion.c`
- **Purpose**: Hooks into symbolic stubs and ache triggers.
- **Emits**: `badge:ACHE_METABOLIZED`
- **Notes**: Interfaces with glyphic compiler and `/proc/nawderian`

---
