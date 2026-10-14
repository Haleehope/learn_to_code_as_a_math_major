# ###################################################################
# Draw your first seismic wave
# ###################################################################

# first, you need to install a couple libraries to your computer if you haven't already: numpy and matplotlib 
# if you still need to do this, you open a terminal (which is ctrl+shift+` in VSCode) and run:
# pip install numpy matplotlib
# you really don't need to know what pip is, but you can look into it more if you want

# when you import a library, you can alias the name of the library to make it shorter with the "as" keyword
# matplotlib.pyplot is a portion of the matplotlib library that is especially great for plotting
# matplotlib.pyplot is usually aliased as plt and numpy is usually aliased as np, but you can rename them to whatever you want
import numpy as np
import matplotlib.pyplot as plt

# generate 1000 time points between 0 and 10 seconds
time = np.linspace(0, 10, 1000)

# first, create a wave with some amplitude and frequency
amplitude1 = 4
frequency1 = 0.5

# wave = amplitude*sin(2pi*freuqncy*t)
wave1 = amplitude1 * np.sin(2 * np.pi * frequency1 * time)

# create another wave with a different amplitude and frequency to see how it changes
amplitude2 = 0.5
frequency2 = 4

# wave = amplitude*sin(2pi*freuqncy*t)
wave2 = amplitude2 * np.sin(2 * np.pi * frequency2 * time)

# combine two sine waves
combined_wave = wave1 + wave2

# plot all three on the same plot to see how the amplitude and frequency changed the waves
# I, personally, have never cared enough to memorize how to plot in Python, 
# so I usually reuse code and google how to make specific changes when needed 
plt.figure(figsize=(10, 5))
plt.plot(time, wave1, label="Wave 1")
plt.plot(time, wave2, label="Wave 2")
plt.plot(time, combined_wave, label="Combined wave", linewidth=2)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Synthetic Seismic Waves")
plt.legend()
plt.grid(True)
plt.show()
