import numpy as np
import sounddevice as sd

fs = 44100  # Sampling frequency
duration = 2  # seconds
frequency = 440  # Hz (A4 note)

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
tone = np.sin(2 * np.pi * frequency * t)
sd.play(tone)
sd.wait()
