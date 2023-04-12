
class Department():
    def __init__(self, id, name, employee_count, labor_cost, department_domain):
        self.id = id
        self.name = name
        self.employee_count = employee_count
        self.labor_cost = labor_cost
        self.department_domain = department_domain

    def hire_employee(self):
        employee = Employee()
        return employee.to_dict()
