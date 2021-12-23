class Student:
    """Lớp mô tả thông tin và hành động của sinh viên"""

    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def do_exam(self, subject):
        print(f'Student {self.name} is doing {subject} exam.')

    def work(self):
        print(f'Student {self.name} is working.')

    def do_homework(self, subject):
        print(f'Student {self.name} is doing {subject} homework.')


huong = Student("SV001", "Huong", "CNTT")
lan = Student("SV005", "Lan", "QTKD")
huong.do_exam('Python')
lan.do_homework('Math')
huong.work()
print(f'{huong.name}\'s student id: {huong.student_id}')
print(f'{huong.name}\'s student major: {huong.major}')
