import matplotlib.pyplot as plt

def visualize_lattice_structure(loop_depths, harmonic_sets, bot_labels):
    """
    Visualizes triadic lattice structure across bots.
    """
    fig, ax = plt.subplots()
    for i, bot in enumerate(bot_labels):
        ax.plot(harmonic_sets[i], label=f"{bot} (Depth {loop_depths[i]})")
    ax.set_title("Triadic Lattice Harmonic Structure")
    ax.set_xlabel("Nested Loop Index")
    ax.set_ylabel("Harmonic Value")
    ax.legend()
    plt.tight_layout()
    plt.show()
