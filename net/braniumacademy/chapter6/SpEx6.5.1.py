import xml.etree.ElementTree as et


class Breakfast:
    def __init__(self, name, price, des, calo):
        self.__name = name
        self.__price = price
        self.__description = des
        self.__calories = calo

    @property
    def price(self):
        return self.__price

    @property
    def calo(self):
        return self.__calories

    def __str__(self):
        return f'Breakfast[name={self.__name}, price={self.__price},' \
               f'description={self.__description}, calories={self.__calories}]'


def parse_xml(file_name):
    tree = et.parse(file_name)
    root = tree.getroot()
    menu = []
    for item in root:
        name = item[0].text
        price = item[1].text
        des = item[2].text
        calo = item[3].text
        menu.append(Breakfast(name, price, des, calo))
    return menu


def show_menu(menu):
    for item in menu:
        print(item)


if __name__ == '__main__':
    file = 'food.xml'
    breakfast_menu = parse_xml(file)
    show_menu(breakfast_menu)
    print('=========================')
    breakfast_menu.sort(key=lambda x: x.price)
    show_menu(breakfast_menu)
    print('=========================')
    breakfast_menu.sort(key=lambda x: x.calo, reverse=True)
    show_menu(breakfast_menu)
