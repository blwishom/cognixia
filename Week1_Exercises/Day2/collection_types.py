# LISTS
fruits = ['apple', 'orange', 'grapes', 'peach', 'strawberry', 'strawberry']
print(fruits, '<===== List of fruits')

numbers = [1, 20, 3, 40, 5]

# Indexing
my_choice = fruits[2]
print(my_choice, '<===== My choice fruit')

first_fruit = fruits[0]
print(first_fruit, '<===== First fruit in list')

last_fruit = fruits[-1]
print(last_fruit, '<===== Last fruit in list')

# Methods:

# append
add_nectarine = fruits.append('nectarine')
print(fruits, '<===== Appended nectarine')

# copy
copy_fruit_list = fruits.copy()
print(copy_fruit_list, '<===== Copied fruits list')

# count
count_fruit_list = fruits.count('strawberry')
print(count_fruit_list, 'Counted fruit list')

# extend
print(fruits, '<=== Before extend')
extended_fruit_list = fruits.extend(numbers)
print(fruits, '<===== Extended fruit list with numbers list')

# index
indexed_fruit_list = fruits.index('peach')
print(indexed_fruit_list, '<===== Index place of fruit from list')

# insert
insert_into_fruit_list = fruits.insert(3, 'lemon')
print(fruits, '<===== Inserted lemon into fruit list at index 3')

# pop
print(numbers, '<=== Before pop')
pop_last_element = numbers.pop()
print(numbers, '<===== After pop last element (5) from numbers list')

# remove
print(fruits, '<=== Before removing lemon')
fruit_removed = fruits.remove('lemon')
print(fruits, '<===== After lemon is removed')

# reverse
print(numbers, '<=== Before reverse')
reversed_numbers = numbers.reverse()
print(numbers, '<===== After reverse')

# sort
print(numbers, '<=== Before sorted numbers list')
sort_numbers = numbers.sort()
print(numbers, '<===== After sorted numbers list')

# clear
clear_fruit_list = fruits.clear()
print(fruits, '<===== Cleared fruit list')
