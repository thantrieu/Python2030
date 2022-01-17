import mysql.connector


def show_students(mstudents):
    for x in mstudents:
        print(x)


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register1'
)
sql = 'SELECT * FROM student WHERE id="SV1005"'
mycursor = mydb.cursor()
mycursor.execute(sql)
students = mycursor.fetchall()
show_students(students)