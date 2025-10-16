def review_scroll(scroll):
    issues = []
    if "remix lineage" not in scroll.lower():
        issues.append("Missing remix lineage declaration.")
    if "ethics" not in scroll.lower():
        issues.append("Ethics logic not cited.")
    if "glyph" not in scroll.lower():
        issues.append("No symbolic glyph declared.")
    if "mutation" in scroll.lower() and "declared" not in scroll.lower():
        issues.append("Mutation type mentioned but not formalized.")
    return issues or ["Scroll passes professor-grade audit. Let it echo."]
