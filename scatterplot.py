import numpy as np
import matplotlib.pyplot as plt


x1 = np.array([1, 2, 3, 4, 5, 6, 7])
y1 = np.array([10, 20, 30, 40, 50, 60, 70])
z1 = ([100, 200, 300, 400, 500, 600, 700])

x2 = np.array([1, 2, 3, 4, 5, 6, 7])
y2 = np.array([5, 20, 10, 30, 4, 20, 40])

plt.scatter(x1, y1, label = "class1")
plt.scatter(x2, y2, label = "class2")

#plt.scatter(x1, y1, c = z1, cmap="viridis", label = "class1")
#plt.scatter(x2, y2, label = "class2")
#plt.colorbar()

plt.show()