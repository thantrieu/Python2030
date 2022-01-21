class Address:
    """Lớp mô tả thông tin địa chỉ."""

    def __init__(self, wards, district, city):
        self.__wards = wards
        self.__district = district
        self.__city = city

    @property
    def wards(self):
        return self.__wards

    @wards.setter
    def wards(self, value):
        self.__wards = value

    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, value):
        self.__district = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def address(self):
        return self.__str__()

    def __str__(self):
        return f'{self.__wards}, {self.__district}, {self.__city}'


class FullName:
    """Lớp mô tả thông tin họ và tên."""

    def __init__(self, first, mid, last):
        self.__first = first
        self.__mid = mid
        self.__last = last

    @property
    def first_name(self):
        return self.__first

    @property
    def mid_name(self):
        return self.__mid

    @property
    def last_name(self):
        return self.__last

    @first_name.setter
    def first_name(self, value):
        self.__first = value

    @last_name.setter
    def last_name(self, value):
        self.__last = value

    @mid_name.setter
    def mid_name(self, value):
        self.__mid = value

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.__last} {self.__mid} {self.__first}'


class Student:
    """This class describe student infomation."""

    def __init__(self, sid, name, age, major, address, gpa):
        self.__student_id = sid
        self.__full_name = name
        self.__age = age
        self.__major = major
        self.__address = address
        self.__gpa = gpa

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    def __str__(self):
        return f'{self.__student_id:10}{self.full_name.full_name:30}' \
               f'{self.__age:<10}{self.address.address:35}{self.__gpa:<10.2f}' \
               f'{self.__major:15}'
