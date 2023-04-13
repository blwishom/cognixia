from db import insert_employee, view_employees, update_department, delete_department, view_employee
from employee_class import Employee

class Department():

    company = 'Cognixia'

    def __init__(self, name, employee_count, department_domain, labor_costs):
        self.name = name
        self.employee_count = employee_count
        self.department_domain = department_domain
        self.labor_costs = labor_costs

    def hire_employee(self):
        fname = input("What is the first name of the employee: ")
        lname = input("What is the last name of the employee: ")
        doe = input("When did this employee start (type day then month then year with forward slashes and without spaces ex: DD/MM/YYYY): ")
        salary = input("What is the employee salary (type a number without commas or spaces ex: 12345): ")

        employee = Employee(fname.capitalize(), lname.capitalize(), doe, salary)
        insert_employee(employee.to_dict())
        print(employee.to_dict())

    def to_dict(self): # Creates dictionary of values to print to CSV file
        return {
            'name': self.name,
            'employee_count': self.employee_count,
            'department_domain': self.department_domain,
            'labor_costs': self.labor_costs,
        }


# department = Department('Engineering', 22, '@engineering.io', 100476)
# department2 = Department('Engineering', 22, '@engineering.io', 100476)
# department3 = Department('Engineering', 22, '@engineering.io', 100476)

# department.hire_employee()
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
