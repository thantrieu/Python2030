import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
sql = 'DELETE FROM student.py WHERE id = %s'
data = ('SV1002',)
mycursor = mydb.cursor()
mycursor.execute(sql, data)
# mydb.commit()
print(f'Số hàng bị xóa khỏi bảng: {mycursor.rowcount}')
# mydb.rollback()
# print(f'Số hàng được khôi phục: {mycursor.rowcount}')
