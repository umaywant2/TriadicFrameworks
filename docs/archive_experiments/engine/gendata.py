from battery_generator import generate_tft_battery
import pandas as pd

rows = generate_tft_battery(n_cycles=3500, seed=42)
df = pd.DataFrame(rows)
df.to_csv("data/tft_battery_3500cycles.csv", index=False)
