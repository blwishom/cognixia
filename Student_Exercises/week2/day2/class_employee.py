full_name = input('Employee\'s full name: ')
age = int(input('Employee\'s age: '))
birthyear = input('Employee\'s birthyear: ')
email = (full_name.replace(' ', '.') + birthyear[2:] + '@company.com').lower()

class Employee:
    def __init__(self, full_name, age, birthyear, email):
        self.full_name
        self.age
        self.birthyear
        self.email
    def employee_name(self):
        return f'Employee\'s name is {self.full_name}'

employee1 = Employee('John Fuller', 23, 2000, 'jfuller@company.com')
