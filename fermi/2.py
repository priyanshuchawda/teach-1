import numpy as np
import matplotlib.pyplot as plt

# Define constants
k = 8.617333262145e-5  # Boltzmann constant in eV/K
E_F = 0.0  # Fermi level, reference energy in eV

# Fermi-Dirac distribution function
def fermi_dirac(E, E_F, T):
    if T == 0:
        return 1 if E < E_F else 0
    else:
        return 1 / (1 + np.exp((E - E_F) / (k * T)))

# Temperatures in Kelvin
T0 = 0  # Absolute zero
T1 = 300  # Room temperature
T2 = 600  # Elevated temperature

# Energy range
E = np.linspace(-0.5, 0.5, 500)  # Energy range in eV

# Calculate Fermi-Dirac distribution for different temperatures
P_T0 = [fermi_dirac(e, E_F, T0) for e in E]
P_T1 = [fermi_dirac(e, E_F, T1) for e in E]
P_T2 = [fermi_dirac(e, E_F, T2) for e in E]

# Plot the probability distribution curve
plt.figure(figsize=(8, 6))
plt.plot(E, P_T0, label="T = 0 K", linestyle='--', color='blue')
plt.plot(E, P_T1, label="T = 300 K", linestyle='-', color='green')
plt.plot(E, P_T2, label="T = 600 K", linestyle='-.', color='red')

# Add labels, legend, and grid
plt.title("Fermi-Dirac Distribution Function")
plt.xlabel("Energy (E) [eV]")
plt.ylabel("Probability P(E)")
plt.axvline(E_F, color='black', linestyle=':', label="Fermi Level (E_F)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Calculate specific probabilities for the question
# T = 0 K: P(E) for E > E_F, E < E_F, and E = E_F
P_E_gt_EF_T0 = fermi_dirac(0.1, E_F, T0)  # E > E_F
P_E_lt_EF_T0 = fermi_dirac(-0.1, E_F, T0)  # E < E_F
P_E_eq_EF_T0 = fermi_dirac(E_F, E_F, T0)  # E = E_F

# T > 0 K: P(E) for E = E_F at T = 300 K and T = 600 K
P_E_eq_EF_T1 = fermi_dirac(E_F, E_F, T1)
P_E_eq_EF_T2 = fermi_dirac(E_F, E_F, T2)

# Print calculated probabilities
probabilities = {
    "T = 0 K, E > E_F": P_E_gt_EF_T0,
    "T = 0 K, E < E_F": P_E_lt_EF_T0,
    "T = 0 K, E = E_F": P_E_eq_EF_T0,
    "T = 300 K, E = E_F": P_E_eq_EF_T1,
    "T = 600 K, E = E_F": P_E_eq_EF_T2,
}
probabilities
