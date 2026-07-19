import matplotlib.pyplot as plt

def visualize_observer_angle(angle):
    """
    Visualizes observer angle on a resonance quadrant compass.
    """
    labels = ['N', 'E', 'S', 'W']
    angles = [0, 90, 180, 270]

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    for label, a in zip(labels, angles):
        ax.text(a * (3.14/180), 1.1, label, ha='center', va='center', fontsize=12)

    ax.plot([angle * (3.14/180)], [1], marker='o', markersize=10, color='purple')
    ax.set_rticks([])
    ax.set_title(f"Observer Angle: {angle}°", va='bottom')
    plt.show()
