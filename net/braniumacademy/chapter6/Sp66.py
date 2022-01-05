import json
from net.braniumacademy.chapter6.Lesson65 import decode_student
from net.braniumacademy.chapter6.student \
    import Student, FullName, Address


def create_student():
    full_name = FullName("Thanh", "Văn", "Hoàng")
    address = Address("Phú Thượng", "Hoàng Mai", "Hà Nội")
    student_id = "SV001"
    age = 20
    gpa = 3.56
    major = "CNTT"
    return Student(student_id, full_name, age, major, address, gpa)


class StudentEncoder(json.JSONEncoder):
    """This class encode student data to JSON format."""

    def default(self, obj):
        return obj.__dict__


with open('student_data.json', encoding='UTF-8') as student_data, \
        open('student_data3.json', 'w', encoding='UTF-8') as student_data3:
    data = student_data.read()
    students = json.loads(data, object_hook=decode_student)
    encoded_data = json.dumps(students, cls=StudentEncoder, indent=4, ensure_ascii=False)
    student_data3.write(encoded_data)
