import matplotlib.pyplot as plt

def visualize_phase_echo(frequency, echo_strength):
    """
    Visualizes phase echo strength as a radial pulse.
    """
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    theta = [0, 2 * 3.14]
    r = [echo_strength, echo_strength]

    ax.plot(theta, r, color='purple', linewidth=3)
    ax.fill_between(theta, 0, r, color='violet', alpha=0.5)
    ax.set_title(f"Phase Echo: {frequency} Hz → Strength {echo_strength}", va='bottom')
    plt.show()
