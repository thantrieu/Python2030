import json
from net.braniumacademy.chapter6.student import Address, FullName, Student


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


def print_data(mdata):
    for e in mdata:
        print(e)


with open('student_data.json', encoding='UTF-8') as student_data:
    data = student_data.read()
    students = json.loads(data, object_hook=decode_student)
    print_data(students)
