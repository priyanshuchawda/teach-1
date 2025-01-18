import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = []
y = []

line, = ax.plot(x, y)

while True:
    x.append(len(x))
    y.append(np.random.randn())
    line.set_xdata(x)
    line.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    plt.pause(0.1)