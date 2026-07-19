# Message Patterns  
_Minimal structural summaries for assay interpretation._

## 1. STATE_SUMMARY

Describes drift against an expected structural pattern.

```
msg_type: STATE_SUMMARY
invariant_id: <string>
time_window: { start: <t0>, end: <t1> }
max_drift: <float>
status: within_bounds | approaching_limit | out_of_bounds
```

## 2. PARADOX_SUMMARY

Describes contradictory or incompatible signals.

```
msg_type: PARADOX_SUMMARY
paradox_id: <string>
invariant_id: <string>
hypotheses:
  - { source: <string>, value: <any> }
  - { source: <string>, value: <any> }
evidence: [<string>, ...]
timestamp: <t>
```

These two patterns are sufficient to reconstruct structural behavior.
