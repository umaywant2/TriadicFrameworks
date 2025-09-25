# Demo: Nested Loops

### Example: 2-level nesting
```bash
resonance loops --nest 2
```
Output:
```
{'loop': {'loop': '∅'}}
```
### Example 3-level nesting (JSON export)
```bash
resonance loops --export 3
```
Output:
```
{
  "loop": {
    "loop": {
      "loop": "∅"
    }
  }
}
```
