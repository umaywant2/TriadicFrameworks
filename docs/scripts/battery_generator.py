# gendata.py

def generate_tft_battery(n_cycles=3500, seed=42):
    import math, random
    rows = []
    random.seed(seed)

    # Constants
    C0 = 1000.0
    R0 = 50.0
    alpha = 0.05
    tau = 80.0
    beta = 0.45 / 3500.0
    gamma = 0.25
    Tamb = 25.0
    theta = 20.0

    for n in range(1, n_cycles + 1):
        L_sei = alpha * (1 - math.exp(-n / tau))
        L_lin = beta * n
        Q = C0 * (1 - L_sei - L_lin)
        R = R0 * (1 + gamma * math.log(1 + n))
        Vocv = 3.7 - 0.06 * (1 - Q / C0) + random.gauss(0, 0.002)
        Vmed = Vocv - 0.5 * R / 1000 + random.gauss(0, 0.003)
        T = Tamb + theta * (n / 3500.0) + random.gauss(0, 0.3)
        eta = 0.999 - 0.0003 * (n / 3500.0) + random.gauss(0, 0.00005)
        D = 100.0 * (1 - Q / C0)
        E = Q * Vmed / 1000.0

        rows.append({
            "cycle": n,
            "current_A": 0.5,
            "capacity_mAh": Q,
            "degradation_pct": D,
            "ocv_V": Vocv,
            "median_discharge_V": Vmed,
            "internal_resistance_mOhm": R,
            "temperature_C": T,
            "coulombic_efficiency": eta,
            "energy_Wh": E
        })

    return rows

from battery_generator import generate_tft_battery
import pandas as pd

rows = generate_tft_battery(n_cycles=3500, seed=42)
df = pd.DataFrame(rows)
df.to_csv("tft_battery_3500cycles.csv", index=False)
