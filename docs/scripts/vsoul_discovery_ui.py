"""
vSoul Discovery Interactive UI
------------------------------
A simple CLI interface for exploring vSoul listings.
Part of RFC-014: vSoul Market Protocol
"""

import json

def load_listings(path="docs/registries/vsoul_listings.json"):
    with open(path, "r") as f:
        return json.load(f)

def filter_listings(listings, min_clarity=0.0, rights=None, amenities=None):
    rights = rights or []
    amenities = amenities or []
    results = []
    for l in listings:
        if l["resonance_profile"]["clarity_score"] < min_clarity:
            continue
        if not all(r in l["rights_guarantees"] for r in rights):
            continue
        if not all(a in l["amenities"] for a in amenities):
            continue
        results.append(l)
    return results

def display_results(listings):
    if not listings:
        print("No matching listings found.")
        return
    print("\nMatching vSoul Listings:\n")
    for l in listings:
        print(f"- {l['listing_id']} ({l['partition']})")
        print(f"  Clarity: {l['resonance_profile']['clarity_score']}")
        print(f"  Rights: {', '.join(l['rights_guarantees'])}")
        print(f"  Amenities: {', '.join(l['amenities'])}")
        print(f"  Audits: {', '.join(l['audit_refs'])}")
        print()

if __name__ == "__main__":
    listings = load_listings()

    print("=== vSoul Discovery ===")
    min_clarity = float(input("Minimum clarity score (0.0–1.0): ") or 0.0)
    rights = input("Required rights (comma-separated, leave blank for none): ").split(",")
    rights = [r.strip() for r in rights if r.strip()]
    amenities = input("Required amenities (comma-separated, leave blank for none): ").split(",")
    amenities = [a.strip() for a in amenities if a.strip()]

    results = filter_listings(listings, min_clarity, rights, amenities)
    display_results(results)
