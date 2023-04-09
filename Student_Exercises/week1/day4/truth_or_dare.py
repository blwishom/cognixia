import random

print(' ')
print('Let\'s play truth or dare!')
print(' ')
def truth_or_dare():

    truths = ['When was the last time you picked your nose?', 'Have you ever put too much dip on your chip?', 'Have you ever faked sick to miss school or work?', 'Do you shower everyday?', 'What is the longest period of time you\'ve went without leaving the house?']
    dares = ['Put milk in a bag of chips and eat them!', 'Tell someone they have a really nice forehead!', 'Open your window and yell "HELPPPPP!"', 'Do 10 push-ups!', 'Call a friend and tell them you wet the bed last night!']
    playing = True

    while playing:
        print(' ')
        select_truth_or_dare = input('Would you like to choose a truth or a dare? ')

        # TRUTH OR DARE CHOICE BLOCK
        if (select_truth_or_dare == 'truth'):
            print(' ')
            print('Tell the truth: ', random.choice(truths))
            print(' ')

        elif (select_truth_or_dare == 'dare'):
            print(' ')
            print('Here is your dare: ', random.choice(dares))
            print(' ')

        elif (select_truth_or_dare != 'truth') or (select_truth_or_dare != 'dare'):
            print(' ')
            print('Please enter truth or dare for your response')
            print(' ')
            truth_or_dare()

        # PLAY AGAIN BLOCK
        play_again = input('Type "play" to play again or "quit" to quit: ')

        if play_again == 'play':
            playing

        elif (play_again == 'quit'):
            print(' ')
            print('Thanks for playing!')
            print(' ')
            break

        elif (play_again != 'play') or (play_again != 'quit'):
            print(' ')
            print('WARNING: If you do not type "play" or "quit" you will be exited from the game.')
            print(' ')
            play_again = input('Type "play" to play again or "quit" to quit: ')
            print(' ')

            if play_again == 'play':
                playing

            elif (play_again == 'quit'):
                print(' ')
                print('Thanks for playing!!!!!!!')
                print(' ')
                break


truth_or_dare()
