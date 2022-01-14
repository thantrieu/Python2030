import json
from collections import OrderedDict
from operator import itemgetter
from Exercises1 import Subject, Student, Register, FullName
from decoders import decode_student, decode_subject
from net.braniumacademy.ex_chapter6.lesson66.ex1.decoders import decode_register
from net.braniumacademy.ex_chapter6.lesson66.ex1.encoders \
    import StudentEncoder, RegisterEncoder, SubjectEncoder


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


def load_students():
    with open('STUDENT.json', encoding='UTF-8') as reader:
        data = reader.read()
        mstudents = json.loads(data, object_hook=decode_student)
        return mstudents


def write_file_student(list_student):
    with open('STUDENT.json', 'w', encoding='UTF-8') as writer:
        encoded_data = json.dumps(list_student, cls=StudentEncoder, indent=4, ensure_ascii=False)
        writer.write(encoded_data)


def create_subject():
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(name, credit)


def load_subjects():
    with open('SUBJECT.json', encoding='UTF-8') as reader:
        data = reader.read()
        msubjects = json.loads(data, object_hook=decode_subject)
        return msubjects


def write_file_subject(list_subject):
    with open('SUBJECT.json', 'w', encoding='UTF-8') as writer:
        encoded_data = json.dumps(list_subject, cls=SubjectEncoder, indent=4, ensure_ascii=False)
        writer.write(encoded_data)


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


def update_register(mregister, mstudents, msubjects):
    for register in mregister:
        student = None
        subject = None
        for e in mstudents:
            if e.student_id == register.student:
                student = e
                break
        for item in msubjects:
            if item.subject_id == register.subject:
                subject = item
                break
        register.student = student
        register.subject = subject


def load_registers(mstudents, msubjects):
    with open('REGISTER.json', encoding='UTF-8') as reader:
        data = reader.read()
        mregisters = json.loads(data, object_hook=decode_register)
        update_register(mregisters, mstudents, msubjects)
        return mregisters


def write_file_register(list_register):
    with open('REGISTER.json', 'w', encoding='UTF-8') as writer:
        encoded_data = json.dumps(list_register, cls=RegisterEncoder, indent=4, ensure_ascii=False)
        writer.write(encoded_data)


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
    students = load_students()
    subjects = load_subjects()
    registers = load_registers(students, subjects)
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
             'Xin mời chọn chức năng(1-16): '
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
