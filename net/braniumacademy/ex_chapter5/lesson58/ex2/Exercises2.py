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


def create_teacher_id():
    """Tạo mã giảng viên tự động tăng từ GV1001."""
    teacher_id = f'GV{Teacher.AUTO_ID}'
    Teacher.AUTO_ID += 1
    return teacher_id


class Teacher(Person):
    """Lớp mô tả thông tin giảng viên."""
    AUTO_ID = 10001

    def __init__(self, pid='', full_name=None, dob=None,
                 teacher_id=None, salary=0, expertise=''):
        super().__init__(pid, full_name, dob)
        if teacher_id is None:
            self.teacher_id = self.__teacher_id = create_teacher_id()
        else:
            self.teacher_id = teacher_id
        self.__salary = salary
        self.__expertise = expertise

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        self.__teacher_id = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def expertise(self):
        return self.__expertise

    @expertise.setter
    def expertise(self, value):
        self.__expertise = value

    def __str__(self):
        return f'{super().__str__()}{self.teacher_id:10}{self.salary < 10}' \
               f'{self.expertise:20}'

    def __eq__(self, other):
        """Hai giảng viên coi là trùng nhau nếu cùng mã giảng viên."""
        return other.teacher_id == self.teacher_id


class Transcript:
    AUTO_ID = 100

    """Lớp mô tả thông tin về bảng điểm."""

    def __int__(self, transcript_id=0, student=None, gpa=0, capacity=''):
        if transcript_id == 0:
            self.__transcript_id = Transcript.AUTO_ID
            Transcript.AUTO_ID += 1
        else:
            self.__transcript_id = transcript_id
        self.__student = student
        self.__gpa = gpa
        self.__capacity = capacity

    @property
    def transcript_id(self):
        return self.__transcript_id

    @transcript_id.setter
    def transcript_id(self, value):
        self.__transcript_id = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def __str__(self):
        return f'{self.transcript_id:10}{self.student.student_id:10}' \
               f'{self.gpa:<10}{self.capacity:15}'

    def __eq__(self, other):
        return self.__transcript_id == other.transcript_id


def create_course_id():
    couse_id = f'C{Course.AUTO_ID}'
    Course.AUTO_ID += 1
    return couse_id


class Course:
    """Lớp mô tả thông tin lớp học phần."""
    AUTO_ID = 100

    def __int__(self, couse_id='', subject=None,
                teacher=None, room='', transcripts=None):
        if couse_id == '':
            self.__couse_id = create_course_id()
        else:
            self.__couse_id = couse_id
        self.__subject = subject
        self.__teacher = teacher
        self.__room = room
        self.__transcripts = transcripts

    @property
    def course_id(self):
        return self.__couse_id

    @course_id.setter
    def course_id(self, value):
        self.__couse_id = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        self.__teacher = value

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        self.__room = value

    @property
    def transcripts(self):
        return self.__transcripts

    @transcripts.setter
    def transcripts(self, value):
        self.__transcripts = value

    def __str__(self):
        return f'{self.course_id:10}{self.subject.subject_id:10}' \
               f'{self.subject.name:30}{self.teacher.teacher_id:10}' \
               f'{self.teacher.full_name:30}{self.room:10}'

    def __eq__(self, other):
        return other.course_id == self.course_id
