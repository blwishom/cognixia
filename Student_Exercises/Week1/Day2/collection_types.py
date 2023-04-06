# # LISTS
# fruits = ['apple', 'orange', 'grapes', 'peach', 'strawberry', 'strawberry']
# print(fruits, '<===== List of fruits')

# numbers = [1, 20, 3, 40, 5]

# # Indexing
# my_choice = fruits[2]
# print(my_choice, '<===== My choice fruit')

# first_fruit = fruits[0]
# print(first_fruit, '<===== First fruit in list')

# last_fruit = fruits[-1]
# print(last_fruit, '<===== Last fruit in list')

# # Methods:

# # append
# add_nectarine = fruits.append('nectarine')
# print(fruits, '<===== Appended nectarine')

# # copy
# copy_fruit_list = fruits.copy()
# print(copy_fruit_list, '<===== Copied fruits list')

# # count
# count_fruit_list = fruits.count('strawberry')
# print(count_fruit_list, 'Counted fruit list')

# # extend
# print(fruits, '<=== Before extend')
# extended_fruit_list = fruits.extend(numbers)
# print(fruits, '<===== Extended fruit list with numbers list')

# # index
# indexed_fruit_list = fruits.index('peach')
# print(indexed_fruit_list, '<===== Index place of fruit from list')

# # insert
# insert_into_fruit_list = fruits.insert(3, 'lemon')
# print(fruits, '<===== Inserted lemon into fruit list at index 3')

# # pop
# print(numbers, '<=== Before pop')
# pop_last_element = numbers.pop()
# print(numbers, '<===== After pop last element (5) from numbers list')

# # remove
# print(fruits, '<=== Before removing lemon')
# fruit_removed = fruits.remove('lemon')
# print(fruits, '<===== After lemon is removed')

# # reverse
# print(numbers, '<=== Before reverse')
# reversed_numbers = numbers.reverse()
# print(numbers, '<===== After reverse')

# # sort
# print(numbers, '<=== Before sorted numbers list')
# sort_numbers = numbers.sort()
# print(numbers, '<===== After sorted numbers list')

# # clear
# clear_fruit_list = fruits.clear()
# print(fruits, '<===== Cleared fruit list')

# ==================================================================================================== #

# # TUPPLES
# fruit_tuple = ('apple', 'orange', 'strawberry', 'peach', 'grapes', 'apple', 'apple')
# number_tuple = (1, 20, 3, 40, 5, 60)

# # Methods:

# # count
# counted_fruit_tuple = fruit_tuple.count('apple')
# print(counted_fruit_tuple, '<=== How many times does "apple" appears in the tuple')

# # index
# index_fruit_tuple = fruit_tuple.index('strawberry')
# print(index_fruit_tuple, '<=== Index of "strawberry" in fruit tuple')

# # + operator
# add_tuples_together = fruit_tuple + number_tuple
# print(add_tuples_together, '<=== Added number tuple to fruit tuple')

# ==================================================================================================== #

# SETS
fruit_set = {'apple', 'orange', 'strawberry', 'peach', 'grapes', 'apple', 'apple'}
number_set = {22, 13, 20, 3, 40, 5, 60, -15}

# Methods:

#add
add_to_fruit_set = fruit_set.add('lemon')
print(fruit_set, '<== add lemon to end of fruit set')

# copy
copy_number_set = number_set.copy()
print(copy_number_set, '<== copy of number set')

# discard
print(fruit_set, '<== before discard')
discard_fruit = fruit_set.discard('apple')
print(fruit_set, '<== discarded "apple" from set')

# pop
pop_number = number_set.pop()
pop_fruit = fruit_set.pop()
print(pop_number, '<== popped lowest positive number from set')
print(pop_fruit, '<== popped fruit from beginning of set')

# remove
remove_fruit = fruit_set.remove('peach')
print(fruit_set, '<== removed specified fruit from set')

# update
update_fruit = fruit_set.update({'apple', 'mango', 'pineapple'})
print(fruit_set, '<== updated fruit set')
