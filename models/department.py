import itertools
import csv

class Department():

    company = 'Cognixia'
    id_obj = itertools.count()


    def __init__(self, name, employee_count, department_domain, labor_costs):
        self.id = next(Department.id_obj)
        self.name = name
        self.employee_count = employee_count
        self.department_domain = department_domain
        self.labor_costs = labor_costs

    def hire_employee(self):
        employee = Employee()
        return employee.to_dict()


department = Department('Engineering', 22, '@engineering.io', 100476)
department2 = Department('Engineering', 22, '@engineering.io', 100476)
column_name = ["Id", "Name", "Employee Count", "Department Domain", "Labor Cost"] #The name of the columns
data = {department2.id, department2.name, department2.employee_count, department2.department_domain, department2.labor_costs}

with open('db.csv', 'a') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(data) #this is the data
