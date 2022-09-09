class FullName:
    def __init__(self, first, mid, last):
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
    def mid_name(self):
        return self.__mid

    @mid_name.setter
    def mid_name(self, value):
        self.__mid = value

    @property
    def last_name(self):
        return self.__last

    @last_name.setter
    def last_name(self, value):
        self.__last = value

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Person:
    def __init__(self, pid='', full_name='', dob=''):
        self.person_id = pid
        self.full_name = full_name
        self.birth_date = dob

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
        return f'{self.person_id:15}{self.full_name.__str__():30}' \
               f'{self.birth_date.strftime("%d/%m/%Y"):15}'

    @full_name.setter
    def full_name(self, value):
        if isinstance(value, str):
            name = value.split(' ')
            first = name[len(name) - 1]
            last = name[0]
            mid = ''
            for i in range(1, len(name) - 1):
                mid += name[i] + ' '
            self.__full_name = FullName(first, mid.strip(), last)
        else:
            self.__full_name = value

    @birth_date.setter
    def birth_date(self, value):
        self.__birth_date = value

    @person_id.setter
    def person_id(self, value):
        self.__person_id = value
