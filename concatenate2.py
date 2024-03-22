import numpy as np

a = np.array([[1,1,1,1],[1,1,1,1]])
b = np.array([[9,9,9,9],[9,9,9,9]])

print(np.concatenate((a,b)))
print(np.concatenate((a,b) , axis = 0))
print(np.concatenate((a,b) , axis = 1))

print(np.hstack((a,b)))

print(np.vstack((a,b)))