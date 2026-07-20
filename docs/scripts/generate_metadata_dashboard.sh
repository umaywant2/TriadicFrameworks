#!/bin/bash
ROOT="./docs"
DASHBOARD="./docs/metadata/DASHBOARD.md"

echo "Generating metadata dashboard at $DASHBOARD"

cat > "$DASHBOARD" <<EOF
# 📊 TriadicFrameworks AI‑Metadata Dashboard

This dashboard summarizes AI‑metadata coverage across modules.

---

## 📁 Module Status

| Module | Summary | Category | Metadata | Sitemap |
|--------|---------|----------|----------|---------|
EOF

SITEMAP="./docs/sitemap_main.xml"

for dir in $(find $ROOT -maxdepth 3 -type d | sort); do
  MODULE=$(basename "$dir")
  [ "$MODULE" = "docs" ] && continue
  INDEX="$dir/index.html"
  README="$dir/README.md"

  if [ -f "$INDEX" ]; then
    TARGET="$INDEX"
  elif [ -f "$README" ]; then
    TARGET="$README"
  else
    continue
  fi

  SUMMARY=$(grep -oP 'meta name="ai.module.summary" content="\K[^"]+' "$TARGET" 2>/dev/null || echo "—")
  CATEGORY=$(grep -oP 'meta name="ai.module.category" content="\K[^"]+' "$TARGET" 2>/dev/null || echo "—")

  if grep -q "AI Metadata: TriadicFrameworks Module" "$TARGET"; then
    META="✔️"
  else
    META="❌"
  fi

  if [ -f "$SITEMAP" ] && grep -q "$MODULE" "$SITEMAP"; then
    SITE="✔️"
  else
    SITE="⚠️"
  fi

  echo "| $MODULE | $SUMMARY | $CATEGORY | $META | $SITE |" >> "$DASHBOARD"
done

echo >> "$DASHBOARD"
echo "Dashboard generation complete."
