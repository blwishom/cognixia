class Employee:
    title = 'Supervisor'
    def __init__(self, full_name, age, birthyear):
        self.full_name = full_name
        self.age = age
        self.birthyear = birthyear
        self.email = (full_name.replace(' ', '.')).lower() + '@company.com'
    def name(self):
        return f'Employee\'s name is {self.full_name}.'

    def employee_age(self):
        return f'{self.full_name} is {self.age} years old.'

    def employee_birthyear(self):
        return f'{self.full_name}\'s birthyear is {self.birthyear}.'

    def employee_email(self):
        return f'{self.full_name}\'s email is {self.email}.'

    def employee_title(self):
        return f'{self.full_name} is a(n) {self.title} at Company.'

employee1 = Employee('John Fuller', 22, 2001)
employee1.title = 'Administrator'
emp2 = Employee('Jimmy John', 24, 1999)

# print(employee1.full_name, employee1.age, employee1.birthyear, employee1.email)
# print('{} {} {}'.format(employee1.full_name, employee1.age, employee1.birthyear))
# print(employee1.name())
# print(employee1.employee_age())
# print(employee1.employee_email())
# print(employee1.title)
print(employee1.employee_title())
print(emp2.employee_title())

# print(Employee.__dict__)
