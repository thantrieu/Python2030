from person import Person
from exercises2_utils import is_gpa_valid


class Student(Person):
    """Lớp mô tả thông tin sinh viên"""
    AUTO_ID = 1001

    def __init__(self, sid=None, gpa='', major=''):
        self.student_id = sid
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
            self.__student_id = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if is_gpa_valid(value):
            self.__gpa = value
        else:
            self.__gpa = 0.0

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
