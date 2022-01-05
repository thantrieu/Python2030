import json
from collections import OrderedDict
from operator import itemgetter


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f'Person[name={self.__name}, age={self.__age}]'


def decode_person(dct):
    if 'name' in dct:
        return Person(dct['name'], int(dct['age']))
    else:
        return None


def listed_people(mpeople):
    print('==> Các đối tượng có trong file: ')
    for person in mpeople:
        print(person)


def listed_people_by_age(mpeople):
    result_dict = {}
    for person in mpeople:
        if person.age in result_dict:
            result_dict[person.age] += 1
        else:
            result_dict[person.age] = 1
    # Sắp xếp các phần tử của dict giảm dần theo value
    result_dict = OrderedDict(
        sorted(result_dict.items(), key=itemgetter(1), reverse=True))
    print('==> Các đối tượng theo từng độ tuổi: ')
    for key in result_dict.keys():
        print(f'{key}: {result_dict[key]}')


def find_max(mpeople):
    result_dict = {}
    for person in mpeople:
        if person.age in result_dict:
            result_dict[person.age] += 1
        else:
            result_dict[person.age] = 1
    max_value = 0
    for e in result_dict:
        if result_dict.get(e) > max_value:
            max_value = e
    return max_value


def find_min(mpeople):
    result_dict = {}
    for person in mpeople:
        if person.age in result_dict:
            result_dict[person.age] += 1
        else:
            result_dict[person.age] = 1
    min_value = find_max(mpeople)
    for e in result_dict:
        if result_dict.get(e) > min_value:
            min_value = e
    return min_value


if __name__ == '__main__':
    source = 'data2.json'
    with open(source) as json_reader:
        data = json_reader.read()
        people = json.loads(data, object_hook=decode_person)
        listed_people(people)
        print("=================================")
        listed_people_by_age(people)
        print("=================================")
        print(f'Nhóm tuổi có nhiều người nhất: {find_max(people)}')
        print("=================================")
        print(f'Nhóm tuổi có ít người nhất: {find_min(people)}')
