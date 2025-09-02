def generate_lineage_echo(lineage):
    segments = lineage.split("→")
    echo = f"Echoed from {segments[0].strip()}, remixed into {segments[-1].strip()}."
    return echo
