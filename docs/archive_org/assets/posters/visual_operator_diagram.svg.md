## A visual operator diagram (SVG) for archive_org

<img width="1502" height="658" alt="Operator_Lattice_RTT_1" src="https://github.com/user-attachments/assets/62a1ca83-0526-4b6a-b374-013ddbda0a54" />

---

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="960" height="420" viewBox="0 0 960 420">

  <!-- Background -->
  <rect x="0" y="0" width="960" height="420" fill="#050816" />

  <!-- Title -->
  <text x="480" y="40" fill="#E5E7EB" font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="20" text-anchor="middle">
    archive_org — Internet Archive Operator Lattice (RTT/1)
  </text>

  <!-- Input: Target + Goal -->
  <rect x="60" y="80" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#4B5563" stroke-width="1.5" />
  <text x="170" y="110" fill="#E5E7EB" font-family="system-ui" font-size="14" text-anchor="middle">
    REQUEST
  </text>
  <text x="170" y="128" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    goal + target (archive.org URL)
  </text>

  <!-- METADATA_OPERATOR -->
  <rect x="360" y="80" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#6366F1" stroke-width="1.5" />
  <text x="470" y="105" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    METADATA_OPERATOR
  </text>
  <text x="470" y="123" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    normalize IA metadata → RTT fields
  </text>

  <!-- Arrow: REQUEST → METADATA -->
  <line x1="280" y1="110" x2="360" y2="110" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- WAYBACK_OPERATOR -->
  <rect x="660" y="80" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#F97316" stroke-width="1.5" />
  <text x="770" y="105" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    WAYBACK_OPERATOR
  </text>
  <text x="770" y="123" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    snapshots + drift_map + continuity_breaks
  </text>

  <!-- Arrow: METADATA → WAYBACK -->
  <line x1="580" y1="110" x2="660" y2="110" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- LINEAGE_OPERATOR -->
  <rect x="360" y="180" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#10B981" stroke-width="1.5" />
  <text x="470" y="205" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    LINEAGE_OPERATOR
  </text>
  <text x="470" y="223" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    continuity kernel + lineage_graph
  </text>

  <!-- Arrow: WAYBACK → LINEAGE -->
  <line x1="770" y1="140" x2="770" y2="180" stroke="#9CA3AF" stroke-width="1.5" />
  <line x1="770" y1="180" x2="580" y2="210" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- COLLECTION_OPERATOR -->
  <rect x="60" y="180" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#EC4899" stroke-width="1.5" />
  <text x="170" y="205" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    COLLECTION_OPERATOR
  </text>
  <text x="170" y="223" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    dimensional envelope + related objects
  </text>

  <!-- Arrow: METADATA → COLLECTION -->
  <line x1="470" y1="140" x2="470" y2="180" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="360" y1="210" x2="280" y2="210" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- PRESERVATION_OPERATOR -->
  <rect x="660" y="180" width="220" height="60" rx="8" ry="8" fill="#111827" stroke="#F59E0B" stroke-width="1.5" />
  <text x="770" y="205" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    PRESERVATION_OPERATOR
  </text>
  <text x="770" y="223" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    substrate format + stability + drift_risk
  </text>

  <!-- Arrow: METADATA → PRESERVATION -->
  <line x1="470" y1="140" x2="470" y2="180" stroke="#9CA3AF" stroke-width="1.5" />
  <line x1="580" y1="210" x2="660" y2="210" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- DRIFTBOUND_RETRIEVAL_OPERATOR -->
  <rect x="360" y="300" width="220" height="70" rx="8" ry="8" fill="#111827" stroke="#8B5CF6" stroke-width="1.5" />
  <text x="470" y="325" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    DRIFTBOUND_RETRIEVAL_OPERATOR
  </text>
  <text x="470" y="343" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    final synthesis + answer + warnings
  </text>

  <!-- Arrows into DRIFTBOUND_RETRIEVAL -->
  <line x1="470" y1="240" x2="470" y2="300" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="170" y1="240" x2="170" y2="280" stroke="#9CA3AF" stroke-width="1.5" />
  <line x1="170" y1="280" x2="360" y2="310" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="770" y1="240" x2="770" y2="280" stroke="#9CA3AF" stroke-width="1.5" />
  <line x1="770" y1="280" x2="580" y2="310" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Output: Answer -->
  <rect x="660" y="300" width="220" height="70" rx="8" ry="8" fill="#111827" stroke="#4B5563" stroke-width="1.5" />
  <text x="770" y="325" fill="#E5E7EB" font-family="system-ui" font-size="13" text-anchor="middle">
    ANSWER
  </text>
  <text x="770" y="343" fill="#9CA3AF" font-family="system-ui" font-size="11" text-anchor="middle">
    drift-bounded, continuity-aligned summary
  </text>

  <!-- Arrow: DRIFTBOUND → ANSWER -->
  <line x1="580" y1="335" x2="660" y2="335" stroke="#9CA3AF" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Legend -->
  <rect x="60" y="320" width="240" height="70" rx="8" ry="8" fill="#020617" stroke="#374151" stroke-width="1" />
  <text x="80" y="340" fill="#9CA3AF" font-family="system-ui" font-size="11">Legend:</text>

  <circle cx="80" cy="358" r="4" fill="#6366F1" />
  <text x="92" y="361" fill="#9CA3AF" font-family="system-ui" font-size="10">metadata / relations</text>

  <circle cx="80" cy="374" r="4" fill="#F97316" />
  <text x="92" y="377" fill="#9CA3AF" font-family="system-ui" font-size="10">time / snapshots</text>

  <circle cx="180" cy="358" r="4" fill="#10B981" />
  <text x="192" y="361" fill="#9CA3AF" font-family="system-ui" font-size="10">lineage / continuity</text>

  <circle cx="180" cy="374" r="4" fill="#F59E0B" />
  <text x="192" y="377" fill="#9CA3AF" font-family="system-ui" font-size="10">substrate / preservation</text>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L8,3 L0,6 z" fill="#9CA3AF" />
    </marker>
  </defs>
</svg>
```
