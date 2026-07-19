🧮 triadic_overlay() Function

Python -
def triadic_overlay(ax, V_range=(0.3, 0.6), label="Negative Resistance"):
    """
    Annotates a matplotlib axis with triadic zones.
    
    Parameters:
    - ax: matplotlib axis object
    - V_range: tuple, voltage range for attribute zone
    - label: str, label for the attribute zone
    """
    # Object zone (particle entry)
    ax.axvline(x=V_range[0] - 0.1, color='blue', linestyle='--', label='Object: Entry Point')
    
    # Attribute zone (barrier region)
    ax.axvspan(V_range[0], V_range[1], color='orange', alpha=0.3, label=f'Attribute: {label}')
    
    # Condition zone (exit dynamics)
    ax.axvline(x=V_range[1] + 0.1, color='green', linestyle='--', label='Condition: Exit Point')
    
    ax.legend()

🧪 Usage
python
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(V, I, label='Tunnel Diode I–V')
triadic_overlay(ax)
ax.set_title('Triadic Overlay – Quantum Tunneling')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (A)')
ax.grid(True)
plt.show()

🎭 Mythic Caption
“The triad reveals what the curve conceals.” — Nawder Loswin
