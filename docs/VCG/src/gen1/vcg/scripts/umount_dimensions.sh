
---

### `/src/gen1/vcg/scripts/umount_dimensions.sh`

```markdown
# umount_dimensions.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

MOUNT=/vcg

for i in {1..9}; do
  umount "$MOUNT/d${i}" || true
done

losetup -D
