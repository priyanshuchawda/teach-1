import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1.38e-23  # Boltzmann constant (J/K)
E_F = 0  # Fermi energy in eV (centered at 0 for simplicity)
T0 = 0  # Absolute zero
T1 = 300  # Room temperature (approx. in Kelvin)
T2 = 600  # Higher temperature

# Energy range in eV
E = np.linspace(-1, 1, 1000)

# Fermi-Dirac distribution function
def fermi_dirac(E, E_F, T):
    if T == 0:
        # Step function for T=0
        return np.where(E < E_F, 1, 0)
    else:
        # Smooth function for T > 0
        return 1 / (1 + np.exp((E - E_F) / (k * T / 1.60218e-19)))  # kT in eV

# Calculate P(E) for different temperatures
P_T0 = fermi_dirac(E, E_F, T0)
P_T1 = fermi_dirac(E, E_F, T1)
P_T2 = fermi_dirac(E, E_F, T2)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(E, P_T0, label='T = 0 K', linestyle='--', color='blue')
plt.plot(E, P_T1, label='T = 300 K', linestyle='-', color='green')
plt.plot(E, P_T2, label='T = 600 K', linestyle='-', color='red')

plt.axvline(x=E_F, color='black', linestyle=':', label='Fermi Energy ($E_F$)')
plt.title('Fermi-Dirac Distribution Function')
plt.xlabel('Energy (E)')
plt.ylabel('Probability P(E)')
plt.legend()
plt.grid()
plt.show()
