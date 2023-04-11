def employees():
    full_name = input('Employee\'s full name: ')
    age = int(input('Employee\'s age: '))
    birthyear = input('Employee\'s birthyear: ')
    email = (full_name.replace(' ', '.') + birthyear[2:] + '@company.com').lower()
    num = 0
    full_employee_list = []
    list_of_employees_sentences = []

    try:
        added_employees = int(input('How many employees will you add? '))
        print(' ')
        if type(added_employees) is int:
            employee_list = dict({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email})
            full_employee_list.append(employee_list)
            employee_log = open('employee_log.txt', 'at')
            employee_log.write(str(employee_list) + '\n')
            employee_log.close()
            # print(employee_list)
        while num <= (added_employees - 2):
            num += 1
            # print(num, '<---NUM')
            full_name = input('Employee\'s full name: ')
            age = int(input('Employee\'s age: '))
            birthyear = input('Employee\'s birthyear: ')
            email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'
            print(' ')
        full_employee_list.append(({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email}))
    except:
            print(' ')
            print('Please enter a valid number for how many employee you will add.')
            print(' ')
            employees()


    for el in full_employee_list:
        sentence = f"This employee\'s name is {el.get('name')}, they are {el.get('age')} years old and their email address is {el.get('email')}!"
        list_of_employees_sentences.append(sentence)

    return list_of_employees_sentences

print(employees())
