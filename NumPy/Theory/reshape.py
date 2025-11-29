import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# array = array.reshape(3, 4) # 2 dimentional
# array = array.reshape(3, 2, 2) # 3 dimentional
array = array.reshape(1, -1)

# print(array.shape)
print(array)