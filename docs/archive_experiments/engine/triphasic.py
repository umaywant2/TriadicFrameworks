def generate_triphasic_signals(forces, fluids, frequency, cycles=3500):
    signals = []
    for n in range(1, cycles + 1):
        # Simple placeholder logic for now
        voltage = 3.7 - 0.0001 * n
        capacity = 1000 - 0.3 * n
        temperature = 25 + 0.005 * n

        signals.append({
            "cycle": n,
            "voltage": voltage,
            "capacity_mAh": capacity,
            "temperature_C": temperature,
            "forces_label": forces,
            "fluids_label": fluids,
            "frequency_label": frequency
        })
    return signals
