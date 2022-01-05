class Address:
    """This class describe address data."""

    def __init__(self, wards, district, city):
        self.wards = wards
        self.district = district
        self.city = city

    def __str__(self):
        return f'{self.wards}, {self.district}, {self.city}'


class FullName:
    """This class describe full name data."""

    def __init__(self, first, mid, last):
        self.first = first
        self.mid = mid
        self.last = last

    def __str__(self):
        return f'{self.last} {self.mid} {self.first}'


class Student:
    """This class describe student infomation."""

    def __init__(self, sid, name, age, major, address, gpa):
        self.student_id = sid
        self.full_name = name
        self.age = age
        self.major = major
        self.address = address
        self.gpa = gpa

    def __str__(self):
        return f'Student[id={self.student_id}, full_name={self.full_name}, ' \
               f'age={self.age}, major={self.major}, address={self.address},' \
               f' gpa={self.gpa}]'
