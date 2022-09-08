import copy

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
    """This method create and return a student object."""
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
    """This method create and return a subject object."""
    subject_id = input("Mã môn học: ")
    subject_name = input("Tên môn học: ")
    credit = int(input("Số tín chỉ: "))
    lesson = int(input("Số tiết học: "))
    test = int(input("Số bài kiểm tra: "))
    return Subject(sid=subject_id, name=subject_name,
                   credit=credit, lesson=lesson, test=test)


def find_student_by_id(students, student_id):
    """This method find and return a student with given id if exists."""
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def create_transcript(transcripts, students):
    """This method create and return a transcript of a student. Return None if student is not available."""
    student_id = input("Mã sinh viên: ")
    student = find_student_by_id(students, student_id)
    if student is not None and not is_transcript_exists(transcripts, student_id):
        grade1 = float(input("Điểm hệ số 1: "))
        grade2 = float(input("Điểm hệ số 2: "))
        grade3 = float(input("Điểm hệ số 3: "))
        return Transcript(tid=0, grade1=grade1, grade2=grade2,
                          grade3=grade3, student=student)
    else:
        print('==> Sinh viên không tồn tại. Hoặc đã được nhập điểm trước đó. <==')
        return None


def find_course_by_id(courses, course_id):
    """This method find and return course by id."""
    if len(courses) == 0:
        return None
    for c in courses:
        if c.course_id == course_id:
            return c
    return None


def is_transcript_exists(transcripts, student_id):
    """This method check whether this student has transcript before."""
    for t in transcripts:
        if t.student.student_id == student_id:
            return True
    return False


def add_transcript_to_course(courses, students):
    """This method add transcript for course."""
    course_id = input('Mã lớp: ')
    course = find_course_by_id(courses, course_id)
    if course is None:
        print('==> Lớp học cần nhập bảng điểm không tồn tại. <==')
    else:
        tran = create_transcript(course.transcripts, students)
        # trong một lớp học thì bảng điểm của mỗi sinh viên chỉ được xuất hiện 1 lần
        if tran is not None:
            tran.calculate_gpa()
            course.transcripts.append(tran)
            print('==> Thêm bảng điểm cho sinh viên thành công! <==')
        else:
            print('==> Tạo bảng điểm thất bại. <==')


def show_subjects(subjects):
    """This method print subject on screen."""
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
    """This method print students on screen."""
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
    """This method print course on screen."""
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


def show_transcripts(courses):
    """This method print transcripts of each course on screen."""
    if len(courses) > 0:
        for c in courses:
            print('======================================='
                  '============================================')
            print(f'Mã lớp: {c.course_id}')
            print(f'Tên lớp: {c.name}')
            print(f'Số lượng SV: {len(c.transcripts)}')
            print('==> Bảng điểm chi tiết: ')
            print(f'{"Mã SV":15}{"Điểm hệ 1":15}{"Điểm hệ 2":15}'
                  f'{"Điểm hệ 3":15}{"Điểm TB":15}{"Học lực":15}')
            for tran in c.transcripts:
                print(f'{tran.student.student_id:15}{tran.grade1:<15.2f}{tran.grade2:<15.2f}'
                      f'{tran.grade3:<15.2f}{tran.gpa:<15.2f}{tran.capacity:15}')
    else:
        print('==> Danh sách lớp học trống. <==')


def find_capacity(courses):
    """This method calculate capacity for all student in courses."""
    if len(courses) > 0:
        for c in courses:
            for t in c.transcripts:
                t.calculate_capacity()
    else:
        print('==> Danh sách lớp học rỗng. <==')


def create_fake_students():
    """This method create and return fake students."""
    students = [Student('SV100', 'Long', 'Hoàng', 'Văn', 'longhoangshark@xmail.com', 'Hà Nội', 'Nam', 'CNTT'),
                Student('SV103', 'Oanh', 'Nguyễn', 'Hồng', 'hongoanhunin@xmail.com', 'Hồ Chí Minh', 'Nữ', 'CNTT'),
                Student('SV104', 'Nhung', 'Phạm', 'Thị Hồng', 'hongnhungcute@xmail.com', 'Hà Nội', 'Nữ', 'HTTT'),
                Student('SV105', 'Nhung', 'Lê', 'Hồng', 'hongnhunglele@xmail.com', 'Thái Bình', 'Nữ', 'HTTT'),
                Student('SV107', 'Nhung', 'Nguyễn', 'Thị Hồng', 'hongnhungahihi@xmail.com', 'Bắc Giang', 'Nữ', 'HTTT'),
                Student('SV109', 'Minh', 'Trần', 'Đức', 'ducminhbaboy@xmail.com', 'Bình Dương', 'Nam', 'CNTT')]
    return students


def create_fake_subjects():
    subjects = [Subject('SJ1000', 'Java', 3, 45, 4),
                Subject('SJ1001', 'C++', 3, 46, 5),
                Subject('SJ1002', 'C#', 4, 60, 5),
                Subject('SJ1003', 'NodeJS', 3, 45, 4),
                Subject('SJ1004', 'Android Java', 4, 60, 5),
                Subject('SJ1005', 'ASP.NET', 4, 60, 5),
                Subject('SJ1006', 'SQL', 3, 45, 5)]
    return subjects


def create_fake_couses(subjects):
    """This method create and return fake courses."""
    courses = [Course('C100', 'Java 1', 'A2-205', '14-16h', subjects[0]),
               Course('C101', 'Java 2', 'A2-205', '16-18h', subjects[0]),
               Course('C102', 'Android 1', 'A2-201', '10-12h', subjects[4]),
               Course('C103', 'Android 2', 'A2-105', '14-16h', subjects[4])]
    return courses


def create_fake_transcripts(courses, students):
    courses[0].transcripts.append(Transcript(0, students[0], 6, 9, 8))
    courses[0].transcripts.append(Transcript(0, students[1], 7, 9, 9))
    courses[0].transcripts.append(Transcript(0, students[2], 8, 9, 9.5))
    courses[0].transcripts.append(Transcript(0, students[3], 10, 8, 9))
    courses[0].transcripts.append(Transcript(0, students[4], 6, 7, 8))
    courses[0].transcripts.append(Transcript(0, students[5], 9, 9, 8.5))
    courses[1].transcripts.append(Transcript(0, students[0], 6, 9, 7))
    courses[1].transcripts.append(Transcript(0, students[1], 8, 9, 8))
    courses[1].transcripts.append(Transcript(0, students[2], 6.5, 9, 8))
    courses[2].transcripts.append(Transcript(0, students[3], 8, 9, 9.5))
    courses[2].transcripts.append(Transcript(0, students[1], 6, 9, 8))
    courses[2].transcripts.append(Transcript(0, students[0], 6, 9, 8))
    courses[3].transcripts.append(Transcript(0, students[1], 9, 9, 8.5))
    courses[3].transcripts.append(Transcript(0, students[2], 9, 9, 8.5))
    courses[3].transcripts.append(Transcript(0, students[3], 8, 9, 9))
    courses[3].transcripts.append(Transcript(0, students[0], 8, 9, 9.5))


def sort_transcripts(courses):
    """This method create rule for sorting transcripts."""
    for c in courses:
        c.transcripts.sort(key=lambda x: (-x.gpa, x.student.first_name))


def find_student_in_course(courses):
    """This method find student"""
    student_id = input('Mã sinh viên cần tìm: ')
    course_id = input('Mã lớp cần tìm: ')
    course = find_course_by_id(courses, course_id)
    if course is None:
        print('==> Lớp học cần tìm không tồn tại. <==')
    else:
        is_found = False
        for tran in course.transcripts:
            if tran.student.student_id == student_id:
                print(f'==> Sinh viên mã {student_id} CÓ trong lớp học mã lớp {course_id}')
                is_found = True
                break
        if not is_found:
            print(f'==> Sinh viên mã {student_id} KHÔNG có trong lớp học mã lớp {course_id}')


def find_student_with_max_gpa(courses):
    """This method find and show students have max gpa."""
    sort_transcripts(courses)
    max_gpa = -1  # giả định giá trị max_gpa k hợp lệ
    for c in courses:
        for t in c.transcripts:
            if t.gpa > max_gpa:
                max_gpa = t.gpa
                break
    # nếu giá trị mặc định không đổi -> không có sv nào đc nhập điểm vào bất kì danh sách lớp nào
    if max_gpa != -1:
        result = copy.deepcopy(courses)  # tạo bản sao của ds các lớp học
        for c in result:
            c.transcripts.clear()  # xóa hết các bản ghi về bảng điểm
        # thêm dữ liệu vào bảng điểm. Do bảng điểm gốc và copy là như nhau -> vị trí các lớp học là như nhau
        index = 0
        for course in courses:  # tìm các bảng điểm có điểm TB cao nhất
            for t in course.transcripts:
                if t.gpa == max_gpa:
                    result[index].transcripts.append(t)  # thêm vào ds kết quả
            index += 1

        print(f'==> Điểm TB cao nhất: {max_gpa}')
        print('==> Danh sách sinh viên có điểm cao nhất: ')
        show_transcripts(result)
    else:
        print('==> Danh sách bảng điểm rỗng. <==')


def find_student_with_given_gpa(courses):
    """This method find transcript with given gpa."""
    start_gpa = float(input('Điểm thấp nhất cần tìm: '))
    end_gpa = float(input('Điểm cao nhất cần tìm: '))
    # ý tưởng là ta tạo bản sao của ds khóa học để giữ nguyên thông tin lớp học
    # trong đó chứa sv có bảng điểm thỏa mãn tiêu chí cần tìm.
    result = copy.deepcopy(courses)  # tạo bản sao của danh sách lớp học
    for c in result:
        for t in c.transcripts:
            if start_gpa > t.gpa or t.gpa > end_gpa:
                c.transcripts.remove(t)  # xóa bỏ các bảng điểm không thỏa mãn
    print('==> Danh sách bảng điểm cần tìm: <==')
    show_transcripts(result)
