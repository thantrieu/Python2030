import xml.etree.ElementTree as et
from operator import itemgetter
from collections import OrderedDict
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
    for item in catalog:
        print(item)


def statistics_by_zone(catalog):
    zones = {}
    for plant in catalog:
        if plant.zone in zones:
            zones[plant.zone] += 1
        else:
            zones[plant.zone] = 1
    return OrderedDict(sorted(zones.items(), key=itemgetter(0), reverse=True))


def print_statistics(dct):
    for key in dct.keys():
        print(f'{key:15}: {dct.get(key)}')


if __name__ == '__main__':
    file = 'student.xml'
    students = parse_xml(file)
    print('====================================')
    print('==> Danh sách các sinh viên: ')
    print_students(students)
    # print('====================================')
    # print('==> Danh sách các thực vật theo giá tăng dần: ')
    # students.sort(key=lambda x: x.price)
    # print('====================================')
    # print('==> Danh sách số lượng các loài thực vật theo zone: ')
    # result = statistics_by_zone(students)
    # print_statistics(result)
