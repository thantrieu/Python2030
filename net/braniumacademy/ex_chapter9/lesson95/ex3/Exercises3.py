import json
import urllib.request
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
    """Hàm liệt kê danh sách sinh viên."""
    print(f'{"Mã SV":10}{"Họ và tên":30}{"Tuổi":10}'
          f'{"Địa chỉ":35}{"Điểm TB":10}{"Chuyên ngành":15}')
    for student in mstudents:
        print(student)


def find_by_id(mstudents):
    """Hàm tìm sinh viên theo mã sinh viên."""
    student_id = input('Nhập mã học sinh: ').upper()
    for s in mstudents:
        if s.student_id == student_id:
            return s
    return None


def find_by_name(mstudents):
    """Hàm tìm sinh viên theo tên."""
    key = input('Nhập tên sinh viên cần tìm: ').lower()
    mresult = []
    for student in mstudents:
        if student.full_name.first_name.lower() == key:
            mresult.append(student)
    return mresult


def find_by_gpa(mstudents):
    """ Hàm tìm sinh viên theo điểm TB."""
    mresult = []
    gpa = float(input('Nhập điểm TB: '))
    for student in mstudents:
        if student.gpa == gpa:
            mresult.append(student)
    return mresult


def remove_by_id(mstudents):
    """Hàm xóa sinh viên theo mã sinh viên."""
    student_id = input('Nhập mã sinh viên: ').upper()
    success = False
    for x in range(len(mstudents)):
        if mstudents[x].student_id == student_id:
            mstudents.pop(x)
            success = True
            break
    if success is True:
        print('==> Xóa thành công! <==')
    else:
        print('==> Xóa thất bạ! <==')
    return success


def listed_by_district(mstudents):
    result_dict = {}
    for student in mstudents:
        if student.address.district in result_dict:
            result_dict[student.address.district] += 1
        else:
            result_dict[student.address.district] = 1
    # Hiện kết quả
    print('==> Số lượng sinh viên theo từng quận: ')
    for key in result_dict.keys():
        print(f'{key:20}{result_dict[key]:<10}')


def listed_by_age(mstudents):
    result_dict = {}
    for student in mstudents:
        if student.age in result_dict:
            result_dict[student.age] += 1
        else:
            result_dict[student.age] = 1
    # Hiện kết quả
    print('==> Số lượng sinh viên theo độ tuổi: ')
    for key in result_dict.keys():
        print(f'{key:<10}{result_dict[key]:10}')


def listed_by_gpa(mstudents):
    result_dict = {}
    for student in mstudents:
        if student.gpa in result_dict:
            result_dict[student.gpa] += 1
        else:
            result_dict[student.gpa] = 1
    # Hiện kết quả
    print('==> Số lượng sinh viên theo đầu điểm: ')
    for key in result_dict.keys():
        print(f'{key:<10}{result_dict[key]:10}')


def find_student_max_gpa(mstudents):
    """Hàm tìm học sinh có điểm TB cao nhất.
        B1: sắp xếp danh sách học sinh giảm dần điểm TB.
        B2: lấy điểm TB max.
        B3: duyệt từ đầu danh sách và kiểm tra, nếu điểm hs là max thì in ra.
        B4: nếu điểm tb khác max thì kết thúc.
    """
    mstudents.sort(key=lambda x: -x.gpa)
    max_gpa = mstudents[0].gpa
    print('==> Danh sách sinh viên có điểm TB cao nhất: ')
    mresult = []
    for student in mstudents:
        if student.gpa == max_gpa:
            mresult.append(student)
        else:
            break
    return mresult


def load_data(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    mdata = response.read()
    data_string = str(mdata, encoding='UTF-8')
    urllib.request.urlcleanup()
    return data_string


if __name__ == '__main__':
    url = 'https://braniumacademy.net/resources/lesson95_data3.json'
    data = load_data(url)
    students = json.loads(data, object_hook=decode_student)
    option = '================= CÁC TÙY CHỌN =================\n' \
             '1. Liệt kê danh sách sinh viên.\n' \
             '2. Sắp xếp danh sách sinh viên theo tên.\n' \
             '3. Sắp xếp danh sách sinh viên theo điểm.\n' \
             '4. Tìm sinh viên theo mã sinh viên.\n' \
             '5. Tìm sinh viên theo tên.\n' \
             '6. Tìm sinh viên theo điểm TB.\n' \
             '7. Xóa bỏ một sinh viên theo mã.\n' \
             '8. Liệt kê số lượng sinh viên theo quận.\n' \
             '9. Liệt kê số lượng sinh viên theo độ tuổi.\n' \
             '10. Liệt kê số lượng sinh viên theo đầu điểm.\n' \
             '11. Liệt kê các sinh viên có điểm cao nhất.\n' \
             '12. Thoát chương trình.\n' \
             'Xin mời chọn: '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                if len(students) > 0:
                    print('==> Các sinh viên có trong file: ')
                    listed_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 2:
                if len(students) > 0:
                    print('==> Danh sách sinh viên sau khi sắp xếp theo tên tăng dần: ')
                    students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
                    listed_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 3:
                if len(students) > 0:
                    print('==> Danh sách sinh viên sau khi sắp xếp theo điểm giảm dần: ')
                    students.sort(key=lambda x: (-x.gpa, x.age))
                    listed_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 4:
                if len(students) > 0:
                    result = find_by_id(students)
                    if result is not None:
                        print('==> thông tin sinh viên cần tìm: ')
                        result_list = [result]
                        listed_students(result_list)
                    else:
                        print('==> Không tìm thấy kết quả nào. <==')
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 5:
                if len(students) > 0:
                    result = find_by_name(students)
                    if len(result) > 0:
                        print('==> Kết quả tìm kiếm: ')
                        listed_students(result)
                    else:
                        print('==> Không có kết quả nào phù hợp <==')
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 6:
                if len(students) > 0:
                    result = find_by_gpa(students)
                    if len(result) > 0:
                        print('==> Kết quả tìm kiếm: ')
                        listed_students(result)
                    else:
                        print('==> Không có kết quả nào phù hợp <==')
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 7:
                if len(students) > 0:
                    if remove_by_id(students) is True:
                        print('==> Danh sách sinh viên sau khi xóa: ')
                        listed_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 8:
                if len(students) > 0:
                    listed_by_district(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 9:
                if len(students) > 0:
                    listed_by_age(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 10:
                if len(students) > 0:
                    listed_by_gpa(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 11:
                if len(students) > 0:
                    students_max_gpa = find_student_max_gpa(students)
                    print('==> Danh sách sinh viên có điểm TB cao nhất: ')
                    listed_students(students_max_gpa)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 12:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Sai chức năng. Vui lòng chọn chức năng 1-12.')
