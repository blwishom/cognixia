import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
print(test_1)

# import from csv file as an array
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
print(test_2)
