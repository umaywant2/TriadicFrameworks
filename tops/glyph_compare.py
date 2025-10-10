import matplotlib.pyplot as plt

def compare_glyphs(results, title="Triconceptual Glyph Comparison"):
    """
    Visualize and compare glyphs across direct, reflected, and inverted views.
    results: dictionary from tops_session.run_tops_session()
    """
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    modes = ["direct", "reflected", "inverted"]
    colors = ["#0077cc", "#cc3300", "#6600cc"]

    for i, mode in enumerate(modes):
        axs[i].set_title(f"{mode.capitalize()} Views")
        for key, (x, y) in results[mode].items():
            axs[i].plot(x, y, label=str(key), color=colors[i], alpha=0.6)
        axs[i].axis('equal')
        axs[i].legend()
        axs[i].grid(True)

    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    from tops_session import run_tops_session
    results = run_tops_session()
    compare_glyphs(results)
