import numpy as np

a = np.array([1,2,3,4,5,6])

b = np.copy(a)

b[0] = 10 
print(b)