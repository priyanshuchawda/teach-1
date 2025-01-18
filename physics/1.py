import numpy as np
import matplotlib.pyplot as plt

# Define parameters
wavelength = 500e-9  # 500 nm
slit_width = 2e-6    # 2 micrometers
theta = np.linspace(-np.pi/2, np.pi/2, 1000)  # Angular range in radians

# Calculate alpha and intensity
alpha = (np.pi * slit_width / wavelength) * np.sin(theta)
intensity = (np.sin(alpha) / alpha)**2
intensity[alpha == 0] = 1  # Handle division by zero for central maximum

# Plot the intensity distribution
plt.figure(figsize=(8, 5))
plt.plot(np.degrees(theta), intensity, label="Intensity Pattern")
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.title("Fraunhofer Diffraction Intensity Distribution (Single Slit)")
plt.xlabel("Angle (degrees)")
plt.ylabel("Normalized Intensity")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
