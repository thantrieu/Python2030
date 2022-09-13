from person import Person
from filters import *


def create_id():
    student_id = f'SV{Student.AUTO_ID}'
    Student.AUTO_ID += 1
    return student_id


class Student(Person):
    AUTO_ID = 1000

    def __init__(self, pid='', full_name=None, dob=None,
                 student_id=None, major='', gpa=0.0):
        super().__init__(pid, full_name, dob)
        self.student_id = student_id
        self.gpa = gpa
        self.major = major

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        try:
            if is_gpa_valid(f'{value}'):
                self.__gpa = value
        except GpaError as e:
            print(e)
            self.__gpa = 0

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if value is None:
            self.__student_id = create_id()
        else:
            try:
                if is_student_id_valid(value):
                    self.__student_id = value.upper()
            except StudentIdError as e:
                print(e)
                self.__student_id = None

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
        return f'{super().__str__()}{self.student_id:15}{self.gpa:<15.2}' \
               f'{self.major:15}'

    def __eq__(self, other):
        """Hai sinh viên coi là trùng nhau nếu cùng mã sinh viên."""
        return other.student_id == self.student_id

    def output_data_format(self):
        return f'{self.person_id}\n{self.full_name.full_name}\n' \
               f'{self.birth_date.strftime("%d/%m/%Y")}\n' \
               f'{self.student_id}\n{self.gpa}\n{self.major}\n'

    @major.setter
    def major(self, value):
        self.__major = value
