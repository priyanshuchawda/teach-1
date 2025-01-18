import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(np.random.rand(50), label='Random Data')
ax1.legend()

ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(np.random.rand(10, 10), cmap='viridis')
ax2.set_title('Random Image')

ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(np.random.randn(1000), bins=30, color='skyblue')
ax3.set_xlabel('Value')
ax3.set_ylabel('Frequency')

ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(np.random.rand(50), np.random.rand(50), c='red', marker='x')
ax4.set_title('Scatter Plot')

plt.tight_layout()
plt.show()