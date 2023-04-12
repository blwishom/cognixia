import sqlite3

def create_db():
    connection = sqlite3.connect('ems.db')

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            [id] INTEGER PRIMARY KEY,
            [name] TEXT,
            [employee_count] INTEGER,
            [department_domain] TEXT,
            [labor_cost] INTEGER
            )
            ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            [id] INTEGER PRIMARY KEY,
            [fname] VARCHAR(255) NOT NULL,
            [lname] VARCHAR(255) NOT NULL,
            [doe] VARCHAR(255) NOT NULL,
            [salary] INTEGER NOT NULL
            );
            ''')
    connection.close()

def insert_department(department):
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO departments (name, employee_count, department_domain, labor_cost) VALUES('{department['name']}', {department['employee_count']}, '{department['department_domain']}', {department['labor_cost']})")
    connection.commit()

def view_departments():
    connection = sqlite3.connect('ems.db')

    cursor = connection.cursor()
    cursor.execute(
            '''
            SELECT * FROM departments
            '''
    )

    results = cursor.fetchall()
    print(results)
    connection.close()

def insert_employee(employee):
    print(employee)
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()
    params = (employee['fname'], employee['lname'], employee['doe'], employee['salary'] )
    cursor.execute(f"INSERT INTO employees (fname, lname, doe, salary) VALUES(?, ?, ?, ?)", params)
    connection.commit()
    connection.close()

def view_employees():
    connection = sqlite3.connect('ems.db')

    cursor = connection.cursor()
    cursor.execute(
            '''
            SELECT * FROM employees
            '''
    )

    results = cursor.fetchall()
    print(results)
    connection.close()

def update_employee(payload):
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute(f"UPDATE employees set name = '{payload.name}', employee_count = {payload.employee_count}, department_domain = '{payload.department_domain}', labor_cost = {payload.labor_cost}) WHERE id = {payload.id}")
    results = cursor.fetchall()
    print(results)
    connection.commit()
    connection.close()

def update_department(payload):
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute(f"UPDATE departments set fname = '{payload.fname}', lname = {payload.lname}, doe = '{payload.doe}', salary = {payload.salary}) WHERE id = {payload.id}")
    results = cursor.fetchall()
    print(results)
    connection.commit()

def delete_employee(employee):
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE from employees WHERE id = {employee.id}")
    print("successfully deleted")
    connection.commit()
    connection.close()

def delete_department(department):
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute(f"DELETE from departments WHERE id = {department.id}")
    print("successfully deleted")
    connection.commit()
    connection.close()
