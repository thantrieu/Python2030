from student import Person


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
        return f'{super().__str__()}{self.teacher_id:10}{round(self.salary, 0):<10}' \
               f'{self.expertise:20}'

    def __eq__(self, other):
        """Hai giảng viên coi là trùng nhau nếu cùng mã giảng viên."""
        return other.teacher_id == self.teacher_id
