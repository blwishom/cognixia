import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
print(test_1)

# import from csv file as an array
test_2 = np.genfromtxt('test_2.csv', delimiter=',')
print(test_2)


# add 2 to each element in the array
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2
print(test_3_fixed)


# get final grade for class
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade / 3

print(final_grade)
