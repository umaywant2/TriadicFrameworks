def select_quantum_backend(goal):
    """
    Selects optimal quantum backend based on resonance optimization goal.
    """
    backends = {
        "fold_coherence": "D-Wave",
        "glyph overlay scoring": "IBM Q",
        "phase echo mapping": "Rigetti",
        "symbolic lineage optimization": "IonQ"
    }

    return backends.get(goal, "D-Wave")
