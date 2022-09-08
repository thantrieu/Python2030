import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
# print(mydb)
sql = 'SELECT * FROM student.py'
mycursor = mydb.cursor()
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)
