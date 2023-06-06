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

# creating 2-D arrays
coin_toss = np.array([1, 0, 0, 1, 0])
print(coin_toss, '<---1st Coin Toss')

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])
print(coin_toss_again, '<---2nd Coin Toss')

# indexing 1-D and 2-D arrays
# 	Tanya	Manual	Adwoa	Jeremy	Cody
# test_1	92	94	88	91	87
# test_2	79	100	86	93	91
# test_3	87	85	72	90	92

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]
print(jeremy_test_2)

manual_adwoa_test_1 = np.array([test_1[1], test_1[2]])
print(manual_adwoa_test_1)

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2, 0]
print(tanya_test_3)

cody_test_scores = student_scores[0:, 4]
print(cody_test_scores)

# logical operators
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[(porridge < 60)]
hot = porridge[(porridge > 80)]
just_right = porridge[(porridge > 60) & (porridge < 80)]
print(cold)
print(hot)
print(just_right)
