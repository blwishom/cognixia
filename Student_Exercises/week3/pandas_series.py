import pandas as pd
from datetime import datetime

null = 0
ids = pd.Series([5, 11, 26, 31])
names = pd.Series(['Joe', 'Paula', 'Wendy', 'Devin'])
salary = pd.Series([75000, 80000, 75000, None])
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

print(employeeData)
print(names[0], f'\'s salary is ${salary[0]:.2f}.')
print(f'{names[1]} works in the {departments[1]} department.')
