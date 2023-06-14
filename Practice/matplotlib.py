import codecademylib
import numpy as np
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# plt.hist(commutes)
plt.hist(commutes, bins=6)
plt.show()
