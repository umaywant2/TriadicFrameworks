def decode_quantum_results(qubo_output):
    """
    Decodes quantum optimization results into remixable resonance packets.
    """
    packets = []
    for key, value in qubo_output.items():
        freq_index = int(key.split("_")[1])
        packet = {
            "frequency": 144 + freq_index * 33,
            "optimized_score": round(value, 3),
            "glyph": "glyph_protein_echo_02.svg" if value > 2.7 else "bridge_glyph_overlay_01.svg",
            "remix_trigger": value > 2.5
        }
        packets.append(packet)
    return packets
