# ROCK PAPER SCISSORS WITH WHILE LOOP
user_1 = input('Player 1 please enter your name: ')
user_2 = input('Player 2 please enter your name: ')

def rock_paper_scissors():
    user1_points = 0
    user2_points = 0
    draw = 0
    play_again = 'yes'

    while (play_again == 'yes'):
        user1_choice = input(f'{user_1}, please choose r (rock), p (paper), or s (scissors): ')
        user2_choice = input(f'{user_2}, please choose r (rock), p (paper), or s (scissors): ')
        
        # It's a tie logic
        if (user1_choice == 'r' and user2_choice == 'r') or (user1_choice == 'p' and user2_choice == 'p') or (user1_choice == 's' and user2_choice == 's'):
            draw += 1
            print('It\'s a tie!', f'{user_1}\'s score:{user1_points}', f'{user_2}\'s score:{user2_points}', f'Draw:{draw}')
        # User 1 is the winner logic
        elif (user1_choice == 'r' and user2_choice == 's') or (user1_choice == 'p' and user2_choice == 'r') or (user1_choice == 's' and user2_choice == 'p'):
            user1_points += 1
            print(f'{user_1} is the winner! Congratulations!', f'{user_1}\'s score:{user1_points} ', f'{user_2}\'s score:{user2_points} ', f'Draw:{draw}')
        # User 2 is the winner logic
        elif (user2_choice == 'r' and user1_choice == 's') or (user2_choice == 'p' and user1_choice == 'r') or (user2_choice == 's' and user1_choice == 'p'):
            user2_points += 1
            print(f'{user_2} is the winner! Congratulations!', f'{user_1}\'s score: {user1_points}', f'{user_2}\'s score: {user2_points}', f'Draw:{draw}')
        # Invalid choice
        elif (user1_choice or user2_choice != 'r') or (user1_choice or user2_choice != 'p') or (user1_choice or user2_choice != 's'):
            print('Please only choose r, p, or s when playing this game. Let\'s try again!')

        play_again = input('Type "yes" to play again or "no" to quit: ')


rock_paper_scissors()
