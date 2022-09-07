from student import Student
from course import Course
from subject import Subject
from transcript import Transcript


def find_subject_by_id(subjects, subject_id):
    """Find subject by subject id."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None


def create_course(subjects):
    """This method create and return a course."""
    if len(subjects) > 0:
        course = Course()
        course.course_id = input("Mã lớp: ")
        course.name = input("Tên lớp: ")
        course.room = input("Phòng học: ")
        course.time = input("Giờ học: ")
        subject_id = input("Mã môn học: ")
        subject = find_subject_by_id(subjects, subject_id)
        if subject is None:
            return None
        else:
            course.subject = subject
            return course
    else:
        print('==> Danh sách môn học rỗng. <==')
        return None


def create_student():
    student = Student()
    student.student_id = input("Mã sinh viên: ")
    student.last_name = input("Họ: ")
    student.mid_name = input("Đệm: ")
    student.first_name = input("Tên: ")
    student.address = input("Địa chỉ: ")
    student.email = input("Email: ")
    student.gender = input("Giới tính: ")
    student.faculty = input("Khoa: ")
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
        title = f'{"Mã môn":15}{"Tên môn học":35}' \
                f'{"Số tín":15}{"Số tiết":15}{"Số bài KT":15}'
        print(title)
        for s in subjects:
            print(f'{s.subject_id:15}{s.name:35}'
                  f'{s.credit:<15}{s.lesson:<15}{s.test:<15}')
    else:
        print('==> Danh sách môn học rỗng <==')


def show_students(students):
    if len(students) > 0:
        title = f'{"Mã SV":15}{"Họ và tên":30}' \
                f'{"Địa chỉ":25}{"Email":25}{"Giới tính":15}{"Khoa":15}'
        print(title)
        for s in students:
            full_name = f'{s.last_name} {s.mid_name} {s.first_name}'
            print(f'{s.student_id:15}{full_name:30}'
                  f'{s.address:25}{s.email:25}'
                  f'{s.gender:15}{s.faculty:15}')
    else:
        print('==> Danh sách sinh viên rỗng. <==')


def show_courses(courses):
    if len(courses) > 0:
        title = f'{"Mã lớp":15}{"Tên lớp":20}{"Phòng":15}' \
                f'{"Thời gian":15}{"Mã môn":15}' \
                f'{"Tên môn":25}{"Sĩ số":12}'
        print(title)
        for c in courses:
            print(f'{c.course_id:15}{c.name:20}'
                  f'{c.room:15}{c.time:15}'
                  f'{c.subject.subject_id:15}'
                  f'{c.subject.name:25}'
                  f'{len(c.transcripts):<12}')
    else:
        print('==> Danh sách lớp học rỗng. <==')
