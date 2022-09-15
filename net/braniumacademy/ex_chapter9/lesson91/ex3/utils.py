import copy
from datetime import datetime

from student import Student
from subject import Subject
from teacher import Teacher
from course import Course
from transcript import Transcript
from filters import *


def create_student():
    """Phương thức nhập và tạo mới đối tượng sinh viên."""
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    full_name = input('Họ tên đầy đủ: ')
    if not is_name_valid(full_name):
        raise ValueError(f'Họ tên không hợp lệ: {full_name}.'
                         f'Họ tên chỉ được chứa chữ cái và khoảng trắng.')
    birth_date = input('Ngày sinh: ')
    if not is_birth_date_valid(birth_date):
        raise ValueError(f'Ngày sinh không đúng định dạng: {birth_date}. '
                         f'Định dạng đúng: 15/10/2000.')
    major = input('Chuyên ngành: ')
    gpa = input('Điểm TB: ')
    if not is_gpa_valid(gpa):
        raise ValueError(f'Điểm gpa không hợp lệ: {gpa}. '
                         f'Điểm gpa hợp lệ trong khoảng [0.0, 4.0]')
    return Student(pid, full_name, birth_date, None, major, float(gpa))


def create_teacher():
    """Phương thức nhập thông tin và tạo mới đối tượng giảng viên."""
    print('============ Nhập thông tin giảng viên ============')
    pid = input('Số CMND/CCCD: ')
    full_name = input('Họ tên đầy đủ: ')
    if not is_name_valid(full_name):
        raise ValueError(f'Họ tên không hợp lệ: {full_name}. '
                         f'Họ tên chỉ được chứa chữ cái và khoảng trắng.')
    birth_date = input('Ngày sinh: ')
    if not is_birth_date_valid(birth_date):
        raise ValueError(f'Ngày sinh không đúng định dạng: {birth_date}. '
                         f'Định dạng đúng: 15/10/2000.')
    expertise = input('Chuyên môn: ')
    salary = input('Mức lương: ')
    if not is_salary_valid(salary):
        raise ValueError(f'Mức lương không hợp lệ: {salary}. '
                         f'Lương phải là số nguyên.')
    return Teacher(pid, full_name, birth_date, None, int(salary), expertise)


def create_subject():
    """Phương thức nhập thông tin và tạo mới đối tượng môn học."""
    name = input('Tên môn học: ')
    credit = input('Số tín chỉ: ')
    if not is_credit_valid(credit):
        raise ValueError(f'Số tín chỉ không hợp lệ: {credit}. '
                         f'Giá trị hợp lệ từ 1-15.')
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
        if e.teacher_id.lower() == teacher_id.lower():
            return e
    return None


def find_subject(subjects, subject_id):
    """Phương thức tìm môn học trong danh sách môn học cho trước."""
    for e in subjects:
        if e.subject_id == subject_id:
            return e
    return None


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
        if t.teacher_id.lower() == teacher_id.lower():
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
        if s.student_id.lower() == student_id.lower():
            return s
    return None


def read_transcripts_from_file(students):
    """This method read and return transcript data in the file."""
    transcripts = []
    with open('TRANSCRIPT.DAT', encoding='UTF-8') as reader:
        tran_id = reader.readline().strip()
        while tran_id != '':
            course_id = reader.readline().strip()
            student = find_student_by_id(students, reader.readline().strip())
            tran = Transcript(int(tran_id), course_id,
                              student, float(reader.readline().strip()),
                              reader.readline().strip())
            transcripts.append(tran)
            tran_id = reader.readline().strip()
    return transcripts


def fill_transcript_for_courses(courses, transcripts):
    """This method assign transcripts into courses."""
    for i in range(len(courses)):
        for j in range(len(transcripts)):
            if courses[i].course_id == transcripts[j].course_id:
                courses[i].transcripts.append(transcripts[j])
    return transcripts


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
    try:
        if is_course_id_valid(course_id):
            start_gpa = float(input('Điểm gpa tối thiểu: '))
            try:
                if is_gpa_valid(f'{start_gpa}'):
                    end_gpa = float(input('Điểm gpa tối đa: '))
                    try:
                        if is_gpa_valid(f'{end_gpa}'):
                            index = courses.index(Course(cid=course_id.upper()))
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
                    except GpaError as e:
                        print(e)
            except GpaError as e:
                print(e)
    except CourseIdError as e:
        print(e)


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


def sort_course(courses):
    """This method sort transcripts in a given course."""
    course_id = input('Mã lớp cần sắp xếp: ')
    try:
        if is_course_id_valid(course_id):
            for i in range(len(courses)):
                if courses[i].course_id == course_id.strip().upper():
                    courses[i].transcripts.sort(key=lambda x: -x.gpa)
                    show_transcripts([courses[i]])
                    break
    except CourseIdError as e:
        print(e)


def find_course_by_id(courses, course_id):
    """This method find and return course by id."""
    if len(courses) == 0:
        return None
    index = courses.index(Course(cid=course_id.upper()))
    if index >= 0:
        return courses[index]
    else:
        return None  # if not found


def stat_student_in_course(courses):
    """This method statistic number of student in each level from highest to lowest."""
    course_id = input('Mã lớp cần xem thống kê: ')
    try:
        if is_course_id_valid(course_id):
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
    except CourseIdError as e:
        print(e)


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
    subject_id = input("Mã môn học: ")
    if not is_subject_id_valid(subject_id):
        raise ValueError(f'Mã môn học không đúng: {subject_id}. '
                         f'Ví dụ mã hợp lệ: 1005.')
    teacher_id = input('Mã giảng viên: ')
    if not is_teacher_id_valid(teacher_id):
        raise ValueError(f'Mã giảng viên không đúng: {teacher_id}. '
                         f'Ví dụ mã hợp lệ: GV1005')
    subject = find_subject_by_id(subjects, int(subject_id))
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
    if not is_course_id_valid(course_id):
        raise ValueError(f'Mã lớp không đúng: {course_id}. '
                         f'Ví dụ về mã lớp hợp lệ: C102.')
    course = find_course_by_id(courses, course_id)
    if course is None:
        print('==> Lớp học không tồn tại. <==')
        return None
    student_id = input('Mã sinh viên: ')
    if not is_student_id_valid(student_id):
        raise ValueError(f'Mã sinh viên không đúng: {student_id}. '
                         f'Ví dụ mã hợp lệ: SV1005')
    student = find_student_by_id(students, student_id)
    if student is None:
        print('==> Sinh viên không tồn tại. <==')
        return None
    tran = Transcript()
    tran.transcript_id = 0
    tran.student = student
    tran.course_id = course_id
    gpa = input('Điểm Gpa hệ 4: ')
    if not is_gpa_valid(gpa):
        raise ValueError(f'Điểm không hợp lệ: {gpa}. '
                         f'Ví dụ điểm hợp lệ: 3.25.')
    tran.gpa = float(gpa)
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


def update_student_gpa(students):
    """This method update gpa of given student."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    try:
        if is_student_id_valid(student_id):
            student = find_student_by_id(students, student_id)
            if student is not None:
                gpa = input('Điểm gpa thay thế: ')
                try:
                    if is_gpa_valid(gpa):
                        student.gpa = float(gpa)
                        print('==> Cập nhật điểm thành công! <==')
                except GpaError as e:
                    print(e)
            else:
                print('==> Sinh viên không tồn tại <==')
    except StudentIdError as e:
        print(e)


def update_credit(subjects):
    """This method update credit for given subject."""
    subject_id = input('Mã môn học: ')
    try:
        if is_subject_id_valid(subject_id):
            subject = find_subject_by_id(subjects, int(subject_id))
            if subject is not None:
                credit = input('Số tín chỉ thay thế: ')
                try:
                    if is_credit_valid(credit):
                        subject.credit = int(credit)
                        print('==> Cập nhật số tín chỉ thành công! <==')
                except CreditError as e:
                    print(e)
            else:
                print('==> Môn học cần update không tồn tại. <==')
    except SubjectIdError as e:
        print(e)


def update_salary(teachers):
    """This method update salary for given teacher."""
    teacher_id = input('Mã giảng viên cần cập nhật: ')
    try:
        if is_teacher_id_valid(teacher_id):
            teacher = find_teacher_by_id(teachers, teacher_id)
            if teacher is not None:
                salary = input('Mức lương thay thế: ')
                try:
                    if is_salary_valid(salary):
                        teacher.salary = int(salary)
                        print('==> Cập nhật mức lương thành công! <==')
                except SalaryError as e:
                    print(e)
            else:
                print('==> Giảng viên này không tồn tại! <==')
    except TeacherIdError as e:
        print(e)


def remove_subject_by_id(subjects):
    """This method remove a subject by id."""
    if len(subjects) == 0:
        print('==> Danh sách môn học trống <==')
        return
    subject_id = input('Mã môn học cần xóa: ')
    try:
        if is_subject_id_valid(subject_id):
            subject = find_subject_by_id(subjects, int(subject_id))
            if subject is not None:
                confirm = input('Bạn có chắc chắn mốn xóa không?(Y/N) ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    subjects.remove(subject)
                    print('==> Xóa môn học thành công <==')
            else:
                print('==> Môn học này không tồn tại! <==')
    except SubjectIdError as e:
        print(e)


def remove_student_by_id(students):
    """This method remove a student by id."""
    if len(students) == 0:
        print('==> Danh sách sinh viên trống <==')
        return
    student_id = input('Mã sinh viên cần xóa: ')
    try:
        if is_student_id_valid(student_id):
            student = find_student_by_id(students, student_id)
            if student is not None:
                confirm = input('Bạn có chắc chắn mốn xóa không?(Y/N) ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    students.remove(student)
                    print('==> Xóa sinh viên thành công <==')
            else:
                print('==> Sinh viên này không tồn tại! <==')
    except StudentIdError as e:
        print(e)


def remove_teacher_by_id(teachers):
    """This method remove a teacher by id."""
    if len(teachers) == 0:
        print('==> Danh sách giảng viên trống <==')
        return
    teacher_id = input('Mã giảng viên cần xóa: ')
    try:
        if is_teacher_id_valid(teacher_id):
            teacher = find_teacher_by_id(teachers, teacher_id)
            if teacher is not None:
                confirm = input('Bạn có chắc chắn mốn xóa không?(Y/N) ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    teachers.remove(teacher)
                    print('==> Xóa giảng viên thành công <==')
            else:
                print('==> Giảng viên này không tồn tại! <==')
    except TeacherIdError as e:
        print(e)


def remove_course_by_id(courses):
    """This method remove a course by id."""
    if len(courses) == 0:
        print('==> Danh sách lơ học trống <==')
        return
    course_id = input('Mã lớp học cần xóa: ')
    try:
        if is_course_id_valid(course_id):
            course = find_course_by_id(courses, course_id)
            if course is not None:
                confirm = input('Bạn có chắc chắn mốn xóa không?(Y/N) ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    courses.remove(course)
                    print('==> Xóa lớp học thành công <==')
            else:
                print('==> Lớp học này không tồn tại! <==')
    except CourseIdError as e:
        print(e)


def find_transcript_by_id(transcripts, transcript_id):
    """This method find and return transcript by id."""
    for t in transcripts:
        if t.transcript_id == transcript_id:
            return t
    return None  # if not found


def remove_transcript_by_id(transcripts, courses):
    """This method remove a transcript by id."""
    if len(transcripts) == 0:
        print('==> Danh sách bảng điểm trống <==')
        return
    transcript_id = input('Mã bảng điểm cần xóa: ')
    try:
        if is_transcript_id_valid(transcript_id):
            transcript = find_transcript_by_id(transcripts, int(transcript_id))
            if transcript is not None:
                confirm = input('Bạn có chắc chắn mốn xóa không?(Y/N) ')
                if confirm.lower() == 'y' or confirm.lower() == 'yes':
                    transcripts.remove(transcript)
                    # xóa cả trong danh sách lớp để đảm bảo không sót lại dữ liệu thừa
                    for c in courses:
                        for t in c.transcripts:
                            if t == transcript:
                                c.transcripts.remove(t)
                    print('==> Xóa bảng điểm thành công <==')
            else:
                print('==> Bảng điểm này không tồn tại! <==')
    except TranscriptIdError as e:
        print(e)
