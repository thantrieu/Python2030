import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
sql = 'ALTER TABLE subject DROP COLUMN lesson'
mycursor = mydb.cursor()
mycursor.execute(sql)
