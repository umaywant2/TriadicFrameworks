## Demo: Export Quadratic Lattice for CPU

### Example
```bash
resonance tft --export cpu
```
Output:
```
{
  "cpu": {
    "triadic": [
      "E = Instruction flow",
      "M = Clock cycles",
      "OC = Interrupt/branch"
    ],
    "quadratic": [
      ["E×E", "E×M", "E×OC"],
      ["M×E", "M×M", "M×OC"],
      ["OC×E", "OC×M", "OC×OC"]
    ]
  }
}
```
