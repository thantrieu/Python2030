import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    password="",
    database='student_register'
)
mycursor = mydb.cursor()
sql = 'SELECT * FROM student'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
