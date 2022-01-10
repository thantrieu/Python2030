import datetime


class FullName:
    def __init__(self, first, mid, last):
        self.__first = first
        self.__last = last
        self.__mid = mid

    @property
    def first_name(self):
        return self.__first

    @property
    def mid_name(self):
        return self.__mid

    @property
    def last_name(self):
        return self.__last

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Person:
    def __init__(self, pid, full_name, address, dob):
        self.__person_id = pid
        self.__full_name = full_name
        self.__address = address
        self.__birth_date = dob

    @property
    def person_id(self):
        return self.__person_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def address(self):
        return self.__address

    @property
    def birth_date(self):
        return self.__birth_date

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')

    def show_info(self):
        print(f'Person[id={self.person_id}, full_name={self.full_name},\n'
              f'address={self.address}, birth_date={self.birth_date}]')


class Student(Person):
    AUTO_ID = 1000

    def __init__(self, pid, full_name, address, dob, gpa, major):
        super().__init__(pid, full_name, address, dob)
        self.__student_id = self.__create_id()
        self.__gpa = gpa
        self.__major = major

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def major(self):
        return self.__major

    def __create_id(self):
        student_id = f'SV{Student.AUTO_ID}'
        Student.AUTO_ID += 1
        return student_id

    def do_exam(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' final exam.')

    def register(self, subject):
        print(f'Student {self.full_name} registered subject {subject}.')

    def show_info(self):
        print(f'Student[student_id={self.student_id}, gpa={self.gpa},\n'
              f'major={self.major}, id={self.person_id},\n'
              f'full_name={self.full_name}, address={self.address}, \n'
              f'birth_date={self.birth_date}]')


class Subject:
    AUTO_ID = 1000

    def __init__(self, name, credit):
        self.__subject_id = self.__create_subject_id()
        self.__name = name
        self.__credit = credit

    @property
    def name(self):
        return self.__name

    @property
    def credit(self):
        return self.__credit

    @property
    def subject_id(self):
        return self.__subject_id

    def __create_subject_id(self):
        sid = Subject.AUTO_ID
        Subject.AUTO_ID += 1
        return sid


class Register:
    AUTO_ID = 100

    def __init__(self, student=None, subject=None):
        self.__register_id = self.create_register_id()
        self.__register_date = datetime.datetime.now()  # Thời gian đăng ký lấy từ hệ thống
        self.__subject = subject
        self.__student = student

    def create_register_id(self):
        rid = Register.AUTO_ID
        Register.AUTO_ID += 1
        return rid

    @property
    def register_id(self):
        return self.__register_id

    @property
    def register_date(self):
        return self.__register_date

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

