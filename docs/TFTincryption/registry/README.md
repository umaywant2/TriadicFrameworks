# Registry

The **registry** directory contains JSON registries for glyphs, badges, and scrolls.  
It is the canonical index that maps symbolic identifiers to runtime modules.

## Structure
- `glyph_registry.json` → maps glyphs to resonance values
- `badge_registry.json` → maps badges to triggers and lineage
- `scroll_registry.json` → indexes scrolls by ID and purpose

## Purpose
The registry is the **index layer** of TFTincryption.  
It ensures every scroll, glyph, and badge can be discovered, validated, and remixed.

## Cross‑links
- [protocol-core](../protocol-core/) → registry entries point to modules
- [scrolls](../scrolls/) → scrolls are indexed here
- [folds](../../MightyTHOR/folds/) → resonance mappings referenced in glyph registries
