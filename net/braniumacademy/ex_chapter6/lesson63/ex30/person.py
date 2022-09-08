class FullName:
    def __init__(self, first, mid, last):
        self.__first = first
        self.__last = last
        self.__mid = mid

    @property
    def first_name(self):
        return self.__first

    @property
    def mid_name(self):
        return self.__mid

    @property
    def last_name(self):
        return self.__last

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Person:
    def __init__(self, pid, full_name, dob):
        self.__person_id = pid
        self.__full_name = full_name
        self.__birth_date = dob

    @property
    def person_id(self):
        return self.__person_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def birth_date(self):
        return self.__birth_date

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')

    def show_info(self):
        print(self)

    def __str__(self):
        return f'{self.person_id:15}{self.full_name.full_name:25}' \
               f'{self.birth_date:12}'
