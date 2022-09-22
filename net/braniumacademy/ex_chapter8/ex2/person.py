from filter import *


class FullName:
    """Lớp mô tả thông tin đầy đủ của họ và tên."""

    def __init__(self, f_id=0, first='', last='', mid=''):
        self.full_name_id = f_id
        self.first_name = first
        self.last_name = last
        self.mid_name = mid

    @property
    def full_name_id(self):
        return self.__full_name_id

    @full_name_id.setter
    def full_name_id(self, value):
        self.__full_name_id = value

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


class Address:
    def __init__(self, address_id=0, wards='', district='', city=''):
        self.wards = wards
        self.address_id = address_id
        self.district = district
        self.city = city

    @property
    def address_id(self):
        return self.__address_id

    @address_id.setter
    def address_id(self, value):
        self.__address_id = value

    @property
    def wards(self):
        return self.__wards

    @wards.setter
    def wards(self, value):
        self.__wards = value

    @property
    def district(self):
        return self.__district

    @property
    def city(self):
        return self.__city

    @district.setter
    def district(self, value):
        self.__district = value

    @city.setter
    def city(self, value):
        self.__city = value

    def __str__(self):
        return f'{self.wards}, {self.district}, {self.city}'


class BirthDate:
    def __init__(self, bd_id=0, day=0, month=0, year=0):
        self.birth_date_id = bd_id
        self.day = day
        self.month = month
        self.year = year

    @property
    def birth_date_id(self):
        return self.__birth_date_id

    @birth_date_id.setter
    def birth_date_id(self, value):
        self.__birth_date_id = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


class Person:
    """Lớp mô tả thông tin người"""

    def __init__(self, pid=None, name='', birth_date='', address=''):
        self.person_id = pid
        self.full_name = name
        self.birth_date = birth_date
        self.address = address

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
        try:
            if isinstance(value, str) and is_name_valid(value):
                names = value.split(' ')
                mid = ''
                for i in range(1, len(names) - 1):
                    mid += names[i] + ' '
                self.__full_name = FullName(first=names[len(names) - 1], last=names[0], mid=mid.strip())
            elif isinstance(value, FullName):
                self.__full_name = value
        except FullNameError as e:
            print(e)
            self.__full_name = 'No Name'

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if isinstance(value, BirthDate):
            self.__birth_date = value
        else:
            try:
                if isinstance(value, str) and is_birth_date_valid(value):
                    data = value.split('/')
                    self.__birth_date = BirthDate(day=int(data[0]), month=int(data[1]), year=int(data[2]))
            except BirthDateError as e:
                print(e)
                self.__birth_date = BirthDate(0, 1, 1, 2020)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if isinstance(value, Address):
            self.__address = value
        else:
            try:
                if is_address_valid(value):
                    data = value.split('-')
                    if len(data) == 1:
                        self.__address = Address(city=data[0])
                    elif len(data) == 2:
                        self.__address = Address(district=data[0], city=data[1])
                    else:
                        self.__address = Address(wards=data[0], district=data[1], city=data[2])
            except AddressError as e:
                print(e)

    def work(self, task):
        print(f'{self.full_name} is doing {task}')

    def show_info(self):
        print(f'CMND/CCCD: {self.person_id}')
        print(f'Họ và tên: {self.full_name}')
        print(f'Ngày sinh: {self.birth_date.__str__()}')
        print(f'Địa chỉ: {self.address.__str__()}')
