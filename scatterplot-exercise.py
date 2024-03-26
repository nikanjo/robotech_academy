import numpy as np
import matplotlib.pyplot as plt
import random


numbers = []
sizes = []

for i in range(100):
    numbers += [random.sample(range(80), 2)]



for i in range(0,50):
    plt.scatter(numbers[i][0],numbers[i][1], cmap="nipy-spectral",  alpha = 0.5)


plt.show()