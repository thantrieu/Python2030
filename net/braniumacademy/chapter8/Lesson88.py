import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
# sql = 'DELETE FROM student WHERE id = %s'
# data = ('SV1000',)
mycursor = mydb.cursor()
mycursor.execute("drop database student_register")
# sql = 'DELETE FROM student WHERE id = %s'
# data = ('SV1005',)
# mycursor.execute(sql, data)
# mydb.commit()
# mydb.rollback()
