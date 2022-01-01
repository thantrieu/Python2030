import json

from net.braniumacademy.chapter6.student import Address, FullName, Student


def decode_address(address):
    if address is not None and len(address) > 0:
        return Address(address["wards"], address["district"], address["city"])
    else:
        return address


def decode_full_name(fname):
    if fname is not None and len(fname) > 0:
        return FullName(fname["first"], fname["mid"], fname["last"])
    else:
        return fname


def decode_student(data):
    # if data is not None and len(data) > 0:
    student_id = data["id"]
    name = decode_full_name(data["full_name"])
    address = decode_address(data["address"])
    age = int(data["age"])
    gpa = float(data["gpa"])
    major = data["major"]
    return Student(student_id, name, age, major, address, gpa)
    # else:
    # return data


with open('student_data.json', encoding='UTF-8') as student_data:
    data = student_data.read()
    students = json.loads(data, object_hook=decode_student)
    print(students)
