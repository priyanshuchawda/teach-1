import matplotlib.pyplot as plt

def draw_energy_band_diagram():
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Energy Band Diagram at 0K", fontsize=16)
    
    # N-type semiconductor
    axes[0].set_title("N-Type Semiconductor")
    axes[0].axhline(y=0, color='black', linewidth=1)  # Reference line
    axes[0].text(-0.5, 0, "Valence Band (EV)", verticalalignment='bottom')
    axes[0].axhline(y=1, color='blue', linewidth=2)  # Donor Level (ED)
    axes[0].text(-0.5, 1, "Donor Level (ED)", verticalalignment='bottom')
    axes[0].axhline(y=2, color='red', linewidth=2)  # Conduction Band (EC)
    axes[0].text(-0.5, 2, "Conduction Band (EC)", verticalalignment='bottom')
    axes[0].axhline(y=1.5, color='green', linestyle='--', linewidth=2)  # Fermi Level (EF)
    axes[0].text(-0.5, 1.5, "Fermi Level (EF)", verticalalignment='bottom')
    axes[0].set_xlim(-1, 1)
    axes[0].set_ylim(-1, 3)
    axes[0].set_ylabel("Energy (eV)")
    axes[0].get_xaxis().set_visible(False)

    # P-type semiconductor
    axes[1].set_title("P-Type Semiconductor")
    axes[1].axhline(y=0, color='red', linewidth=2)  # Valence Band (EV)
    axes[1].text(-0.5, 0, "Valence Band (EV)", verticalalignment='bottom')
    axes[1].axhline(y=1, color='blue', linewidth=2)  # Acceptor Level (EA)
    axes[1].text(-0.5, 1, "Acceptor Level (EA)", verticalalignment='bottom')
    axes[1].axhline(y=2, color='black', linewidth=1)  # Conduction Band (EC)
    axes[1].text(-0.5, 2, "Conduction Band (EC)", verticalalignment='bottom')
    axes[1].axhline(y=0.5, color='green', linestyle='--', linewidth=2)  # Fermi Level (EF)
    axes[1].text(-0.5, 0.5, "Fermi Level (EF)", verticalalignment='bottom')
    axes[1].set_xlim(-1, 1)
    axes[1].set_ylim(-1, 3)
    axes[1].get_xaxis().set_visible(False)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Call the function to draw the diagram
draw_energy_band_diagram()
