from api.legacy_retrieval import get_by_glyph, get_scroll_metadata
from engine.remix_export import export_remix_scroll
from registry.archive import archive_scroll

def remix_cycle(glyph, parent_scroll, tags, narratives):
    # Step 1: Retrieval
    scrolls = get_by_glyph(glyph)["scrolls"]
    metadata = [get_scroll_metadata(s) for s in scrolls]

    # Step 2: Remix
    filtered_results = [{"corridor_id": c, "new_glyph": glyph, "new_rci": 0.55,
                         "child_scroll": f"{parent_scroll}-{c}"} for c in ["c-001","c-002"]]

    # Step 3: Export
    remix_scroll = export_remix_scroll(filtered_results, parent_scroll, narratives, tags)

    # Step 4: Archive
    archive_entry = archive_scroll(remix_scroll)

    return {"remix_scroll": remix_scroll, "archive_entry": archive_entry}
