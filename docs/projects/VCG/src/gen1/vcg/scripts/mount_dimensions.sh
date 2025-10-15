
---

### `/src/gen1/vcg/scripts/mount_dimensions.sh`

```markdown
# mount_dimensions.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

BASE=/var/lib/vcg
MOUNT=/vcg

mkdir -p "$MOUNT"

for i in {1..9}; do
  IMG="$BASE/d${i}.img"
  LOOP=$(losetup -f --show --direct-io=on "$IMG")
  mkdir -p "$MOUNT/d${i}"
  mount -o noatime,nodiratime,data=writeback,barrier=0,discard "$LOOP" "$MOUNT/d${i}"
done
