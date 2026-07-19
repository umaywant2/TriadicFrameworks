# 🛡️ Badge Trigger Validator
# Unifies manifest validation, remix lineage tracking, and honor roll updates

import json
from validate_manifest import validate_manifest
from remix_lineage_tracker import track_lineage
from update_honor_roll import update_honor_roll

def confirm_badge_trigger(manifest_path, remix_chain, contributor_id, honor_roll_path):
    print("🔍 Validating manifest...")
    manifest_result = validate_manifest(manifest_path)

    print("🧬 Tracking remix lineage...")
    lineage_result = track_lineage(remix_chain)

    badge_name = None
    if manifest_result["badge_eligible"] and lineage_result["depth"] >= 2:
        badge_name = "Curriculum Weaver"
    elif manifest_result["badge_eligible"]:
        badge_name = "Echo Weaver"
    elif lineage_result["depth"] >= 3:
        badge_name = "Glyphic Echoer"

    if badge_name:
        print(f"🏅 Badge confirmed: {badge_name}")
        update_honor_roll(contributor_id, badge_name, honor_roll_path)
    else:
        print("⚠️ No badge triggered.")

    return {
        "contributor_id": contributor_id,
        "badge": badge_name,
        "manifest_score": manifest_result["score"],
        "lineage_depth": lineage_result["depth"]
    }
