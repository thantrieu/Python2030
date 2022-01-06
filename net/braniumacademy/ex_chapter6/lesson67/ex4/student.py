class Address:
    """This class describe address data."""

    def __init__(self, wards, district, city):
        self.__wards = wards
        self.__district = district
        self.__city = city

    @property
    def wards(self):
        return self.__wards

    @property
    def city(self):
        return self.__city

    @property
    def district(self):
        return self.__district

    @property
    def address(self):
        return self.__wards + ', ' + self.__district + ', ' + self.__city


class FullName:
    """This class describe full name data."""

    def __init__(self, first, mid, last):
        self.__first = first
        self.__mid = mid
        self.__last = last

    @property
    def first_name(self):
        return self.__first

    @property
    def last_name(self):
        return self.__last

    @property
    def mid_name(self):
        return self.__mid

    @property
    def full_name(self):
        return self.__last + ' ' + self.__mid + ' ' + self.__first


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
    def fullname(self):
        return self.__full_name

    @property
    def address(self):
        return self.__address

    @property
    def gpa(self):
        return self.__gpa

    @property
    def age(self):
        return self.__age

    @property
    def id(self):
        return self.__student_id

    @property
    def major(self):
        return self.__major

    def __str__(self):
        return f'{self.__student_id:10}{self.major:10}' \
               f'{self.__age:<10}{self.fullname.full_name:25}' \
               f'{self.address.address:35}{self.__gpa:<10}'
