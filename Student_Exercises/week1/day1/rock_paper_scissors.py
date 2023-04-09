user_1 = input('Player 1 please enter your name: ')
user_2 = input('Player 2 please enter your name: ')
user1_choice = input(f'{user_1}, please choose r (rock), p (paper), or s (scissors): ')
user2_choice = input(f'{user_2}, please choose r (rock), p (paper), or s (scissors): ')

def rock_paper_scissors():
    # It's a tie logic
    if (user1_choice == 'r' and user2_choice == 'r') or (user1_choice == 'p' and user2_choice == 'p') or (user1_choice == 's' and user2_choice == 's'):
        print('It\'s a tie! Please play again.')
    # User 1 is the winner logic
    elif (user1_choice == 'r' and user2_choice == 's') or (user1_choice == 'p' and user2_choice == 'r') or (user1_choice == 's' and user2_choice == 'p'):
        print(f'{user_1} is the winner! Congratulations!')
    # User 2 is the winner logic
    elif (user2_choice == 'r' and user1_choice == 's') or (user2_choice == 'p' and user1_choice == 'r') or (user2_choice == 's' and user1_choice == 'p'):
        print(f'{user_2} is the winner! Congratulations!')
    # Invalid choice
    elif (user1_choice or user2_choice != 'r') or (user1_choice or user2_choice != 'p') or (user1_choice or user2_choice != 's'):
        print('Please only choose r, p, or s when playing this game. Let\'s try again!')

rock_paper_scissors()
