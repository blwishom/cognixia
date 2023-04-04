# USING DICTIONARIES, LISTS, TUPLES, AND SETS

def user_info_dict():
    name = input('What is your name? ')
    age = input('How old are you? ')

    print(f'Hi, {name}! Let us know what your first few programming languages were.')
    programming_language_1 = input('What was the first programming languages you learned? ')
    programming_language_2 = input('What was the second programming languages you learned? ')
    programming_language_3 = input('What was the third programming languages you learned? ')
    user_programming_info = (f'{programming_language_1}', f'{programming_language_2}', f'{programming_language_3}')
    user_tuple = tuple(user_programming_info)
    print(f'{name}\'s first 3 programming languages were {user_tuple}.')

    print('=======================================================================')
    
    print(f'Thanks for sharing {name}, now let\'s do favorites!')

    fav_language_1 = input('What is your favorite programming language? ')
    fav_language_2 = input('What is your second favorite programming language? ')
    fav_language_3 = input('What is your third favorite programming language? ')
    user_fav_info = (f'{fav_language_1}', f'{fav_language_2}', f'{fav_language_3}')
    user_list = list(user_fav_info)
    print(f'{name}\'s favorite 3 programming languages are {user_list}.')

    print('=======================================================================')

    user_dict : dict = {'name': name, 'age': age, 'programing_languages': user_tuple, 'favorite_languages': user_list}
    print(f"This user\'s name is {user_dict['name']} and they are {user_dict['age']} years old. Their first 3 programming languages were {user_dict['programing_languages']} and their favorite languages are {user_dict['favorite_languages']}!")

user_info_dict()
