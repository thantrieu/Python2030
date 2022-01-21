import mysql.connector
from student import Student

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
sql = 'DELETE FROM student WHERE full_name LIKE %s'
data = ('%anh%',)
mycursor = mydb.cursor()
mycursor.execute(sql, data)
mydb.commit()

# sql = 'CREATE DATABASE student_register'

# sql = 'CREATE TABLE student (id VARCHAR(20) PRIMARY KEY, ' \
#       'full_name VARCHAR(40) NULL,' \
#       'email VARCHAR(40) NULL,' \
#       'gpa float NULL,' \
#       'major VARCHAR(40) NULL' \
#       ') DEFAULT CHARSET=utf8mb4;'
# sql = 'INSERT INTO student(id, full_name, email, gpa, major) VALUES(%s, %s, %s, %s, %s)'
# data = [
#     ('SV1000', 'Trần Trọng Anh', 'tronganh@xmail.com', 3.26, 'CNTT'),
#     ('SV1002', 'Hoàng Thành Nam', 'thanhnam@xmail.com', 3.65, 'CNTT'),
#     ('SV1003', 'Mai Thúy Anh', 'thuyanh@xmail.com', 3.19, 'CNTT'),
#     ('SV1004', 'Quách Tuấn Du', 'dutuan@xmail.com', 3.36, 'CNTT'),
#     ('SV1005', 'Trần Thu Thủy', 'thuthuy@xmail.com', 3.29, 'CNTT'),
#     ('SV1006', 'Ngô Tuấn Anh', 'tuânnh@xmail.com', 3.69, 'CNTT'),
#     ('SV1007', 'Hoàng Thị Hiên', 'hienhoang@xmail.com', 3.27, 'CNTT'),
#     ('SV1008', 'Lê Công Nhật Minh', 'nhatminhle@xmail.com', 3.85, 'CNTT'),
#     ('SV1009', 'Mã Đại Hải', 'madaihai@xmail.com', 3.85, 'CNTT')
# ]
# sql = 'UPDATE student SET gpa = %s WHERE id = %s'
# data = (3.55, 'SV1008')
# sql = 'SELECT id, full_name, gpa FROM student WHERE full_name LIKE %s'
# data = ('%am%',)
# mycursor = mydb.cursor()
# mycursor.execute(sql, data)
# students = mycursor.fetchall()
#
# student_objects = []
#
#
# def get_students(mstudents, mstudent_objects):
#     for s in mstudents:
#         mstudent_objects.append(Student(s[0], s[1], float(s[2])))
#
#
# get_students(students, student_objects)
# for e in student_objects:
#     e.gpa = (e.gpa + 0.5) if (e.gpa + 0.5) <= 4.0 else 4.0
# sql = 'UPDATE student SET gpa = %s WHERE id = %s'
# data = []
# for item in student_objects:
#     data.append(item.totuple)
#
# mycursor.executemany(sql, data)

sql = 'DELETE FROM student WHERE full_name LIKE %s'
data = ('%anh%',)
mycursor = mydb.cursor()
mycursor.execute(sql, data)
mydb.commit()
