# ✅ Result Validation Logic: TFT-FFF Grid

---

## 🧪 Acceptance vs Validation

- **Accepted Result**: Meets minimum fidelity threshold (e.g. ≥ 0.95)
- **Validated Result**: Reproduced ≥ 3 times across distinct agents with identical output

---

## 🧬 Staging Area Logic

- Results first enter `/outputs/staging/`
- Validator checks:
  - Fidelity score
  - Remix lineage trace
  - Glyphstream pulse sync
- If validated, result moves to `/outputs/validated/`

---

## 🔁 Duplicate Success Threshold

- Minimum: 3 matching results
- Agents must differ in:
  - Host environment
  - Job segment
  - Timestamp (≥ 1 min apart)

---

## 🛡️ Fault Handling

- If mismatch detected:
  - Log to `validator_faults.log`
  - Trigger badge downgrade or retry
- If glyphstream desync:
  - Pulse flagged in `glyphstream_fault.log`
