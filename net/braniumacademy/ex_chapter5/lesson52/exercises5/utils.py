from student import Student
from course import Course
from subject import Subject
from transcript import Transcript


def create_course(subjects):
    course_id = input("Mã lớp: ")
    course_name = input("Tên lớp: ")
    room = input("Phòng học: ")
    time = input("Giờ học: ")
    subject_id = input("Mã môn học: ")
    subject = get_subject_by_id(subjects, subject_id)
    return Course(id=course_id, name=course_name, room=room, time=time, subject=subject)


def get_subject_by_id(subjects, subject_id):
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None


def create_student():
    student_id = input("Mã sinh viên: ")
    last_name = input("Họ: ")
    mid_name = input("Đệm: ")
    first_name = input("Tên: ")
    address = input("Địa chỉ: ")
    email = input("Email: ")
    gender = input("Giới tính: ")
    faculty = input("Khoa: ")
    student = Student()
    student.student_id = student_id
    student.last_name = last_name
    student.first_name = first_name
    student.mid_name = mid_name
    student.gender = gender
    student.email = email
    student.address = address
    student.faculty = faculty
    return student


def create_subject():
    subject_id = input("Mã môn học: ")
    subject_name = input("Tên môn học: ")
    credit = int(input("Số tín chỉ: "))
    lesson = int(input("Số tiết học: "))
    test = int(input("Số bài kiểm tra: "))
    return Subject(sid=subject_id, name=subject_name,
                   credit=credit, lesson=lesson, test=test)


def find_student_by_id(students, student_id):
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def create_transcript(students):
    transcript_id = int(input("Mã bảng điểm: "))
    student_id = input("Mã sinh viên: ")
    student = find_student_by_id(students, student_id)
    grade1 = float(input("Điểm hệ số 1: "))
    grade2 = float(input("Điểm hệ số 2: "))
    grade3 = float(input("Điểm hệ số 3: "))
    return Transcript(tid=transcript_id,
                      grade1=grade1, grade2=grade2,
                      grade3=grade3, student=student)


def show_subjects(subjects):
    if len(subjects) > 0:
        title = f'{"Mã môn":15}{"Tên môn học":35}{"Số tín":15}{"Số tiết":15}{"Số bài KT":15}'
        print(title)
        for s in subjects:
            print(f'{s.subject_id:15}{s.name:35}{s.credit:<15}{s.lesson:<15}{s.test:<15}')
    else:
        print('==> Danh sách môn học rỗng <==')


def show_students(students):
    if len(students) > 0:
        title = f'{"Mã SV":15}{"Họ và tên":30}{"Địa chỉ":25}{"Email":25}{"Giới tính":15}{"Khoa":15}'
        print(title)
        for s in students:
            full_name = f'{s.last_name} {s.mid_name} {s.first_name}'
            print(f'{s.student_id:15}{full_name:30}{s.address:25}{s.email:25}{s.gender:15}{s.faculty:15}')
    else:
        print('==> Danh sách sinh viên rỗng. <==')
