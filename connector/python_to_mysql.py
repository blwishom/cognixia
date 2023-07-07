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

my_cursor.execute('CREATE DATABASE if not exists test_db')
my_cursor.execute('SHOW DATABASES')


for db in my_cursor:
    print(db)
