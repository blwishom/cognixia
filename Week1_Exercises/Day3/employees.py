def employees():
    full_name = input('Employee\'s full name: ')
    age = int(input('Employee\'s age: '))
    birthyear = input('Employee\'s birthyear: ')
    email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'
    num = 0
    full_employee_list = []
    list_of_employees_sentences = []

    try:
        added_employees = int(input('How many employees will you add? '))
        print('                                         ')
        if type(added_employees) is int:
            employee_list = dict({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email})
            full_employee_list.append(employee_list)
            # print(employee_list)
    except:
        print('                                         ')
        print('Please enter a valid number for how many employee you will add.')
        print('                                         ')
        employees()

    while num <= (added_employees - 2):
        num += 1
        # print(num, '<---NUM')
        full_name = input('Employee\'s full name: ')
        age = int(input('Employee\'s age: '))
        birthyear = input('Employee\'s birthyear: ')
        email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'
        print('                                         ')
        full_employee_list.append(({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email}))

    for el in full_employee_list:
        sentence = f"This employee\'s name is {el.get('name')}, they are {el.get('age')} years old and their email address is {el.get('email')}!"
        list_of_employees_sentences.append(sentence)

    return list_of_employees_sentences

print(employees())


###############     WORKING ON ERROR HANDLING FOR AGE AND BIRTHYEAR        #################
# def employees():
#     full_name = input('Employee\'s full name: ')
#     num = 0
#     full_employee_list = []
#     list_of_employees_sentences = []

#     try:
#         age = int(input('Employee\'s age: '))
#         if type(age) is int:
#             pass
#             # print(employee_list)
#     except:
#         print('                                         ')
#         print('Please enter a valid number for age.')
#         print('                                         ')
#         employees()

#     try:
#         birthyear = input('Employee\'s birthyear: ')
#         if type(birthyear) is int:
#             pass
#     except:
#         print('                                         ')
#         print('Please enter a valid number for birthyear.')
#         print('                                         ')
#         employees()

#     email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'

#     try:
#         added_employees = int(input('How many employees will you add? '))
#         print('                                         ')
#         if type(added_employees) is int:
#             employee_list = dict({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email})
#             full_employee_list.append(employee_list)
#             # print(employee_list)
#     except:
#         print('                                         ')
#         print('Please enter a valid number for how many employee you will add.')
#         print('                                         ')
#         employees()

#     while num <= (added_employees - 2):
#         num += 1
#         # print(num, '<---NUM')
#         full_name = input('Employee\'s full name: ')
#         age = int(input('Employee\'s age: '))
#         birthyear = input('Employee\'s birthyear: ')
#         email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'
#         print('                                         ')
#         full_employee_list.append(({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email}))

#     for el in full_employee_list:
#         sentence = f"This employee\'s name is {el.get('name')}, they are {el.get('age')} years old and their email address is {el.get('email')}!"
#         list_of_employees_sentences.append(sentence)

#     return list_of_employees_sentences

# print(employees())
