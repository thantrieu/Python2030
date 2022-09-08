class FullName:
    """Lớp mô tả thông tin đầy đủ của họ và tên."""

    def __init__(self, first='', last='', mid=''):
        self.first_name = first
        self.last_name = last
        self.mid_name = mid

    @property
    def first_name(self):
        return self.__first

    @first_name.setter
    def first_name(self, value):
        self.__first = value

    @property
    def last_name(self):
        return self.__last

    @last_name.setter
    def last_name(self, value):
        self.__last = value

    @property
    def mid_name(self):
        return self.__mid

    @mid_name.setter
    def mid_name(self, value):
        self.__mid = value

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


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
        self.__person_id = value

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        names = value.split(' ')
        mid = ''
        for i in range(1, len(names) - 1):
            mid += names[i] + ' '
        self.__full_name = FullName(names[len(names) - 1], names[0], mid.strip())

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    def work(self, task):
        print(f'{self.full_name} is doing {task}')

    def show_info(self):
        print(f'CMND/CCCD: {self.person_id}')
        print(f'Họ và tên: {self.full_name}')
        print(f'Ngày sinh: {self.birth_date}')
