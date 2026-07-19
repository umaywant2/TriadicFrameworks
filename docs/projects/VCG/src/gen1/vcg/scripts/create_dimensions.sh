# create_dimensions.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

BASE=/var/lib/vcg
SIZE_GB=${SIZE_GB:-4}

mkdir -p "$BASE"

for i in {1..9}; do
  IMG="$BASE/d${i}.img"
  if [[ ! -f "$IMG" ]]; then
    echo "Creating image for Dimension $i..."
    fallocate -l ${SIZE_GB}G "$IMG"
    LOOP=$(losetup -f --show --direct-io=on "$IMG")
    mkfs.ext4 -F -E lazy_itable_init=0,lazy_journal_init=0 -O ^has_journal "$LOOP"
    losetup -d "$LOOP"
  else
    echo "Image for Dimension $i already exists, skipping."
  fi
done
