from db import insert_employee, view_employees, update_department, delete_department, view_employee, create_db, view_department, insert_department
from employee_class import Employee
# importing datetime module
import datetime


class Department():

    company = 'Cognixia'

    def __init__(self, name, employee_count, department_domain, labor_cost):
        self.name = name
        self.employee_count = employee_count
        self.department_domain = department_domain
        self.labor_cost = labor_cost

    def hire_employee(self):

        selection = False

        while selection == False:
            try:
                fname = input("What is the first name of the employee: ")

                lname = input("What is the last name of the employee: ")

                doe = datetime.date.today()
                print(f'date of hire is {doe}')

                salary = input("What is the employee salary (type a number without commas or spaces ex: 12345): ")
                if not int(salary):
                    raise Exception

                department = self.name

                selection = True

            except:
                print("Please enter a valid response")

        employee = Employee(fname.capitalize(), lname.capitalize(), doe, salary, department)
        insert_employee(employee.to_dict())

    def to_dict(self): # Creates dictionary of values to print to CSV file
        return {
            'name': self.name,
            'employee_count': self.employee_count,
            'department_domain': self.department_domain,
            'labor_cost': self.labor_cost,
        }

# TESTING

department = Department('Engineering', 22, '@engineering.io', 100476)
# department2 = Department('Engineering', 22, '@engineering.io', 100476)
# department3 = Department('Engineering', 22, '@engineering.io', 100476)
create_db()
insert_department(department.to_dict())
view_department('Engineering')
# view_employees()
# view_employee('User')

# payload = {
#     'id': 1,
#     'name': 'engineering2',
#     'employee_count': 23,
#     'department_domain': '@engineering2.io',
#     'labor_cost': 120000
# }

# department = {
#     'id': '1'
# }

# update_department(payload)
# delete_department(department)
