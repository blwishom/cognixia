import random
import sys

print(' ')
print('Let\'s play a guessing game!')
print(' ')
def number_guess():
    guesses = 0
    num = random.randint(1,10)
    user_input = int(input('Guess a number between 1 and 10: '))

    if user_input == num:
        print(' ')
        print(f'You guessed it! The number was {num}!')
        print(' ')
    elif user_input < num:
        print(' ')
        print('Try again! Your guess was too low.')
        print(' ')
        number_guess()
    elif user_input > num:
        print(' ')
        print('Try again! Your guess was too high.')
        print(' ')
        number_guess()

    play_again_input = input('Type "play" to play again or "quit" to quit the game: ')
    print(' ')

    if play_again_input == 'play':
        number_guess()
    if play_again_input == 'quit':
        print(' ')
        print('Thanks for playing!')
        print(' ')
        sys.exit()
    elif (play_again_input != 'play') or (play_again_input != 'quit'):
        print(' ')
        print('WARNING: If you type anything other than "yes" to play again or "no" to quit you will be exited from the game')
        print(' ')
        play_again_input = input('Type "play" to play again or "quit" to quit the game: ')
        print(' ')
        if play_again_input == 'play':
            number_guess()
        else:
            print('Thanks for playing!')
            print(' ')
            sys.exit()

    if play_again_input == 'quit':
        print(' ')
        print('Thanks for playing!')
        print(' ')
        sys.exit()

number_guess()


######################### WORKING ON HELPER FUNCTION ##########################
# def play_again():
#     playing = True
#     play_again_input = input('Type "play" to play again or "quit" to quit the game: ')

#     # if play_again() == 'quit':
#     #     print('Thanks for playing!')
#     #     sys.exit()
#     # elif play_again_input == 'play':
#     #     number_guess()
#     while playing:
#         if play_again() == 'quit':
#             print('Thanks for playing!')
#             sys.exit()
#         elif play_again_input == 'play':
#             number_guess()
