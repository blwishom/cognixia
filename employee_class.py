from nanoid import generate
import itertools
import json
import sys

class Employee():
    eid = itertools.count()
    def __init__(self, eid, fname, lname, doe, salary):
        self.eid = next(Employee.eid)
        self.fname = fname
        self.lname = lname
        self.doe = doe
        self.salary = salary

    def emp_id(self):
        return f'{self.fname} {self.lname}\'s id is {self.eid}'

    def emp_name(self):
        return f'Employee\'s name is {self.fname} {self.lname}.'

    def date_of_employment(self):
        return f'{self.fname} {self.lname}\'s date of employment began on {self.doe}.'

    def emp_salary(self):
        return f'{self.fname} {self.lname}\'s salary is {self.salary}.'

    def full_emp_info(self):
        return dict({'id':self.eid, 'First Name':self.fname, 'Last Name':self.lname, 'Date of Employment':self.doe, 'Salary':self.salary})

def emp_info(Employee):
    employee_info = {
        'id':self.eid,
        'First Name':self.fname,
        'Last Name':self.lname,
        'Date of Employment':self.doe,
        'Salary':self.salary
    }

    try:
       with open('emp_file.csv', 'rt') as emp_file:
        print()

    except FileNotFoundError:
        print('Emp file was not found.')
    else:
        print('Emp file was opened.')
    finally:
        emp_file.close()
        print('Emp file is closed.')
        sys.exit()

#     def __call__(self, *args, **kwargs):
#         print('Call function', args, kwargs)

# @Employee(eid, fname, lname, doe, salary)
# def emp_info():
#     # emp_dict = dict({'id':self.eid, 'First Name':self.fname, 'Last Name':self.lname, 'Date of Employment':self.doe, 'Salary':self.salary})
#     print('Hello')

emp1 = Employee(id, 'Johnny', 'Walker', '04-12-2023', 75000)
emp2 = Employee(id, 'Yan', 'Ho', '04-12-2023', 75000)

# print(emp1.emp_id())
# print(emp2.emp_id())
# print(emp1.emp_name())
# print(emp2.date_of_employment())
# print(emp1.emp_salary())
print(emp_info(emp1))
