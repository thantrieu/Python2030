class Student:
    def __init__(self, sid="", name="", age=0, math=0.0, physic=0.0, english=0.0):
        self.__student_id = sid
        self.__full_name = name
        self.__age = age
        self.__math = math
        self.__physic = physic
        self.__english = english

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
    def math(self):
        return self.__math

    @math.setter
    def math(self, value):
        self.__math = value

    @property
    def physic(self):
        return self.__physic

    @physic.setter
    def physic(self, value):
        self.__physic = value

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, value):
        self.__english = value

    def __str__(self):
        return f'{self.student_id:12}{self.full_name:30}' \
               f'{self.age:<12}{self.math:<12.2f}' \
               f'{self.physic:<12.2f}{self.english:<12.2f}'
