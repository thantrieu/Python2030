import mysql.connector


def get_db_connect():
    """Hàm kết nối và trả về đối tượng kết nối tới db định trước."""
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='python_exercises_chapter8'
    )
    return mydb


def get_all_address():
    conn = get_db_connect()
    sql = f'SELECT * FROM address'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def get_all_birth_date():
    conn = get_db_connect()
    sql = f'SELECT * FROM birth_date'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def get_all_full_name():
    conn = get_db_connect()
    sql = f'SELECT * FROM full_name'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def get_all_subject():
    conn = get_db_connect()
    sql = f'SELECT * FROM subject'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def get_all_student():
    conn = get_db_connect()
    sql = f'SELECT * FROM student'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def get_all_register():
    conn = get_db_connect()
    sql = f'SELECT * FROM register'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()


def insert_address(data):
    """
    Hàm chèn dữ liệu vào bảng address.
    :param data: tuple chứa dữ liệu cần chèn vào bảng.
    :return: id của hàng vừa chèn vào.
    """
    founded_row = find_address_by_data(data[0], data[1], data[2])
    if founded_row is not None and len(founded_row):
        return founded_row[0]  # nếu bản ghi cần chèn đã tồn tại, trả về id của nó
    conn = get_db_connect()
    sql = 'INSERT INTO address(wards, district, city) VALUES(%s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    sql2 = 'SELECT MAX(id) FROM address'
    my_cursor.execute(sql2)
    row = my_cursor.fetchone()
    return row[0]


def find_address_by_data(wards, district, city):
    conn = get_db_connect()
    sql = f'SELECT * FROM address ' \
          f'WHERE wards =\'{wards}\' ' \
          f'AND district = \'{district}\' ' \
          f'AND city = \'{city}\''
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    return row


def find_birth_date_by_data(day, month, year):
    conn = get_db_connect()
    sql = f'SELECT * FROM birth_date ' \
          f'WHERE day = {day} ' \
          f'AND month = {month} ' \
          f'AND year = {year}'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    return row


def insert_birth_date(data):
    """
    Hàm chèn dữ liệu vào bảng birth_date.
    :param data: tuple chứa dữ liệu cần chèn.
    :return: id của hàng vừa chèn vào bảng.
    """
    founded_row = find_birth_date_by_data(data[0], data[1], data[2])
    if founded_row is not None and len(founded_row):
        return founded_row[0]  # nếu bản ghi cần chèn đã tồn tại, trả về id của nó
    conn = get_db_connect()
    sql = 'INSERT INTO birth_date(day, month, year) VALUES(%s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    sql2 = 'SELECT MAX(id) FROM birth_date'
    my_cursor.execute(sql2)
    row = my_cursor.fetchone()
    return row[0]


def find_full_name_by_data(first, mid, last):
    """
    Hàm tìm thông tin họ tên cho trước đã tồn tại trong CSDL chưa.
    :param first: tên
    :param mid: đệm
    :param last: họ
    :return: Dòng dữ liệu truy vấn được
    """
    conn = get_db_connect()
    sql = f'SELECT * FROM full_name ' \
          f'WHERE first_name =\'{first}\' ' \
          f'AND mid_name = \'{mid}\' ' \
          f'AND last_name = \'{last}\''
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    return row


def insert_full_name(data):
    """
    Hàm chèn dữ liệu vào bảng full_name.
    :param data: dữ liệu cần chèn.
    :return: giá trị id của hàng dữ liệu vừa chèn vào.
    """
    founded_row = find_full_name_by_data(data[0], data[1], data[2])
    if founded_row is not None and len(founded_row):
        return founded_row[0]  # nếu bản ghi cần chèn đã tồn tại, trả về id của nó
    conn = get_db_connect()
    sql = 'INSERT INTO full_name(first_name, mid_name, last_name) VALUES(%s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()
    sql2 = 'SELECT MAX(id) FROM full_name'
    my_cursor.execute(sql2)
    row = my_cursor.fetchone()
    return row[0]


def insert_student(data):
    """Hàm chèn dữ liệu vào bảng student."""
    if is_recourd_existed('student', 'student_id', data[0]):
        return  # kết thúc
    conn = get_db_connect()
    sql = 'INSERT INTO student(student_id, person_id, full_name_id' \
          ', address_id, birth_date_id, email, gpa, major) ' \
          'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()


def insert_subject(data):
    """
    Hàm chèn dữ liệu vào bảng subject.
    :param data: dữ liệu cần chèn.
    """
    if is_recourd_existed('subject', 'id', data[0]):
        return  # kết thúc
    conn = get_db_connect()
    sql = 'INSERT INTO subject(id, name, credit) VALUES(%s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()


def is_recourd_existed(table_name, column_name, record_id):
    """
    Hàm kiểm tra xem bản ghi trong bảng cho trước đã tồn tại chưa
    :param table_name: tên bảng
    :param column_name: tên cột cần ktra
    :param record_id: giá trị của cột tương ứng
    :return: True nếu bản ghi đã tồn tại và False nếu ngược lại
    """
    conn = get_db_connect()
    sql = f'SELECT * FROM {table_name} WHERE {column_name}=\'{record_id}\''
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    if row is not None:
        return True
    return False


def insert_register(data):
    """
    Hàm chèn dữ liệu vào bảng register.
    :param data: dữ liệu cần chèn.
    """
    if is_register_existed(data[1], data[2]):
        return  # nếu bản đăng ký của sinh viên x với môn học y đã tồn tại
    elif is_recourd_existed('register', 'id', data[0]):
        return  # nếu bản đăng ký với mã cho trước đã tồn tại, thoát
    conn = get_db_connect()
    sql = 'INSERT INTO register(id, student_id, subject_id, register_time) VALUES(%s, %s, %s, %s)'
    my_cursor = conn.cursor()
    my_cursor.execute(sql, data)
    conn.commit()


def is_register_existed(student_id, subject_id):
    """
    Hàm kiểm tra xem bản đăng ký của một sinh viên nào đó đã có trong bảng đăng ký chưa.
    Mỗi sinh viên với 1 môn học trong 1 kỳ học chỉ được đăng ký 1 lần duy nhất.
    :param student_id: mã sinh viên
    :param subject_id: mã môn mà sv đó đăng ký
    :return: True nếu sinh viên x đã đăng ký môn học y và False nếu ngược lại.
    """
    conn = get_db_connect()
    sql = f'SELECT * FROM register ' \
          f'WHERE student_id=\'{student_id}\' ' \
          f'AND subject_id=\'{subject_id}\''
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    if row is not None:
        return True
    return False


def find_subject_by_student_id(student_id):
    """
    Hàm tìm và trả về danh sách các môn học mà sinh viên có mã cho trước đã đăng ký.
    :param student_id: mã sinh viên cần tìm
    :return: các môn học mà sv mã x đã đăng ký
    """
    conn = get_db_connect()
    sql = f'SELECT s.* ' \
          f'FROM register r, subject s ' \
          f'WHERE r.student_id=\'{student_id}\' ' \
          f'AND s.id = r.subject_id;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc


def find_student_by_subject_id(subject_id):
    """
    Hàm tìm và trả về danh sách các sinh viên đã đăng ký môn học x.
    :param subject_id: mã môn cần tìm
    :return: các sv đã đk môn học có mã x
    """
    conn = get_db_connect()
    sql = f'SELECT s.* ' \
          f'FROM register r, student s ' \
          f'WHERE r.subject_id=\'{subject_id}\' ' \
          f'AND s.student_id = r.student_id;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc
