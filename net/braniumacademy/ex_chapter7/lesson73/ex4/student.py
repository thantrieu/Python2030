from filters import *


class Student:
    def __init__(self, sid="", name="", age=0,
                 math=0.0, physic=0.0, english=0.0):
        self.student_id = sid
        self.full_name = name
        self.age = age
        self.math = math
        self.physic = physic
        self.english = english

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        try:
            if is_student_id_valid(value):
                self.__student_id = value
        except ValueError as e:
            print(e)
            self.__student_id = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        try:
            if is_name_valid(value):
                self.__full_name = value
        except ValueError as e:
            print(e)
            self.__full_name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        try:
            if is_age_valid(f'{value}'):
                self.__age = value
        except ValueError as e:
            print(e)
            self.__age = 0

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, value):
        try:
            if is_grade_valid(value):
                self.__math = float(value)
        except ValueError as e:
            print(e)
            self.__math = 0.0

    @property
    def physic(self):
        return self.__physic

    @physic.setter
    def physic(self, value):
        try:
            if is_grade_valid(value):
                self.__physic = float(value)
        except ValueError as e:
            print(e)
            self.__physic = 0.0

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, value):
        try:
            if is_grade_valid(value):
                self.__english = float(value)
        except ValueError as e:
            print(e)
            self.__english = 0.0

    def __str__(self):
        name = self.full_name
        if self.full_name is None:
            name = "None"
        return f'{self.student_id:12}{name:30}' \
               f'{self.age:<12}{self.math:<12.2f}' \
               f'{self.physic:<12.2f}{self.english:<12.2f}'
