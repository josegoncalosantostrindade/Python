import numpy as np

# Integer
'''rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=101, size=(3, 2))) # second number is exclusive'''

# Float
'''np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=3))'''

# Shuffle
'''rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)

print(array)'''

# Random Choice
rng = np.random.default_rng()
fruits = np.array(['🍏', '🍊', '🍌', '🥥', '🍍'])
fruit = rng.choice(fruits, size=(3, 3))

print(fruit)