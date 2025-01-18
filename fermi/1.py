import numpy as np

# Fermi-Dirac distribution function
def fermi_dirac(E, E_F, T):
    k_B = 8.617333262145e-5  # Boltzmann constant in eV/K
    if T == 0:
        if E > E_F:
            return 0
        elif E < E_F:
            return 1
        else:
            return 0.5
    else:
        return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

# Constants
E_F = 5.0  # Fermi energy in eV (example value)
T0 = 0     # Temperature at 0 K
T1 = 300   # Temperature at 300 K
T2 = 600   # Temperature at 600 K

# Calculate probabilities
P_E_gt_EF_T0 = fermi_dirac(E_F + 0.1, E_F, T0)  # E > E_F at T = 0 K
P_E_lt_EF_T0 = fermi_dirac(E_F - 0.1, E_F, T0)  # E < E_F at T = 0 K
P_E_eq_EF_T0 = fermi_dirac(E_F, E_F, T0)        # E = E_F at T = 0 K
P_E_eq_EF_T1 = fermi_dirac(E_F, E_F, T1)        # E = E_F at T = 300 K
P_E_eq_EF_T2 = fermi_dirac(E_F, E_F, T2)        # E = E_F at T = 600 K

# Store probabilities in a dictionary
probabilities = {
    "T = 0 K, E > E_F": P_E_gt_EF_T0,
    "T = 0 K, E < E_F": P_E_lt_EF_T0,
    "T = 0 K, E = E_F": P_E_eq_EF_T0,
    "T = 300 K, E = E_F": P_E_eq_EF_T1,
    "T = 600 K, E = E_F": P_E_eq_EF_T2,
}

# Print the probabilities
for key, value in probabilities.items():
    print(f"{key}: {value}")