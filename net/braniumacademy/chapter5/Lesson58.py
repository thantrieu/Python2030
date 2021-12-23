class FullName:
    def __init__(self, fname):
        self.__first_name = ''
        self.__mid_name = ''
        self.__last_name = ''
        self.set_full_name(fname)

    def set_full_name(self, fname):
        words = fname.split()
        self.__first_name = words[len(words) - 1]
        self.__last_name = words[0]
        for i in range(1, len(words) - 1):
            self.__mid_name += words[i] + ' '

    def __str__(self):
        return f'{self.__last_name} {self.__mid_name}{self.__first_name}'


class BirthDate:
    def __init__(self, dob):
        self.__day = 0
        self.__month = 0
        self.__year = 0
        self.set_dob(dob)

    def set_dob(self, dob):
        data = [int(x) for x in dob.split('/')]
        self.__day = data[0]
        self.__month = data[1]
        self.__year = data[2]

    def __str__(self):
        return f'{self.__day}/{self.__month}/{self.__year}'


class Person:
    def __init__(self, fname, gender, dob):
        self.__full_name = FullName(fname)
        self.__gender = gender
        self.__birth_date = BirthDate(dob)

    def eat(self, food):
        print(f'{self.__full_name} is eating {food}')

    def __str__(self):
        return f'[{self.__full_name}, {self.__gender}, {self.__birth_date}]'


huong = Person('Tran Thi Thu Huong', 'Female', '28/08/2005')
print(huong)
huong.eat('Fish')
