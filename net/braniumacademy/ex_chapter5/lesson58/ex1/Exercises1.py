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

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Person:
    def __init__(self, pid, full_name, dob):
        self.__person_id = pid
        self.__full_name = full_name
        self.__birth_date = dob

    @property
    def person_id(self):
        return self.__person_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def birth_date(self):
        return self.__birth_date

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')

    def show_info(self):
        print(self)

    def __str__(self):
        return f'{self.person_id:15}{self.full_name.full_name:25}' \
               f'{self.birth_date:12}'


def create_id():
    student_id = f'SV{Student.AUTO_ID}'
    Student.AUTO_ID += 1
    return student_id


class Student(Person):
    AUTO_ID = 1000

    def __init__(self, pid='', full_name=None,
                 dob=None, gpa=0.0, major='', student_id=None):
        super().__init__(pid, full_name, dob)
        if student_id is None:
            self.student_id = self.__student_id = create_id()
        else:
            self.student_id = student_id
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

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value.upper()

    @property
    def major(self):
        return self.__major

    def do_exam(self, subject):
        print(f'Student {self.full_name} is doing {subject}\' final exam.')

    def register(self, subject):
        print(f'Student {self.full_name} registered subject {subject}.')

    def show_info(self):
        print(self)

    def __str__(self):
        return f'{super().__str__()}{self.student_id:10}{self.gpa:<10}' \
               f'{self.major:15}'

    def __eq__(self, other):
        """Hai sinh viên coi là trùng nhau nếu cùng mã sinh viên."""
        return other.student_id == self.student_id


def create_subject_id():
    sid = Subject.AUTO_ID
    Subject.AUTO_ID += 1
    return sid


class Subject:
    AUTO_ID = 1000

    def __init__(self, name='', credit=0, subject_id=0):
        if subject_id == 0:
            self.__subject_id = create_subject_id()
        else:
            self.__subject_id = subject_id
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

    def __str__(self):
        return f'{self.subject_id:<10}{self.name:15}{self.credit:<10}'

    def __eq__(self, other):
        """Hai môn học gọi là trùng khớp nếu chúng cùng mã môn."""
        return self.subject_id == other.subject_id


def create_register_id():
    rid = Register.AUTO_ID
    Register.AUTO_ID += 1
    return rid


class Register:
    AUTO_ID = 100

    def __init__(self, student=None, subject=None):
        self.__register_id = create_register_id()
        self.__register_date = datetime.datetime.now()  # Thời gian đăng ký lấy từ hệ thống
        self.__subject = subject
        self.__student = student

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

    def __str__(self):
        date_str = f'{self.register_date.day:02}/{self.register_date.month:02}/' \
                   f'{self.register_date.year:4} {self.register_date.hour:02}:' \
                   f'{self.register_date.minute:02}:{self.register_date.second:02}'
        return f'{self.register_id:<10}{self.student.student_id:10}' \
               f'{self.student.full_name.full_name:25}' \
               f'{self.subject.subject_id:<10}{self.subject.name:15}' \
               f'{date_str:25}'

    def __eq__(self, other):
        """Hai bản đăng ký gọi là trùng khớp nếu chúng thuộc về cùng
            1 sinh viên và cùng môn học.
        """
        return self.subject.subject_id == other.subject.subject_id and \
            self.student.student_id == other.student.student_id
