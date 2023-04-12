from nanoid import generate
import itertools
import csv

employee_list = []
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

emp1 = Employee(id, 'Johnny', 'Walker', '04-12-2023', 75000)
emp2 = Employee(id, 'Yan', 'Ho', '04-12-2023', 75000)
emp3 = Employee(id, 'Janet', 'Jones', '04-12-2023', 75000)
emp4 = Employee(id, 'Tracy', 'Long', '04-12-2023', 75000)
emp5 = Employee(id, 'Wallace', 'Peyton', '04-12-2023', 75000)

emp_data = {emp1.eid, emp1.fname, emp1.lname, emp1.doe, emp1.salary}
emp_data2 = {emp2.eid, emp2.fname, emp2.lname, emp2.doe, emp2.salary}
emp_data3 = {emp3.eid, emp3.fname, emp3.lname, emp3.doe, emp3.salary}
emp_data4 = {emp4.eid, emp4.fname, emp4.lname, emp4.doe, emp4.salary}
emp_data5 = {emp5.eid, emp5.fname, emp5.lname, emp5.doe, emp5.salary}
employee_list.append(emp_data5)
print(employee_list)

with open('employee_db.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(employee_list) #this is the data
