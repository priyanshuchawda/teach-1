import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'b-')
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi, 1.5),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.show()