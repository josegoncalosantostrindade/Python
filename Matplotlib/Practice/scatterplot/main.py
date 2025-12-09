import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
numbers = rng.integers(1, 20, (1,5))
test = np.array(['Um', 'Dois', 'Três', 'Quatro', 'Cinco'])

plt.scatter(numbers, test)

plt.show()