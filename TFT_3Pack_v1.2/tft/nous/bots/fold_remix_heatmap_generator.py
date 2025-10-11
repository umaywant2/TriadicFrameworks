import seaborn as sns
import matplotlib.pyplot as plt

def generate_remix_heatmap(fold_data):
    """
    Generates a heatmap of remix intensity across folds.
    """
    folds = [entry["fold"] for entry in fold_data]
    strengths = [entry["echo_strength"] for entry in fold_data]

    sns.heatmap([strengths], annot=True, xticklabels=folds, cmap="magma", cbar=True)
    plt.title("Fold Remix Intensity Heatmap")
    plt.xlabel("Folds")
    plt.ylabel("Echo Strength")
    plt.tight_layout()
    plt.show()
