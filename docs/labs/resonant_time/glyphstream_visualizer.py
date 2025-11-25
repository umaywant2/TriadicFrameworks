import matplotlib.pyplot as plt

def visualize_glyphstream(frequencies, echo_strengths, glyphs):
    """
    Visualizes glyphstream echoes across frequencies.
    """
    fig, ax = plt.subplots()
    ax.bar(frequencies, echo_strengths, color="#6c00ff")
    for i, glyph in enumerate(glyphs):
        ax.text(frequencies[i], echo_strengths[i] + 0.02, glyph, ha='center', fontsize=8)
    ax.set_ylabel("Echo Strength")
    ax.set_title("Glyphstream Echo Visualization")
    plt.show()
