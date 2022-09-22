from person import Person
from filter import *


class Student(Person):
    """Lớp mô tả thông tin sinh viên"""
    AUTO_ID = 1000

    def __init__(self, pid=None, full_name='', birth_date='',
                 address='', sid=None, email='', gpa='', major=''):
        super().__init__(pid, full_name, birth_date, address)
        self.student_id = sid
        self.email = email
        self.gpa = gpa
        self.major = major

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if value is None:
            self.__student_id = f'SV{Student.AUTO_ID}'
            Student.AUTO_ID += 1
        else:
            try:
                if is_student_id_valid(value):
                    self.__student_id = value
            except StudentIdError as e:
                print(e)
                self.__student_id = None

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

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
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    def show_info(self):
        super().show_info()
        print(f'Mã sinh viên: {self.student_id}')
        print(f'Điểm Gpa: {self.gpa}')
        print(f'Chuyên ngành: {self.major}')

    def do_exam(self, subject):
        print(f'Sinh viên {self.student_id} đang làm bài thi môn {subject}')

    def register(self, subject):
        print(f'Sinh viên {self.student_id} đang đăng ký môn học {subject}')

    def __str__(self):
        return f'{self.person_id:15}{self.full_name.__str__():30}' \
               f'{self.address.__str__():35}' \
               f'{self.birth_date.__str__():20}{self.student_id:15}' \
               f'{self.email:30}{self.major:15}{self.gpa:<15}'
