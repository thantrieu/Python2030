import datetime

from filters import *


class Student:
    def __init__(self, sid="", name="", birth_date=0,
                 math=0.0, physic=0.0, english=0.0):
        self.student_id = sid
        self.full_name = name
        self.birth_date = birth_date
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
        except StudentIdError as e:
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
        except FullNameError as e:
            print(e)
            self.__full_name = None

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        try:
            if is_birth_date_valid(value):
                self.__birth_date = datetime.datetime.strptime(value, '%d/%m/%Y')
        except StudentAgeError as e:
            print(e)
            self.__birth_date = None

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, value):
        try:
            if is_grade_valid(value):
                self.__math = float(value)
        except GradeError as e:
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
        except GradeError as e:
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
        except GradeError as e:
            print(e)
            self.__english = 0.0

    def __str__(self):
        name = self.full_name
        birth_date = "None"
        if self.birth_date is not None:
            birth_date = self.birth_date.strftime('%d/%m/%Y')
        if self.full_name is None:
            name = "None"
        sid = 'None'
        if self.student_id is not None:
            sid = self.student_id
        return f'{sid:12}{name:30}' \
               f'{birth_date:15}{self.math:<12.2f}' \
               f'{self.physic:<12.2f}{self.english:<12.2f}'
