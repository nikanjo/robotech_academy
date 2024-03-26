import numpy as np
import matplotlib.pyplot as plt


x1 = ([1, 2, 3, 4])
y1 = ([12, 17, 23, 30])


x2 = ([1, 2, 3, 4])
y2 = ([10, 20, 30, 40])

x3 = ([1, 2, 3, 4])
y3 = ([15, 30, 15, 60])

x4 = ([1, 2, 3, 4])
y4 = (20, 30, 10, 50)

plt.subplot(2, 2, 1)
plt.plot(x1, y1)

plt.subplot(2, 2, 2)
plt.plot(x2, y2)

plt.subplot(2, 2, 3)
plt.plot(x3, y3)

plt.subplot(2, 2, 4)
plt.plot(x4, y4)
plt.show()