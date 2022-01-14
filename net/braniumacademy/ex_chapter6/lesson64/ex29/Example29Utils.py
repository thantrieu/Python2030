from datetime import datetime
from collections import OrderedDict
from operator import itemgetter

from Exercises29 import Subject, Student, Register, FullName


def create_student():
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    last = input('Họ: ').capitalize()
    mid = input('Đệm: ').capitalize()
    first = input('Name: ').capitalize()
    birth_date = input('Ngày sinh: ')
    if len(birth_date) != 10:
        return None
    major = input('Chuyên ngành: ')
    gpa = float(input('Điểm TB: '))
    full_name = FullName(first, mid, last)
    return Student(pid, full_name, birth_date, gpa, major)


def read_students_from_file():
    mstudents = []
    with open('STUDENT.DAT', encoding='UTF-8') as student_reader:
        pid = student_reader.readline().strip()
        while pid != '':
            fname = student_reader.readline().strip().split()
            last = fname[0]
            mid = ''
            for i in range(1, len(fname) - 1):
                mid += fname[i] + ' '
            first = fname[len(fname) - 1]
            birth_date = student_reader.readline().strip()
            student_id = student_reader.readline().strip()
            gpa = float(student_reader.readline().strip())
            major = student_reader.readline().strip()
            full_name = FullName(first, mid.strip(), last)
            mstudents.append(
                Student(pid, full_name, birth_date,
                        gpa, major, student_id=student_id)
            )
            pid = student_reader.readline().strip()
    return mstudents


def write_file_student(list_student):
    with open('STUDENT.DAT', 'w', encoding='UTF-8') as writer:
        for s in list_student:
            writer.write(f'{s.person_id}\n')
            writer.write(f'{s.full_name}\n')
            writer.write(f'{s.birth_date}\n')
            writer.write(f'{s.student_id}\n')
            writer.write(f'{s.gpa}\n')
            writer.write(f'{s.major}\n')


def write_file_subject(list_subject):
    with open('SUBJECT.DAT', 'w', encoding='UTF-8') as writer:
        for s in list_subject:
            writer.write(f'{s.subject_id}\n')
            writer.write(f'{s.name}\n')
            writer.write(f'{s.credit}\n')


def write_file_register(list_register):
    with open('REGISTER.DAT', 'w', encoding='UTF-8') as writer:
        for r in list_register:
            writer.write(f'{r.register_id}\n')
            writer.write(f'{r.subject.subject_id}\n')
            writer.write(f'{r.student.student_id}\n')
            mformat = '%d/%m/%Y %H:%M:%S'
            writer.write(f'{r.register_time.strftime(mformat)}\n')


def create_subject():
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(name, credit)


def read_subjects_from_file():
    msubjects = []
    with open('SUBJECT.DAT', encoding='UTF-8') as subj_reader:
        subj_id = subj_reader.readline().strip()
        while subj_id != '':
            name = subj_reader.readline().strip()
            credit = int(subj_reader.readline().strip())
            msubjects.append(Subject(name, credit, subject_id=int(subj_id)))
            subj_id = subj_reader.readline().strip()
    return msubjects


def create_register(mstudents, msubjects):
    student_id = input('Mã sinh viên: ').upper()
    subject_id = int(input('Mã môn học(số nguyên 4 chữ số): '))
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


def read_registers_from_file(mstudents, msubjects):
    mregisters = []
    with open('REGISTER.DAT', encoding='UTF-8') as reg_reader:
        reg_id_str = reg_reader.readline().strip()
        while reg_id_str != '':
            reg_id = int(reg_id_str)
            subject_id = int(reg_reader.readline().strip())
            student_id = reg_reader.readline().strip()
            # để chuyển đổi ngày giờ, ví dụ 14/02/2025 12:36:48, dùng định dạng sau:
            mformat = '%d/%m/%Y %H:%M:%S'
            date_time_str = reg_reader.readline().strip()
            reg_time = datetime.strptime(date_time_str, mformat)
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
            mregisters.append(Register(reg_id=reg_id,
                                       student=student,
                                       subject=subject, reg_time=reg_time))
            reg_id_str = reg_reader.readline().strip()
    return mregisters


def is_register_exist(mregisters, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in mregisters:
        if item == r:
            return True
    return False


def show_students(mstudents):
    print('==> Danh sách sinh viên:')
    print(f'{"CMND/CC":15}{"Họ và tên":25}{"Ngày sinh":12}'
          f'{"Mã SV":10}{"Điểm TB":10}{"C.Ngành":15}')
    for e in mstudents:
        print(e)


def show_subjects(msubjects):
    print('==> Danh sách môn học:')
    print(f'{"Mã môn":10}{"Tên môn":35}{"Số tín":<10}')
    for s in msubjects:
        print(s)


def show_registers(mregisters):
    print('==> Danh sách đăng ký:')
    print(f'{"Mã ĐK":10}{"Mã SV":10}{"Tên SV":25}'
          f'{"Mã Môn":<10}{"Tên Môn":35}{"Thời Gian ĐK":25}')
    for r in mregisters:
        print(r)


def find_registed_subject(mregisters):
    sort_registers(mregisters)
    student_id = input('Nhập mã sinh viên: ').upper()
    result = []
    for r in mregisters:
        if r.student.student_id == student_id:
            result.append(r.subject)
    if len(result) > 0:
        print(f'==> Danh sách môn học sinh viên mã {student_id} đã đăng ký: ')
        show_subjects(result)
    else:
        print(f'==> Sinh viên mã {student_id} không đăng ký môn học nào.')


def sort_registers(mregisters):
    mregisters.sort(key=lambda x: (x.register_time.year, x.register_time.month,
                                   x.register_time.day, x.register_time.hour,
                                   x.register_time.minute, x.register_time.second)
                    )


def find_student_by_subject(mregisters):
    subject_id = int(input('Nhập mã môn học(số nguyên 4 chữ số): '))
    result = []
    for r in mregisters:
        if r.subject.subject_id == subject_id:
            result.append(r.student)
    if len(result) > 0:
        show_students(result)
    else:
        print(f'==> Môn học mã {subject_id} không có sinh viên đăng ký.')


def get_list_item(data, key):
    for d in data:
        if d.subject_id == key:
            return d
    return None


def print_statistic(order_dct, msubjects):
    print(f'{"Tên môn":35}{"Số SV ĐK":12}')
    for item in order_dct.keys():
        subject = get_list_item(msubjects, item)
        print(f'{subject.name:35}{order_dct[item]:<12}')


def statistics_by_subject(mregisters, msubjects):
    subject_dct = {}
    for r in mregisters:
        if r.subject.subject_id not in subject_dct:
            subject_dct[r.subject.subject_id] = 1
        else:
            subject_dct[r.subject.subject_id] += 1
    order_dct = OrderedDict(sorted(subject_dct.items(), key=itemgetter(1), reverse=True))
    print_statistic(order_dct, msubjects)


def earliest_register(mregisters):
    result = []
    for r in mregisters:
        if r.register_time == mregisters[0].register_time:
            result.append(r)
    print('==> Bản đăng ký sớm nhất: ')
    show_registers(result)


def latest_register(mregisters):
    result = []
    size = len(mregisters)
    for r in mregisters:
        if r.register_time == mregisters[size - 1].register_time:
            result.append(r)
    print('==> Bản đăng ký muộn nhất: ')
    show_registers(result)


if __name__ == '__main__':
    students = read_students_from_file()
    subjects = read_subjects_from_file()
    registers = read_registers_from_file(students, subjects)
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
             '15. Lưu các danh sách vào file.\n' \
             '16. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-15): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                new_student = create_student()
                if new_student is not None:
                    students.append(new_student)
                else:
                    print('==> Tạo sinh viên thất bại <==')
            case 2:
                new_subject = create_subject()
                subjects.append(new_subject)
            case 3:
                new_register = create_register(students, subjects)
                if new_register is not None:
                    if not is_register_exist(registers, new_register):
                        registers.append(new_register)
                    else:
                        print(f'==> Sinh viên mã '
                              f'{new_register.student.student_id} '
                              f'đã đăng ký môn học này.')
                else:
                    print('==> Tạo bản đăng ký thất bại.')
            case 4:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
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
                    sort_registers(registers)
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
                if len(registers) > 0:
                    find_registed_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 11:
                if len(registers) > 0:
                    find_student_by_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 12:
                if len(registers) > 0:
                    statistics_by_subject(registers, subjects)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 13:
                if len(registers) > 0:
                    sort_registers(registers)
                    earliest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 14:
                if len(registers) > 0:
                    sort_registers(registers)
                    latest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 15:
                if len(students) > 0:
                    write_file_student(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
                if len(subjects) > 0:
                    write_file_subject(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
                if len(registers) > 0:
                    write_file_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 16:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-16. <==')
