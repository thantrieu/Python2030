import xml.etree.ElementTree as et
from collections import OrderedDict
from operator import itemgetter

from models import FullName, Student, Subject, Register


def parse_xml(file_name):
    """Hàm thực hiện bóc tách dữ liệu từ file xml và tạo
       đối tượng tương ứng trong Python. Trả về danh sách các CD.
    """
    tree = et.parse(file_name)
    root = tree.getroot()
    mstudents = []
    for item in root:
        pid = item[0].text
        first = item[1][0].text
        mid = item[1][1].text
        last = item[1][2].text
        birth_date = item[2].text
        student_id = item[3].text
        gpa = float(item[4].text)
        major = item[5].text
        full_name = FullName(first, mid, last)
        mstudents.append(Student(pid, full_name, birth_date, gpa, major, student_id))
    return mstudents


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
    file_name = 'student.xml'
    tree = et.parse(file_name)
    root = tree.getroot()
    mstudents = []
    for item in root:
        pid = item[0].text
        first = item[1][0].text
        mid = item[1][1].text
        last = item[1][2].text
        birth_date = item[2].text
        student_id = item[3].text
        gpa = float(item[4].text)
        major = item[5].text
        full_name = FullName(first, mid, last)
        mstudents.append(Student(pid, full_name, birth_date, gpa, major, student_id))
    return mstudents


def create_students_xml_data(mstudents):
    root = et.Element('students')
    for student in mstudents:
        new_element = et.SubElement(root, 'student')
        et.SubElement(new_element, 'id').text = student.person_id
        full_name = et.SubElement(new_element, 'full_name')
        et.SubElement(full_name, 'first').text = student.full_name.first_name
        et.SubElement(full_name, 'mid').text = student.full_name.mid_name
        et.SubElement(full_name, 'last').text = student.full_name.last_name
        et.SubElement(new_element, 'birth_date').text = student.birth_date
        et.SubElement(new_element, 'student_id').text = student.student_id
        et.SubElement(new_element, 'gpa').text = str(student.gpa)
        et.SubElement(new_element, 'major').text = student.major
    et.indent(root, space='\t')
    return str(et.tostring(root, encoding='UTF-8', xml_declaration=True), 'UTF-8')


def update_xml_file(data, file_name):
    with open(file_name, 'w', encoding='UTF-8') as xml_writer:
        xml_writer.write(data)


def create_subject():
    name = input('Tên môn học: ')
    credit = int(input('Số tín chỉ: '))
    return Subject(name, credit)


def load_subjects():
    file_name = 'subject.xml'
    tree = et.parse(file_name)
    root = tree.getroot()
    msubjects = []
    for item in root:
        subject_id = int(item[0].text)
        subject_name = item[1].text
        credit = int(item[2].text)
        msubjects.append(Subject(subject_id=subject_id, name=subject_name, credit=credit))
    return msubjects


def create_subjects_xml_data(msubjects):
    root = et.Element('subjects')
    for subject in msubjects:
        new_element = et.SubElement(root, 'subject')
        et.SubElement(new_element, 'id').text = str(subject.subject_id)
        et.SubElement(new_element, 'name').text = subject.name
        et.SubElement(new_element, 'credit').text = str(subject.credit)
    et.indent(root, space='\t')
    return str(et.tostring(root, encoding='UTF-8', xml_declaration=True), 'UTF-8')


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


def find_subject_by_id(msubjects, subject_id):
    for item in msubjects:
        if item.subject_id == subject_id:
            return item
    return None


def find_student_by_id(mstudents, student_id):
    for item in mstudents:
        if item.student_id == student_id:
            return item
    return None


def load_registers(mstudents, msubjects):
    file_name = 'register.xml'
    tree = et.parse(file_name)
    root = tree.getroot()
    mregisters = []
    for item in root:
        register_id = int(item[0].text)
        subject_id = int(item[1].text)
        student_id = item[2].text
        register_time = item[3].text
        student = find_student_by_id(mstudents, student_id)
        subject = find_subject_by_id(msubjects, subject_id)
        mregisters.append(Register(register_id, student, subject, register_time))
    return mregisters


def create_register_xml_data(mregisters):
    root = et.Element('registers')
    for register in mregisters:
        new_element = et.SubElement(root, 'register')
        et.SubElement(new_element, 'id').text = str(register.register_id)
        et.SubElement(new_element, 'subject_id').text = str(register.subject.subject_id)
        et.SubElement(new_element, 'student_id').text = register.student.student_id
        et.SubElement(new_element, 'reg_time').text = register.register_time
    et.indent(root, space='\t')
    return str(et.tostring(root, encoding='UTF-8', xml_declaration=True), 'UTF-8')


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
          f'{"Mã Môn":<10}{"Tên Môn":30}{"Thời Gian ĐK":25}')
    for r in mregisters:
        print(r)


def find_registed_subject(mregisters):
    sort_registers(mregisters)
    student_id = input('Nhập mã sinh viên: ').upper()
    local_result = []
    for r in mregisters:
        if r.student.student_id == student_id:
            local_result.append(r.subject)
    if len(local_result) > 0:
        print(f'==> Danh sách môn học sinh viên mã {student_id} đã đăng ký: ')
        show_subjects(local_result)
    else:
        print(f'==> Sinh viên mã {student_id} không đăng ký môn học nào.')


def sort_registers(mregisters):
    mregisters.sort(key=lambda x: (x.register_time.year, x.register_time.month,
                                   x.register_time.day, x.register_time.hour,
                                   x.register_time.minute, x.register_time.second)
                    )


def find_student_by_subject(mregisters):
    subject_id = int(input('Nhập mã môn học(số nguyên 4 chữ số): '))
    local_result = []
    for r in mregisters:
        if r.subject.subject_id == subject_id:
            local_result.append(r.student)
    if len(local_result) > 0:
        show_students(local_result)
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
    local_result = []
    for r in mregisters:
        if r.register_time == mregisters[0].register_time:
            local_result.append(r)
    print('==> Bản đăng ký sớm nhất: ')
    show_registers(local_result)


def latest_register(mregisters):
    local_result = []
    size = len(mregisters)
    for r in mregisters:
        if r.register_time == mregisters[size - 1].register_time:
            local_result.append(r)
    print('==> Bản đăng ký muộn nhất: ')
    show_registers(local_result)


def remove_register(mregisters):
    student_id = input('Nhập mã sinh viên: ').upper()
    subject_id = int(input('Nhập mã môn học: '))
    index = 0
    is_success = False
    for item in mregisters:
        if student_id == item.student.student_id and \
                subject_id == item.subject.subject_id:
            mregisters.pop(index)
            is_success = True
            break
        index += 1
    return is_success
