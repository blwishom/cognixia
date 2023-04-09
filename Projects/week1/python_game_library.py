import sys
import logging

print(' ')
print('Check out these games!')
print(' ')
def game_library():

    menu = ['1. Rock, Paper, Scissors', '2. Truth or Dare', '3. Number Guess']

    for el in menu:
        print(el)
        print(' ')

    select_game = int(input('Select a game to play by entering the number next to the game: '))

    if select_game == 1:
        try:
            # importing rock paper scissors module from same directory
            sys.path.append(r'/home/blair/cognixia/Projects/games')
            import rock_paper_scissors
        except:
            print('The rock, paper, scissors game is closed')
    elif select_game == 2:
        try:
            # importing truth or dare module from nested directory outside of current directory
            sys.path.append(r'/home/blair/cognixia/Student_Exercises/Week1/day4')
            import truth_or_dare
        except:
            print('The truth or dare game is closed')
    elif select_game == 3:
        try:
            # importing importing number guess module from same directory
            sys.path.append(r'/home/blair/cognixia/Projects/games')
            import number_guess
        except:
            print('The number guess game is closed')

game_library()
