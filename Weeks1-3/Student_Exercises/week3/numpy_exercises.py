import numpy as np

# CREATE AN ARRAY
numpyArr = np.array([1, 2, 3, 4, 5])
print(numpyArr, type(numpyArr), '<---NumPy array')

pythonList = [1, 2, 3, 4, 5]
numpyArr2 = np.array(pythonList)
print(numpyArr2, type(numpyArr2), '<---Python list to NumPy array')
