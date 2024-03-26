import numpy as np
import matplotlib.pyplot as plt

#x = np.array([1,2])
#y = np.array([10,15])

#plt.plot(x,y, 'o')
#plt.plot(x,y, 'o--m')


#================

#x = np.array([1,2,5,9])
#y = np.array([10, 15, 19, 7])
#plt.plot(x,y, 'v--b', linewidth = '5')
#plt.show()

#=================

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1, label ='train')
plt.plot(y2, label = 'test')

plt.xlabel("EPOCH")
plt.ylabel("Loss")


font1 = {"family" : "serif", "color" : "red" , "size": 20}
plt.title("classification" , fontdict= font1, loc ="right")
plt.legend()

plt.grid()
plt.show()
