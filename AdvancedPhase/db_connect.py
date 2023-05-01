# import sys

# sys.path.append('')
# import mysql


import mysql.connector
from pprint import pprint #pretty print formats print statements.. good for sql queries

conn = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'root',
    database='<<DB Name>>'
)

cursor = conn.cursor()

with conn.cursor() as cursor:
    cursor.execute('''CREATE TABLE pets (
        id INT Primary Key AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        species VARCHAR)(50),
        age INT
        );''')

cursor.execute("INSERT INTO pets (name, species, age) VALUES ()")
cursor.execute("INSERT INTO pets (name, species, age) VALUES ()")
cursor.execute("INSERT INTO pets (name, species, age) VALUES ()")
conn.commit()

cursor.execute("SELECT * FROM pets;")
for row in cursor:
    print(row)

result = cursor.fetchone()
print(result)

cursor.execute('SHOW DATABASES')
print(cursor)

for db in cursor:
    print(db)


conn.close()
