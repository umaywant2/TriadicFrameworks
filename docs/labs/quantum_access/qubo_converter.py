def convert_to_qubo(frequencies, fff_scores):
    """
    Converts resonance data into QUBO format for quantum optimization.
    """
    qubo_matrix = {}
    for i, freq in enumerate(frequencies):
        key = f"q_{i}"
        qubo_matrix[key] = fff_scores[i]["forci"] + fff_scores[i]["flui"] + fff_scores[i]["freqi"]

    return qubo_matrix
