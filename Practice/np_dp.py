import numpy as np
import pandas as pd

# NUMPY CREATING ARRAYS
arr1 = np.array(['yes', 'no', 'maybe so', 'uhhhh', 1, 2, 3, 4, 3.0])
arr2 = np.array([ 1, 2, 3, 4, 3.0, 'yes', 'no', 'maybe so', 'uhhhh'])
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([21, 4, 9, 1, 55])
# print(arr1, '<----', arr1.dtype)
# print(arr2, '<----', arr2.dtype)
# print(arr3, '<----', arr3.dtype)

# zeros = np.zeros(4 + 2)
# print(zeros)

# empty = np.empty(4)
# print(empty)

# range1 = np.arange(5)
# range2 = np.arange(5, 15)
# range3 = np.arange(2, 41, 6)
# print(range1)
# print(range2)
# print(range3)

# ELEMENT OPERATIONS
print(arr1.sort())
print(arr4)
print('********************SORT OPERATION********************')
print(arr4.sort(), '<---DIDN\'T SORT WITH METHOD CALLED DIRECTLY ON VARIABLE')

arr5 = np.sort(arr4)
print(arr5, '<---SORTED AFTER BEING SAVED TO A VARIABLE')

print('********************CONCATENATE OPERATION********************')
print(np.concatenate((arr3, arr4)))
print(np.concatenate((arr4, arr3)))
print(np.concatenate((arr1, arr4)), '<---TURNED INTs INTO STRs')
