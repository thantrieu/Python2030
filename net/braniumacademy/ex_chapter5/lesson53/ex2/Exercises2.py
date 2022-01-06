class Person:
    def __init__(self, pid, full_name, address, email):
        self.person_id = pid
        self.full_name = full_name
        self.address = address
        self.email = email

    def eat(self):
        print(f'{self.full_name} is eating some food...')

    def sleep(self):
        print(f'{self.full_name} is sleeping on the bed.')

    def relax(self, thing):
        print(f'{self.full_name} is relaxing with {thing}.')

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')


class Student(Person):
    def __init__(self, pid, full_name, address, email, sid, gpa, major):
        super().__init__(pid, full_name, address, email)
        self.student_id = sid
        self.gpa = gpa
        self.major = major

    def do_homework(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' homework.')

    def do_exam(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' final exam.')

    def payfee(self, amount):
        print(f'Student {self.full_name} paid {amount}$ for tuition fee.')


class GraduatedStudent(Student):
    def __init__(self, year, capacity, salary,
                 pid='', full_name='', address='',
                 email='', sid='SV001', gpa=0.0, major='CNTT'):
        super().__init__(pid, full_name, address, email, sid, gpa, major)
        self.salary = salary
        self.year = year
        self.capacity = capacity

    def goto_work(self, by):
        print(f'{self.full_name} going to work by {by}')

    def receive_certificate(self, level):
        print(f'{self.full_name} receiving his {level} certificate.')


class UnderGraduatedStudent(Student):
    def __init__(self, year, failed, pid='', full_name='',
                 address='', email='', sid='', gpa=0.0, major='CNTT'):
        super().__init__(pid, full_name, address, email, sid, gpa, major)
        self.year = year
        self.failed = failed

    def register(self, subject):
        print(f'Student {self.full_name} is registering {subject}')

    def do_intern(self, company):
        print(f'Student {self.full_name} is working at {company}.')

    def restudy(self, subject):
        print(f'Student {self.full_name} is restudying {subject}')


class Lecturer(Person):
    def __init__(self, lid, level, salary, role,
                 pid='', full_name='', address='', email=''):
        super().__init__(pid, full_name, address, email)
        self.salary = salary
        self.lecturer_id = lid
        self.role = role
        self.level = level

    def teach(self, subject):
        print(f'Lecturer {self.full_name} is teaching {subject}.')

    def receive_salary(self, amount):
        print(f'Lecturer {self.full_name}\'s real salary this month is {amount}.')

    def mark_exam(self, subject):
        print(f'Lecturer {self.full_name} is marking {subject} exam.')

    def create_exam(self, subject):
        print(f'Lecturer {self.full_name} is creating {subject}\'s final exam.')


if __name__ == '__main__':
    # tạo đối tượng của Person
    print('-------------------------------------------------------------')
    person = Person('0123456', 'Trần Quang Lâm', 'Hà Nội', 'quanghung@xmail.com')
    person.eat()
    person.work('fix bug')
    person.sleep()
    person.relax('play video game')

    # tạo đối tượng của Student
    print('-------------------------------------------------------------')
    student = Student('0231546987', 'Nguyễn Thùy Anh',
                      'Cà Mau', 'thuyanh@xmail.com', 'SV001', 3.26, 'CNTT')
    student.do_exam('Python')
    student.payfee(500)
    student.do_homework('Java')
    student.relax('Coding')

    # tạo đối tượng của GraduatedStudent
    print('-------------------------------------------------------------')
    g_student = GraduatedStudent(2025, 'Good', 15200, full_name='Mai Thanh Tùng')
    g_student.receive_certificate('Very good')
    g_student.goto_work('Car')

    # tạo đối tượng của UnderGraduatedStudent
    print('-------------------------------------------------------------')
    u_student = UnderGraduatedStudent(3, 10, full_name='Trương Quỳnh Anh')
    u_student.register('C#')
    u_student.do_intern('Branium')
    u_student.restudy('C++')

    # tạo đối tượng của Lecturer
    print('-------------------------------------------------------------')
    lecturer = Lecturer('L001', 'Professor', 50500, 'Main teacher', full_name='Đỗ Quang Sáng')
    lecturer.create_exam('Python OOP')
    lecturer.receive_salary(16800)
    lecturer.mark_exam('ASP.NET')
    print('-------------------------------------------------------------')

