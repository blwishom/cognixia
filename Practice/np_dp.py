import numpy as np
import pandas as pd

# # NUMPY
# #
# # #CREATING ARRAYS
# arr1 = np.array(['yes', 'no', 'maybe so', 'uhhhh', 1, 2, 3, 4, 3.0])
# arr2 = np.array([ 1, 2, 3, 4, 3.0, 'yes', 'no', 'maybe so', 'uhhhh'])
# arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# arr4 = np.array([21, 4, 9, 1, 55])
# # print(arr1, '<----', arr1.dtype)
# # print(arr2, '<----', arr2.dtype)
# # print(arr3, '<----', arr3.dtype)

# # zeros = np.zeros(4 + 2)
# # print(zeros)

# # empty = np.empty(4)
# # print(empty)

# # range1 = np.arange(5)
# # range2 = np.arange(5, 15)
# # range3 = np.arange(2, 41, 6)
# # print(range1)
# # print(range2)
# # print(range3)

# # ELEMENT OPERATIONS
# # print(arr1.sort())
# # print(arr4)
# # print('********************SORT OPERATION********************')
# # print(arr4.sort(), '<---DIDN\'T SORT WITH METHOD CALLED DIRECTLY ON VARIABLE')

# # arr5 = np.sort(arr4)
# # print(arr5, '<---SORTED AFTER BEING SAVED TO A VARIABLE')

# # print('********************CONCATENATE OPERATION********************')
# # print(np.concatenate((arr3, arr4)))
# # print(np.concatenate((arr4, arr3)))
# # print(np.concatenate((arr1, arr4)), '<---TURNED INTs INTO STRs')

# reshaped = np.reshape(arr3, (4, 2))
# reshaped2 = np.reshape(arr3, (2, 4))
# print(arr3)
# print('============================')
# print(reshaped)
# print('============================')
# print(reshaped2)
# print('============================')

# # newAxis = arr3[np.newaxis, np.newaxis, np.newaxis]
# # print(newAxis)


# # CONDITIONS
# condition = arr3[arr3 > 4]
# print(condition, '<---condition')

# condition2 = arr3[arr3 <= 3]
# print(condition2)

# print(arr3[:4].sum())
# print(arr3.max())


# ********************     PANDAS     ********************
series1 = pd.Series([5, 4, 3, 2, 1])
series2 = pd.Series({5: 'five', 4: 'four', 3: 'three', 'two': 'two or 2', 1: 'one'})
series3 = pd.Series({'one': 1, 'two': 2, 'three': 3, 'four': '4 or four', 'five': '5 or five'})
series4 = pd.Series(['uno', 'dos', 'tres', 'quatro'])

# LOC and ILOC
Iloc = series1.iloc[0]
Loc = series2.loc[3]
print(Iloc)
print(Loc)

print('============================')

Iloc2 = series3.iloc[4]
loc2 = series3['four']
print(Iloc2)
print(loc2)

print('============================')

# HEAD and TAIL
head = series4.head(2)
head2 = series3.head(2)
print(head, '<---HEAD')
print(head2, '<---HEAD 2')

tail = series2.tail(3)
tail2 = series4.tail(2)
print(tail, '<---TAIL')
print(tail2, '<---TAIL 2')

print('============================')

# CONDITION
condition = series1[series1 < 3]
condition2 = series3[series3 != 2]
print(condition, '<---CONDITION')
print(condition2, '<---CONDITION 2')

# MATH
describe = series1.describe()
print(describe, '<---DESCRIBE')
