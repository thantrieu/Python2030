from student import Person
from filters import *


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
        self.teacher_id = teacher_id
        self.salary = salary
        self.expertise = expertise

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if value is None:
            self.__teacher_id = create_teacher_id()
        else:
            try:
                if is_teacher_id_valid(value):
                    self.__teacher_id = value
            except TeacherIdError as e:
                print(e)
                self.__teacher_id = None

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        try:
            if is_salary_valid(f'{value}'):
                self.__salary = value
        except SalaryError as e:
            print(e)
            self.__salary = 0

    @property
    def expertise(self):
        return self.__expertise

    @expertise.setter
    def expertise(self, value):
        self.__expertise = value

    def __str__(self):
        return f'{super().__str__()}{self.teacher_id:15}' \
               f'{round(self.salary, 0):<15}' \
               f'{self.expertise:25}'

    def __eq__(self, other):
        """Hai giảng viên coi là trùng nhau nếu cùng mã giảng viên."""
        return other.teacher_id == self.teacher_id

    def output_data_format(self):
        return f'{self.person_id}\n{self.full_name.full_name}\n' \
               f'{self.birth_date.strftime("%d/%m/%Y")}\n' \
               f'{self.teacher_id}\n{self.salary}\n{self.expertise}\n'
