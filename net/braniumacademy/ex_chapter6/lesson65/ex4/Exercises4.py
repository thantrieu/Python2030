import json

from models import Address, Student, FullName


def decode_address(address):
    if 'wards' in address:
        return Address(address['wards'], address['district'], address['city'])
    else:
        return None


def decode_full_name(fname):
    if 'first' in fname:
        return FullName(fname['first'], fname['mid'], fname['last'])
    else:
        return None


def decode_student(dct):
    if 'id' in dct:
        student_id = dct['id']
        name = decode_full_name(dct['full_name'])
        address = decode_address(dct['address'])
        age = int(dct['age'])
        gpa = float(dct['gpa'])
        major = dct['major']
        return Student(student_id, name, age, major, address, gpa)
    else:
        return dct


def listed_students(mstudents):
    print(f'{"Mã SV":10}{"Họ và tên":30}{"Tuổi":15}{"Địa chỉ":35}{"Điểm TB":10}{"Chuyên ngành":15}')
    for student in mstudents:
        print(student)


if __name__ == '__main__':
    source = 'data3.json'
    with open(source, encoding='UTF-8') as json_reader:
        data = json_reader.read()
        students = json.loads(data, object_hook=decode_student)
    option = '1. Liệt kê danh sách học sinh.\n' \
             '2. Sắp xếp danh sách học sinh theo điểm giảm dần.\n' \
             '3. Liệt kê thông tin các học sinh có điểm TB cao nhất.\n' \
             '4. Liệt kê số lượng học sinh theo đầu điểm.\n' \
             '5. Liệt kê các học sinh có điểm bằng x.\n' \
             '6. Liệt kê các học sinh theo tháng sinh.\n' \
             '7. Liệt kê các học sinh theo ngày sinh.\n' \
             '8. Liệt kê các học sinh theo ngày sinh tăng, tháng sinh giảm.\n' \
             '9. Xóa bỏ một học sinh theo mã.\n' \
             '0. Thoát chương trình.\n' \
             'Xin mời chọn: '
    while True:
        choice = int(input(option))
        match choice:
            case 0:
                print('==> Chương trình kết thúc <==')
                break
            case 1:
                if len(students) > 0:
                    print('==> Các học sinh có trong file: ')
                    listed_students(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 2:
                if len(students) > 0:
                    students.sort(key=lambda x: (-x.gpa, get_name(x.name)))
                    print('==> Danh sách học sinh sau khi sắp xếp: ')
                    listed_students(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 3:
                if len(students) > 0:
                    find_student_max_gpa(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 4:
                if len(students) > 0:
                    listed_students_by_gpa(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 5:
                if len(students) > 0:
                    listed_student_with_givent_gpa(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 6:
                if len(students) > 0:
                    listed_student_by_birth_month(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 7:
                if len(students) > 0:
                    listed_student_by_birth_day(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 8:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.birth_date.day, -x.birth_date.month))
                    print('==> Danh sách học sinh sau khi sắp xếp:')
                    listed_students(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case 9:
                if len(students) > 0:
                    if remove_by_id(students) is True:
                        print('==> Danh sách học sinh sau khi xóa: ')
                        listed_students(students)
                    print("============================================================")
                else:
                    print('==> Danh sách học sinh rỗng <==')
            case _:
                print('==> Sai chức năng. Vui lòng chọn chức năng 0-9.')