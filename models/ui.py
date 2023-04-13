from department import Department
from db import create_db, view_departments, view_department, insert_department, update_department, delete_department, view_employees, delete_employee, update_employee
import datetime

def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. View All Departments")
    print("2. View Department")
    print("3. Add Department")
    print("4. Update Department")
    print("5. Delete Department")
    print("6. Hire Employee")
    print("7. View All Employees")
    print("8. Delete Employee")
    print("9. Update Employee")
    print("0. Quit")
    print(67 * "-")

create_db()

loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [0-9]: ")

    if choice == '1':
        view_departments()
    elif choice == '2':
        name = input("Enter the name of the department: ")
        view_department(name)
    elif choice == '3':
        name = input("Enter the name of the department: ")
        # employee_count = input("Enter the number of employees in the department: ")
        employee_count = 0
        department_domain = input("Enter the department domain: ")
        # labor_cost = input("Enter the labor cost: ")
        labor_cost = 0
        department = Department(name, employee_count, department_domain, labor_cost)
        insert_department(department.to_dict())
        print("Department added successfully.")
    elif choice == '4':
        id = input("Enter the ID of the department to update: ")
        name = input("Enter the new name of the department: ")
        employee_count = input("Enter the new number of employees in the department: ")
        department_domain = input("Enter the new department domain: ")
        labor_cost = input("Enter the new labor cost: ")
        payload = {'id': id, 'name': name, 'employee_count': employee_count, 'department_domain': department_domain, 'labor_cost': labor_cost}
        update_department(payload)
        print("Department updated successfully.")
    elif choice == '5':
        id = input("Enter the ID of the department to delete: ")
        payload = {'id': id}
        delete_department(payload)
        print("Department deleted successfully.")
    elif choice == '6':
        department_name = input("Enter the name of the department to hire an employee: ")
        department = view_department(department_name)
        if department:
            department = Department(department[1], department[2], department[3], department[4])
            department.hire_employee()
        else:
            print(f"No department found with name {department_name}")
    elif choice == '7':
        view_employees()
    elif choice == '8':
        id = input("Enter the ID of the employee to delete: ")
        payload = {'id': id}
        delete_employee(payload)
        print("Employee deleted successfully.")
    elif choice == '9':
        id = input("Enter the ID of the employee to update: ")
        fname = input("Enter the new first name of the employee: ")
        lname = input("Enter the new last name of the employee: ")
        doe = datetime.date.today()
        salary = input("Enter the new salary of the employee: ")
        while(True):
            department_name = input("Enter the name of the department to hire an employee: ")
            department = view_department(department_name)
            if department:
                break
            else:
                True
        payload = {'id': id, 'fname': fname, 'lname': lname, 'doe': doe, 'salary': salary, 'department' : department_name}
        update_employee(payload)
        print("Employee updated successfully.")
    elif choice == '0':
        loop = False
    else:

        print("Invalid choice. Please enter a number from 1 to 8.")

print_menu()

