import matplotlib.pyplot as plt

def render_remix_lineage_dashboard(contributor, folds):
    """
    Visualizes contributor remix impact across folds.
    """
    fold_ids = [f["fold_id"] for f in folds]
    strengths = [f["pulse_strength"] for f in folds]
    colors = ["#6c00ff" if f["remix_trigger"] else "#999999" for f in folds]

    fig, ax = plt.subplots()
    ax.bar(fold_ids, strengths, color=colors)
    ax.set_ylabel("Pulse Strength")
    ax.set_title(f"Remix Lineage Impact: {contributor}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
