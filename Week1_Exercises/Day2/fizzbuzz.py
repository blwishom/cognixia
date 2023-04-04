# FIZZBUZZ
def user_fizz_buzz():
    user_list = []
    user_int = 0

    while user_int <= 0:
        user_int = int(input(f'Enter a number greater than zero: '))
        print(f'Try again!')


    for i in range(1, user_int+1):
        if i % 3 == 0 and i % 5 ==0:
            user_list.append('Fizzbuzz')
            print(user_list)
        elif i % 3 == 0:
            user_list.append('Fizz')
            print(user_list)
        elif i % 5 == 0:
            user_list.append('Buzz')
            print(user_list)

user_fizz_buzz()
