import json
from net.braniumacademy.chapter6.Lesson65 import decode_student
from net.braniumacademy.chapter6.student import FullName, Address, Student


def create_student():
    full_name = FullName("Thanh", "Văn", "Hoàng")
    address = Address("Phú Thượng", "Hoàng Mai", "Hà Nội")
    student_id = "SV001"
    age = 20
    gpa = 3.56
    major = "CNTT"
    return Student(student_id, full_name, age, major, address, gpa)


class StudentJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


with open('student_data3.json', 'w', encoding='UTF-8') as student_data3, \
        open('student_data.json', encoding='UTF-8') as student_data:
    data = student_data.read()
    students = json.loads(data, object_hook=decode_student)
    encoded_data = json.dumps(students, cls=StudentJSONEncoder,
                              indent=4, ensure_ascii=False, sort_keys=True)
    student_data3.write(encoded_data)
