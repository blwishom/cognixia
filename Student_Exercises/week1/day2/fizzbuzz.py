# FIZZBUZZ
def user_fizz_buzz():
    user_list = []
    user_int = 0

    # while loop to ensure user enters a number greater than zero
    while user_int <= 0:
        user_int = int(input(f'Enter a number greater than zero: '))
        print(f'Try again!')

    # # if statement that has same functionality as while loop above
    # if user_int <= 0:
    #     user_int = int(input(f'Enter a number greater than zero: '))
    #     print(f'Try again!')

    # for loop to iterate through the range of numbers from 0 to user's input
    for i in range(1, user_int+1):
        if i % 3 == 0 and i % 5 ==0:
            user_list.append('Fizzbuzz')
            # print(user_list)
        elif i % 3 == 0:
            user_list.append('Fizz')
            # print(user_list)
        elif i % 5 == 0:
            user_list.append('Buzz')
            # print(user_list)
    if len(user_list) == 0:
        print('Your number did not meet the fizz or buzz or fizzbuzz conditions')
    return user_list

print(user_fizz_buzz())
