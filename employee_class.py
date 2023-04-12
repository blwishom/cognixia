from nanoid import generate

class Employee():
    def __init__(self, id, fname, lname, doe, salary):
        self.id = generate()
        self.fname = fname
        self.lname = lname
        self.doe = doe
        self.salary = salary

    def emp_id(self):
        return f'{self.fname} {self.lname}\'s id is {self.id}'

    def emp_name(self):
        return f'Employee\'s name is {self.fname} {self.lname}.'

    def date_of_employment(self):
        return f'{self.fname} {self.lname}\'s date of employment began on {self.doe}.'

    def emp_salary(self):
        return f'{self.fname} {self.lname}\'s salary is {self.salary}.'

emp1 = Employee(id, 'Johnny', 'Walker', '04-12-2023', 75000)
emp2 = Employee(id, 'Yan', 'Ho', '04-12-2023', 75000)

print(emp1.emp_id())
print(emp2.emp_id())
print(emp1.emp_name())
print(emp2.date_of_employment())
print(emp1.emp_salary())
