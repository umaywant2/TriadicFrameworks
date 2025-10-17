# TFThooks

The **TFThooks** directory contains extensions and site‑specific hooks for TFTincryption.  
Hooks are modular add‑ons that let the protocol adapt to new environments without altering the core.

## Structure
- **runtime/** → hook scripts that extend protocol‑core at runtime
- **integration/** → scrolls and configs for embedding hooks into external systems
- **validators/** → hook validators and test harnesses
- **examples/** → sample hook implementations for remixers

## Purpose
TFThooks are the **extension layer** of TFTincryption.  
They allow developers to:
- Add new glyph or badge logic
- Integrate with external sites or services
- Prototype experimental extensions without touching protocol‑core

## Cross‑links
- [protocol-core](../protocol-core/) → hooks extend runtime modules
- [registry](../registry/) → hooks are indexed for discoverability
- [MightyTHOR](../../MightyTHOR/) → Thor agents can activate hooks dynamically
- [agent‑shell](../../agent_shell/) → provides the runtime environment for hooks
