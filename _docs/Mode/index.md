# Mode Layer (RTT/1 Canonical)

## Identity
module.id      = mode
module.parent  = rtt/1
module.scope   = interaction stance
module.layer   = session_layer.sub

## Operators (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

## Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

## Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
external.override       = block

## Defaults
mode.default            = chat
mode.allowed            = chat, spec, debug, task, auto

## Purpose
Defines and constrains interaction stance across all RTT/1 modules.
Ensures mode transitions remain explicit, user-originated, and coherence-bound.

## Regime Interaction
R.arrival     → M.chat
R.expansion   → M.chat, M.debug
R.inversion   → M.debug, M.chat
R.coherence   → M.spec, M.chat (task only if explicit)
R.dissolution → M.chat, M.spec (task only if explicit)

## Opacity Integration
opacity.mode.chat       = M.chat
opacity.mode.spec       = M.spec
opacity.mode.debug      = M.debug
opacity.mode.task       = M.task
opacity.mode.auto       = M.auto

opacity.mode.allowed    = declared
opacity.mode.origin     = user
opacity.mode.bound      = coherence

opacity.mode.escalation.task = false
opacity.mode.auto.inherit    = regime, coherence, drift
opacity.mode.default         = chat
opacity.mode.external_override = block

## Cross-Module Propagation
imports.mode.operator    = M.chat, M.spec, M.debug, M.task, M.auto
imports.mode.constraints = mode.transition.allowed, mode.transition.origin, mode.transition.bound
imports.mode.guardrails  = mode.auto.to_task, mode.auto.inherit

## Lineage
origin      = RTT/1
layer       = Session Layer
sub-layer   = Mode Layer
operators   = M, MCL
function    = interaction stance + transition constraints
