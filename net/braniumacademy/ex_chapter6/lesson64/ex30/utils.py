import copy
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
    first = input('Tên: ')
    birth_date = input('Ngày sinh: ')
    major = input('Chuyên ngành: ')
    gpa = float(input('Điểm TB: '))
    full_name = FullName(first, mid, last)
    return Student(pid, full_name, birth_date, None, major, gpa)


def create_teacher():
    """Phương thức nhập thông tin và tạo mới đối tượng giảng viên."""
    print('============ Nhập thông tin giảng viên ============')
    pid = input('Số CMND/CCCD: ')
    last = input('Họ: ')
    mid = input('Đệm: ')
    first = input('Tên: ')
    birth_date = input('Ngày sinh: ')
    expertise = input('Chuyên môn: ')
    salary = float(input('Mức lương: '))
    full_name = FullName(first, mid, last)
    return Teacher(pid, full_name, birth_date, None, salary, expertise)


def create_subject():
    """Phương thức nhập thông tin và tạo mới đối tượng môn học."""
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(0, name, credit)


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
        for course in courses:
            print(course)
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
    """This method print transcript on screen."""
    for course in courses:
        if len(course.transcripts) == 0:  # nếu danh sách sv rỗng -> bỏ qua
            continue
        print('================================'
              '=====================================')
        print(f'==> Mã lớp: {course.course_id}')
        print(f'==> Tên lớp: {course.name}')
        print(f'==> Phòng học: {course.room}')
        print(f'==> Môn học: {course.subject.name}')
        print(f'==> Giảng viên: {course.teacher.full_name}')
        print(f'==> Số lượng sinh viên: {len(course.transcripts)}')
        print('==> Danh sách bảng điểm của lớp: ')
        print(f'{"Mã BĐ":10}{"Mã SV":10}'
              f'{"Họ tên SV":30}{"Điểm Gpa":10}{"Học lực":15}')
        for t in course.transcripts:
            print(t)


def find_max_gpa(courses):
    """This method find and return max gpa of students."""
    max_gpa = 0.0
    for course in courses:
        for t in course.transcripts:
            if t.gpa > max_gpa:
                max_gpa = t.gpa
    return max_gpa


def listed_student_with_max_gpa(courses):
    """This method find and show on screen student with max gpa."""
    max_gpa = find_max_gpa(courses)
    result = copy.deepcopy(courses)
    for course in result:
        course.transcripts.clear()
    for index in range(len(courses)):
        for t in courses[index].transcripts:
            if t.gpa == max_gpa:
                result[index].transcripts.append(t)
    show_transcripts(result)


def find_student_in_course(courses):
    """This method find and display student with given gpa on screen."""
    course_id = input('Mã lớp cần tìm: ')
    start_gpa = float(input('Điểm gpa tối thiểu: '))
    end_gpa = float(input('Điểm gpa tối đa: '))
    index = courses.index(Course(cid=course_id))
    if index >= 0:
        target_course = courses[index]
        course = copy.deepcopy(target_course)
        if course is not None:
            result = []
            for t in course.transcripts:
                if start_gpa <= t.gpa <= end_gpa:
                    result.append(t)
            course.transcripts = result
            show_transcripts([course])
        else:
            print('==> Không tồn tại lớp học cần tìm. <==')
    else:
        print('==> Mã lớp không đúng! <==')


def find_max_gpa_by_subject(courses, subject):
    """This method find max gpa of student in courses by subject."""
    max_gpa = 0.0
    for course in courses:
        if course.subject == subject:
            for t in course.transcripts:
                if t.gpa > max_gpa:
                    max_gpa = t.gpa
    return max_gpa


def is_subject_have_couse(courses, subject):
    """This method check wether a given subject has any course or not."""
    for course in courses:
        if course.subject == subject:
            return True
    return False


def find_highest_gpa_by_subject(subjects, courses):
    """This method find and display students have max gpa for each subject on screen."""
    for s in subjects:
        if is_subject_have_couse(courses, s):
            # tìm điểm Gpa lớn nhất của môn học
            max_gpa = find_max_gpa_by_subject(courses, s)
            result = []
            for course in courses:
                if course.subject == s and len(course.transcripts) > 0:
                    for t in course.transcripts:
                        if t.gpa == max_gpa:
                            result.append(t.student)
            print(f'==> Mã môn: {s.subject_id}')
            print(f'==> Tên môn: {s.name}')
            print(f'==> Số tín: {s.credit}')
            print(f'==> Điểm cao nhất: {max_gpa}')
            if len(result) == 0:
                print('==> Môn học này không có sinh viên nào đăng ký. <==')
            else:
                print('==> Danh sac sinh viên có điểm cao nhất: ')
                show_students(result)


def find_course_by_id(courses, course_id):
    """This method find and return course by id."""
    if len(courses) == 0:
        return None
    index = courses.index(Course(cid=course_id))
    if index >= 0:
        return courses[index]
    else:
        return None  # if not found


def stat_student_in_course(courses):
    """This method statistic number of student in each level from highest to lowest."""
    course_id = input('Mã lớp cần xem thống kê: ')
    print('============================================')
    course = find_course_by_id(courses, course_id)
    my_dict = {
        "Xuất sắc": 0,
        "Giỏi": 0,
        "Khá": 0,
        "Trung bình": 0,
        "Yếu": 0
    }
    for t in course.transcripts:
        if t.capacity == "Xuất sắc":
            my_dict["Xuất sắc"] += 1
        elif t.capacity == "Giỏi":
            my_dict["Giỏi"] += 1
        elif t.capacity == "Khá":
            my_dict["Khá"] += 1
        elif t.capacity == "Trung bình":
            my_dict["Trung bình"] += 1
        elif t.capacity == "Yếu":
            my_dict["Yếu"] += 1
    print(f'Mã lớp học: {course.course_id}')
    print(f'Tên lớp học: {course.name}')
    print(f'Môn học: {course.subject.name}')
    print(f'Phòng học: {course.room}')
    print(f'Số lượng SV: {len(course.transcripts)}')
    print('==> Kết quả thống kê: ')
    print(f'{"Học lực":15}: {"Số lượng":10}')
    for key, value in my_dict.items():
        print(f'{key:15}: {value:<10}')


def stat_student_by_subjects(subjects, courses):
    """This method statistic number of very good and excillent student in each subject."""
    print('============================================')
    for s in subjects:
        num_of_student = 0
        if is_subject_have_couse(courses, s):
            for course in courses:
                if course.subject == s and len(course.transcripts) > 0:
                    for t in course.transcripts:
                        if t.gpa >= 3.2:  # find all student with gpa >= 3.2
                            num_of_student += 1
        print(f'==> Mã môn: {s.subject_id}')
        print(f'==> Tên môn: {s.name}')
        print(f'==> Số tín: {s.credit}')
        print(f'==> Số sv giỏi và xuất sắc: {num_of_student}')
        print('============================================')


def create_new_course(subjects, teachers):
    """This method create and return a new course."""
    course_name = input("Tên lớp: ")
    subject_id = int(input("Mã môn học: "))
    teacher_id = input('Mã giảng viên: ')
    subject = find_subject_by_id(subjects, subject_id)
    teacher = find_teacher_by_id(teachers, teacher_id)
    if subject is None:
        print('==> Môn học không tồn tại. <==')
        return None
    if teacher is None:
        print('==> Giảng viên không tồn tại. <==')
        return None
    room = input('Tên phòng học: ')
    return Course(cid='', name=course_name,
                  subject=subject, teacher=teacher, room=room)


def create_new_transcript(courses, students):
    """This method create and return a transcript."""
    course_id = input('Mã lớp: ')
    course = find_course_by_id(courses, course_id)
    if course is None:
        print('==> Lớp học không tồn tại. <==')
        return None
    student_id = input('Mã sinh viên: ')
    student = find_student_by_id(students, student_id)
    if student is None:
        print('==> Sinh viên không tồn tại. <==')
        return None
    tran = Transcript()
    tran.transcript_id = 0
    tran.student = student
    tran.course_id = course_id
    tran.gpa = float(input('Điểm Gpa hệ 4: '))
    tran.calculate_capacity()
    course.transcripts.append(tran)


def update_course_auto_id(courses):
    """This method update auto id of course."""
    max_id = 0
    for c in courses:
        number = int(c.course_id[1:])
        if number > max_id:
            max_id = number
    Course.AUTO_ID = max_id + 1


def update_subject_auto_id(subjects):
    """This method update auto id of subject."""
    max_id = 0
    for s in subjects:
        if s.subject_id > max_id:
            max_id = s.subject_id
    Subject.AUTO_ID = max_id + 1


def update_transcript_auto_id(courses):
    """This method update auto id of subject."""
    max_id = 0
    for c in courses:
        for t in c.transcripts:
            if t.transcript_id > max_id:
                max_id = t.transcript_id
    Transcript.AUTO_ID = max_id + 1


def update_teacher_auto_id(teachers):
    """This method update auto id of teacher."""
    max_id = 0
    for t in teachers:
        number = int(t.teacher_id[2:])
        if number > max_id:
            max_id = number
    Teacher.AUTO_ID = max_id + 1


def update_student_auto_id(students):
    """This method update auto id of student."""
    max_id = 0
    for s in students:
        number = int(s.student_id[2:])
        if number > max_id:
            max_id = number
    Student.AUTO_ID = max_id + 1


def write_data_to_file(data, file_name):
    """This method write given data to given text file."""
    with open(file_name, 'w', encoding='UTF-8') as writer:
        for item in data:
            writer.write(item.output_data_format())
