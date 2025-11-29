import numpy as np

array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

array = array.astype(np.int16)

print(array)
print(array.dtype)
print(f'{array.nbytes} bytes')