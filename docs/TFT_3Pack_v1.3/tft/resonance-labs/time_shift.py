import numpy as np

def simulate_time_shift(field, entropy_mode="recursive", delay_factor=0.1):
    """
    Apply temporal distortion to a harmonic field.
    field: input signal (from resonance_model)
    entropy_mode: 'recursive' or 'linear'
    delay_factor: symbolic delay coefficient
    """
    distorted = np.copy(field)

    if entropy_mode == "recursive":
        for i in range(1, len(field)):
            distorted[i] += delay_factor * distorted[i - 1]
    elif entropy_mode == "linear":
        distorted += delay_factor * np.linspace(0, 1, len(field))

    return distorted

def visualize_shift(original, distorted, title="Temporal Distortion"):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 4))
    plt.plot(original, label="Original", color="#999")
    plt.plot(distorted, label="Distorted", color="#cc3300")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    from resonance_model import generate_harmonic_field
    t, f = generate_harmonic_field(base_freq=1.0, loops=5)
    shifted = simulate_time_shift(f, entropy_mode="recursive", delay_factor=0.2)
    visualize_shift(f, shifted)
