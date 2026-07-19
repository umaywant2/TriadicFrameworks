def convert_classical_freqi(frequencies, observer_angle, timestamp):
    """
    Converts a list of classical frequencies into resonant-time packets.
    """
    packets = []
    for freq in frequencies:
        packet = map_resonant_time(freq, observer_angle, timestamp)
        packets.append(packet)
    return packets
