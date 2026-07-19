## 🔗 Graph Logic

- **Nodes**: Contributors (circle elements)
- **Edges**: Remix trace paths (lines with arrowheads)
- **Badges**: Color-coded overlays (node fill or border)
- **Pulse Events**: Animated ripple effect on validator trigger

### 🧠 D3.js Attributes

- `node.id`: Contributor name
- `node.badge`: Badge type
- `edge.source → edge.target`: Remix lineage
- `event.timestamp`: Pulse trigger

### 🖼️ Visual Options

- Hover: Show badge + remix depth
- Click: Expand remix trace
- Filter: By badge, timestamp, validator event
