from exercises2_utils import *


class Person:
    """Lớp mô tả thông tin người"""

    def __init__(self, pid=None, name='', birth_date=''):
        self.person_id = pid
        self.full_name = name
        self.birth_date = birth_date

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value):
        if is_person_id_valid(value):
            self.__person_id = value
        else:
            raise ValueError('Số CMND/CCCD không hợp lệ')

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        if is_name_valid(value):
            self.__full_name = value
        else:
            self.__full_name = 'No Name'
            raise ValueError('Họ và tên không hợp lệ')

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if is_birth_date_valid(value):
            self.__birth_date = value
        else:
            self.__birth_date = None
            raise ValueError('Ngày sinh không hợp lệ')

    def work(self, task):
        print(self.full_name + ' is doing ' + task)

    def show_info(self):
        print(f'CMND/CCCD: {self.person_id}')
        print(f'Họ và tên: {self.full_name}')
        print(f'Ngày sinh: {self.birth_date}')
