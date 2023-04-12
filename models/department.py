import itertools
import csv
from employee_class import Employee

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

    def write_departments_to_csv(file_name, department): # Writes department data to CSV file
        data = [department.id, department.name, department.employee_count, department.department_domain, department.labor_costs]
        with open('department_db.csv', 'a') as f:
            writer = csv.writer(f) #this is the writer object
            writer.writerow(data) #this is the data

        with open('department_db.csv', "r") as csv_file: # Prints the updated CSV
            reader = csv.reader(csv_file)
            for item in reader:
                print(item)

    def to_dict(self): # Creates dictionary of values to print to CSV file
        return {
            'id': self.id,
            'name': self.name,
            'employee_count': self.employee_count,
            'department_domain': self.department_domain,
            'labor_costs': self.labor_costs,
        }


department = Department('Engineering', 22, '@engineering.io', 100476)
department2 = Department('Engineering', 22, '@engineering.io', 100476)
department3 = Department('Engineering', 22, '@engineering.io', 100476)
column_name = ["Id", "Name", "Employee Count", "Department Domain", "Labor Cost"] #The name of the columns
data = [department3.id, department2.name, department2.employee_count, department2.department_domain, department2.labor_costs]


with open('department_db.csv', "r") as csv_file:
    reader = csv.reader(csv_file)
    for item in reader:
        print(item)
