import codecademylib
import numpy as np
from matplotlib import pyplot as plt


# HISTOGRAM PLOT
commutes = np.genfromtxt('commutes.csv', delimiter=',')

# plt.hist(commutes)
plt.hist(commutes, bins=6)
plt.show()



# NORMAL DISTRIBUTON
import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(loc=6.7, scale=0.7, size=1000)

# Fictionosaurus
f_data = np.random.normal(loc=7.7, scale=0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()
