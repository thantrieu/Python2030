import json
from collections import OrderedDict
from operator import itemgetter


class BirthDate:
    """Lớp mô tả thông tin về ngày sinh."""

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, value):
        self.__day = value

    @month.setter
    def month(self, value):
        self.__month = value

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def birth_date(self):
        return self.__str__()

    def __str__(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'


class Student:
    """Lớp mô tả thông tin của học sinh."""

    def __init__(self, sid, name, birth_date, gpa):
        self.__name = name
        self.__gpa = gpa
        self.__student_id = sid
        self.__birth_date = birth_date

    @property
    def student_id(self):
        return self.__student_id

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def gpa(self):
        return self.__gpa

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'{self.student_id:10}{self.name:30}' \
               f'{self.birth_date.birth_date:15}{self.gpa:<10.2f}'


def decode_birth_date(dct):
    if 'day' in dct:
        return BirthDate(int(dct['day']), int(dct['month']), int(dct['year']))
    else:
        return None


def decode_student(dct):
    if 'birth_date' in dct:
        birth_date = decode_birth_date(dct['birth_date'])
        return Student(dct['id'], dct['name'], birth_date, float(dct['gpa']))
    else:
        return dct


def listed_students(mstudents):
    print(f'{"Mã HS":10}{"Họ và tên":30}{"Ngày sinh":15}{"Điểm TB":10}')
    for student in mstudents:
        print(student)


def listed_students_by_gpa(mstudents):
    result_dict = {}
    mstudents.sort(key=lambda x: -x.gpa)  # sắp xếp danh sách học sinh theo điểm giảm dần
    for student in mstudents:
        if student.gpa in result_dict:  # nếu điểm x đã tồn tại trong dict
            result_dict[student.gpa] += 1  # tăng biến đếm của đầu điểm đó lên
        else:
            result_dict[student.gpa] = 1  # ngược lại, thêm mới đầu điểm
    # Hiện kết quả
    print('==> Số lượng học sinh theo từng đầu điểm: ')
    for key in result_dict.keys():
        print(f'{key}: {result_dict[key]}')


def get_name(fname):
    """Hàm tách lấy tên trong họ và tên."""
    words = fname.split()
    return words[len(words) - 1]


def find_student_max_gpa(mstudents):
    """Hàm tìm học sinh có điểm TB cao nhất.
        B1: sắp xếp danh sách học sinh giảm dần điểm TB.
        B2: lấy điểm TB max.
        B3: duyệt từ đầu danh sách và kiểm tra, nếu điểm hs là max thì in ra.
        B4: nếu điểm tb khác max thì kết thúc.
    """
    mstudents.sort(key=lambda x: -x.gpa)
    max_gpa = mstudents[0].gpa
    print('==> Danh sách học sinh có điểm TB cao nhất: ')
    print(f'{"Mã HS":10}{"Họ và tên":30}{"Ngày sinh":15}{"Điểm TB":10}')
    for student in mstudents:
        if student.gpa == max_gpa:
            print(student)
        else:
            break


def listed_student_with_givent_gpa(mstudents):
    gpa = float(input('Nhập điểm cần tìm: '))
    result = []  # danh sách kết quả tìm kiếm
    for student in mstudents:
        if student.gpa == gpa:  # nếu tìm thấy
            result.append(student)  # thêm học sinh vào danh sách kết quả
    print(f'==> Danh sách học sinh có điểm bằng {gpa}: ')
    listed_students(result)


def listed_student_by_birth_month(mstudents):
    result_dict = {}
    for student in mstudents:
        if student.birth_date.month in result_dict:
            result_dict[student.birth_date.month] += 1
        else:
            result_dict[student.birth_date.month] = 1
    ordered_dict = OrderedDict(sorted(result_dict.items(), key=itemgetter(1)))
    # Hiện kết quả
    print('==> Số lượng học sinh theo tháng sinh: ')
    for key in ordered_dict.keys():
        print(f'{key:<2}{ordered_dict[key]:10}')


def listed_student_by_birth_day(mstudents):
    result_dict = {}
    for student in mstudents:
        if student.birth_date.day in result_dict:
            result_dict[student.birth_date.day] += 1
        else:
            result_dict[student.birth_date.day] = 1
    ordered_dict = OrderedDict(sorted(result_dict.items(), key=itemgetter(1), reverse=True))
    # Hiện kết quả
    print('==> Số lượng học sinh theo ngày sinh: ')
    for key in ordered_dict.keys():
        print(f'{key:<2}{ordered_dict[key]:10}')


def remove_by_id(mstudents):
    student_id = input('Nhập mã học sinh: ').upper()
    success = False
    for x in range(len(mstudents)):
        if mstudents[x].student_id == student_id:
            mstudents.pop(x)
            success = True
            break  # xóa xong thì kết thúc vòng lặp vì chỉ có tối đa duy nhất 01 học sinh có mã đã nhập
    if success is True:
        print('==> Xóa thành công! <==')
    else:
        print('==> Xóa thất bạ! <==')
    return success


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
