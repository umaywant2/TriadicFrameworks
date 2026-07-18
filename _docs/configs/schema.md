# Triadic Dimensional Schema

## Node
- **id**: Unique string `N:Type:Name`
- **kind**: goal | metric | artifact | person | ritual
- **tags**: free-form labels

## Edge
- **id**: `E:<NodeID>-><NodeID>`
- **kind**: influences | depends_on | validates | echoes
- **weight**: float 0–1

## Triad
- **id**: `T:<NodeA>|<NodeB>|<NodeC>`
- **roles**: mapping of A/B/C → role name
- **harmonics**: similarity | authority | relevance | validator
- **decay**: half-life days, days since last touch
- **H**: computed harmonic score
- **provenance**: {source, path, lines}
- **tags**: used for resonance parity

## Context Snapshot
- Anchor goal + asks
- Constants at capture time
- Active Constellation triads
