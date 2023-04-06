
def employee():
    full_name = input('Employee\'s full name: ')
    age = int(input('Employee\'s age: '))
    birthyear = input('Employee\'s birthyear: ')
    email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'

    return f"This employee\'s name is {full_name.capitalize()}, they are {age} years old, and their email address is {email.lower()}!"

print(employee())
