import mysql.connector

# try:
#     conn = mysql.connector.connect(host='localhost', username='root', password='root')
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS new_schema")

#     conn.commit()
#     print('Database created successfully!')
# except mysql.connector.Error as error:
#     print('Error:', error)
# finally:
#     if conn.is_connected():
#         cursor.close()
#         conn.close()

my_db = mysql.connector.connect(host='localhost', user='root', password='root', database='test_db')
print(my_db)

my_cursor = my_db.cursor()

# my_cursor.execute('CREATE DATABASE if not exists test_db')
# my_cursor.execute('SHOW DATABASES')
# my_cursor.execute('CREATE TABLE if not exists students (name VARCHAR(255), age INT(10))')
# my_cursor.execute('SHOW TABLES')

insert_students = 'INSERT INTO students (name, age) VALUES (%s, %s)'
# update_students = 'UPDATE students SET name=%s'
# delete_students = 'DELETE FROM students WHERE name LIKE "%s"'

student1 = ('Jimmy', 22)
# student2 = ('Linwood', 22)
# student3 = ('Paula', 19)
# student4 = ('Vanessa', 21)
# student5 = ('Logan', 20)
students = [('Rodney', 21),
            ('Wilma', 47),
            ('Jamie', 23),
            ('Ned', 20)]

# INSERT UPDATE and DELETE executions
# my_cursor.execute(insert_students, student1)
# my_cursor.executemany(insert_students, students)
# my_cursor.execute('UPDATE students SET name="Ben" WHERE name LIKE "Jimmy"')
# my_cursor.execute('DELETE FROM students WHERE name LIKE "Jimmy"')

# my_cursor.execute('DESCRIBE students')
my_cursor.execute('SELECT * FROM students')
for db in my_cursor:
    print(db)
# for tb in my_cursor:
#     print(tb)

my_db.commit()
