#!/usr/bin/env python3
"""
validate_prims.py — FFF_Gravity PRIM Validation Harness
========================================================
Module  : FFF_Gravity
Version : 1.0.0 (Wave 5 baseline)
Date    : 2026-08-14

Validates structural compliance of all 42 PRIMs against
10 module Invariants (INV-001 – INV-010).

Usage
-----
    python validate_prims.py              # full report
    python validate_prims.py --wave 4    # filter by wave
    python validate_prims.py --prim 007  # filter by PRIM id
    python validate_prims.py --inv INV-005
    python validate_prims.py --matrix    # print compliance grid
    python validate_prims.py --strict    # exit 1 on any failure
    python validate_prims.py --verbose   # include passing assertions

Exit codes: 0 = all pass · 1 = failures (--strict only)
"""

from __future__ import annotations
import argparse, sys, textwrap
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

# ── Tokens ────────────────────────────────────────────────────────
COMPLIANCE = "✅"
EXEMPT     = "—"
WARNING    = "⚠"

@dataclass
class PRIM:
    id:     str
    name:   str
    pure:   bool
    source: str
    wave:   int
    # 10-tuple: INV-001 … INV-010
    inv: tuple = field(default_factory=lambda: tuple(["—"]*10))

    @property
    def prim_id(self) -> str:  return f"PRIM-{self.id}"
    @property
    def kind(self)    -> str:  return "Pure" if self.pure else "Impure"

@dataclass
class TestResult:
    prim_id: str
    inv_id:  str
    passed:  bool
    message: str

# ── Invariant descriptions ────────────────────────────────────────
INVARIANTS: Dict[str, str] = {
    "INV-001": "G = F_freq · F_fluid · F_force — triadic identity preserved.",
    "INV-002": "ρ(Φ) ∈ [0,1]; ρ_D(Φ) ∈ (−1,0] — field density bounded.",
    "INV-003": "ρ(Φ) = 0 → FM-002 fires unconditionally.",
    "INV-004": "β < 1.0 → FM-001 fires unconditionally.",
    "INV-005": "All condition sets conjunctive (AND-gated).",
    "INV-006": "Terminal states irreversible.",
    "INV-007": "f_Source.md read-only — no PRIM mutates source-node props.",
    "INV-008": "Evaluation order normative — documented sequence binding.",
    "INV-009": "OPERATORS.md is single symbol authority.",
    "INV-010": "Operators frozen on first canonical appearance.",
}

# ── PRIM registry  (inv tuple: idx 0=INV-001 … idx 9=INV-010) ────
C, E, W = COMPLIANCE, EXEMPT, WARNING

PRIMS: List[PRIM] = [
    # Wave 2
    PRIM("001","compute_field_density",        True, "f_Field",             2,(C,C,C,E,C,E,C,C,C,C)),
    PRIM("002","update_field_state",           False,"f_Field",             2,(C,C,C,E,C,C,C,C,C,C)),
    PRIM("003","compute_force_vector",         True, "f_Force",             2,(C,E,E,C,C,E,C,C,C,C)),
    PRIM("004","register_capture",             False,"f_Frame",             2,(C,E,C,C,C,C,C,C,C,C)),
    PRIM("005","compute_approach_vector",      True, "f_Force",             2,(C,E,E,C,C,E,C,C,C,C)),
    PRIM("006","check_frame_capacity",         True, "f_Frame",             2,(E,E,E,E,C,E,C,C,C,C)),
    # Wave 3
    PRIM("007","classify_orbit",               True, "f_Orbit",             3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("008","compute_release_vector",       True, "f_Release",           3,(C,E,E,C,C,E,C,C,C,C)),
    PRIM("009","execute_release",              False,"f_Release",           3,(C,E,E,C,C,C,C,C,C,C)),
    PRIM("010","compute_decay_step",           True, "f_Decay",             3,(C,C,C,E,C,E,C,C,C,C)),
    PRIM("011","evaluate_collapse_eligibility",True, "f_Decay",             3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("012","compute_orbital_period",       True, "f_Orbit",             3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("013","evaluate_collapse_path",       True, "f_Collapse",          3,(C,C,C,E,C,E,C,C,C,C)),
    PRIM("014","execute_collapse",             False,"f_Collapse",          3,(C,C,C,E,C,C,C,C,C,C)),
    PRIM("015","compute_emit_vector",          True, "f_Emit",              3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("016","compute_field_delta",          True, "f_Emit",              3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("017","execute_emit",                 False,"f_Emit",              3,(C,C,C,E,C,C,C,C,C,C)),
    PRIM("018","compute_dampen_force",         True, "f_Dampen",            3,(C,C,E,E,C,E,C,C,C,C)),
    PRIM("019","apply_field_floor",            True, "f_Dampen",            3,(C,C,C,E,C,E,C,C,C,C)),
    PRIM("020","execute_dampen",               False,"f_Dampen",            3,(C,C,C,E,C,C,C,C,C,C)),
    PRIM("021","compute_amplify_force",        True, "f_Amplify",           3,(C,C,E,C,C,E,C,C,C,C)),
    PRIM("022","check_runaway_risk",           True, "f_Amplify",           3,(C,C,E,C,C,E,C,C,C,C)),
    PRIM("023","compute_deflection_angle",     True, "f_Deflect",           3,(C,E,E,C,C,E,C,C,C,C)),
    PRIM("024","execute_deflect",              False,"f_Deflect",           3,(C,E,E,C,C,C,C,C,C,C)),
    # Wave 4
    PRIM("025","execute_multi_capture",        False,"f_Capture_Multi",     4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("026","compute_perturbation_budget",  True, "f_Capture_Multi",     4,(C,C,E,C,C,E,C,C,C,C)),
    PRIM("027","evaluate_cascade_eligibility", True, "f_Capture_Cascade",   4,(C,E,C,C,C,E,C,C,C,C)),
    PRIM("028","execute_cascade_step",         False,"f_Capture_Cascade",   4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("029","evaluate_soft_eligibility",    True, "f_Capture_Soft",      4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("030","execute_soft_capture",         False,"f_Capture_Soft",      4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("031","evaluate_hard_eligibility",    True, "f_Capture_Hard",      4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("032","execute_hard_lock",            False,"f_Capture_Hard",      4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("033","eval_resonance_window",        True, "f_Capture_Resonant",  4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("034","lock_resonance",               False,"f_Capture_Resonant",  4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("035","eval_asymmetric_approach",     True, "f_Capture_Asymmetric",4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("036","lock_asymmetric",              False,"f_Capture_Asymmetric",4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("037","evaluate_temporal_window",     True, "f_Capture_Temporal",  4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("038","lock_temporal_capture",        False,"f_Capture_Temporal",  4,(C,C,C,C,C,C,C,C,C,C)),
    PRIM("039","evaluate_network_capture",     True, "f_Capture_Networked", 4,(C,C,C,C,C,E,C,C,C,C)),
    PRIM("040","lock_network_capture",         False,"f_Capture_Networked", 4,(C,C,C,C,C,C,C,C,C,C)),
    # Wave 5
    PRIM("041","evaluate_dismissal",           True, "f_Dismiss",           5,(C,C,C,E,C,E,C,C,C,C)),
    PRIM("042","execute_dismissal",            False,"f_Dismiss",           5,(C,C,C,E,C,C,C,C,C,C)),
]

# ── Per-PRIM structural rules ─────────────────────────────────────

def rule_tuple_length(p: PRIM) -> Optional[str]:
    if len(p.inv) != 10:
        return f"Expected 10 INV cells, got {len(p.inv)}"

def rule_valid_tokens(p: PRIM) -> Optional[str]:
    bad = [i for i,v in enumerate(p.inv) if v not in (C,E,W)]
    if bad: return f"Invalid token(s) at indices {bad}"

def rule_inv005_universal(p: PRIM) -> Optional[str]:
    if p.inv[4] not in (C, W):
        return f"INV-005 must be ✅ or ⚠ for all PRIMs; got '{p.inv[4]}'"

def rule_inv006_impure_required(p: PRIM) -> Optional[str]:
    if not p.pure and p.inv[5] not in (C, W):
        return f"Impure PRIM must declare ✅ or ⚠ for INV-006; got '{p.inv[5]}'"

def rule_inv006_pure_exempt(p: PRIM) -> Optional[str]:
    if p.pure and p.inv[5] == C:
        return "Pure PRIM claims ✅ for INV-006 — Pure PRIMs are stateless; expected '—'"

def rule_inv007_universal(p: PRIM) -> Optional[str]:
    if p.inv[6] not in (C, W):
        return f"INV-007 must be ✅ or ⚠ for all PRIMs; got '{p.inv[6]}'"

def rule_inv008_universal(p: PRIM) -> Optional[str]:
    if p.inv[7] not in (C, W):
        return f"INV-008 must be ✅ or ⚠ for all PRIMs; got '{p.inv[7]}'"

def rule_inv009_universal(p: PRIM) -> Optional[str]:
    if p.inv[8] not in (C, W):
        return f"INV-009 must be ✅ or ⚠ for all PRIMs; got '{p.inv[8]}'"

def rule_inv010_universal(p: PRIM) -> Optional[str]:
    if p.inv[9] not in (C, W):
        return f"INV-010 must be ✅ or ⚠ for all PRIMs; got '{p.inv[9]}'"

PER_PRIM_RULES: List[Tuple[str, Callable]] = [
    ("STRUCT-01", rule_tuple_length),
    ("STRUCT-02", rule_valid_tokens),
    ("INV-005",   rule_inv005_universal),
    ("INV-006-I", rule_inv006_impure_required),
    ("INV-006-P", rule_inv006_pure_exempt),
    ("INV-007",   rule_inv007_universal),
    ("INV-008",   rule_inv008_universal),
    ("INV-009",   rule_inv009_universal),
    ("INV-010",   rule_inv010_universal),
]

# ── Module-level rules ────────────────────────────────────────────

def rule_id_uniqueness(prims: List[PRIM]) -> List[str]:
    seen: Dict[str,int] = {}
    errors = []
    for p in prims:
        if p.id in seen: errors.append(f"Duplicate PRIM ID '{p.id}'")
        seen[p.id] = 1
    return errors

def rule_total_count(prims: List[PRIM]) -> List[str]:
    n = len(prims)
    return [] if n == 42 else [f"Expected 42 PRIMs, found {n}"]

def rule_pure_impure_pairing(prims: List[PRIM]) -> List[str]:
    impure_src = {p.source for p in prims if not p.pure}
    pure_src   = {p.source for p in prims if p.pure}
    return [
        f"'{s}' has Impure PRIM(s) but no Pure gate PRIM"
        for s in sorted(impure_src - pure_src)
    ]

def rule_wave_ordering(prims: List[PRIM]) -> List[str]:
    errors = []
    by_src: Dict[str, List[PRIM]] = {}
    for p in prims: by_src.setdefault(p.source, []).append(p)
    for src, ps in by_src.items():
        ids = [int(p.id) for p in ps]
        if ids != sorted(ids):
            errors.append(f"'{src}': PRIM IDs out of order → {ids}")
    return errors

def rule_wave_range(prims: List[PRIM]) -> List[str]:
    return [
        f"{p.prim_id}: wave={p.wave} outside valid range 2–5"
        for p in prims if p.wave not in (2,3,4,5)
    ]

MODULE_RULES: List[Tuple[str, Callable]] = [
    ("MOD-01", rule_id_uniqueness),
    ("MOD-02", rule_total_count),
    ("MOD-03", rule_pure_impure_pairing),
    ("MOD-04", rule_wave_ordering),
    ("MOD-05", rule_wave_range),
]

# ── Test runners ─────────────────────────────────────────────────

def run_per_prim(
    prims, wave_f=None, prim_f=None, inv_f=None
) -> List[TestResult]:
    results = []
    for p in prims:
        if wave_f and p.wave != wave_f: continue
        if prim_f and p.id  != prim_f:  continue
        for rid, fn in PER_PRIM_RULES:
            if inv_f and not rid.startswith(inv_f[:7]): continue
            err = fn(p)
            results.append(TestResult(p.prim_id, rid, err is None, err or ""))
        for idx, cell in enumerate(p.inv):
            lbl = f"INV-{idx+1:03d}-CELL"
            if inv_f and not lbl.startswith(inv_f[:7]): continue
            ok = cell in (C, E)
            results.append(TestResult(
                p.prim_id, lbl, ok,
                f"Declared {cell!r}" if ok else f"Unexpected token {cell!r}"
            ))
    return results

def run_module(prims) -> List[TestResult]:
    results = []
    for rid, fn in MODULE_RULES:
        errs = fn(prims)
        if errs:
            for e in errs: results.append(TestResult("MODULE", rid, False, e))
        else:
            results.append(TestResult("MODULE", rid, True, ""))
    return results

# ── Report helpers ────────────────────────────────────────────────

SEP = "═"*80
THIN= "─"*80

def print_matrix(prims):
    hdr = f"{'PRIM':<14}  {'Kind':<7}  W  {'Source':<24}"
    for i in range(10): hdr += f"  I{i+1:02d}"
    print(SEP); print("  INV COMPLIANCE MATRIX"); print(THIN); print(hdr); print(THIN)
    cur_wave = None
    for p in prims:
        if p.wave != cur_wave:
            if cur_wave: print()
            print(f"  ── Wave {p.wave} {'─'*65}")
            cur_wave = p.wave
        row = f"{p.prim_id:<14}  {p.kind:<7}  {p.wave}  {p.source:<24}"
        for cell in p.inv:
            icon = {C:" ✅", E:" — ", W:" ⚠ "}.get(cell, f" {cell}")
            row += f"  {icon}"
        print(row)
    print(SEP)

def print_inv_registry():
    print(SEP); print("  INVARIANT REGISTRY"); print(THIN)
    for k,v in INVARIANTS.items():
        wrapped = textwrap.fill(v, 66, subsequent_indent="                 ")
        print(f"  {k}  {wrapped}")
    print(SEP)

def print_wave_stats(prims):
    print(SEP); print("  PRIM COUNT BY WAVE"); print(THIN)
    print(f"  {'Wave':<6}  {'Total':<7}  {'Pure':<7}  {'Impure':<8}  Sources")
    print(THIN)
    for w in sorted({p.wave for p in prims}):
        wp  = [p for p in prims if p.wave == w]
        pu  = sum(1 for p in wp if p.pure)
        im  = sum(1 for p in wp if not p.pure)
        src = ", ".join(sorted({p.source for p in wp}))
        print(f"  W{w:<5}  {len(wp):<7}  {pu:<7}  {im:<8}  {src}")
    print(SEP)

def print_results(results, verbose=False):
    failed  = [r for r in results if not r.passed]
    passing = [r for r in results if r.passed]
    if failed:
        print(SEP); print("  FAILURES"); print(THIN)
        for r in failed:
            print(f"  ✗  {r.prim_id:<14}  {r.inv_id:<14}  {r.message}")
    if verbose and passing:
        print(SEP); print("  PASSED (structural assertions)"); print(THIN)
        for r in [x for x in passing if "CELL" not in x.inv_id]:
            print(f"  ✓  {r.prim_id:<14}  {r.inv_id}")
    return len(passing), len(failed)

def print_summary(passed, failed):
    total  = passed + failed
    status = "ALL PASS ✅" if failed == 0 else f"FAILURES ✗  ({failed} failed)"
    print(SEP); print("  SUMMARY"); print(THIN)
    print(f"  PRIMs registered : {len(PRIMS)}")
    print(f"  Invariants       : {len(INVARIANTS)}")
    print(f"  Assertions run   : {total}")
    print(f"  Passed           : {passed}")
    print(f"  Failed           : {failed}")
    print(f"  Warnings (⚠)    : {sum(1 for p in PRIMS for c in p.inv if c==W)}")
    print(f"  Status           : {status}")
    print(SEP)

# ── Entry point ───────────────────────────────────────────────────

def parse_args():
    ap = argparse.ArgumentParser(
        description="FFF_Gravity PRIM validation harness v1.0.0"
    )
    ap.add_argument("--wave",      type=int, default=None)
    ap.add_argument("--prim",      type=str, default=None)
    ap.add_argument("--inv",       type=str, default=None)
    ap.add_argument("--strict",    action="store_true")
    ap.add_argument("--matrix",    action="store_true")
    ap.add_argument("--verbose",   action="store_true")
    ap.add_argument("--no-module", action="store_true")
    return ap.parse_args()

def main() -> int:
    args = parse_args()
    print()
    print(SEP)
    print("  FFF_Gravity — PRIM Validation Harness  v1.0.0")
    print("  29 files · 42 PRIMs · 10 INVs · Waves 0–5")
    print(SEP)
    print_inv_registry()
    print_wave_stats(PRIMS)

    filtered = [p for p in PRIMS
                if (args.wave is None or p.wave == args.wave)
                and (args.prim is None or p.id == args.prim)]

    if args.matrix: print_matrix(filtered)

    per   = run_per_prim(PRIMS, args.wave, args.prim, args.inv)
    mod   = run_module(PRIMS) if (not args.no_module
                                  and args.wave is None
                                  and args.prim is None) else []

    passed, failed = print_results(per + mod, verbose=args.verbose)
    print_summary(passed, failed)

    return 1 if (args.strict and failed > 0) else 0

if __name__ == "__main__":
    sys.exit(main())

