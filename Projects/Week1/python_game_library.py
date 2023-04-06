import sys


def game_library():

    menu = ['1. Rock, Paper, Scissors', '2. Truth or Dare']

    for el in menu:
        print(el)

    select_game = int(input('Please select a game to play by entering the number next to the game: '))

    if select_game == 1:
        try:
            # importing rock paper scissors module from same directory
            sys.path.append(r'/home/blair/cognixia/Projects/Games')
            import rock_paper_scissors
        except:
            print('File was not opened')
    elif select_game == 2:
        try:
            # importing truth or dare module from nested directory outside of current directory
            sys.path.append(r'/home/blair/cognixia/Student_Exercises/Week1/Day4')
            import truth_or_dare
        except:
            print('Truth or Dare file was not opened')

game_library()
