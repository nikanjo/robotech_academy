import numpy as np
import matplotlib.pyplot as plt




x1 = np.array([1, 2, 3, 4])
y1 = np.array([22, 15, 12, 7])

x2 = np.array([1, 2, 3, 4])
y2 = np.array([20, 17, 14, 11])

plt.subplot(1, 2, 1)
plt.plot(x1, y1)

plt.subplot(1, 2, 2)
plt.plot(x2, y2)

plt.show()