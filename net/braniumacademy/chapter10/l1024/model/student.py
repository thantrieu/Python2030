class FullName:
    def __init__(self, first, last, mid):
        self.__first = first
        self.__last = last
        self.__mid = mid

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
    def __init__(self, person_id, full_name, birth_date):
        self.__person_id = person_id
        self.__full_name = full_name
        self.__birth_date = birth_date

    @property
    def person_id(self):
        return self.__person_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def birth_date(self):
        return self.__birth_date

    @person_id.setter
    def person_id(self, value):
        self.__person_id = value

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value


class Student(Person):
    def __init__(self, person_id, full_name,
                 birth_date, student_id, email, gpa, major):
        super().__init__(person_id, full_name, birth_date)
        self.__student_id = student_id
        self.__email = email
        self.__gpa = gpa
        self.__major = major

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value
