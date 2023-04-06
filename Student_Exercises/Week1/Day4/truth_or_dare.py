import random

print(' ')
print('Let\'s play truth or dare!')
print(' ')
def truth_or_dare():


    truths = ['When was the last time you picked your nose?', 'Have you ever put too much dip on your chip?']
    dares = ['I dare you to put milk in a bag of chips and eat them!', 'I dare you to tell someone they have a really nice forehead!']
    play_again = 'yes'

    # if (select_truth_or_dare == 'quit'):
    #     print(' ')
    #     print('Thanks for playing')

    # if (select_truth_or_dare == 'dare') or (select_truth_or_dare == 'truth'):
    #     playing = True

    while (play_again == 'yes'):
        print(' ')
        select_truth_or_dare = input('Would you like to choose a truth or a dare? ')
        print(' ')

        if (play_again == 'no'):
            print(' ')
            print('Thanks for playing!')
            break
            play_again = input('Type "yes" to play again or "no" to quit: ')
        elif (select_truth_or_dare == 'dare'):
            print(' ')
            print('Here is your dare: ', random.choice(dares))
            print(' ')
            play_again = input('Type "yes" to play again or "no" to quit: ')
            if (play_again == 'no'):
                print(' ')
                print('Thanks for playing!')
                break
            else:
                truth_or_dare()
        elif (select_truth_or_dare != 'truth'):
            print(' ')
            print('Please enter truth or dare for your response')
            print(' ')
            truth_or_dare()
        elif (select_truth_or_dare == 'truth'):
            print(' ')
            print('Tell the truth: ', random.choice(truths))
            print(' ')
            play_again = input('Type "yes" to play again or "no" to quit: ')
            if (play_again == 'no'):
                print(' ')
                print('Thanks for playing!')
                break
            else:
                truth_or_dare()
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
