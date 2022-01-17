import mysql.connector
# sql = 'SELECT id, full_name, gpa FROM student'
# sql = 'SELECT id, full_name, gpa FROM student WHERE gpa >= 3.5'
# sql = 'SELECT * FROM student WHERE id = "SV1008"'
# sql = 'SELECT * FROM student WHERE full_name LIKE %s AND gpa >= %s'
# sql = 'SELECT * FROM student ORDER BY gpa DESC'


def show_students(mstudents):
    for student in mstudents:
        print(student)


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register1'
)
sql = 'SELECT * FROM student ORDER BY gpa DESC'
mycursor = mydb.cursor()
mycursor.execute(sql)
students = mycursor.fetchall()
show_students(students)
