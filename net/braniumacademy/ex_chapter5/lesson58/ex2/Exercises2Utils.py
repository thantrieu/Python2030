from Exercises2 import FullName, Student, Subject, Teacher, Course


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


def show_students(mstudents):
    """Phương thức hiển thị thông tin sinh viên."""
    print('==> Danh sách sinh viên:')
    print(f'{"CMND/CC":15}{"Họ và tên":25}{"Ngày sinh":12}'
          f'{"Mã SV":10}{"Điểm TB":10}{"C.Ngành":15}')
    for e in mstudents:
        print(e)


def show_teacher(mteachers):
    """Phương thức hiển thị thông tin giảng viên."""
    print('==> Danh sách giảng viên <==')
    print(f'{"CMND/CC":15}{"Họ và tên":25}{"Ngày sinh":12}'
          f'{"Mã GV":10}{"Mức lương":10}{"Chuyên môn":20}')
    for teacher in mteachers:
        print(teacher)


def show_subjects(msubjects):
    """Phương thức hiển thị danh sách môn học."""
    print('==> Danh sách môn học:')
    print(f'{"Mã môn":10}{"Tên môn":15}{"Số tín":<10}')
    for s in msubjects:
        print(s)


def find_teacher(mteachers, teacher_id):
    """Phương thức tìm giảng viên trong danh sách giảng viên cho trước."""
    for e in mteachers:
        if e.teacher_id == teacher_id:
            return e
    return None


def find_subject(msubjects, subject_id):
    """Phương thức tìm môn học trong danh sách môn học cho trước."""
    for e in msubjects:
        if e.subject_id == subject_id:
            return e
    return None


def create_course(msubjects, mteachers):
    """Phương thức tạo mới một lớp học phần."""
    teacher_id = input('Mã giảng viên: ')
    target_teacher = find_teacher(mteachers, teacher_id)
    subject_id = input('Mã môn học: ')
    target_subject = find_subject(msubjects, subject_id)
    room = input('Phòng học: ')
    return Course('', target_subject, target_teacher, room)


def show_course(mcourses):
    """Phương thức hiển thị danh sách các lớp học phần."""
    print('==> Danh sách các lớp học phần: <==')
    print(f'{"Mã lớp":10}{"Mã môn":10}{"Tên môn học":30}'
          f'{"Mã GV":10}{"Tên giảng viên":30}{"Phòng học":10}')
    for c in mcourses:
        print(c)


if __name__ == '__main__':
    students = []
    teachers = []
    subjects = []
    courses = []
    option = '============================== OPTION ==============================\n' \
             '1. Thêm mới sinh viên vào danh sách sinh viên.\n' \
             '2. Thêm mới giảng viên vào danh sách giảng viên.\n' \
             '3. Thêm mới môn học vào danh sách môn học.\n' \
             '4. Thêm mới lớp học vào danh sách lớp học.\n' \
             '5. Nhập danh sách sinh viên cho lớp học.\n' \
             '6. Hiển thị danh sách sinh viên ra màn hình.\n' \
             '7. Hiển thị danh sách môn học ra màn hình.\n' \
             '8. Hiển thị danh sách giảng viên ra màn hình.\n' \
             '9. Hiển thị danh sách các lớp học.\n' \
             '10. Hiển thị danh sách bảng điểm của từng lớp.\n' \
             '11. Sắp xếp danh sách sinh viên theo tên tăng dần.\n' \
             '12. Sắp xếp danh sách sinh viên theo ngày sinh tăng dần.\n' \
             '13. Sắp xếp danh sách môn học theo tên môn học.\n' \
             '14. Sắp xếp danh sách lớp học theo tên phòng học.\n' \
             '15. Sắp xếp danh sách sinh viên trong lớp theo điểm giảm dần.\n' \
             '16. Liệt kê các sinh viên có điểm cao nhất trong lớp theo mã lớp.\n' \
             '17. Liệt kê các sinh viên có điểm cao nhất theo từng môn học.\n' \
             '18. Tìm sinh viên trong lớp theo điểm và mã lớp.\n' \
             '19. Thống kê số lượng sinh viên trong một lớp theo học lực giảm dần.\n' \
             '20. Thống kê số lượng sinh viên có học lực giỏi, xuất sắc theo từng môn.\n' \
             '21. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-21): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                new_student = create_student()
                students.append(new_student)
            case 2:
                new_teacher = create_teacher()
                teachers.append(new_teacher)
            case 3:
                subject = create_subject()
                subjects.append(subject)
            case 4:
                break
            case 5:
                break
            case 6:
                if len(students) > 0:
                    show_students(students)
                else:
                    print("==> Danh sách sinh viên rỗng. <==")
            case 7:
                if len(subjects) > 0:
                    show_subjects(subjects)
                else:
                    print("==> Danh sách môn học rỗng. <==")
            case 8:
                if len(teachers) > 0:
                    show_teacher(teachers)
                else:
                    print("==> Danh sách giảng viên rỗng. <==")
            case 21:
                print("==> Chương trình kết thúc. <==")
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-20. <==')
