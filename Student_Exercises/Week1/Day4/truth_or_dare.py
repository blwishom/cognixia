import random

print(' ')
print('Let\'s play truth or dare!')
print(' ')
def truth_or_dare():


    truths = ['When was the last time you picked your nose?', 'Have you ever put too much dip on your chip?', 'Have you ever faked sick to miss school or work?', 'Do you shower everyday?', 'What is the longest period of time you\'ve went without leaving the house?']
    dares = ['Put milk in a bag of chips and eat them!', 'Tell someone they have a really nice forehead!', 'Open your window and yell "HELPPPPP!"', 'Do 10 push-ups!', 'Call a friend and tell them you wet the bed last night!']
    play_again = 'play'

    while (play_again == 'play'):
        print(' ')
        select_truth_or_dare = input('Would you like to choose a truth or a dare? ')

        if (play_again == 'quit'):
            print(' ')
            print('Thanks for playing!')
            break
        elif (select_truth_or_dare == 'dare'):
            print(' ')
            print('Here is your dare: ', random.choice(dares))
            print(' ')
            play_again = input('Type "play" to play again or "quit" to quit: ')
            if (play_again == 'quit'):
                print(' ')
                print('Thanks for playing!')
                break
        elif (select_truth_or_dare != 'truth'):
            print(' ')
            print('Please enter truth or dare for your response')
            print(' ')
            truth_or_dare()

        elif (select_truth_or_dare == 'truth'):
            print(' ')
            print('Tell the truth: ', random.choice(truths))
            print(' ')
            play_again = input('Type "play" to play again or "quit" to quit: ')
            if (play_again == 'quit'):
                print(' ')
                print('Thanks for playing!')
                print(' ')
                break
        elif (select_truth_or_dare != 'dare'):
            print(' ')
            print('Please enter truth or dare for your response')
            print(' ')

truth_or_dare()

# def truth_or_dare():
#     play_prompt = input('Would you like to play truth or dare? ')
#     playing = True
#     select_truth_or_dare = input('Ok, truth or dare? ')

#     truths = ['When was the last time you picked your nose?', 'Have you ever put too much dip on your chip?']
#     dares = ['I dare you to put milk in a bag of chips and eat them!', 'I dare you to tell someone they have a really nice forehead!']

#     if play_prompt == 'yes':
#         playing

#     while playing:
#         print(' ')
#         if (select_truth_or_dare == 'quit'):
#             break
#         elif (select_truth_or_dare == 'dare'):
#             print(' ')
#             print('Here is your dare: ', random.choice(dares))
#             print(' ')
#             truth_or_dare()
#         elif (select_truth_or_dare != 'truth'):
#             print(' ')
#             print('Please enter truth or dare for your response')
#             print(' ')
#             truth_or_dare()
#         elif (select_truth_or_dare == 'truth'):
#             print(' ')
#             print('Tell the truth: ', random.choice(truths))
#             print(' ')
#             truth_or_dare()
#         elif (select_truth_or_dare != 'dare'):
#             print(' ')
#             print('Please enter truth or dare for your response')
#             print(' ')
