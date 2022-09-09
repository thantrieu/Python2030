from datetime import datetime

from person import FullName
from student import Student
from subject import Subject
from teacher import Teacher
from course import Course
from transcript import Transcript


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
    if len(courses) > 0:
        print('==> Danh sách các lớp học phần: <==')
        print(f'{"Mã lớp":10}{"Tên lớp":20}{"Mã môn":10}{"Tên môn học":30}'
              f'{"Mã GV":10}{"Tên giảng viên":30}{"Phòng học":10}')
        for c in courses:
            print(c)
    else:
        print('==> Danh sách lớp học rỗng. <==')


def read_students_from_file():
    """Phương thức đọc thông tin sv từ file."""
    students = []
    with open('STUDENT.DAT', encoding='UTF-8') as reader:
        pid = reader.readline().strip()
        while pid != '':
            fname = reader.readline().strip()
            birth_date = datetime.strptime(reader.readline().strip(), '%d/%m/%Y')
            student_id = reader.readline().strip()
            gpa = float(reader.readline().strip())
            major = reader.readline().strip()
            students.append(Student(pid, fname, birth_date, student_id, major, gpa))
            pid = reader.readline().strip()
    return students


def read_teachers_from_file():
    """Phương thức đọc thông tin giảng viên từ file."""
    teachers = []
    with open('LECTURER.DAT', encoding='UTF-8') as reader:
        tid = reader.readline().strip()
        while tid != '':
            fname = reader.readline().strip()
            birth_date = reader.readline().strip()
            teacher_id = reader.readline().strip()
            salary = int(reader.readline().strip())
            major = reader.readline().strip()
            teachers.append(Teacher(tid, fname, birth_date, teacher_id, salary, major))
            tid = reader.readline().strip()
    return teachers


def read_subject_from_file():
    """Phương thức đọc thông tin môn học từ file."""
    subjects = []
    with open('SUBJECT.DAT', encoding='UTF-8') as reader:
        subject_id = reader.readline().strip()
        while subject_id != '':
            name = reader.readline().strip()
            credit = int(reader.readline().strip())
            subjects.append(Subject(int(subject_id), name, credit))
            subject_id = reader.readline().strip()
    return subjects


def find_teacher_by_id(teachers, teacher_id):
    """This method find and return teacher by id if exists."""
    for t in teachers:
        if t.teacher_id == teacher_id:
            return t
    return None  # in case result not found


def find_subject_by_id(subjects, subject_id):
    """This method find and return subject by id if exists."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None  # in case result not found


def read_course_from_file(teachers, subjects):
    """Phương thức đọc thông tin lớp học từ file."""
    courses = []
    with open('COURSE.DAT', encoding='UTF-8') as reader:
        cid = reader.readline().strip()
        while cid != '':
            name = reader.readline().strip()
            subject_id = int(reader.readline().strip())
            teacher_id = reader.readline().strip()
            teacher = find_teacher_by_id(teachers, teacher_id)
            subject = find_subject_by_id(subjects, subject_id)
            room = reader.readline().strip()
            courses.append(Course(cid, name, subject, teacher, room))
            cid = reader.readline().strip()
    return courses


def find_student_by_id(students, student_id):
    """This method find and return student by id if exists."""
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def read_transcripts_from_file(students):
    """This method read and return transcript data in the file."""
    transcripts = []
    with open('TRANSCRIPT.DAT', encoding='UTF-8') as reader:
        tran_id = reader.readline().strip()
        while tran_id != '':
            tran = Transcript()
            tran.transcript_id = int(tran_id)
            tran.course_id = reader.readline().strip()
            tran.student = find_student_by_id(students, reader.readline().strip())
            tran.gpa = float(reader.readline().strip())
            tran.capacity = reader.readline().strip()
            transcripts.append(tran)
            tran_id = reader.readline().strip()
    return transcripts


def fill_transcript_for_courses(courses, students):
    """This method fill transcript """
    transcripts = read_transcripts_from_file(students)
    for i in range(len(courses)):
        for j in range(len(transcripts)):
            if courses[i].course_id == transcripts[j].course_id:
                courses[i].transcripts.append(transcripts[j])


def show_transcripts(courses):
    for c in courses:
        print('================================'
              '=====================================')
        print(f'==> Mã lớp: {c.course_id}')
        print(f'==> Tên lớp: {c.name}')
        print(f'==> Phòng học: {c.room}')
        print(f'==> Môn học: {c.subject.name}')
        print(f'==> Giảng viên: {c.teacher.full_name}')
        print(f'==> Số lượng sinh viên: {len(c.transcripts)}')
        print('==> Danh sách bảng điểm của lớp: ')
        print(f'{"Mã BĐ":10}{"Mã SV":10}'
              f'{"Họ tên SV":30}{"Điểm Gpa":10}{"Học lực":15}')
        for t in c.transcripts:
            print(t)
