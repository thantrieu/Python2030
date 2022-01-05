import json
import urllib.error
from urllib.request import urlopen, Request
from net.braniumacademy.chapter6.student import Address, FullName, Student


def decode_address(address):
    if address is not None and len(address) > 0:
        return Address(address["wards"], address["district"], address["city"])
    else:
        return None


def decode_full_name(fname):
    if fname is not None and len(fname) > 0:
        return FullName(fname["first"], fname["mid"], fname["last"])
    else:
        return None


def decode_student(dct):
    if 'full_name' in dct:
        student_id = dct["id"]
        name = decode_full_name(dct["full_name"])
        address = decode_address(dct["address"])
        age = int(dct["age"])
        gpa = float(dct["gpa"])
        major = dct["major"]
        return Student(student_id, name, age, major, address, gpa)
    else:
        return dct


def print_data(mdata):
    for e in data:
        print(e)


url = 'https://braniumacademy.net/student_data.json'
try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}, method='GET')
    data = str(json.loads(urlopen(req).read()))
    students = json.loads(data, object_hook=decode_student)
    print_data(students)
except urllib.error.HTTPError as e:
    print(e)
