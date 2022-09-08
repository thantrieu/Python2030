import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student_register'
)
sql = 'INSERT INTO student.py (id, full_name, email, gpa, major) VALUES(%s, %s, %s, %s, %s)'
data = [
    ('SV1000', 'Trần Trọng Anh', 'tronganh@xmail.com', 3.26, 'CNTT'),
    ('SV1001', 'Lê Văn Tấn', 'tanle@xmail.com', 3.47, 'CNTT'),
    ('SV1002', 'Hoàng Thành Nam', 'thanhnam@xmail.com', 3.65, 'CNTT'),
    ('SV1003', 'Mai Thúy Anh', 'thuyanh@xmail.com', 3.19, 'CNTT'),
    ('SV1004', 'Quách Tuấn Du', 'dutuan@xmail.com', 3.36, 'CNTT'),
    ('SV1005', 'Trần Thu Thủy', 'thuthuy@xmail.com', 3.29, 'CNTT'),
    ('SV1006', 'Ngô Tuấn Anh', 'tuânnh@xmail.com', 3.69, 'CNTT'),
    ('SV1007', 'Hoàng Thị Hiên', 'hienhoang@xmail.com', 3.27, 'CNTT'),
    ('SV1008', 'Lê Công Nhật Minh', 'nhatminhle@xmail.com', 3.85, 'CNTT'),
    ('SV1009', 'Mã Đại Hải', 'madaihai@xmail.com', 3.85, 'CNTT')
]
mycursor = mydb.cursor()
mycursor.executemany(sql, data)
students = mycursor.fetchall()
mydb.commit()
print(f'Số dòng được thêm vào bảng: {mycursor.rowcount}')