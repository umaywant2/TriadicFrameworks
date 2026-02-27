def cycle_fidelity(sim_results, variables):
    # compute mean/variance across repeats and return CF%
    return cf

def energy_stability(sim_results, window):
    # windowed variance/mean for Energy_Wh
    return es

def asymmetry_index(sim_results, response):
    # compute AI per F using up/down windows and chosen response
    return {"forces": aiF, "fluids": aiL, "frequency": aiQ}

def hysteresis_area(sim_results, response):
    # loop area between driver s_F and response over a cycle
    return {"forces": HF, "fluids": HL, "frequency": HQ}

def phase_lag(sim_results, response):
    # cross-correlation to find lag (cycles)
    return {"forces": phiF, "fluids": phiL, "frequency": phiQ}

def symbolic_emergence(sim_results, baseline_label):
    # residual correlation between drivers and response residuals
    return ses
