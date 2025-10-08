## Demo: Export TFE Domain Mapping

### Example: Export computing domain
```bash
resonance tfe --export computing

Output:
{
  "computing": [
    "E = Data flow (arrows of execution)",
    "M = Clock cycles (symmetric timing)",
    "OC = Interrupts/novel input (originating change)"
  ]
}
```
### Example: Export biology domain
```bash
resonance tfe --export biology

Output:
{
  "biology": [
    "E = Evolutionary lineage (arrow of descent)",
    "M = Circadian rhythms (biological clocks)",
    "OC = Mutation/novel trait (originating change)"
  ]
}
