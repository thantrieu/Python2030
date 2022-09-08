from person import FullName
from student import Student
from subject import Subject
from teacher import Teacher
from course import Course


def create_student():
    """Phương thức nhập và tạo mới đối tượng sinh viên."""
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    last = input('Họ: ')
    mid = input('Đệm: ')
    first = input('Name: ')
    birth_date = input('Ngày sinh: ')
    major = input('Chuyên ngành: ')
    gpa = float(input('Điểm TB: '))
    full_name = FullName(first, mid, last)
    return Student(pid, full_name, birth_date, gpa, major)


def create_teacher():
    """Phương thức nhập thông tin và tạo mới đối tượng giảng viên."""
    print('============ Nhập thông tin giảng viên ============')
    pid = input('Số CMND/CCCD: ')
    last = input('Họ: ')
    mid = input('Đệm: ')
    first = input('Name: ')
    birth_date = input('Ngày sinh: ')
    expertise = input('Chuyên môn: ')
    salary = float(input('Mức lương: '))
    full_name = FullName(first, mid, last)
    return Teacher(pid, full_name, birth_date, None, salary, expertise)


def create_subject():
    """Phương thức nhập thông tin và tạo mới đối tượng môn học."""
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(name, credit)


def show_students(students):
    """Phương thức hiển thị thông tin sinh viên."""
    print('==> Danh sách sinh viên:')
    print(f'{"CMND/CC":15}{"Họ và tên":30}{"Ngày sinh":15}'
          f'{"Mã SV":15}{"Điểm TB":15}{"C.Ngành":15}')
    for e in students:
        print(e)


def show_teacher(teachers):
    """Phương thức hiển thị thông tin giảng viên."""
    print('==> Danh sách giảng viên <==')
    print(f'{"CMND/CC":15}{"Họ và tên":30}{"Ngày sinh":15}'
          f'{"Mã GV":15}{"Mức lương":15}{"Chuyên môn":25}')
    for teacher in teachers:
        print(teacher)


def show_subjects(subjects):
    """Phương thức hiển thị danh sách môn học."""
    print('==> Danh sách môn học:')
    print(f'{"Mã môn":15}{"Tên môn":35}{"Số tín":<15}')
    for s in subjects:
        print(s)


def find_teacher(teachers, teacher_id):
    """Phương thức tìm giảng viên trong danh sách giảng viên cho trước."""
    for e in teachers:
        if e.teacher_id == teacher_id:
            return e
    return None


def find_subject(subjects, subject_id):
    """Phương thức tìm môn học trong danh sách môn học cho trước."""
    for e in subjects:
        if e.subject_id == subject_id:
            return e
    return None


def create_course(subjects, mteachers):
    """Phương thức tạo mới một lớp học phần."""
    teacher_id = input('Mã giảng viên: ')
    target_teacher = find_teacher(mteachers, teacher_id)
    subject_id = input('Mã môn học: ')
    target_subject = find_subject(subjects, subject_id)
    room = input('Phòng học: ')
    return Course('', target_subject, target_teacher, room)


def show_course(courses):
    """Phương thức hiển thị danh sách các lớp học phần."""
    print('==> Danh sách các lớp học phần: <==')
    print(f'{"Mã lớp":10}{"Mã môn":10}{"Tên môn học":30}'
          f'{"Mã GV":10}{"Tên giảng viên":30}{"Phòng học":10}')
    for c in courses:
        print(c)


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


def read_teachers_from_file():
    """Phương thức đọc thông tin giảng viên từ file."""
    teachers = []
    with open('LECTURER.DAT', encoding='UTF-8') as teacher_reader:
        tid = teacher_reader.readline().strip()
        while tid != '':
            fname = teacher_reader.readline().strip()
            birth_date = teacher_reader.readline().strip()
            teacher_id = teacher_reader.readline().strip()
            salary = int(teacher_reader.readline().strip())
            major = teacher_reader.readline().strip()
            teachers.append(Teacher(tid, fname, birth_date, teacher_id, salary, major))
            tid = teacher_reader.readline().strip()
    return teachers


def read_subject_from_file():
    """Phương thức đọc thông tin môn học từ file."""
    subjects = []
    with open('SUBJECT.DAT', encoding='UTF-8') as subject_reader:
        subject_id = subject_reader.readline().strip()
        while subject_id != '':
            name = subject_reader.readline().strip()
            credit = int(subject_reader.readline().strip())
            subjects.append(Subject(int(subject_id), name, credit))
            subject_id = subject_reader.readline().strip()
    return subjects
