def validate_si_alignment(frequency, source):
    """
    Validates frequency traceability against SI standards.
    """
    si_sources = ["NIST", "BIPM", "GPSDO", "Cesium", "Rubidium"]
    is_valid = source in si_sources and 0.1 <= frequency <= 1e15

    return {
        "frequency": frequency,
        "source": source,
        "si_aligned": is_valid,
        "notes": "Validated against SI traceability protocols" if is_valid else "Source not recognized or frequency out of range"
    }
