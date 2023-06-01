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

# NUMS % 2 IF EVEN PRINT 0 IF ODD PRINT 1 #
nums = [4, 8, 15, 16, 23, 42]
parity = [num%2 for num in nums]
print(parity)

# STRINGS ADD HELLO #
names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ['Hello, '+name for name in names]
print(greetings)

# INDEX A STRING #
names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]
print(first_character)

# LENGTH OF NAMES #
names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]
print(lengths)

# BOOLEANS #
booleans = [True, False, True]
opposite = [not boo for boo in booleans]
print(opposite)

names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [name is "Jerry" for name in names]
print(is_Jerry)

nums = [5, -10, 40, 20, 0]
greater_than_two = [num > 2 for num in nums]
print(greater_than_two)
