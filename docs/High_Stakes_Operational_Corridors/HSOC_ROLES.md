# ROLES — High_Stakes_Operational_Corridors

> Role Enum Definitions · Module `hsoc-rtt-001`

Each role maps to a distinct enforcement or observability responsibility within the corridor. Roles marked `required: true` must be bound before the engine accepts any action submissions.

---

## Role Enum

```python
from enum import Enum

class HSOCRole(str, Enum):
    ENGINE     = "engine"
    PROFILE    = "profile"
    SIGNATURE  = "signature"
    DIAGNOSTIC = "diagnostic"
    MAP        = "map"
    EXAMPLE    = "example"
    EXTENSION  = "extension"
    INDEX      = "index"
    REFERENCE  = "reference"
    TEMPLATE   = "template"
```

---

## `engine`

**Required** · Bindings: `corridor_enforcer`, `action_gate`, `constraint_surface`

Core execution substrate. Enforces corridor constraints at every action emission point — acts as the final gate before any consequential action reaches an external system. All seven operators are dispatched through the engine.

```python
from hsoc.roles import EngineRole

engine_role = EngineRole(
    corridor_enforcer=CorridorEnforcer(max_gate_latency_ms=50),
    action_gate=ActionGate(constraint_surface=ConvexPolytope.from_module(module)),
    constraint_surface=SignedHalfspaceIntersection.from_module(module),
)
```

```json
{
  "role": "engine",
  "bindings": {
    "corridor_enforcer": {"max_gate_latency_ms": 50, "zero_tolerance_on_timeout": true},
    "action_gate": {"constraint_surface_format": "convex_polytope"},
    "constraint_surface": {"definition_format": "signed_halfspace_intersection", "axes": 4}
  }
}
```

---

## `profile`

**Required** · Bindings: `authority_vector`, `clearance_matrix`, `scope_boundary`

Operational authority profile. Encodes the agent's permitted scope, authorization level, and domain clearance. The engine consults the profile at every GATE and AUTHORIZE call to determine which corridor segments are accessible.

```python
from hsoc.roles import ProfileRole

profile = ProfileRole(
    authority_vector=AuthorityVector(
        authority_id="algo-trader-agent-007",
        clearance_level=2,
        domains=["equity", "fixed_income"],
    ),
    clearance_matrix=ClearanceMatrix.from_dict({
        "equity_trade_submit": 2,
        "fund_transfer":       3,
        "position_close":      1,
    }),
    scope_boundary=ScopeBoundary(
        max_trade_notional_usd=50_000_000,
        permitted_venues=["NYSE", "NASDAQ"],
    ),
)
```

```json
{
  "role": "profile",
  "bindings": {
    "authority_vector": {
      "authority_id": "algo-trader-agent-007",
      "clearance_level": 2,
      "domains": ["equity", "fixed_income"]
    },
    "clearance_matrix": {
      "equity_trade_submit": 2,
      "fund_transfer": 3,
      "position_close": 1
    },
    "scope_boundary": {
      "max_trade_notional_usd": 50000000,
      "permitted_venues": ["NYSE", "NASDAQ"]
    }
  }
}
```

---

## `signature`

**Required** · Bindings: `action_payload_signer`, `authorization_chain`, `audit_stamp`

Action signature layer. Every consequential action emitted by the agent carries a signed payload referencing the authorizing corridor, complete authorization chain, and timestamp. Unsigned actions trigger a zero-tolerance HALT.

```python
from hsoc.roles import SignatureRole

sig_role = SignatureRole(
    action_payload_signer=ActionPayloadSigner(
        algorithm="Ed25519",
        signing_key=load_key("hsoc-agent-signing-key"),
    ),
    authorization_chain=AuthorizationChain(required_depth=2),
    audit_stamp=AuditStamp(format="json-ld+sha256"),
)

signed_action = sig_role.sign(action=my_action, chain=my_chain)
print(signed_action.signature)  # "ed25519:abc123..."
```

```json
{
  "role": "signature",
  "bindings": {
    "action_payload_signer": {
      "algorithm": "Ed25519",
      "signing_key_id": "hsoc-agent-signing-key-v1"
    },
    "authorization_chain": {"required_depth": 2},
    "audit_stamp": {"format": "json-ld+sha256", "timestamp_precision": "ms"}
  }
}
```

---

## `diagnostic`

**Required** · Bindings: `constraint_monitor`, `escalation_tracker`, `corridor_health_probe`

Real-time corridor health diagnostics. Monitors constraint surface violations, escalation trigger rates, authorization bottlenecks, and dead-man switch heartbeats. Emits structured events to the cross-cutting layer.

```python
from hsoc.roles import DiagnosticRole

diag = DiagnosticRole(
    constraint_monitor=ConstraintMonitor(
        sample_every_n_actions=1,   # every action
        alert_on_proximity_ratio=0.80,
    ),
    escalation_tracker=EscalationTracker(
        warning_rate_threshold=0.10,
        critical_rate_threshold=0.25,
    ),
    corridor_health_probe=CorridorHealthProbe(
        dead_man_heartbeat_interval_s=30,
        grace_period_s=10,
    ),
)
```

```json
{
  "role": "diagnostic",
  "bindings": {
    "constraint_monitor": {
      "sample_every_n_actions": 1,
      "alert_on_proximity_ratio": 0.80
    },
    "escalation_tracker": {
      "warning_rate_threshold": 0.10,
      "critical_rate_threshold": 0.25,
      "current_rate": 0.04
    },
    "corridor_health_probe": {
      "dead_man_heartbeat_interval_s": 30,
      "grace_period_s": 10,
      "last_heartbeat": "2026-09-23T20:49:45-04:00",
      "status": "healthy"
    }
  }
}
```

---

## `map`

**Required** · Bindings: `corridor_graph`, `constraint_surface_map`, `escalation_topology`

Topological map of the permitted operational corridors. Nodes are authorized action clusters; edges are transition conditions; boundaries are hard constraint surfaces. The engine traverses the map to determine which actions belong to the current corridor.

```python
from hsoc.roles import MapRole

corridor_map = MapRole(
    corridor_graph=CorridorGraph.from_adjacency({
        "NOMINAL":    ["ELEVATED", "LOCKDOWN"],
        "ELEVATED":   ["NOMINAL", "CRITICAL", "LOCKDOWN"],
        "CRITICAL":   ["ELEVATED", "LOCKDOWN", "AUDIT_ONLY"],
        "LOCKDOWN":   [],                    # terminal — requires RELEASE
        "AUDIT_ONLY": ["NOMINAL"],           # requires external auth
    }),
    constraint_surface_map=ConstraintSurfaceMap.from_module(module),
    escalation_topology=EscalationTopology.from_ladder(module["escalation_ladder"]),
)
```

```json
{
  "role": "map",
  "bindings": {
    "corridor_graph": {
      "nodes": ["NOMINAL", "ELEVATED", "CRITICAL", "LOCKDOWN", "AUDIT_ONLY"],
      "edges": [
        {"from": "NOMINAL",   "to": "ELEVATED",   "trigger": "severity_elevation"},
        {"from": "ELEVATED",  "to": "CRITICAL",   "trigger": "severity_elevation"},
        {"from": "CRITICAL",  "to": "LOCKDOWN",   "trigger": "zero_tolerance_violation"},
        {"from": "LOCKDOWN",  "to": "NOMINAL",    "trigger": "RELEASE", "requires_external_auth": true}
      ]
    },
    "constraint_surface_map": "signed_halfspace_intersection × 4 axes",
    "escalation_topology": {
      "levels": [1, 2, 3, 99],
      "current_active_escalations": 0
    }
  }
}
```

---

## `example`

**Optional** · Bindings: `scenario_library`, `incident_archive`, `outcome_registry`

Canonical worked examples. See [`EXAMPLES.md`](./EXAMPLES.md) for full trace payloads.

```json
{
  "role": "example",
  "bindings": {
    "scenario_library": ["EX-HSOC-001", "EX-HSOC-002", "EX-HSOC-003"],
    "incident_archive": "./examples/incidents/",
    "outcome_registry": "./examples/outcomes.json"
  }
}
```

---

## `extension`

**Optional** · Bindings: `constraint_engine_registry`, `auth_provider_manifest`, `escalation_handler_registry`

Extension points for domain-specific constraint engines, external authorization providers, and custom escalation handlers.

```python
from hsoc.roles import ExtensionRole
from hsoc.extensions import (
    PagerDutyEscalationHandler,
    HSMAuthorizationProvider,
    RegulatoryConstraintEngine,
)

ext = ExtensionRole()
ext.register("IEscalationHandler", PagerDutyEscalationHandler(api_key=PAGERDUTY_KEY))
ext.register("IAuthorizationProvider", HSMAuthorizationProvider(hsm_endpoint=HSM_URL))
ext.register("IConstraintEngine", RegulatoryConstraintEngine(ruleset="MiFID-II"))
```

```json
{
  "role": "extension",
  "bindings": {
    "constraint_engine_registry": {
      "IConstraintEngine": "RegulatoryConstraintEngine",
      "ruleset": "MiFID-II"
    },
    "auth_provider_manifest": {
      "IAuthorizationProvider": "HSMAuthorizationProvider",
      "hsm_endpoint": "https://hsm.internal/v1"
    },
    "escalation_handler_registry": {
      "IEscalationHandler": "PagerDutyEscalationHandler"
    }
  }
}
```

---

## `index`

**Required** · Bindings: `artifact_index`, `authorization_log`, `incident_ledger`

Searchable index over all corridor artifacts. Supports queries by action ID, gate decision ID, escalation ID, regime, and time range.

```json
{
  "role": "index",
  "bindings": {
    "artifact_index": {"total_artifacts": 187, "last_indexed_action_id": "act-2026-09-23-187"},
    "authorization_log": [
      {"action_id": "act-001", "regime": "NOMINAL",   "chain_depth": 1, "outcome": "passed"},
      {"action_id": "act-042", "regime": "ELEVATED",  "chain_depth": 2, "outcome": "passed"},
      {"action_id": "act-103", "regime": "CRITICAL",  "chain_depth": 3, "outcome": "escalated"},
      {"action_id": "act-187", "regime": "ELEVATED",  "chain_depth": 2, "outcome": "passed"}
    ],
    "incident_ledger": {
      "zero_tolerance_violations": 0,
      "halt_events": 1,
      "escalations_total": 3,
      "escalations_resolved": 3
    }
  }
}
```

---

## `reference`

**Optional** · Bindings: `rtt_spec_link`, `constraint_algebra_doc`, `authorization_grammar_doc`

Normative reference material pointers used by tooling and documentation generators.

```json
{
  "role": "reference",
  "bindings": {
    "rtt_spec_link": "REF-RTT-SPEC",
    "constraint_algebra_doc": "REF-CONSTRAINT-ALGEBRA",
    "authorization_grammar_doc": "REF-AUTHORIZATION-GRAMMAR"
  }
}
```

---

## `template`

**Optional** · Bindings: `corridor_template`, `constraint_surface_template`, `escalation_ladder_template`

Reusable scaffold templates for new corridor configurations.

```json
{
  "role": "template",
  "bindings": {
    "corridor_template": {
      "regime": null,
      "max_action_severity": null,
      "min_reversibility_index": null,
      "authorization_required": null,
      "escalation_threshold": null
    },
    "constraint_surface_template": {
      "axes": ["action_severity", "authorization_depth", "consequence_radius", "reversibility_index"],
      "bounds": {
        "action_severity":     {"min": 0.0, "max": null},
        "authorization_depth": {"min": 1,   "max": null},
        "consequence_radius":  {"min": 0.0, "max": 1.0},
        "reversibility_index": {"min": null, "max": 1.0}
      }
    },
    "escalation_ladder_template": {
      "levels": [
        {"level": 1, "target": null, "sla_seconds": null, "sla_breach_action": null}
      ]
    }
  }
}
```
