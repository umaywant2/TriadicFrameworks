import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    ["Vantage Lighthouse (WI)", 2, 2, 1, 2, 2, 1, 3, 2],
    ["Vantage Shackelford (TX)", 2, 1, 1, 2, 2, 1, 3, 2],
    ["Microsoft Lighthouse (WI)", 3, 2, 1, 3, 2, 1, 3, 2],
    ["AWS us-east-1", 3, 3, 1, 3, 2, 1, 3, 2],
    ["Google Columbus Cluster", 3, 2, 1, 3, 2, 1, 3, 2],
    ["Google Omaha Cluster", 3, 2, 1, 3, 2, 1, 3, 2],
    ["Meta Prometheus Campus", 3, 2, 1, 3, 2, 1, 3, 2],
    ["Meta Hyperion Campus", 3, 2, 1, 3, 2, 1, 3, 2],
    ["Meta Monroe Campus", 3, 2, 1, 3, 2, 1, 3, 2],
    ["xAI Colossus (Memphis)", 2, 1, 1, 2, 2, 1, 3, 2],
    ["OpenAI Stargate (Abilene)", 2, 1, 1, 2, 2, 1, 3, 2],
    ["Oracle Project Jupiter", 2, 2, 1, 2, 2, 1, 3, 2],
    ["START Campus (Portugal)", 2, 2, 1, 2, 2, 1, 3, 2],
    ["The Heptagon (Saudi Arabia)", 2, 2, 1, 2, 2, 1, 3, 2],
    ["Yondr Toronto", 2, 2, 1, 2, 2, 1, 3, 2],
    ["Yondr Northern Virginia", 2, 2, 1, 2, 2, 1, 3, 2],
    ["Digital Realty (Global)", 3, 3, 2, 3, 2, 1, 3, 2],
    ["Equinix (Global)", 3, 3, 2, 3, 2, 1, 3, 2],
    ["Apple (US/EU)", 3, 3, 2, 3, 2, 1, 3, 2],
    ["Alibaba Zhangbei", 2, 2, 1, 2, 2, 1, 3, 2],
    ["China Telecom Hohhot", 2, 2, 1, 2, 2, 1, 3, 2],
    ["Harbin Data Center", 2, 2, 1, 2, 2, 1, 3, 2],
]

cols = ["Datacenter", "FAC", "GOV", "CUL", "STD", "HUM", "PLA", "INF", "TAX"]
df = pd.DataFrame(data, columns=cols).set_index("Datacenter")

plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap="magma", vmin=0, vmax=3, cbar_kws={"label": "Index (0–3)"})
plt.title("Datacenter Structural Indices — Heatmap")
plt.tight_layout()
plt.savefig("overview_heatmap.png", dpi=300)
plt.show()
