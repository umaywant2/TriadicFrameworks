import matplotlib.pyplot as plt

def visualize_legacy_echo(contributors, folds, strengths):
    """
    Visualizes contributor echoes across folds.
    """
    fig, ax = plt.subplots()
    ax.bar(folds, strengths, color="#6c00ff")
    for i, name in enumerate(contributors):
        ax.text(folds[i], strengths[i] + 0.02, name, ha='center', fontsize=8)
    ax.set_ylabel("Echo Strength")
    ax.set_title("Legacy Echo Visualization")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
