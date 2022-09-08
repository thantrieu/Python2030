from collections import OrderedDict
from operator import itemgetter
from register import Register
from subject import Subject
from student import Student


def create_student():
    """Phương thức tạo mới thông tin sv."""
    print('============ Nhập thông tin sinh viên ============')
    pid = input('Số CMND/CCCD: ')
    name = input('Họ và tên: ')
    birth_date = input('Ngày sinh: ')
    major = input('Chuyên ngành: ')
    gpa = input('Điểm TB: ')
    return Student(pid, name, birth_date, None, gpa, major)


def read_students_from_file():
    """Phương thức đọc thông tin sv từ file."""
    students = []
    with open('STUDENT.DAT', encoding='UTF-8') as student_reader:
        pid = student_reader.readline().strip()
        while pid != '':
            fname = student_reader.readline().strip()
            birth_date = student_reader.readline().strip()
            student_id = student_reader.readline().strip()
            gpa = student_reader.readline().strip()
            major = student_reader.readline().strip()
            students.append(Student(pid, fname, birth_date, student_id, gpa, major))
            pid = student_reader.readline().strip()
    return students


def create_subject():
    """Phương thức tạo mới môn học."""
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(None, name, credit)


def read_subject_from_file():
    """Phương thức đọc thông tin môn học từ file."""
    subjects = []
    with open('SUBJECT.DAT', encoding='UTF-8') as subject_reader:
        subject_id = subject_reader.readline().strip()
        while subject_id != '':
            name = subject_reader.readline().strip()
            credit = int(subject_reader.readline().strip())
            subjects.append(Subject(int(subject_id), name, credit))
            subject_id = subject_reader.readline().strip()
    return subjects


def read_register_from_file(students, subjects):
    """Phương thức đọc thông tin đăng ký từ file."""
    registers = []
    with open('REGISTER.DAT', encoding='UTF-8') as register_reader:
        register_id = register_reader.readline().strip()
        while register_id != '':
            subject_id = int(register_reader.readline())
            student_id = register_reader.readline().strip()  # ở đây phải strip để loại bỏ kí tự \n ở cuối dòng
            student = find_student_by_id(students, student_id)
            subject = find_subject_by_id(subjects, subject_id)
            register_time = register_reader.readline().strip()
            registers.append(Register(int(register_id), register_time, student, subject))
            register_id = register_reader.readline().strip()
    return registers


def find_student_by_id(students, student_id):
    """Phương thức tìm sinh viên theo mã sinh viên."""
    for s in students:
        if s.student_id.lower() == student_id.lower():
            return s
    return None  # nếu k tim thấy, trả về None


def find_subject_by_id(subjects, subject_id):
    """Phương thức tìm môn học theo mã môn học."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None


def is_register_exists(registers, student_id, subject_id):
    """Phương thức kiểm tra xem sinh viên x đã đăng ký môn học y chưa."""
    for reg in registers:
        if reg.subject.subject_id == subject_id and reg.student.student_id == student_id:
            return True  # nếu đã đăng ký, trả về True
    return False  # chưa đăng ký, trả về false


def create_register(registers, students, subjects):
    """Phương thức tạo thông tin đăng ký môn học của sv."""
    student_id = input('Mã sinh viên: ')
    subject_id = int(input('Mã môn học(số nguyên 4 chữ số): '))
    student = find_student_by_id(students, student_id)
    subject = find_subject_by_id(subjects, subject_id)
    if student is None:
        print(f'==> Sinh viên mã \'{student_id}\' không tồn tại.')
        return None
    if subject is None:
        print(f'==> Môn học mã \'{subject_id}\' không tồn tại.')
        return None
    if is_register_exists(registers, student_id, subject_id):
        print(f'==> Sinh viên mã {student_id} đã đăng ký môn học {subject_id} trước đó.')
        return None
    else:
        return Register(None, None, student, subject)


def is_register_exist(registers, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in registers:
        if item == r:
            return True
    return False


def sort_registers(registers):
    """
        Phương thức sắp xếp danh sách đăng ký. Liên quan date time bạn xem chương 9.
        Ta tách thời gian đăng ký và lần lượt sắp xếp theo năm, tháng, ngày, giờ, phút, giây
    """
    registers.sort(key=lambda x: (x.register_time.year, x.register_time.month,
                                  x.register_time.day, x.register_time.hour,
                                  x.register_time.minute, x.register_time.second)
                   )


def update_student_name(students):
    """Phương thức dùng để cập nhật tên sinh viên theo mã sinh viên cho trước."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    student = find_student_by_id(students, student_id)
    if student is not None:
        full_name = input('Họ và tên mới: ')
        try:
            student.full_name = full_name
            print('==> Cập nhật điểm cho sinh viên thành công! <==')
        except ValueError as e:
            print(e)


def update_student_gpa(students):
    """Phương thức dùng để cập nhật điểm Gpa theo mã sv cho trước."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    student = find_student_by_id(students, student_id)
    if student is not None:
        gpa_str = input('Điểm Gpa thay thế: ')
        try:
            student.gpa = gpa_str
            print('==> Cập nhật điểm cho sinh viên thành công! <==')
        except ValueError as e:
            print(e)


def save_data(items, file_name):
    """Phương thức lưu dữ liệu kiểu x ra file tương ứng"""
    with open(file_name, 'w', encoding='UTF-8') as writer:
        for item in items:
            writer.write(item.file_output_format())


def show_students(students):
    """Phương thức dùng để hiển thị danh sách sinh viên."""
    title = f'{"CMND/CCCD":15}{"Họ và tên":30}' \
            f'{"Ngày sinh":20}{"Mã SV":15}{"C.Ngành":15}' \
            f'{"Gpa":15}'
    print(title)
    for student in students:
        print(student)


def show_subjects(subjects):
    """Phương thức dùng để hiển thị danh sách môn học."""
    title = f'{"Mã môn":15}{"Tên môn học":30}{"Số tín chỉ":15}'
    print(title)
    for subject in subjects:
        print(subject)


def show_registers(registers):
    """Phương thức dùng để hiển thị danh sách đăng ký."""
    title = f'{"Mã ĐK":10}{"Mã SV":15}{"Mã MH":15}{"Thời gian đăng ký":30}'
    print(title)
    for r in registers:
        print(r)


def find_registed_subject(registers):
    """Phương thức dùng để tìm môn học đã đăng ký."""
    sort_registers(registers)
    student_id = input('Nhập mã sinh viên: ')
    result = []
    for r in registers:
        if r.student.student_id == student_id:
            result.append(r.subject)
    if len(result) > 0:
        print(f'==> Danh sách môn học sinh viên mã {student_id} đã đăng ký: ')
        show_subjects(result)
    else:
        print(f'==> Sinh viên mã {student_id} không đăng ký môn học nào.')


def find_student_by_subject(registers):
    """Phương thức tìm sinh viên đăng ký theo môn học."""
    subject_id = int(input('Nhập mã môn học(số nguyên 4 chữ số): '))
    result = []
    for r in registers:
        if r.subject.subject_id == subject_id:
            result.append(r.student)
    if len(result) > 0:
        show_students(result)
    else:
        print(f'==> Môn học mã {subject_id} không có sinh viên đăng ký.')


def get_list_item(data, key):
    """Phương thức tìm value theo key cho trước"""
    for d in data:
        if d.subject_id == key:
            return d
    return None


def print_statistic(order_dct, subjects):
    """Phương thức hiển thị kết quả thống kê."""
    print(f'{"Tên môn học":35}{"Số SV đăng ký":10}')
    for item in order_dct.keys():
        subject = get_list_item(subjects, item)
        print(f'{subject.subject_name:35}: {order_dct[item]:<10}')


def statistics_by_subject(registers, subjects):
    """Phương thức thống kê sv đăng ký theo môn học."""
    subject_dct = {}
    for r in registers:
        if r.subject.subject_id not in subject_dct:
            subject_dct[r.subject.subject_id] = 1
        else:
            subject_dct[r.subject.subject_id] += 1
    order_dct = OrderedDict(sorted(subject_dct.items(), key=itemgetter(1), reverse=True))
    print_statistic(order_dct, subjects)


def earliest_register(registers):
    """Phương thức tìm sinh viên đăng ký sớm nhất."""
    result = []
    for r in registers:
        if r.register_time == registers[0].register_time:
            result.append(r)
    print('==> Các bản đăng ký sớm nhất: ')
    show_registers(result)


def latest_register(registers):
    """Phương thức tìm sinh viên đăng ký muộn nhất."""
    result = []
    size = len(registers)
    for r in registers:
        if r.register_time == registers[size - 1].register_time:
            result.append(r)
    print('==> Bản đăng ký muộn nhất: ')
    show_registers(result)


def update_student_auto_id(students):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for student in students:
        id_number = int(student.student_id[2:])
        if id_number > max_id:
            max_id = id_number
    Student.AUTO_ID = max_id + 1


def update_subject_auto_id(subjects):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for subject in subjects:
        if subject.subject_id > max_id:
            max_id = subject.subject_id
    Subject.AUTO_ID = max_id + 1


def update_register_auto_id(registers):
    """Phương thức cập nhật mã tự tăng cho lớp sinh viên."""
    max_id = 1000
    for reg in registers:
        if reg.register_id > max_id:
            max_id = reg.register_id
    Register.AUTO_ID = max_id + 1