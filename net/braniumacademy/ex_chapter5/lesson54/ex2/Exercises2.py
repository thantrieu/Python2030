class Person:
    def __init__(self, pid, full_name, address, email, dob):
        self.person_id = pid
        self.full_name = full_name
        self.address = address
        self.email = email
        self.birth_date = dob

    def eat(self):
        print(f'{self.full_name} is eating some food...')

    def sleep(self):
        print(f'{self.full_name} is sleeping on the bed.')

    def relax(self, thing):
        print(f'{self.full_name} is relaxing with {thing}.')

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')

    def show_info(self):
        print(f'Person[id={self.person_id}, full_name={self.full_name},\n'
              f'address={self.address}, email={self.email},'
              f' birth_date={self.birth_date}]')


class Student(Person):
    def __init__(self, pid, full_name, address, email, sid, gpa, major, dob):
        super().__init__(pid, full_name, address, email, dob)
        self.student_id = sid
        self.gpa = gpa
        self.major = major

    def do_homework(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' homework.')

    def do_exam(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' final exam.')

    def payfee(self, amount):
        print(f'Student {self.full_name} paid {amount}$ for tuition fee.')

    def show_info(self):
        print(f'Student[student_id={self.student_id}, gpa={self.gpa},\n'
              f'major={self.major}, id={self.person_id},\n'
              f'full_name={self.full_name}, address={self.address},\n'
              f'email={self.email}, birth_date={self.birth_date}]')


class GraduatedStudent(Student):
    def __init__(self, year, capacity, salary,
                 pid='', full_name='', address='',
                 email='', sid='SV001', gpa=0.0,
                 major='CNTT', dob='01/01/2020'):
        super().__init__(pid, full_name, address,
                         email, sid, gpa, major, dob)
        self.salary = salary
        self.year = year
        self.capacity = capacity

    def goto_work(self, by):
        print(f'{self.full_name} going to work by {by}')

    def receive_certificate(self, level):
        print(f'{self.full_name} receiving his {level} certificate.')

    def show_info(self):
        print(f'GraduatedStudent[student_id={self.student_id}, '
              f'gpa={self.gpa}, '
              f'major={self.major}, id={self.person_id},\n'
              f'full_name={self.full_name}, address={self.address},\n'
              f'email={self.email}, birth_date={self.birth_date},\n'
              f'year={self.year}, capacity={self.capacity}, '
              f'salary={self.salary}]')


class UnderGraduatedStudent(Student):
    def __init__(self, year, failed, pid='', full_name='',
                 address='', email='', sid='', gpa=0.0,
                 major='CNTT', dob='01/01/2020'):
        super().__init__(pid, full_name, address, email, sid, gpa, major, dob)
        self.year = year
        self.failed = failed

    def register(self, subject):
        print(f'Student {self.full_name} is registering {subject}')

    def do_intern(self, company):
        print(f'Student {self.full_name} is working at {company}.')

    def restudy(self, subject):
        print(f'Student {self.full_name} is restudying {subject}')

    def show_info(self):
        print(f'UnderGraduatedStudent[student_id={self.student_id}, '
              f'gpa={self.gpa}, '
              f'major={self.major}, id={self.person_id},\n'
              f'full_name={self.full_name}, address={self.address},\n'
              f'email={self.email}, birth_date={self.birth_date},\n'
              f'year={self.year}, failed={self.failed}]')


class Lecturer(Person):
    def __init__(self, lid, level, salary, role,
                 pid='', full_name='', address='', email='',
                 dob='01/01/2020'):
        super().__init__(pid, full_name, address, email, dob)
        self.salary = salary
        self.lecturer_id = lid
        self.role = role
        self.level = level

    def teach(self, subject):
        print(f'Lecturer {self.full_name} is teaching {subject}.')

    def receive_salary(self, amount):
        print(f'Lecturer {self.full_name}\'s '
              f'real salary this month is {amount}.')

    def mark_exam(self, subject):
        print(f'Lecturer {self.full_name} is marking {subject} exam.')

    def create_exam(self, subject):
        print(f'Lecturer {self.full_name} '
              f'is creating {subject}\'s final exam.')

    def show_info(self):
        print(f'Lecturer[lecturer_id={self.lecturer_id}, level={self.level},\n'
              f'salary={self.salary}, role={self.role}, id={self.person_id},\n'
              f'full_name={self.full_name}, address={self.address},\n'
              f'email={self.email}, birth_date={self.birth_date}]')


if __name__ == '__main__':
    # tạo đối tượng của Person
    print('-------------------------------------------------------------')
    person = Person('0123456', 'Trần Quang Lâm', 'Hà Nội',
                    'quanghung@xmail.com', '10/08/2000')
    person.eat()
    person.work('fix bug')
    person.sleep()
    person.relax('play video game')
    person.show_info()

    # tạo đối tượng của Student
    print('-------------------------------------------------------------')
    student = Student('0231546987', 'Nguyễn Thùy Anh',
                      'Cà Mau', 'thuyanh@xmail.com',
                      'SV001', 3.26, 'CNTT', '10/10/2005')
    student.do_exam('Python')
    student.payfee(500)
    student.do_homework('Java')
    student.relax('Coding')
    student.show_info()

    # tạo đối tượng của GraduatedStudent
    print('-------------------------------------------------------------')
    g_student = GraduatedStudent(2025, 'Good',
                                 15200, full_name='Mai Thanh Tùng')
    g_student.receive_certificate('Very good')
    g_student.goto_work('Car')
    g_student.show_info()

    # tạo đối tượng của UnderGraduatedStudent
    print('-------------------------------------------------------------')
    u_student = UnderGraduatedStudent(3, 10, full_name='Trương Quỳnh Anh')
    u_student.register('C#')
    u_student.do_intern('Branium')
    u_student.restudy('C++')
    u_student.show_info()

    # tạo đối tượng của Lecturer
    print('-------------------------------------------------------------')
    lecturer = Lecturer('L001', 'Professor', 50500,
                        'Main teacher', full_name='Đỗ Quang Sáng')
    lecturer.create_exam('Python OOP')
    lecturer.receive_salary(16800)
    lecturer.mark_exam('ASP.NET')
    lecturer.show_info()
    print('-------------------------------------------------------------')
