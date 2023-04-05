
def check_range():
    # user_num = int(input(f'Enter a number between 1 and 20: '))
    user_num = input(f'Enter a number between 1 and 20: ')
    new_input = user_num
    final_user_num = user_num.replace(user_num, new_input)

    # while (user_num < 1) or (user_num > 20):
    while (int(user_num) < 1) or (int(user_num) > 20):
        print('Try again!')
        check_range()
        print(final_user_num)
        break

        try:
            if user_num in range(0, 21):
                return user_num

        except ValueError:
            if user_num is not isnumeric():
                print('Please enter a valid number')
                check_range()

    print(new_input, '<== New Input')
    return final_user_num

print('User entered number: ', check_range())
