import datetime

from Exercises1 import Subject, Student, Register, FullName


def create_student():
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


def create_subject():
    name = input('Tên môn học: ')
    credit = int('Số tín chỉ: ')
    return Subject(name, credit)


def create_register(mstudents, msubjects):
    student_id = input('Mã sinh viên: ')
    subject_id = int(input('Mã môn học(số nguyên 3 chữ số): '))
    student = None
    subject = None
    for e in mstudents:
        if e.student_id == student_id:
            student = e
            break
    for item in msubjects:
        if item.subject_id == subject_id:
            subject = item
            break
    if student is None:
        print(f'==> Sinh viên mã \'{student_id}\' không tồn tại.')
        return None
    if subject is None:
        print(f'==> Môn học mã \'{subject_id}\' không tồn tại.')
        return None
    return Register(student=student, subject=subject)


def show_students(students):
    print('==> Danh sách sinh viên:')
    print(f'{"CMND/CC":15}{"Họ và tên":25}{"Ngày sinh":12}'
          f'{"Mã SV":10}{"Điểm TB":10}{"C.Ngành":15}')
    for e in students:
        print(e)


def show_subjects(subjects):
    print('==> Danh sách môn học:')
    for s in subjects:
        print(s)


def show_registers(registers):
    print('==> Danh sách đăng ký:')
    for r in registers:
        print(r)


if __name__ == '__main__':
    students = []
    subjects = []
    registers = []
    option = '============================ OPTION ============================\n' \
             '1. Thêm mới sinh viên vào danh sách.\n' \
             '2. Thêm mới môn học vào danh sách.\n' \
             '3. Thêm mới bảng đăng ký môn học vào danh sách.\n' \
             '4. Sắp xếp danh sách sinh viên theo tên.\n' \
             '5. Sắp xếp danh sách môn học theo tên.\n' \
             '6. Sắp xếp danh sách bảng đăng ký.\n' \
             '7. Hiển thị danh sách sinh viên.\n' \
             '8. Hiển thị danh sách môn học.\n' \
             '9. Hiển thị danh sách bảng đăng ký.\n' \
             '10. Liệt kê danh sách môn học mà sinh viên đăng ký.\n' \
             '11. Liệt kê danh sách sinh viên đăng ký theo mã môn.\n' \
             '12. Thống kê số lượng sinh viên đăng ký theo từng môn học.\n' \
             '13. Cho biết thông tin bản ghi sớm nhất.\n' \
             '14. Cho biết thông tin bản ghi đăng ký muộn nhất.\n' \
             '15. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-15): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                new_student = create_student()
                students.append(new_student)
            case 2:
                new_subject = create_subject()
                subjects.append(new_subject)
            case 3:
                new_register = create_register(students, subjects)
                if new_register is not None:
                    registers.append(new_register)
            case 4:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.full_name.first, x.full_name.last))
                    print('==> Danh sách sinh viên sau khi sắp xếp: ')
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 5:
                if len(subjects) > 0:
                    subjects.sort(key=lambda x: x.name)
                    print('==> Danh sách môn học sau khi sắp xếp: ')
                    show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 6:
                if len(registers) > 0:
                    registers.sort(key=lambda x:
                    (x.register_date.year, x.register_date.month,
                     x.register_date.day, x.register_date.hour,
                     x.register_date.minute, x.register_date.second))
                    print('==> Danh sách đăng ký sau khi sắp xếp: ')
                    show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 7:
                if len(students) > 0:
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 8:
                if len(subjects) > 0:
                    show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 9:
                if len(registers) > 0:
                    show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                print('==> Chương trình kết thúc <==')
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-15. <==')
