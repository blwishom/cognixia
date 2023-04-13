from tkinter import *
import tkinter
import sqlite3

root = tkinter.Tk()
root.title('Employee Management System')
root.geometry('450x400')

connection = sqlite3.connect('ems.db')
cursor = connection.cursor()

connection.execute('''CREATE TABLE IF NOT EXISTS employees
             (first_name TEXT,
              last_name TEXT,
              date_of_employment TEXT,
              salary REAL);''')

def submit_employee():
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO employees VALUES (:f_name, :l_name, :doe, :salary)',
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'doe': doe.get(),
            'salary': salary.get()
        }
    )

    connection.commit()
    connection.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    doe.delete(0, END)
    salary.delete(0, END)

def emp_query():
    connection = sqlite3.connect('ems.db')
    cursor = connection.cursor()

    cursor.execute('SELECT *, oid FROM employees')
    emp_records = cursor.fetchmany(5)
    print(emp_records)

    records = ''
    for emp in emp_records:
        records += str(emp[4]) + str(emp[0:4]) + '\n'
    emp_label = Label(root, text=records)
    emp_label.grid(row=6, column=0, columnspan=2)

    connection.commit()
    connection.close()


#Textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=15)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=15)

doe = Entry(root, width=30)
doe.grid(row=2, column=1, padx=15)

salary = Entry(root, width=30)
salary.grid(row=3, column=1, padx=15)

#Textbox Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

doe_label = Label(root, text='Date of Employment')
doe_label.grid(row=2, column=0)

salary_label = Label(root, text='Salary')
salary_label.grid(row=3, column=0)

submit_button = Button(root, text='Add Employee to Database', command=submit_employee)
submit_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10, ipadx=90)

query_button = Button(root, text='Employee Records', command=emp_query)
query_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, ipadx=90)

connection.commit()
connection.close()

root.mainloop()
