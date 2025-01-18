import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t) + 0.2*np.cos(2*t)
y = np.sin(t) + 0.2*np.sin(2*t)

plt.plot(x, y, 'r-', linewidth=2)
plt.axis('equal')
plt.title('Parametric Curve')
plt.show()