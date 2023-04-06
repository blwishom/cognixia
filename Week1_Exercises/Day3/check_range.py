
def check_range():
    # user_num = int(input(f'Enter a number between 1 and 20: '))

    user_num = input(f'Enter a number between 1 and 20: ')
    # while (user_num < 1) or (user_num > 20):
    while (int(user_num) < 1) or (int(user_num) > 20):
        print('Try again!')
        check_range()
        break

        if user_num in range(0, 21):
            return user_num

        elif user_num.isnumeric() == False:
            print('Please enter a valid number')
            check_range()


    return user_num

print('User entered number: ', check_range())


# WORKING ON NEW SOLUTION
# def check_range():
#     # user_num = int(input(f'Enter a number between 1 and 20: '))
#     user_num = (input(f'Enter a number between 1 and 20: '))
#     new_num = 0

#     if user_num in range(0, 21):
#         user_num += new_num
#         print(user_num, '<--- inside try')
#         return user_num
#     elif user_num.isnumeric() == False:
#         print('Please enter a valid number')
#         check_range()

#     # while (user_num < 1) or (user_num > 20):
#     while (int(user_num) < 1) or (int(user_num) > 20):
#         print('Try again!')
#         check_range()
#         break

#     return user_num

# print('User entered number: ', check_range())
