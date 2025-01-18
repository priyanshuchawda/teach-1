import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)

plt.contourf(X, Y, Z, cmap='coolwarm')
plt.colorbar()
plt.show()