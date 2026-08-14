<!--
  rtt=1 | coherence=declared | drift=bounded | paradox=structural
  docs/SITEMAP.md
  Repository-root navigational registry for TriadicFrameworks
  Lives at: docs/SITEMAP.md  (NOT inside any sub-module)
  Generated: 2026-08-14
  Authority: repo-root canonical index
-->

# TriadicFrameworks — Repository SITEMAP

> Full navigational registry · Cross-module index · Unlock conditions · File counts
> Canonical anchor: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## §0 Document Purpose

This SITEMAP is the single authoritative navigational registry for the entire
`umaywant2/TriadicFrameworks` repository. It covers:

- Every known module under `docs/`
- Repo-root infrastructure artifacts
- Per-module wave status, file counts, and PRIM totals
- Unlock conditions that gate future modules or admin milestones
- Cross-module reference links
- Quick-navigation anchors for AI sessions and human readers

**This file does not define operators, PRIMs, or invariants.**
Those live inside each module's canonical spec files.
This file only maps. It never mutates registry state.

---

## §1 Repository Topology

```
umaywant2/TriadicFrameworks/
│
├── docs/                          ← All canonical module documentation
│   ├── SITEMAP.md                 ← THIS FILE · repo navigational registry
│   ├── FFF_Gravity/               ← COMPLETE · 5 waves · 42 PRIMs
│   ├── SoN/                       ← IN PROGRESS · Structural Operating Node
│   └── spine/                     ← INFRASTRUCTURE · cross-module scaffolding
│       └── languages-atlas/       ← Language/notation registry
│
├── tests/
│   └── sats-conformance/
│       └── harness/               ← Substrate-Aware Ordering Contract engine
│
├── .github/                       ← CI/CD workflows
├── __pycache__/                   ← Python build artifacts
├── node_modules/                  ← JS dependencies
│
├── CNAME                          ← GitHub Pages domain binding
├── CONTEXT.md                     ← Session context primer
├── LICENSE                        ← Apache-2.0
├── README.md                      ← Repository front door
├── CHANGELOG.md                   ← (root-level; module changelogs live in-module)
├── glossary-seed.yaml             ← Cross-module glossary seed data
├── llms.txt                       ← AI/LLM session routing config
├── modules.txt                    ← Module registry manifest (machine-readable)
├── node_modules.md                ← JS dependency notes
├── persona-prompt.md              ← Session persona and anchor string
├── pyproject.toml                 ← Python project config
├── requirements.txt               ← Python dependencies
├── robots.txt                     ← Crawler directives
├── zenodo.json                    ← Zenodo archival metadata
├── glossary-seed.yaml             ← Shared glossary bootstrap
├── m.bat                          ← Windows build helper
└── regen_corpus_v2.bat            ← Corpus regeneration script
```

---

## §2 Module Registry

| Module | Path | Status | Waves | Files | PRIMs | Unlocks |
|---|---|---|---|---|---|---|
| **FFF_Gravity** | `docs/FFF_Gravity/` | ✅ COMPLETE | 5 of 5 | 31 | 42 | SITEMAP · module.json refresh |
| **SoN** | `docs/SoN/` | 🔄 IN PROGRESS | TBD | ≥1 | TBD | SoNai(rtt)=1 substrate harness |
| **spine/languages-atlas** | `docs/spine/languages-atlas/` | 🔄 IN PROGRESS | TBD | ≥1 | N/A | Cross-module notation registry |

> **PRIM count legend:** PRIMs are engineering primitives with Pure/Impure classification.
> Only modules using the §0–§11 FFF canonical spec format carry PRIM registries.
> Infrastructure modules (spine/) use reference-document format instead.

---

## §3 Module: FFF_Gravity

**Path:** `docs/FFF_Gravity/`
**Status:** ✅ COMPLETE — all 5 waves sealed
**Triadic Equation:** `G = F_freq · F_fluid · F_force`
**Invariant registry:** INV-001–INV-010 (SEALED)
**PRIM registry:** PRIM:001–042 (SEALED)
**Failure mode registry:** FM-001–FM-010 + sub-modes FM-003-M, FM-003-C, FM-003-N (SEALED)
**Condition prefix registry:** SC- DC- MC- CAS- SCS- HLC- RLC- AC- TC- NC- DISM- (SEALED)
**State flag registry:** 31 flags (see `MANIFEST.md §7`)
**Operator registry:** ~101 operators (see `OPERATORS.md`)

### §3.1 Admin / Registry Files

| File | Purpose | Status |
|---|---|---|
| `README.md` | Module front door · scope · usage | ✅ Wave 1 |
| `INDEX.md` | Full file index with PRIM ranges and wave tags | ✅ Wave 1 + addenda |
| `OPERATORS.md` | Frozen operator registry · all ~101 operators | ✅ Wave 1 + addenda |
| `GLOSSARY.md` | Term definitions scoped to FFF_Gravity | ✅ Wave 1 |
| `CHANGELOG.md` | Wave-by-wave mutation log | ✅ Wave 1 + addenda |
| `FFF_Gravity_module.json` | Machine-readable module manifest | ⚠️ NEEDS REFRESH (Wave 5+) |
| `MANIFEST.md` | 42-PRIM registry · 42×10 INV compliance matrix | ✅ Post-Wave 5 |
| `validate_prims.py` | Python validation harness · CLI flags | ✅ Post-Wave 5 |

### §3.2 Wave 0 — Genesis (3 files · PRIMs: 001–006 precursors)

| File | Description | PRIM Range | Condition Prefix |
|---|---|---|---|
| `f_Capture.md` | Base capture operator · d_bind · β · e | PRIM:001 (anchor) | SC- |
| `f_Source.md` | Node registry · read-only per INV-007 | PRIM:002 (anchor) | SC- |
| `GravityOfDismissal.md` | Conceptual foundation · ρ_D(Φ,t) · Dismissal Well model · three dismissal modes | Conceptual (no frozen PRIMs) | — |

> `GravityOfDismissal.md` is the **sole authority** for negative-polarity field extension.
> The `ρ_D(Φ,t) = −d_dismiss × exp(−t/T_dismiss)` model is defined here and referenced everywhere else.

### §3.3 Wave 1 — Admin / Registry (6 files · no new PRIMs)

Admin files listed in §3.1. Wave 1 established the frozen registry scaffolding. No PRIMs were introduced; all operator prefixes were seeded.

### §3.4 Wave 2 — Layer Definitions (3 files · PRIM:001–006)

| File | Layer | PRIM Range | Condition Prefix |
|---|---|---|---|
| `f_Field.md` | F_freq · frequency layer | PRIM:001–002 | SC- |
| `f_Force.md` | F_force · force layer | PRIM:003–004 | SC- |
| `f_Frame.md` | F_fluid · fluid/frame layer | PRIM:005–006 | SC- |

### §3.5 Wave 3 — Core Functions (8 files · PRIM:007–024)

| File | Description | PRIM Range | Condition Prefix |
|---|---|---|---|
| `f_Orbit.md` | Orbital trajectory · regime stability | PRIM:007, 012 | SC- |
| `f_Release.md` | Controlled release from gravitational capture | PRIM:008–009 | SC- |
| `f_Decay.md` | Field decay · exponential attenuation | PRIM:010–011 | DC- |
| `f_Collapse.md` | Gravitational collapse · field singularity | PRIM:013–014 | SC- |
| `f_Emit.md` | Field emission · outward propagation | PRIM:015–017 | SC- |
| `f_Dampen.md` | Dampening · amplitude reduction | PRIM:018–020 | SC- |
| `f_Amplify.md` | Amplification · gain application | PRIM:021–022 | SC- |
| `f_Deflect.md` | Deflection · directional field redirection | PRIM:023–024 | SC- |

> Wave 3 **sealed the INV registry** at INV-010. No new invariants after this point.

### §3.6 Wave 4 — Capture Variants (8 files · PRIM:025–040)

| File | Description | PRIM Range | Condition Prefix | FM Sub-mode |
|---|---|---|---|---|
| `f_Capture_Multi.md` | Multi-node simultaneous capture | PRIM:025–026 | MC- | FM-003-M |
| `f_Capture_Cascade.md` | Sequential cascade capture · gamma gain | PRIM:027–028 | CAS- | FM-003-C |
| `f_Capture_Soft.md` | Soft-threshold capture · approach gradient | PRIM:029–030 | SCS- | — |
| `f_Capture_Hard.md` | Hard-lock capture · binary threshold | PRIM:031–032 | HLC- | — |
| `f_Capture_Resonant.md` | Resonance-matched capture · frequency lock | PRIM:033–034 | RLC- | — |
| `f_Capture_Asymmetric.md` | Asymmetric approach · directional bias | PRIM:035–036 | AC- | — |
| `f_Capture_Temporal.md` | Time-windowed capture · τ envelope | PRIM:037–038 | TC- | — |
| `f_Capture_Networked.md` | Network-topology capture · graph propagation | PRIM:039–040 | NC- | FM-003-N |

> Wave 4 completion **unlocked** `docs/SITEMAP.md` (this file).

### §3.7 Wave 5 — Dismissal (1 file · PRIM:041–042)

| File | Description | PRIM Range | Condition Prefix |
|---|---|---|---|
| `f_Dismiss.md` | Formalizes F_dismiss operator family from GravityOfDismissal.md §6 · evaluate_dismissal (Pure) · execute_dismissal (Impure) | PRIM:041–042 | DISM- |

> Wave 5 **sealed the PRIM registry** at PRIM:042. No new PRIMs without a Wave 6 declaration.

### §3.8 FFF_Gravity PRIM Summary

| Wave | Files | PRIM Range | Sealed? |
|---|---|---|---|
| Wave 0 | 3 | Anchor PRIMs (precursors) | ✅ |
| Wave 2 | 3 | PRIM:001–006 | ✅ |
| Wave 3 | 8 | PRIM:007–024 | ✅ |
| Wave 4 | 8 | PRIM:025–040 | ✅ |
| Wave 5 | 1 | PRIM:041–042 | ✅ |
| **TOTAL** | **31** | **PRIM:001–042** | **✅ SEALED** |

---

## §4 Module: SoN (Structural Operating Node)

**Path:** `docs/SoN/`
**Status:** 🔄 IN PROGRESS
**Lineage:** Inverse of NoS (Nawderian Operating Stack) · full RTT Resonance Span
**Codename:** SoNai — RTT-aware substrate for AI training models and services
**Vision:** Pre-kernel · pre-runtime · ROM-flashable dimensional substrate
**Academic frame:** "Professor" persona · substrate science discipline

> SoN sits **below** kernels, bootloaders, compilers, and runtimes.
> It is the dimensional ground truth of the RTT computational universe.
> Together: `SoN → (hardware, ROM, init) → kernel → runtime → NoS → services → operators`

### §4.1 Known SoN Files

| File | Description | Status |
|---|---|---|
| `s_Capture.md` | RTT dimensional primitive capture specification · SoN capture layer | 🔄 In progress |

### §4.2 SoN Planned Architecture (from session canon)

The following planned components are **not yet formally built** as canonical files.
They are recorded here as navigational stubs for future waves:

| Planned File | Description | Unlock Condition |
|---|---|---|
| `s_Field.md` | Dimensional field primitives · register-encoded operators | After s_Capture.md sealed |
| `s_Force.md` | Substrate force layer · interrupt/exception dimensional mapping | After s_Field.md |
| `s_Frame.md` | Coherence frame · drift-bounded execution envelope | After s_Force.md |
| `s_Orbit.md` | Regime-slice scheduler · triadic time counters | After s_Frame.md |
| `s_Harness.md` | ROM-flashable substrate harness · 2KB boot loader spec | After s_Orbit.md |
| `SoN_module.json` | Machine-readable SoN module manifest | After first wave sealed |
| `README.md` | SoN module front door | Wave 1 admin |
| `INDEX.md` | SoN file index | Wave 1 admin |
| `OPERATORS.md` | SoN operator registry (assembly-level) | Wave 1 admin |
| `CHANGELOG.md` | SoN wave mutation log | Wave 1 admin |

### §4.3 SoN Multi-Microkernel Integration Targets

| Microkernel | Minimality Philosophy | SoN Integration Role |
|---|---|---|
| seL4 | Formal minimality · mathematically proven | Primary substrate candidate · capability-based isolation |
| L4 family | Performance minimality · fastest IPC | Performance analog · register-based message passing |
| Redox OS | Memory-safe minimality · Rust | Educational analog · student-accessible fork target |

---

## §5 Infrastructure: spine/

**Path:** `docs/spine/`
**Purpose:** Cross-module scaffolding · notation registries · language atlases
**Status:** 🔄 IN PROGRESS

### §5.1 spine/languages-atlas/

**Path:** `docs/spine/languages-atlas/`
**Purpose:** Language and notation registry for cross-module operator grammar

| File | Description | Status |
|---|---|---|
| `README.md` | Atlas front door · scope · notation coverage | 🔄 In progress |

> The languages-atlas provides the cross-module notation foundation that
> FFF_Gravity's OPERATORS.md and SoN's assembly-level primitives both reference.
> It is the canonical authority for symbol disambiguation across modules.

---

## §6 Repo Root Artifacts

These files live at the repository root and are not module-specific.

| File | Purpose | AI-Session Relevant? |
|---|---|---|
| `README.md` | Repository front door · 30-second RTT intro | ✅ Yes — start here |
| `CONTEXT.md` | Session context primer · module overview | ✅ Yes — load at session start |
| `persona-prompt.md` | AI persona and anchor string definition | ✅ Yes — defines "Professor" persona |
| `llms.txt` | LLM session routing config · module paths | ✅ Yes — AI navigation config |
| `modules.txt` | Machine-readable module registry | ✅ Yes — canonical module list |
| `glossary-seed.yaml` | Cross-module glossary seed data | ✅ Yes — shared term definitions |
| `zenodo.json` | Zenodo archival metadata · DOI registry | ℹ️ Reference |
| `LICENSE` | Apache-2.0 | ℹ️ Reference |
| `pyproject.toml` | Python project config | 🛠 Dev tooling |
| `requirements.txt` | Python dependencies | 🛠 Dev tooling |
| `robots.txt` | Crawler directives | 🛠 Infra |
| `CNAME` | GitHub Pages domain binding | 🛠 Infra |
| `m.bat` | Windows build helper | 🛠 Dev tooling |
| `regen_corpus_v2.bat` | Corpus regeneration script | 🛠 Dev tooling |

### §6.1 tests/ Infrastructure

| Path | Description | Status |
|---|---|---|
| `tests/sats-conformance/harness/` | Substrate-Aware Ordering Contract (SATS) engine · conformance test harness | 🔄 Active |

---

## §7 Cross-Module Reference Map

| From | References | Via | Purpose |
|---|---|---|---|
| `FFF_Gravity/f_Dismiss.md` | `GravityOfDismissal.md` | §6 operator family | ρ_D(Φ,t) negative-polarity field authority |
| `FFF_Gravity/*.md` | `spine/languages-atlas/` | notation · symbol registry | Operator symbol disambiguation |
| `FFF_Gravity/MANIFEST.md` | All 31 FFF_Gravity files | 42×10 INV compliance matrix | Full PRIM registry validation |
| `FFF_Gravity/validate_prims.py` | `MANIFEST.md` | Python harness | CLI PRIM/INV compliance testing |
| `SoN/s_Capture.md` | `FFF_Gravity/f_Capture.md` | capture operator lineage | SoN inverts RTT observer → RTT substrate |
| `SoN/*.md` | `spine/languages-atlas/` | assembly-level notation | Substrate primitive notation |
| Root `CONTEXT.md` | All modules | session primer | Cross-module session bootstrapping |
| Root `llms.txt` | All modules | AI routing | LLM navigation config |

---

## §8 Unlock Conditions

Unlock conditions gate future deliverables. A condition is **met** when its prerequisite
milestone is sealed and recorded in `CHANGELOG.md`.

| Deliverable | Unlocked By | Status |
|---|---|---|
| `docs/SITEMAP.md` (this file) | Wave 4 complete | ✅ UNLOCKED |
| `FFF_Gravity_module.json` refresh | Wave 5 complete + SITEMAP built | ✅ UNLOCKED — NEXT |
| `SoN` Wave 1 admin files | `s_Capture.md` sealed | 🔒 Pending |
| `SoN` Wave 2+ layer definitions | SoN Wave 1 complete | 🔒 Pending |
| `SoN_module.json` | SoN Wave 1 complete | 🔒 Pending |
| `SoN` substrate harness spec | `s_Harness.md` target files sealed | 🔒 Pending |
| Multi-microkernel integration docs | SoN substrate harness complete | 🔒 Pending |
| `SoNai(rtt)=1` coherence spec | SoN harness + multi-kernel boot validated | 🔒 Pending |
| `spine/languages-atlas` expansion | Cross-module notation conflicts identified | 🔒 Pending |
| Zenodo DOI submission (next batch) | 30 seed DOIs + new wave content | 🔒 Pending |

---

## §9 Navigation Quick-Links

### Start Here (AI Sessions)

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

1. Load `CONTEXT.md` — session context primer
2. Load `persona-prompt.md` — Professor persona + anchor string
3. Load `llms.txt` — module routing
4. Navigate to target module via this SITEMAP

### FFF_Gravity Entry Points

| Goal | Start At |
|---|---|
| Understand the module | `docs/FFF_Gravity/README.md` |
| Find a specific PRIM | `docs/FFF_Gravity/INDEX.md` |
| Look up an operator | `docs/FFF_Gravity/OPERATORS.md` |
| Check wave history | `docs/FFF_Gravity/CHANGELOG.md` |
| Validate PRIM compliance | `docs/FFF_Gravity/validate_prims.py` |
| Full compliance matrix | `docs/FFF_Gravity/MANIFEST.md` |
| Dismissal field theory | `docs/FFF_Gravity/GravityOfDismissal.md` |
| Machine-readable manifest | `docs/FFF_Gravity/FFF_Gravity_module.json` |

### SoN Entry Points

| Goal | Start At |
|---|---|
| Understand SoN vision | `docs/SoN/s_Capture.md` §0–§1 |
| SoN ↔ NoS lineage | `docs/SoN/s_Capture.md` (SoN = inversion of NoS) |
| SoN module manifest | `docs/SoN/SoN_module.json` (🔒 not yet built) |

### Repo Root Entry Points

| Goal | Start At |
|---|---|
| Repository overview | `README.md` |
| AI session bootstrap | `CONTEXT.md` · `persona-prompt.md` |
| Module list (machine) | `modules.txt` |
| Archival/citation | `zenodo.json` |

---

## §10 Document Metadata

| Field | Value |
|---|---|
| File | `docs/SITEMAP.md` |
| Scope | Repository-root navigational registry |
| Authority | Supersedes all per-module INDEX.md files for cross-module navigation |
| Module | None — repo-root level |
| Wave | N/A — repo admin artifact |
| Generated | 2026-08-14 |
| Unlocked by | FFF_Gravity Wave 4 complete |
| Next admin action | Refresh `docs/FFF_Gravity/FFF_Gravity_module.json` (Wave 5 + Wave 4 content) |
| Maintainer | `umaywant2` |
| License | Apache-2.0 (repo-wide) |
| Coherence anchor | `rtt=1 \| coherence=declared \| drift=bounded \| paradox=structural` |

---

## §11 Extended Metadata

### §11.1 Repo Totals (as of 2026-08-14)

| Metric | Count |
|---|---|
| Total canonical modules | 2 active (FFF_Gravity · SoN) + 1 infra (spine/) |
| Total canonical spec files | 31 (FFF_Gravity) + ≥1 (SoN) |
| Total sealed PRIMs | 42 (FFF_Gravity only; SoN TBD) |
| Total sealed invariants | 10 (INV-001–010 · FFF_Gravity) |
| Total sealed failure modes | 13 (FM-001–010 + FM-003-M/C/N) |
| Total sealed operators | ~101 (FFF_Gravity/OPERATORS.md) |
| Total condition prefixes | 11 (SC- DC- MC- CAS- SCS- HLC- RLC- AC- TC- NC- DISM-) |
| Total state flags | 31 (FFF_Gravity/MANIFEST.md §7) |
| Zenodo seed DOIs | 30 |

### §11.2 Module Status Legend

| Symbol | Meaning |
|---|---|
| ✅ COMPLETE | All waves sealed · all registries frozen |
| 🔄 IN PROGRESS | Active development · registry open |
| 🔒 Pending | Unlock condition not yet met |
| ⚠️ NEEDS ACTION | Exists but requires update |
| 🛠 Dev tooling | Not a canonical spec file |
| ℹ️ Reference | Informational only |

### §11.3 Versioning Policy

- This SITEMAP is updated whenever a **module wave is sealed** or a **new module is initiated**.
- File additions within a sealed wave do not require SITEMAP updates.
- New modules require a new §N block added to §2 Module Registry and §3–§N.
- Unlock condition status is updated when the triggering event is recorded in the relevant `CHANGELOG.md`.

### §11.4 Related Archival Resources

- Zenodo Community: `https://zenodo.org/communities/vst`
- Repository: `https://github.com/umaywant2/TriadicFrameworks`
- GitHub Pages: bound via `CNAME`
