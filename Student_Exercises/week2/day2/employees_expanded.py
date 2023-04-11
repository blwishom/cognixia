import yaml

def employees():
    full_name = input('Employee\'s full name: ')
    age = int(input('Employee\'s age: '))
    birthyear = input('Employee\'s birthyear: ')
    email = (full_name.replace(' ', '.') + birthyear[2:] + '@company.com').lower()
    num = 0
    full_employee_list = []
    list_of_employees_sentences = []

    # try:
    added_employees = int(input('How many employees will you add? '))
    print(' ')
    if type(added_employees) is int:
        employee_list = dict({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email})
        # employee_list_yaml = list(employee_list.items())

        # print(employee_list_yaml, '<--- YAML EMPLOYEE LIST')

        # full_employee_list.append(employee_list)
        full_employee_list.append(employee_list)
        print(full_employee_list, '<---- Full Employee List')

        ############# LOG FILE STORAGE ##############
        employee_log = open('employee_log.txt', 'wt')
        employee_log.write(str(full_employee_list))
        employee_log.write('\n')
        employee_log.close()

        ############# YAML STORAGE ##############
        yml_data = []
        with open('/home/blair/cognixia/Student_Exercises/week2/day2/employee_log.txt', 'r') as file:
            yml_data = yaml.load(file, Loader=yaml.Loader)
            print(yml_data, '<==== YAML DATA')
        with open('employees2.yaml', 'wt') as file:
            data = yaml.dump(yml_data, sort_keys=False)
            file.write(data)
            print(yml_data, '<==== YAML DATA 2')

    while num <= (added_employees - 2):
        num += 1
        # print(num, '<---NUM')
        full_name = input('Employee\'s full name: ')
        age = int(input('Employee\'s age: '))
        birthyear = input('Employee\'s birthyear: ')
        email = full_name.replace(' ', '.') + birthyear[2:] + '@company.com'
        print(' ')
    full_employee_list.append(({'name':full_name, 'age':age, 'birthyear':birthyear, 'email':email}))

        # under_25 = [employee for employee in full_employee_list if employee['age'] < 25]
        # print(under_25, '<----Under 25')
        # print(' ')

    # except:
    #         print(' ')
    #         print('Please enter a valid number for how many employee you will add.')
    #         print(' ')
    #         employees()


    # for el in full_employee_list:
    #     sentence = f"This employee\'s name is {el.get('name')}, they are {el.get('age')} years old and their email address is {el.get('email')}!"
    #     list_of_employees_sentences.append(sentence)

    return list_of_employees_sentences


employees()
