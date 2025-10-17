import matplotlib.pyplot as plt

def render_bot_dashboard(bot_data):
    """
    Renders dashboard of bot activity and remix impact.
    """
    bots = [entry["bot"] for entry in bot_data]
    strengths = [entry["echo_strength"] for entry in bot_data]
    colors = ["#6c00ff", "#ffcc00", "#00cc99"]

    fig, ax = plt.subplots()
    ax.bar(bots, strengths, color=colors)
    ax.set_ylabel("Echo Strength")
    ax.set_title("Triadic Bot Remix Impact")
    plt.show()
