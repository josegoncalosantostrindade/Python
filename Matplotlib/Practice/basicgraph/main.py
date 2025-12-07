import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
grades = np.array([51, 63, 76, 82, 97])

study = np.array([2, 4, 6, 8, 10])

plt.plot(grades, study)

plt.title('Scores')
plt.xlabel('Grades')
plt.ylabel('# of Study')

plt.show()