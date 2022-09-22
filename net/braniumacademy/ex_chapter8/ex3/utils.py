from register import Register
from subject import Subject
from student import Student
from filter import *
from dbutils import *
from person import FullName, Address, BirthDate


def create_student():
    """Phương thức tạo mới thông tin sv."""
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    name = input('Họ và tên: ')
    birth_date = input('Ngày sinh: ')
    address = input('Địa chỉ(vd phường 5-Quận 7-HCM city): ')
    email = input('Email: ')
    major = input('Chuyên ngành: ')
    gpa = input('Điểm TB: ')
    return Student(pid, name, birth_date, address, None, email, gpa, major)


def find_full_name_by_id(list_name, name_id):
    for name in list_name:
        if name[0] == name_id:
            return name
    return None


def find_address_by_id(list_address, addr_id):
    for addr in list_address:
        if addr[0] == addr_id:
            return addr
    return None


def find_birth_date_by_id(list_dob, dob_id):
    for dob in list_dob:
        if dob[0] == dob_id:
            return dob
    return None


def read_students_from_database():
    """Phương thức đọc thông tin sv từ database."""
    students = []
    data = get_all_student()
    list_bith_date = get_all_birth_date()
    list_full_name = get_all_full_name()
    list_address = get_all_address()
    for s in data:
        name = find_full_name_by_id(list_full_name, s[2])
        fname = FullName(name[0], name[1], name[3], name[2])
        addr = find_address_by_id(list_address, s[3])
        address = Address(addr[0], addr[3], addr[1], addr[2])
        dob = find_birth_date_by_id(list_bith_date, s[4])
        birth_date = BirthDate(dob[0], dob[1], dob[2], dob[3])
        students.append(Student(s[1], fname, birth_date,
                                address, s[0], s[5], s[6], s[7]))
    return students


def create_subject():
    """Phương thức tạo mới môn học."""
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(None, name, credit)


def read_subject_from_database():
    """Phương thức đọc thông tin môn học từ database."""
    subjects = []
    data = get_all_subject()
    for s in data:
        subjects.append(Subject(int(s[0]), s[1], s[2]))
    return subjects


def read_register_from_database(students, subjects):
    """Phương thức đọc thông tin đăng ký từ database."""
    registers = []
    data = get_all_register()
    for r in data:
        subject_id = int(r[2])
        student_id = r[1]
        student = find_student_by_id(students, f'{student_id}')
        subject = find_subject_by_id(subjects, subject_id)
        registers.append(Register(int(r[0]), r[3], student, subject))
    return registers


def find_student_by_id(students, student_id):
    """Phương thức tìm sinh viên theo mã sinh viên."""
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None  # nếu k tim thấy, trả về None


def find_subject_by_id(subjects, subject_id):
    """Phương thức tìm môn học theo mã môn học."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None


def is_register_exists(registers, student_id, subject_id):
    """Phương thức kiểm tra xem sinh viên x đã đăng ký môn học y chưa."""
    for reg in registers:
        if reg.subject.subject_id == subject_id and reg.student.student_id == student_id.upper():
            return True  # nếu đã đăng ký, trả về True
    return False  # chưa đăng ký, trả về false


def create_register(registers, students, subjects):
    """Phương thức tạo thông tin đăng ký môn học của sv."""
    student = None
    subject = None
    student_id = input('Mã sinh viên: ')
    try:
        if is_student_id_valid(student_id):
            student = find_student_by_id(students, student_id)
            if student is None:
                print(f'==> Sinh viên mã \'{student_id}\' không tồn tại.')
                return None
    except StudentIdError as e:
        print(e)
        return None

    subject_id = input('Mã môn học(số nguyên 4 chữ số): ')
    try:
        if is_subject_id_valid(subject_id):
            subject = find_subject_by_id(subjects, int(subject_id))
            if subject is None:
                print(f'==> Môn học mã \'{subject_id}\' không tồn tại.')
                return None
    except SubjectIdError as e:
        print(e)
        return None

    if is_register_exists(registers, student_id, int(subject_id)):
        print(f'==> Sinh viên mã {student_id} đã đăng ký môn học {subject_id} trước đó.')
        return None
    else:
        return Register(None, None, student, subject)


def is_register_exist(registers, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in registers:
        if item == r:
            return True
    return False


def sort_registers(registers):
    """
        Phương thức sắp xếp danh sách đăng ký. Liên quan date time bạn xem chương 9.
        Ta tách thời gian đăng ký và lần lượt sắp xếp theo năm, tháng, ngày, giờ, phút, giây
    """
    registers.sort(key=lambda x: (x.register_time.year, x.register_time.month,
                                  x.register_time.day, x.register_time.hour,
                                  x.register_time.minute, x.register_time.second)
                   )


def stat_student_same_city():
    result = student_in_same_city()
    print('==> Danh sách sinh viên cùng thành phố: <==')
    for r in result:
        print(r)


def update_student_name(students):
    """Phương thức dùng để cập nhật tên sinh viên theo mã sinh viên cho trước."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    try:
        if is_student_id_valid(student_id):
            student = find_student_by_id(students, student_id)
            old_name = student.full_name
            if student is not None:
                full_name = input('Họ và tên mới: ')
                try:
                    if is_subject_name_valid(full_name):
                        student.full_name = full_name
                        update_student_name_db(old_name, student.full_name)
                        print('==> Cập nhật điểm cho sinh viên thành công! <==')
                except FullNameError as e:
                    print(e)
    except StudentIdError as e:
        print(e)


def update_student_gpa(students):
    """Phương thức dùng để cập nhật điểm Gpa theo mã sv cho trước."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    try:
        if is_student_id_valid(student_id):
            student = find_student_by_id(students, student_id)
            if student is not None:
                gpa_str = input('Điểm Gpa thay thế: ')
                try:
                    if is_gpa_valid(gpa_str):
                        student.gpa = gpa_str
                        update_gpa(student.student_id, student.gpa)
                        print('==> Cập nhật điểm cho sinh viên thành công! <==')
                except GpaError as e:
                    print(e)
    except StudentIdError as e:
        print(e)


def student_not_register(students):
    """
    Hàm hiển thị danh sách sinh viên không đăng ký môn học nào cả.
    :param students: danh sách sinh viên
    :return: None
    """
    print("==> Danh sách sinh viên không đăng ký môn học nào: ")
    result = student_zero_register()
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(student)


def stat_scond_max_gpa(students):
    result = find_second_max_gpa()
    print('==> Danh sách sinh viên có điểm TB cao thứ hai: ')
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(student)


def stat_most_register_students(students):
    result = student_most_register()
    print('==> Danh sách sinh viên đăng ký sớm nhất: ')
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}{"Số môn ĐK":15}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(f'{student}{r[1]:<15}')


def save_students(students):
    """Phương thức lưu dữ liệu kiểu x ra database tương ứng"""
    for s in students:
        full_name_data = (s.full_name.first_name, s.full_name.mid_name, s.full_name.last_name)
        full_name_id = insert_full_name(full_name_data)
        address_data = (s.address.wards, s.address.district, s.address.city)
        address_id = insert_address(address_data)
        birth_date_data = (s.birth_date.day, s.birth_date.month, s.birth_date.year)
        birth_date_id = insert_birth_date(birth_date_data)
        student_data = (s.student_id, s.person_id, full_name_id,
                        address_id, birth_date_id, s.email, s.gpa, s.major)
        insert_student(student_data)


def save_subjects(subjects):
    for subject in subjects:
        data = (subject.subject_id, subject.subject_name, subject.credit)
        insert_subject(data)


def save_registers(registers):
    for r in registers:
        data = (r.register_id, r.student.student_id,
                r.subject.subject_id, r.register_time)
        insert_register(data)


def show_students(students):
    """Phương thức dùng để hiển thị danh sách sinh viên."""
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}'
    print(title)
    for student in students:
        print(student)


def show_subjects(subjects):
    """Phương thức dùng để hiển thị danh sách môn học."""
    title = f'{"Mã môn":15}{"Tên môn học":30}{"Số tín chỉ":15}'
    print(title)
    for subject in subjects:
        print(subject)


def show_registers(registers):
    """Phương thức dùng để hiển thị danh sách đăng ký."""
    title = f'{"Mã ĐK":10}{"Mã sinh viên":15}{"Tên sinh viên":35}' \
            f'{"Mã môn học":15}{"Tên môn học":35}{"Thời gian đăng ký":30}'
    print(title)
    for r in registers:
        print(r)


def find_registed_subject():
    """Phương thức dùng để tìm môn học đã đăng ký."""
    student_id = input('Nhập mã sinh viên: ').strip().upper()
    try:
        if is_student_id_valid(student_id):
            result = []
            data = find_subject_by_student_id(student_id)
            for d in data:
                result.append(Subject(d[0], d[1], d[2]))
            if len(result) > 0:
                print(f'==> Danh sách môn học sinh viên mã {student_id} đã đăng ký: ')
                show_subjects(result)
            else:
                print(f'==> Sinh viên mã {student_id} không đăng ký môn học nào.')
    except StudentIdError as e:
        print(e)


def find_student_by_subject(students):
    """Phương thức tìm sinh viên đăng ký theo môn học."""
    subject_id = int(input('Nhập mã môn học(số nguyên 4 chữ số): '))
    try:
        if is_subject_id_valid(f'{subject_id}'):
            result = []
            data = find_student_by_subject_id(subject_id)
            for d in data:
                student = find_student_by_id(students, d[0])
                result.append(student)
            if len(result) > 0:
                print(f'==> Danh sách sinh viên đã đăng ký môn học mã {subject_id}: ')
                show_students(result)
            else:
                print(f'==> Môn học mã {subject_id} không có sinh viên đăng ký.')
    except SubjectIdError as e:
        print(e)


def get_list_item(data, key):
    """Phương thức tìm value theo key cho trước"""
    for d in data:
        if d.subject_id == key:
            return d
    return None


def print_statistic(order_dct, subjects):
    """Phương thức hiển thị kết quả thống kê."""
    print(f'{"Tên môn học":35}{"Số SV đăng ký":10}')
    for item in order_dct.keys():
        subject = get_list_item(subjects, item)
        print(f'{subject.subject_name:35}: {order_dct[item]:<10}')


def statistics_by_subject():
    """Phương thức thống kê sv đăng ký theo môn học."""
    result = stat_register_by_subject()
    print(f'{"Mã môn học":15}{"Tên môn học":35}{"Số SV đăng ký":15}')
    for item in result:
        print(f'{item[0]:<15}{item[1]:35}{item[2]:<15}')


def earliest_register(registers):
    """Phương thức tìm sinh viên đăng ký sớm nhất."""
    result = []
    record = find_earliest()
    for r in record:
        register = find_register_by_id(registers, r[0])
        result.append(register)
    print('==> Các bản đăng ký sớm nhất: ')
    show_registers(result)


def latest_register(registers):
    """Phương thức tìm sinh viên đăng ký muộn nhất."""
    result = []
    record = find_latest()
    for r in record:
        register = find_register_by_id(registers, r[0])
        result.append(register)
    print('==> Các bản đăng ký muộn nhất: ')
    show_registers(result)


def stat_student_by_city():
    """
    Hàm thống kê lượng sv theo từng thành phố.
    :return: None
    """
    result = stat_number_of_student_by_city()
    print(f'{"Thành phố":25}{"Lượng SV":15}')
    for r in result:
        print(f'{r[0]:25}{r[1]:<15}')


def update_student_auto_id(students):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for student in students:
        id_number = int(student.student_id[2:])
        if id_number > max_id:
            max_id = id_number
    Student.AUTO_ID = max_id + 1


def update_subject_auto_id(subjects):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for subject in subjects:
        if subject.subject_id > max_id:
            max_id = subject.subject_id
    Subject.AUTO_ID = max_id + 1


def update_register_auto_id(registers):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for reg in registers:
        if reg.register_id > max_id:
            max_id = reg.register_id
    Register.AUTO_ID = max_id + 1


def top5_register_earliest(students):
    """
    Hàm thống kê top 5 sv đăng ký sớm nhất.
    :param students: danh sách sinh viên
    :return: None
    """
    result = find_top5_earliest()
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}{"Thời gian ĐK":35}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(f'{student}{r[1]}')


def top5_register_latest(students):
    """
        Hàm thống kê top 5 sv đăng ký muộn nhất.
        :param students: danh sách sinh viên
        :return: None
        """
    result = find_top5_latest()
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}{"Thời gian ĐK":35}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(f'{student}{r[1]}')


def update_subject_credit(subjects):
    """Phương thức cập nhật số tín chỉ cho môn học theo mã môn cho trước."""
    subject_id = input('Mã môn học cần cập nhật: ')
    try:
        if is_subject_id_valid(subject_id):
            subject = find_subject_by_id(subjects, int(subject_id))
            if subject is not None:
                credit = input('Số tín chỉ thay thế(số nguyên dương): ')
                try:
                    if is_credit_valid(credit):
                        subject.credit = credit
                        print('==> Cập nhật số tín chỉ cho môn học thành công! <==')
                except CreditError as e:
                    print(e)
    except SubjectIdError as e:
        print(e)


def find_register_by_id(registers, reg_id):
    """Phương thức tìm bản đăng ký theo mã đk."""
    for r in registers:
        if r.register_id == reg_id:
            return r
    return None


def stat_good_students():
    data = find_good_student()
    students = []
    list_bith_date = get_all_birth_date()
    list_full_name = get_all_full_name()
    list_address = get_all_address()
    for s in data:
        name = find_full_name_by_id(list_full_name, s[2])
        fname = FullName(name[0], name[1], name[3], name[2])
        addr = find_address_by_id(list_address, s[3])
        address = Address(addr[0], addr[3], addr[1], addr[2])
        dob = find_birth_date_by_id(list_bith_date, s[4])
        birth_date = BirthDate(dob[0], dob[1], dob[2], dob[3])
        students.append(Student(s[1], fname, birth_date,
                                address, s[0], s[5], s[6], s[7]))
    print('==> Danh sách sinh viên loại giỏi trở lên: ')
    show_students(students)
