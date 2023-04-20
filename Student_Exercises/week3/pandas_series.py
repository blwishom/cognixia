import pandas as pd
from datetime import datetime

null = 0
ids = pd.Series([5, 11, 26, 31])
names = pd.Series(['Joe', 'Paula', 'Wendy', 'Billy'])
salary = pd.Series([75000, 85000, 75000, None])
departments = pd.Series(['HR', 'Maintenence', 'IT', 'Finance'])
startDate = pd.date_range("2023-04-18", periods=4)
currentlyEmployed = salary.notna()



employeeData = pd.DataFrame({
    'ID': ids,
    'Name': names,
    'Salary': salary,
    'Department': departments,
    'Start Date': startDate,
    'Currently Employeed': currentlyEmployed
})

sum_of_salaries = employeeData['Salary'].sum()
ave_salary = employeeData['Salary'].mean()
min_salary = employeeData['Salary'].min()
max_salary = employeeData['Salary'].max()

active_employees = pd.DataFrame({

})

departments_df = pd.DataFrame({
    'Departments': departments
})

# merged_df = employeeData.merge(departments_df, on='Departments')
# print(merged_df)

# if employeeData.query('Salary > 0'):
#     print('Yes')

# print(employeeData.query('Salary > 0'))

print(employeeData)
# print(names[0], f'\'s salary is ${salary[0]:.2f}.')
# print(f'{names[1]} works in the {departments[1]} department.')

print(max_salary)
# print(active_employees)
