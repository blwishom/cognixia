import codecademylib
import numpy as np
from matplotlib import pyplot as plt

emails = np.random.binomial(500, .05, size=10000)

plt.hist(emails)
plt.show()
