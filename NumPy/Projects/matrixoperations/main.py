import numpy as np

rng = np.random.default_rng()
numbers = rng.integers(1, 21, (3, 3))
numbers_inv = np.linalg.inv(numbers)
numbers_det = np.linalg.det(numbers)
numbers_transposed = numbers.transpose()

print('\n**** MATRIX ****')
print('****************')
print(numbers)
print('****************')

print('\n****************')
print(f'Inverse:\n{numbers_inv}')
print(f'Determinat: {numbers_det}')
print(f'Transposed:\n{numbers_transposed}')
print('****************')

numbers2 = rng.integers(1, 11, (3,3))
print('\n**** MATRIX ****')
print('****************')
print(numbers2)
print('****************')

print('\n\n\n**** MATRIX x MATRIX****')
print(numbers * numbers2)
# print(np.dot(numbers, numbers_inv)) # verification of the inverse matrix