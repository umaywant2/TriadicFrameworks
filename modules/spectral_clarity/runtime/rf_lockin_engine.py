# RF lock-in engine scaffold

def init_rf_lockin(frequency, phase, gain):
    # Configure SDR and signal generator
    pass

def capture_rf_quadratures():
    # Acquire I/Q data from SDR
    pass

def lockin_overlay(quadratures, visible_phase):
    # Phase-sensitive detection and overlay
    pass

if __name__ == "__main__":
    init_rf_lockin(1e6, 0, 30)
    capture_rf_quadratures()
