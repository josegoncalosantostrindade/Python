import numpy as np

rng = np.random.default_rng()
numbers = rng.integers(1, 100, (100,3))

# normalization 0-1
numbers_min = numbers.min(axis=0)
numbers_max = numbers.max(axis=0)
numbers_01 = (numbers - numbers_min) / (numbers - numbers_max)

# normalization z-core
numbers_mean = numbers.mean(axis=0)
numbers_std = numbers.std(axis=0)
numbers_zcore = (numbers - numbers_mean) /numbers_std

print('*** MATRIX ***')
print(numbers)

print('\n*** 0-1 MATRIX ***')
print(numbers_01)

print('\n*** z-core MATRIX ***')
print(numbers_zcore)