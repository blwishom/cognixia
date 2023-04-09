import logging

# ROCK PAPER SCISSORS WITH WHILE LOOP
print(' ')
print('Let\'s play rock, paper, scissors!')
print(' ')

def rock_paper_scissors():
    user_1 = input('Player 1 please enter your name: ')
    print(' ')
    user_2 = input('Player 2 please enter your name: ')
    user1_points = 0
    user2_points = 0
    draw = 0
    playing = True

    while playing:
        print(' ')
        user1_choice = input(f'{user_1}, please choose r (rock), p (paper), or s (scissors): ')
        print(' ')
        user2_choice = input(f'{user_2}, please choose r (rock), p (paper), or s (scissors): ')
        print(' ')

        # It's a tie logic
        if (user1_choice == 'r' and user2_choice == 'r') or (user1_choice == 'p' and user2_choice == 'p') or (user1_choice == 's' and user2_choice == 's'):
            draw += 1
            print(' ')
            print('It\'s a tie!', f'{user_1}\'s score:{user1_points}', f'{user_2}\'s score:{user2_points}', f'Draw:{draw}')
            print(' ')
        # User 1 is the winner logic
        elif (user1_choice == 'r' and user2_choice == 's') or (user1_choice == 'p' and user2_choice == 'r') or (user1_choice == 's' and user2_choice == 'p'):
            user1_points += 1
            print(f'{user_1} is the winner! Congratulations!', f'{user_1}\'s score:{user1_points} ', f'{user_2}\'s score:{user2_points} ', f'Draw:{draw}')
            print(' ')
        # User 2 is the winner logic
        elif (user2_choice == 'r' and user1_choice == 's') or (user2_choice == 'p' and user1_choice == 'r') or (user2_choice == 's' and user1_choice == 'p'):
            user2_points += 1
            print(f'{user_2} is the winner! Congratulations!', f'{user_1}\'s score: {user1_points}', f'{user_2}\'s score: {user2_points}', f'Draw:{draw}')
            print(' ')
        # Invalid choice
        elif (user1_choice or user2_choice != 'r') or (user1_choice or user2_choice != 'p') or (user1_choice or user2_choice != 's'):
            print('Please only choose r, p, or s when playing this game.')
            print(' ')

        play_again = input('Type "yes" to play again or "no" to quit: ')
        if play_again == 'yes':
            playing
        elif play_again == 'no':
            print(' ')
            print('Thanks for playing!')
            print(' ')
            break
        elif play_again != 'no' or play_again != 'yes':
            print(' ')
            print('WARNING: If you type anything other than "yes" to play again or "no" to quit you will be exited from the game')
            print(' ')
            play_again = input('Type "yes" to play again or "no" to quit: ')
            print(' ')
            if play_again == 'yes':
                playing
            else:
                print(' ')
                print('Thanks for playing!')
                print(' ')
                break

    if user1_points >= 0:
        message = f'{user_1}\'s score:{user1_points} Draw:{draw}'
        logging = open('/home/blair/cognixia/Projects/Games/log_file.txt', 'at')
        logging.write(message + '\n')
        logging.close()
        print(message)
        print(' ')
    if user2_points >= 0:
        message = f'{user_2}\'s score:{user2_points} Draw:{draw}'
        logging = open('/home/blair/cognixia/Projects/Games/log_file.txt', 'at')
        logging.write(message + '\n')
        logging.close()
        print(message)
        print(' ')

    if user1_points >= user2_points:
        message = f'{user_1} beat {user2}!'
        logging = open('/home/blair/cognixia/Projects/Games/log_file.txt', 'at')
        logging.write(message + '\n')
        logging.close()
        print(message)
        print(' ')
    if user1_points <= user2_points:
        message = f'{user_2} beat {user1}!'
        logging = open('/home/blair/cognixia/Projects/Games/log_file.txt', 'at')
        logging.write(message + '\n')
        logging.close()
        print(message)
        print(' ')
    if user1_points == user2_points:
        message = f'{user_1} and {user2} tied!'
        logging = open('/home/blair/cognixia/Projects/Games/log_file.txt', 'at')
        logging.write(message + '\n')
        logging.close()
        print(message)
        print(' ')

rock_paper_scissors()
