from person import Person


class Student(Person):
    """Lớp mô tả thông tin sinh viên"""
    AUTO_ID = 1000

    def __init__(self, pid=None, full_name='',
                 birth_date='', sid=None, gpa='', major=''):
        super().__init__(pid, full_name, birth_date)
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
        self.__gpa = value

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
               f'{self.birth_date:20}{self.student_id:15}{self.major:15}' \
               f'{self.gpa:<15}'
