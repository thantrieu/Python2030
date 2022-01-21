class Student:
    def __init__(self, sid, full_name, gpa):
        self.__student_id = sid
        self.__full_name = full_name
        self.__gpa = gpa

    @property
    def student_id(self):
        return self.__student_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    def __str__(self):
        return f'{self.student_id}, {self.full_name}, {self.gpa}'

    @property
    def totuple(self):
        return tuple([self.gpa, self.student_id])
