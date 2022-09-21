from datetime import datetime
from filter import *


class Register:
    """Lớp mô tả lớp đăng ký"""
    AUTO_ID = 100

    def __init__(self, cid=None, rtime=None, student=None, subject=None):
        self.register_id = cid
        self.register_time = rtime
        self.student = student
        self.subject = subject

    @property
    def register_id(self):
        return self.__register_id

    @register_id.setter
    def register_id(self, value):
        if value is None:
            self.__register_id = Register.AUTO_ID
            Register.AUTO_ID += 1
        else:
            try:
                if is_register_id_valid(f'{value}'):
                    self.__register_id = value
            except RegisterIdError as e:
                print(e)
                self.__register_id = 0

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        if value is not None:
            if isinstance(value, str):  # nếu là string thì ta chuyển sang datetime
                self.__register_time = datetime.strptime(value, '%d/%m/%Y %H:%M:%S')
            if isinstance(value, datetime):  # nếu sẵn là datetime ta chỉ cần gán thẳng
                self.__register_time = value
        else:
            self.__register_time = datetime.now()  # về date time bạn xem chương 9 nhé

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    def __str__(self):
        return f'{self.register_id:<10}{self.student.student_id:15}' \
               f'{self.student.full_name.__str__():35}{self.subject.subject_id:<15}' \
               f'{self.subject.subject_name:35}' \
               f'{self.register_time.strftime("%d/%m/%Y %H:%M:%S"):30}'
