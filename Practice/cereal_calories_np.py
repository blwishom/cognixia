import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
print(calorie_stats)

average_calories = round(np.mean(calorie_stats) - 60, 2)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

more_calories = round(np.mean(calorie_stats > 60), 2)
print(more_calories)

calorie_std = round(np.std(calorie_stats), 2)
print(calorie_std)

# percentile_25 = np.percentile(calorie_stats, 25)
# print(percentile_25)

# inner_quartile = np.percentile(calorie_stats, 50)
# print(inner_quartile)

# percentile_75 = np.percentile(calorie_stats, 75)
# print(percentile_75)

# percentile_10 = np.percentile(calorie_stats, 10)
# print(percentile_10)

# percentile_5 = np.percentile(calorie_stats, 5)
# print(percentile_5)

# percentile_4 = np.percentile(calorie_stats, 4)
# print(percentile_4)
