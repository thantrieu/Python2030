import re

from register import Register
from subject import Subject
from student import Student


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        return False
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            return False
    return True


def is_person_id_valid(person_id):
    """
        Phương thức kiểm tra xem mã số CMND/CCCD có hợp lệ không.
        Mã hợp lệ nếu chỉ chứa chữ cái và số.
    """
    if len(person_id.strip()) == 0:  # nếu chuỗi rỗng -> id ko hợp lệ
        return False
    if not person_id.isalnum():  # nếu số cmnd/cccd có kí tự khác số và chữ cái
        return False  # mã k hợp lệ
    return True


def is_birth_date_valid(birth_date):
    """Phương thức kiểm tra xem ngày sinh có hợp lệ không."""
    if len(birth_date.strip()) < 10:
        return False
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    return False


def is_gpa_valid(gpa_str):
    """Phương thức kiểm tra xem giá trị gpa có hợp lệ không."""
    if len(gpa_str.strip()) == 0:
        return False
    pattern = '^\\d.\\d{1,2}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, gpa_str):
        return True
    else:
        return False


def is_credit_valid(credit_str):
    """Phương thức kiểm tra số tín chỉ có hợp lệ không."""
    if len(credit_str.strip()) == 0:
        return False
    if credit_str.isdigit():
        return True
    return False


def create_student():
    """Phương thức tạo mới thông tin sv."""
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    name = input('Họ và tên: ')
    birth_date = input('Ngày sinh: ')
    major = input('Chuyên ngành: ')
    gpa = input('Điểm TB: ')
    return Student(pid, name, None, birth_date, gpa, major)


def read_students_from_file():
    """Phương thức đọc thông tin sv từ file."""
    students = []
    with open('STUDENT.DAT', encoding='UTF-8') as student_reader:
        pid = student_reader.readline().strip()
        while pid != '':
            fname = student_reader.readline().strip()
            birth_date = student_reader.readline().strip()
            student_id = student_reader.readline().strip()
            gpa = student_reader.readline().strip()
            major = student_reader.readline().strip()
            students.append(Student(pid, fname, birth_date, student_id, gpa, major))
            pid = student_reader.readline().strip()
    return students


def create_subject():
    """Phương thức tạo mới môn học."""
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(None, name, credit)


def read_subject_from_file():
    """Phương thức đọc thông tin môn học từ file."""
    subjects = []
    with open('SUBJECT.DAT', encoding='UTF-8') as subject_reader:
        subject_id = subject_reader.readline().strip()
        while subject_id != '':
            name = subject_reader.readline().strip()
            credit = int(subject_reader.readline().strip())
            subjects.append(Subject(subject_id, name, credit))
            subject_id = subject_reader.readline().strip()
    return subjects


def find_student_by_id(students, student_id):
    """Phương thức tìm sinh viên theo mã sinh viên."""
    for s in students:
        if s.student_id == student_id:
            return s
    return None  # nếu k tim thấy, trả về None


def find_subject_by_id(subjects, subject_id):
    """Phương thức tìm môn học theo mã môn học."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None


def create_register(students, subjects):
    """Phương thức tạo thông tin đăng ký môn học của sv."""
    student_id = input('Mã sinh viên: ')
    subject_id = int(input('Mã môn học(số nguyên 4 chữ số): '))
    student = find_student_by_id(students, student_id)
    subject = find_subject_by_id(subjects, subject_id)
    if student is None:
        print(f'==> Sinh viên mã \'{student_id}\' không tồn tại.')
        return None
    if subject is None:
        print(f'==> Môn học mã \'{subject_id}\' không tồn tại.')
        return None
    return Register(0, None, student, subject)


def is_register_exist(mregisters, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in mregisters:
        if item == r:
            return True
    return False

