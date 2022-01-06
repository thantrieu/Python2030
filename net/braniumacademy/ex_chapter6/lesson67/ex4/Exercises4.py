import xml.etree.ElementTree as et
from net.braniumacademy.ex_chapter6.lesson67.ex4.student \
    import Student, Address, FullName


def parse_xml(file_name):
    """Hàm thực hiện bóc tách dữ liệu từ file xml và tạo
       đối tượng tương ứng trong Python. Trả về danh sách các CD.
    """
    tree = et.parse(file_name)
    root = tree.getroot()
    mstudents = []
    for item in root:
        sid = item[0].text
        age = int(item[1].text)
        major = item[2].text
        gpa = float(item[3].text)
        first = item[4][0].text
        mid = item[4][1].text
        last = item[4][2].text
        ward = item[5][0].text
        district = item[5][1].text
        city = item[5][2].text
        full_name = FullName(first, mid, last)
        address = Address(ward, district, city)
        mstudents.append(Student(sid, full_name, age, major, address, gpa))
    return mstudents


def print_students(catalog):
    """Hàm hiển thị thông tin sinh viên dạng bảng gồm các hàng, các cột."""
    print("{id:10}{major:10}{age:10}{fullname:25}{address:35}{gpa:10}".
          format(id='Mã SV', major='C.Ngành', age='Tuổi', fullname='Họ và tên',
                 address='Địa chỉ', gpa='Điểm TB'))
    for item in catalog:
        print(item)


def print_statistics(mdict):
    """Hàm hiển thị kết quả thống kê theo từng tiêu chí cụ thể."""
    for key in mdict.keys():
        print(f'{key:15}: {mdict.get(key)}')


def println():
    """Hàm hiển thị đường phân tách các phần dữ liệu."""
    print('==============================================='
          '==================================================')


option = '======================= MENU ========================\n' \
         '01. Liệt kê danh sách sinh viên.\n' \
         '02. Sắp xếp danh sách sinh viên theo tên tăng dần.\n' \
         '03. Sắp xếp danh sách sinh viên theo điểm giảm dần.\n' \
         '04. Tìm sinh viên theo mã sinh viên.\n' \
         '05. Tìm sinh viên theo tên sinh viên.\n' \
         '06. Tìm sinh viên theo điểm TB.\n' \
         '07. Xóa sinh viên theo mã sinh viên.\n' \
         '08. Liệt kê số lượng sinh viên theo quận.\n' \
         '09. Liệt kê số lượng sinh viên theo tuổi.\n' \
         '10. Liệt kê số lượng sinh viên theo điểm trung bình.\n' \
         '11. Cho biết thông tin các sinh viên có điểm cao nhất.\n' \
         '0. Kết thúc chương trình.\n' \
         'Xin mời chọn: '


def find_student_by_name(mstudents):
    """Hàm tìm và hiển thị danh sách sinh viên theo tên."""
    key = input('Nhập tên cần tìm: ')
    result = []
    for s in mstudents:  # không phân biệt chữ hoa, thường
        if s.fullname.first_name.lower() == key.lower():
            result.append(s)
    if len(result) > 0:
        println()
        print('==> Kết quả tìm kiếm: ')
        print_students(result)
    else:
        print('==> Không có kết quả tìm kiếm phù hợp.')


def find_student_by_id(mstudents):
    """Hàm tìm và hiển thị sinh viên theo mã sinh viên."""
    sid = input('Nhập mã sinh viên cần tìm: ')
    is_existed = False
    for s in mstudents:
        if s.id.lower() == sid.lower():
            print('==> Tìm thấy 1 kết quả: ')
            print(s)
            is_existed = True
            break
    if is_existed is False:
        print('==> Không tìm thấy kết quả nào.')


def find_student_by_gpa(mstudents):
    """Hàm tìm và hiển thị danh sách sinh viên theo điểm TB."""
    result = []
    gpa = float(input('Nhập điểm cần tìm: '))
    for s in mstudents:
        if s.gpa == gpa:
            result.append(s)
    if len(result) > 0:
        println()
        print('==> Kết quả tìm kiếm: ')
        print_students(result)
    else:
        print('==> Không tìm thấy kết quả nào.')


def remove_student_by_id(mstudents):
    """Hàm xóa sinh viên theo mã sinh viên."""
    sid = input('Nhập mã sinh viên cần xóa: ')
    is_existed = False
    for s in mstudents:
        if s.id.lower() == sid.lower():
            students.remove(s)
            print(f'==> Xóa thành công: sinh viên mã {sid} '
                  f'đã được xóa khỏi danh sách.')
            is_existed = True
            break
    if is_existed is False:
        print('==> Không tìm thấy sinh viên cần xóa.')


def statistics_student_by_district(mstudents):
    """Hàm thống kê sinh viên theo quận. Trả về một từ điển kết quả."""
    districts = {}
    for s in mstudents:
        if s.address.district in districts:
            districts[s.address.district] += 1
        else:
            districts[s.address.district] = 1
    return districts


def statistics_student_by_age(mstudents):
    """Hàm thống kê sinh viên theo độ tuổi và trả về một từ điển."""
    ages = {}
    for s in mstudents:
        if s.age in ages:
            ages[s.age] += 1
        else:
            ages[s.age] = 1
    return ages


def statistics_student_by_gpa(mstudents):
    """Hàm thống kê sinh viên theo mức điểm TB. Trả về một từ điển."""
    gpas = {}
    for s in mstudents:
        if s.gpa in gpas:
            gpas[s.gpa] += 1
        else:
            gpas[s.gpa] = 1
    return gpas


def find_max_gpa(mstudents):
    """Hàm tìm điểm TB cao nhất trong danh sách SV."""
    max_gpa = 0
    for e in mstudents:
        if e.gpa > max_gpa:
            max_gpa = e.gpa
    return max_gpa


def print_student_with_maxgpa(mstudents):
    """Hàm hiển thị danh sách sinh viên có điểm TB cao nhất."""
    result = []
    max_gpa = find_max_gpa(mstudents)
    for e in mstudents:
        if e.gpa == max_gpa:
            result.append(e)
    if len(result) > 0:
        println()
        print('==> Danh sách sinh viên có điểm TB cao nhất:')
        print_students(result)
    else:
        print('==> Không có sinh viên nào thỏa mãn điểm cao nhất.')


if __name__ == '__main__':
    file = 'student.xml'
    students = parse_xml(file)
    while True:
        choice = int(input(option))
        match choice:
            case 0:
                print('==> Chương trình kết thúc <==')
                break
            case 1:
                println()
                print('==> Danh sách các sinh viên: ')
                print_students(students)
            case 2:
                students.sort(key=lambda s: (s.fullname.first_name, s.fullname.last_name))
                println()
                print('==> Danh sách các sinh viên sau khi sắp xếp: ')
                print_students(students)
            case 3:
                students.sort(key=lambda s: (-s.gpa, s.age))
                println()
                print('==> Danh sách các sinh viên sau khi sắp xếp: ')
                print_students(students)
            case 4:
                find_student_by_id(students)
            case 5:
                find_student_by_name(students)
            case 6:
                find_student_by_gpa(students)
            case 7:
                remove_student_by_id(students)
            case 8:
                print('==> Số lượng sinh viên theo từng quận:')
                dct = statistics_student_by_district(students)
                print_statistics(dct)
            case 9:
                print('==> Số lượng sinh viên theo độ tuổi:')
                dct = statistics_student_by_age(students)
                print_statistics(dct)
            case 10:
                print('==> Số lượng sinh viên theo mức điểm TB:')
                dct = statistics_student_by_gpa(students)
                print_statistics(dct)
            case 11:
                print_student_with_maxgpa(students)
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng chọn lại.')
