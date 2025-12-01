import numpy as np

print('\n**** STATISTIC ANALISOR ****')
print('****************************')

rng = np.random.default_rng()
numbers = rng.integers(1, 101, (1, 200))
mean = np.mean(numbers)
median = np.median(numbers)
std = np.std(numbers)

numbers2 = numbers.reshape(10,20)

print('\n********* 1D ARRAY *********')
print(numbers)
print('****************************')

print(f'Mean: {mean:.2f}')
print(f'Median: {median}')
print(f'Standart Deviation: {std:.2f}')
print('****************************')

print('\n********* 2D ARRAY *********')
print(numbers2)
print('****************************')