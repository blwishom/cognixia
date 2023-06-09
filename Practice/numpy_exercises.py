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


# import and read csv file data, alter data at each index, index arrays, logical operators
temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')
print(temperatures)

temperatures_fixed = temperatures+3

monday_temperatures = temperatures_fixed[0]
print(monday_temperatures)

thursday_friday_morning = temperatures_fixed[3:, 1]
print(thursday_friday_morning)

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print(temperature_extremes)


# BETTY'S BAKERY PROJECT
# Recipe	Cups of Flour	Cups of Sugar	Eggs	Cups of Milk	Cups of Butter
# Cupcakes	…	…	…	…	…
# Pancake	…	…	…	…	…
# Cookie	…	…	…	…	…
# Bread	…	…	…	…	…

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print(cupcakes)
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)
eggs = recipes[:, 2]
print(eggs)
one_egg = recipes[:, 2] == 1
print(one_egg)
cookies = recipes[2, :]
print(cookies)
double_batch = cupcakes*2
print(double_batch)
grocery_list = cookies + double_batch
print(grocery_list)


# Find mean of arrays
store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)
print(store_one_avg, store_two_avg, store_three_avg)


# STORE MEANS GREATER THAN 7 INTO BEST_SELLER VARIABLE

# direct assignment
best_seller = store_two

# list comp
means = [store_one_avg, store_two_avg, store_three_avg]
best_seller = [mean  for mean in means if mean > 7]
print(best_seller)

# for loop
means = [store_one_avg, store_two_avg, store_three_avg]
best_seller = []
for mean in means:
  if mean > 7:
    best_seller.append(mean)
print(best_seller)

# GET PERCENTAGE OF TRUE VALUES IN THE LIST/ARRAY
class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])

millennials = np.mean(class_year > 2005)
print(millennials)


# 2-D ARRAY MEANS
allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
print(total_mean)

trial_mean = np.mean(allergy_trials, axis=1)
print(trial_mean)

patient_mean = np.mean(allergy_trials, axis=0)
print(patient_mean)


# SORT ARRAY TO FIND OUTLIERS
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps)
print(sorted_temps)

# FIND MEDIAN OF DATA SETS
large_set = np.genfromtxt('household_income.csv', delimiter=',')

small_set_median = 40500
print(small_set_median)

large_set_median = np.median(large_set)
print(large_set_median)

# NUMPY PERCENTILES

# find the 30th and 70th percentile of the array
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)
print(thirtieth_percentile)

seventieth_percentile = np.percentile(patrons, 70)
print(seventieth_percentile)


# finding quartiles (first, third, and inner(75th - 25th))
movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
print(first_quarter)

third_quarter = np.percentile(movies_watched, 75)
print(third_quarter)

interquartile_range = third_quarter - first_quarter
print(interquartile_range)


# finding Standard Deviation
pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
print(pumpkin_avg)

acorn_squash_avg = np.mean(acorn_squash)
print(acorn_squash_avg)

pumpkin_std = np.std(pumpkin)
print(pumpkin_std)

acorn_squash_std = np.std(acorn_squash)
print(acorn_squash_std)

# finding percentil, quartile, and standard deviation
rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

rain_mean = np.mean(rainfall)
print(rain_mean)
rain_median = np.median(rainfall)
print(rain_median)
first_quarter = np.percentile(rainfall, 25)
print(first_quarter)
third_quarter = np.percentile(rainfall, 75)
print(third_quarter)
interquartile_range = third_quarter - first_quarter
print(interquartile_range)
rain_std = np.std(rainfall)
print(rain_std)
