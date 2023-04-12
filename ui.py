'''
import employee
import department


while True:

    try except block that offers option to create, read, update, or delete both Employee and Department
    
        create employee called from Department
        create department called from Department
        read, update, delete for employee and department called from respective classes

That all?  Can't think of anything else




'''
import employee
import department
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Welcome to the Employee Management System!")
    print("Please select an option below:")
    print("1. Manage Employees")
    print("2. Manage Departments")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        employee_menu() 
    elif choice == "2":
        department_menu()
    elif choice == "3":
        print("Exiting the program...")
        exit()
    else:
        input("Invalid choice! Press enter to try again...")
        main_menu()

def employee_menu():
    clear_screen()
    print("Employee Menu")
    print("Please select an option below:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. View Employees")
    print("5. Back to Main Menu")
    choice = input("Enter your choice: ")

    employee_manager = EmployeeManager() #Placeholder until other sections are complete

    if choice == "1":
        employee_manager.add_employee() #Placeholder
    elif choice == "2":
        employee_manager.delete_employee() #Placeholder
    elif choice == "3":
        employee_manager.update_employee( )#Placeholder
    elif choice == "4":
        employee_manager.view_employees() #Placeholder
    elif choice == "5":
        main_menu()
    else:
        input("Invalid choice! Press enter to try again...")
        employee_menu()

def department_menu():
    clear_screen()
    print("Department Menu")
    print("Please select an option below:")
    print("1. Add Department")
    print("2. Delete Department")
    print("3. View Departments")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")

    department_manager = DepartmentManager() #Placeholder until other sections are complete

    if choice == "1":
        department_manager.add_department() #Placeholder
    elif choice == "2":
        department_manager.delete_department() #Placeholder
    elif choice == "3":
        department_manager.view_departments() #Placeholder
    elif choice == "4":
        main_menu()
    else:
        input("Invalid choice! Press enter to try again...")
        department_menu()

if __name__ == "__main__":
    main_menu()
