import numpy as np

# Save Array
'''array = np.array([[1, 2, 3], [4, 5, 6]])

np.save('/Users/jgtrindade/Desktop/Curriculo/Python/NumPy/Theory/savearrays/data.npy', array)
print('NumPy array was saved!')'''

# Load Array
'''array = np.load('/Users/jgtrindade/Desktop/Curriculo/Python/NumPy/Theory/savearrays/data.npy')
print(array)'''

# Save Multiple Arrays
'''array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([1.1, 2.2, 3.3, 4.4])
array3 = np.array([2025, 2026, 2027, 2028])

np.savez('/Users/jgtrindade/Desktop/Curriculo/Python/NumPy/Theory/savearrays/dataa', array1, array2, array3)
print('NumPy arrays were saved!')'''

# Save Multiple Arrays Compressed
'''array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([1.1, 2.2, 3.3, 4.4])
array3 = np.array([2025, 2026, 2027, 2028])

np.savez_compressed('/Users/jgtrindade/Desktop/Curriculo/Python/NumPy/Theory/savearrays/dataa2', array1, array2, array3)
print('NumPy arrays were saved!')'''

# Load Multiple Arrays
arrays = np.load('/Users/jgtrindade/Desktop/Curriculo/Python/NumPy/Theory/savearrays/dataa.npz')
array1 = arrays['arr_0']
array2 = arrays['arr_1']
array3 = arrays['arr_2']

print(arrays)
print(array1)
print(array2)
print(array3)