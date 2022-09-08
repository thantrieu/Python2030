import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
sql = 'UPDATE student.py SET gpa =3.48 WHERE id = "SV1001"'  # KHÔNG làm như thế này
sql = 'UPDATE student.py SET gpa = %s WHERE id = %s'  # hãy làm như này!
data = (3.48, 'SV1001')
mycursor = mydb.cursor()
mycursor.execute(sql, data)
mydb.commit()
print(f'Số dòng bị ảnh hưởng trong bảng: {mycursor.rowcount}')
