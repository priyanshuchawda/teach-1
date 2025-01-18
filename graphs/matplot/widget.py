import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from ipywidgets import interact

def plot_sine_wave(freq):
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(freq * x)
    plt.plot(x, y)
    plt.title(f'Sine Wave with Frequency {freq}')
    plt.show()

interact(plot_sine_wave, freq=(1, 10, 0.1))