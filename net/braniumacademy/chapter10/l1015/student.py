class Student:
    """This class describe student infomation."""

    def __init__(self, sid, name, gender, major, gpa):
        self.__student_id = sid
        self.__first = ''
        self.__last = ''
        self.__mid = ''
        self.__gender = gender
        self.__major = major
        self.__gpa = gpa
        self.set_name(name)

    def set_name(self, name):
        words = name.split()
        self.first_name = words[0]
        self.last_name = words[len(words) - 1]
        for i in range(1, len(words) - 1):
            self.__mid += words[i] + ' '
        self.__mid.strip()

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

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

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    @major.setter
    def major(self, value):
        self.__major = value

    @property
    def gpa(self):
        return self.__gpa

    def totuple(self):
        return tuple([self.student_id, self.first_name,
                      self.last_name, self.gender, self.major,
                      f'{self.gpa:0.2f}'])

    def __str__(self):
        return f'[{self.student_id}, {self.first_name}, {self.last_name}, ' \
               f'{self.gender}, {self.major}, {self.gpa}]'
