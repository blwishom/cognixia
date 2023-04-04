full_name = input('Employee\'s full name: ')
# fname = input('Employee\'s first name: ')
# lname = input('Employee\'s last name: ')
age = int(input('Employee\'s age: '))
birthyear = input('Employee\'s birthyear: ')
# email = fname.lower() + '.' + lname.lower() + birthyear[2:] + '@company.com'
email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'


# print(f"This employee\'s name is {fname.capitalize()} {lname.capitalize()}, they are {age} years old, and their email address is {email}.")

# print(f"This employee\'s name is {fname.capitalize()} {lname.capitalize()}, they are {age} years old, and their email address is {email}.")

print(f"This employee\'s name is {full_name.capitalize()}, they are {age} years old, and their email address is {email.lower()}.")
