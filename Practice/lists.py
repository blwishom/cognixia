# DOUBLE NUMS #
nums = [4, 8, 15, 16, 23, 42]
# list comp
double_nums = [num*2 for num in nums]

# # for loop
# double_nums = []
# for num in nums:
#   double_nums.append(num*2)

print(double_nums)

# SQUARED NUMS IN RANGE #
nums = range(11)
# # list comp
squares = [num**2 for num in nums]

# # for loop
# squares = []
# for num in nums:
#     squares.append(num**2)

print(squares)


# ADD TEN #
nums = [4, 8, 15, 16, 23, 42]
add_ten = [num+10 for num in nums]
print(add_ten)

# DIVIDE BY 2 #
nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [int(num/2) for num in nums]
print(divide_by_two)
