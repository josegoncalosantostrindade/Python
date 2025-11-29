import numpy as np

'''array = np.array([1.01, 2.5, 3.99])

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.pi)'''


'''radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)'''


# Element-wise 
'''array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)'''


# Comparasion
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores < 60)
scores[scores < 60] = 0
print(scores)